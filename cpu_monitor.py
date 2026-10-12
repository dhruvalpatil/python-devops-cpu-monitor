
import csv
from datetime import datetime

CPU_THRESHOLD = 75
LOG_FILE = "cpu_monitor.log"


def check_cpu(server_name, cpu_usage):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cpu_usage > CPU_THRESHOLD:
        message = (
            f"{timestamp} ALERT: {server_name} "
            f"CPU usage is {cpu_usage}%!"
        )
    else:
        message = (
            f"{timestamp} OK: {server_name} "
            f"CPU usage is {cpu_usage}%."
        )

    print(message)

    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")


with open("servers.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        server_name = row["server_name"]
        cpu_usage = float(row["CPU_usage"])
        check_cpu(server_name, cpu_usage)
import csv

CPU_THRESHOLD = 75


def check_cpu(server_name, cpu_usage):
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: {server_name} CPU usage is {cpu_usage}%!")
    else:
        print(f"OK: {server_name} CPU usage is {cpu_usage}%.")


with open("servers.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        server_name = row["server_name"]
        cpu_usage = float(row["CPU_usage"])

        check_cpu(server_name, cpu_usage)
