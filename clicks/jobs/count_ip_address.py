from mrjob.job import MRJob


class MRCountIPAddress(MRJob):

    def mapper(self, _, line):
        date, time, ip = line.strip().replace("[", "").replace("]", "").split()
        yield ip, 1

    def reducer(self, key, values):
        total = sum(values)
        if total > 1:
            yield key, total


if __name__ == "__main__":
    MRCountIPAddress.run()
