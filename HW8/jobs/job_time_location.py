from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import requests
from datetime import time

def get_location(IP_adress):
        data_from_url = requests.get("http://ip2c.org/" + IP_adress)
        click_location = data_from_url.text.split(';')[3]
        return click_location

class MRIPFrequencyCountOnLocation(MRJob):

    OUTPUT_PROTOCOL = JSONValueProtocol
    
    def steps(self):
        return [
            MRStep(mapper = self.mapper_hour_location,
                   combiner = self.combiner_time_location_clicks,
                   reducer = self.reducer_time_location_clicks),
             MRStep(reducer = self.reducer_pre_finaly),
             MRStep(reducer = self.reducer_finaly)
         ]

    def mapper_hour_location(self, _, line):
        splitline =  line.split()
        hour = time.fromisoformat(splitline[1][:-1]).hour
        if hour >= 4 and hour <= 19 :
            ip_adress = splitline[2]
            location = get_location(ip_adress)
            yield (hour,location),1
         
    def combiner_time_location_clicks(self, key, values):
        yield key, sum(values)
        
    def reducer_time_location_clicks(self, key, values):
         yield key[0], {key[1]: sum(values)}
     
    def reducer_pre_finaly(self, key, values):
         yield None,(f'{key:2}:00', list(values))
         
    def reducer_finaly(self, key, values):
         yield None,dict(values)
         
if __name__ == '__main__':
    MRIPFrequencyCountOnLocation.run()
