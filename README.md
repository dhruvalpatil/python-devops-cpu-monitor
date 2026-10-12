# Python DevOps CPU Monitoring

A lightweight Python-based monitoring tool that reads server CPU utilization from a CSV file, checks usage against a configurable threshold, and generates timestamped alerts in a log file.

## Features

- Reads server metrics from a CSV file.
- Uses a configurable CPU threshold (default: 75%).
- Identifies servers exceeding the threshold.
- Prints `OK` and `ALERT` messages.
- Records timestamped results in `cpu_monitor.log`.
- Uses Python functions, loops, conditionals, and file handling.

## Project Structure

```text
python-devops-cpu-monitor/
├── cpu_monitor.py
├── servers.csv
├── cpu_monitor.log
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- Git
- Linux, Ubuntu, or WSL

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/dhruvalpatil/python-devops-cpu-monitor.git
cd python-devops-cpu-monitor
```

### 2. Run the monitoring script

```bash
python3 cpu_monitor.py
```

### 3. View monitoring logs

```bash
cat cpu_monitor.log
```

## Sample Input

The `servers.csv` file uses the following format:

```csv
server_name,CPU_usage
web-server-01,45
web-server-02,82
db-server-01,91
app-server-01,75
app-server-02,76
```

## Sample Output

```text
OK: web-server-01 CPU usage is 45.0%.
ALERT: web-server-02 CPU usage is 82.0%!
ALERT: db-server-01 CPU usage is 91.0%!
OK: app-server-01 CPU usage is 75.0%.
ALERT: app-server-02 CPU usage is 76.0%!
```

Output messages include timestamps when the script runs.

## Configuration

The CPU threshold is defined in `cpu_monitor.py`:

```python
CPU_THRESHOLD = 75
```

The script generates an alert only when CPU utilization is **greater than 75%**. Exactly 75% is treated as OK.

## DevOps Skills Demonstrated

- Python scripting and automation
- Linux / Ubuntu / WSL
- CSV and log file handling
- Monitoring and threshold-based alerting
- Git version control
- GitHub repository management

## Future Improvements

- Collect real CPU metrics using system monitoring libraries.
- Send alerts through email or messaging integrations.
- Add command-line configuration for thresholds.
- Schedule monitoring using Linux cron.
- Add automated tests and a CI workflow with GitHub Actions.

## Author

Dhruval Patil

GitHub: https://github.com/dhruvalpatil
