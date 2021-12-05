from mrjob.job import MRJob
from mrjob.step import MRStep
import requests

def get_location(IP_adress):
        data_from_url=requests.get("http://ip2c.org/" + IP_adress)
        click_location = data_from_url.text.split(';')[3]
        return click_location

class MRIPFrequencyCountOnLocation(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper_ip,
                   reducer = self.reducer_ip),
            MRStep(reducer = self.reducer_location),
        ]

    def mapper_ip(self, _, line):
        splitline =  line.split()
        yield splitline[2],1

    def reducer_ip(self, key, values):
        SumIP = sum(values)
        if SumIP >1:
            yield key, SumIP
            
    def reducer_location(self, key, values):
        yield get_location(key), sum(values)
       
if __name__ == '__main__':
    MRIPFrequencyCountOnLocation.run()
