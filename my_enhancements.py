from elastalert.util import pretty_ts
from elastalert.enhancements import BaseEnhancement


class TimeEnhancement(BaseEnhancement):
    def process(self, match):        
        for k, v in match.items():
            if isinstance(v, basestring) and v.endswith('Z'):
                try:
                    match[k] = pretty_ts(v)
                except:
                    pass
