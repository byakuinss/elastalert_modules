from elastalert.alerts import Alerter
import httplib
import urllib
from elastalert.util import EAException
from elastalert.util import elastalert_logger
from elastalert.util import lookup_es_key

class PushoverAlerter(Alerter):
    """ Requested elasticsearch indices are sent by HTTP POST to Pushover. Encoded with JSON. """

    def __init__(self, rule):
        super(PushoverAlerter, self).__init__(rule)
        self.post_payload = self.rule.get('pushover_payload', {})
        self.post_static_payload = self.rule.get('pushover_parameter', {})
        self.post_all_values = self.rule.get('pushover_all_values', not self.post_payload)

    def alert(self, matches):
        body = self.create_alert_body(matches)
        title = self.create_title(matches)

        """ Each match will trigger a POST to the specified endpoint(s). """
        for match in matches:           
            payload = match if self.post_all_values else {}
            for post_key, es_key in self.post_payload.items():
                payload[post_key] = lookup_es_key(match, es_key)
            headers = {"Content-type": "application/x-www-form-urlencoded"}
            data = self.post_static_payload
            data['message'] = body
            data['title'] = title

            try:
                conn = httplib.HTTPSConnection("api.pushover.net:443")
                conn.request("POST", "/1/messages.json",
                             urllib.urlencode(data), headers)

            except httplib.HTTPException as e:
                raise EAException("Error posting Pushover alert: %s" % e)
            elastalert_logger.info("Pushover alert sent.")

    def get_info(self):
        return {'type': 'http_post'}

