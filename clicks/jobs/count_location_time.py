from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import requests
from functools import reduce


def make_counts(prev_el, next_el):
    prev_el[next_el] = prev_el.get(next_el, 0) + 1
    return prev_el


def reduce_location(location):
    return reduce(make_counts, location, {})


class MRCountLocationTime(MRJob):

    OUTPUT_PROTOCOL = JSONValueProtocol
    scope_work_time = [f"0{x}:00" if len(str(x)) == 1 else f"{x}:00" for x in range(8, 20)]

    def mapper(self, _, line):
        date, time, ip = line.strip().replace("[", "").replace("]", "").split()
        time = time.split(":")[0]
        location = requests.get(f"https://ip2c.org/?ip={ip}").text
        time = f"{time}:00"
        if time in self.scope_work_time:
            yield time, location

    def reducer(self, time, location):
        if time in self.scope_work_time:
            counts = reduce_location(location)
            yield None, {time: counts}


if __name__ == "__main__":
    MRCountLocationTime.run()
