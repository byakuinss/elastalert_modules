from elastalert.util import pretty_ts
from elastalert.enhancements import BaseEnhancement


class convertpct(BaseEnhancement):
    def process(self, match):        
        try:
            match['system']['filesystem']['used']['pct'] = match['system']['filesystem']['used']['pct']*100
        except:
            pass
        
#        try:
#            match['system']['cpu']['user']['pct'] = match['system']['cpu']['user']['pct']*100
#        except:
#            pass

        try:
            match['system']['cpu']['user']['pct'] = (match['system']['cpu']['user']['pct']*100) / match['system']['cpu']['cores']
        except:
            pass

        try:
            match['system']['memory']['actual']['used']['pct'] = match['system']['memory']['actual']['used']['pct']*100
        except:
            pass
