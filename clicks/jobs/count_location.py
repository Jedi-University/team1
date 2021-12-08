from mrjob.job import MRJob
import requests


class MRCountLocation(MRJob):

    # OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, line):
        date, time, ip = line.strip().replace("[", "").replace("]", "").split()
        yield requests.get(f"https://ip2c.org/?ip={ip}").text, 1

    def reducer(self, key, values):
        total = sum(values)
        yield key, total


if __name__ == "__main__":
    MRCountLocation.run()
