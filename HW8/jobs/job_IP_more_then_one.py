from mrjob.job import MRJob


class MRIPFrequencyCount(MRJob):

    def mapper(self, _, line):
        splitline =  line.split()
        yield splitline[2],1

    def reducer(self, key, values):
        SumIP = sum(values)
        if SumIP >1:
            yield key, SumIP
       
if __name__ == '__main__':
    MRIPFrequencyCount.run()
