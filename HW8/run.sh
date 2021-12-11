# running 3 jobs
python3 jobs/job_IP_more_then_one.py input/clicksshort.txt > output/grouped.txt
python3 jobs/job_location.py input/clicksshort.txt > output/location.txt
python3 jobs/job_time_location.py input/clicksshort.txt > output/time_location.txt
