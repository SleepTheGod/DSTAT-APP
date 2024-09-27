from flask import Flask, render_template, request, jsonify
import subprocess
import csv
import os
import time

app = Flask(__name__)
LOG_FILE = 'dstat_logs.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_dstat_data', methods=['POST'])
def get_dstat_data():
    ip_address = request.form['ip_address']
    
    # Start dstat to log data (output every second for 10 seconds)
    command = f"dstat --tcp --udp --output {LOG_FILE} 1 10"
    subprocess.Popen(command, shell=True)

    # Allow time for dstat to generate output
    time.sleep(11)

    # Read and parse dstat logs
    data = parse_dstat_logs()

    return jsonify(data)

def parse_dstat_logs():
    time_labels = []
    cpu_usage = []
    disk_usage = []

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Skip header

            for row in reader:
                time_labels.append(row[0])
                cpu_usage.append(float(row[1]))
                disk_usage.append(float(row[2]))

    return {
        'time': time_labels,
        'cpu': cpu_usage,
        'disk': disk_usage
    }

if __name__ == '__main__':
    app.run(debug=True)
