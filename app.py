from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_dstat_data', methods=['POST'])
def get_dstat_data():
    ip_address = request.form['ip_address']
    
    # Command to fetch dstat logs for the given IP (this is a placeholder)
    command = f"dstat --output dstat_logs.csv --ip {ip_address} 1 10"  # Adjust the command as needed

    # Execute the command
    subprocess.Popen(command, shell=True)
    
    # Here, you should process your dstat logs and return the data in a suitable format.
    # For now, we are returning a dummy response.
    data = {
        'time': ['0s', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s'],
        'cpu': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'disk': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
