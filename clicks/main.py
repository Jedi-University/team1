
import os


class Main:

    @staticmethod
    def run():
        os.system("python ./jobs/count_ip_address.py ./tmp/test.txt >> ./tmp/result/grouped.txt")
        os.system("python ./jobs/count_location.py ./tmp/test.txt >> ./tmp/result/location.txt")
        os.system("python ./jobs/count_location_time.py ./tmp/test.txt >> ./tmp/result/time_location.txt")


if __name__ == "__main__":

    Main.run()
