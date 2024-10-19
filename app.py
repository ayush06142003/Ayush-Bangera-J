from flask import Flask
import os
import time
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():

    full_name = "Your Full Name"
    

    system_username = os.getenv('USER') or os.getenv('USERNAME') or 'Unknown User'
    

    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')


    top_output = subprocess.getoutput('top -b -n 1')


    response = f"""
    <html>
    <body>
        <h2>System Information</h2>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>User:</strong> {system_username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre><strong>TOP output:</strong>\n{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
