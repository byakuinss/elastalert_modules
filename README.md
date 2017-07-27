## elastalert_modules
elastalert enhancements for my projects

### Alert Context Enhancement
##### converttimezone.py
Convert timezone from UTC to local timezone.
Usage: add into rule config file
```
match_enhancements:
- "elastalert_modules.my_enhancements.TimeEnhancement"
```

##### convertpct.py #
Convert pct of metricbeat field to x% format (ex. 0.961 -> 96.1%)
Usage: add into rule config file
```
match_enhancements:
- "elastalert_modules.convertpct.convertpct"
```

You can change field or do other calculation in the file. 
Metricbeat documents are formatted using JSON, if you want to get the values in python, you need to split it by the `` "." ``.
Such as `` "system.process.memory.size" ``, you can use `` match['system']['process']['memory']['size'] `` to get the values.

For example: 
```
        try:
            match['system']['cpu']['user']['pct'] = (match['system']['cpu']['user']['pct']*100) / match['system']['cpu']['cores']
        except:
            pass
```

Metricbeat document in elasticsearch:
```
{
  "_index": "metricbeat-2017.07.26",
  "_type": "metricsets",
  "_id": "AV1-KBymqNygytTigzKB",
  "_version": 1,
  "_score": null,
  "_source": {
    "@timestamp": "2017-07-26T09:09:04.220Z",
    "beat": {
      "hostname": "my_host",
      "name": "my_host",
      "version": "5.4.2"
    },
    "metricset": {
      "module": "system",
      "name": "cpu",
      "rtt": 296
    },
    "system": {
      "cpu": {
        "cores": 4,
        "idle": {
          "pct": 0.6638
        },
        "system": {
          "pct": 0.0156
        },
        "user": {
          "pct": 0.2295
        },
        ...
```

### Alerter #
##### Pushover Alerter #
A simple alerter to push alert to Pushover API through HTTP POST.
`` token `` and `` user `` are required. For detailed information please reference to [Pushover API](https://pushover.net/api#messages)
Usage: add into rule config
```
alert:
- "elastalert_modules.pushover_alerts.PushoverAlerter"

pushover_parameter:
  token: "your_app_token"
  user: "your_user_key"
  # device: "your_device" 
```

### Reminder
If you change anything in elastalert_modules, you need to run the `` setup.py `` to re-install elastalert.
And make sure there is no any errors when installing elastalert.
```
cd elastalert
sudo python setup.py install
```

