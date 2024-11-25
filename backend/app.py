from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)

# SQL Server connection settings
server = '99.240.166.116'  # Replace with your SQL Server instance's public IP
database = 'myappdb'  # Your database name
username = 'sqlserver'  # Your SQL Server username
password = 'Haj@1600'  # Your SQL Server password
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a connection to the database
try:
    conn = pyodbc.connect(connection_string)
    print("Connected to SQL Server!")
except pyodbc.Error as e:
    print(f"Error: {e}")
    conn = None  # Set connection to None in case of failure

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_messages', methods=['GET'])
def get_messages():
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages")  # Query to get all messages
        rows = cursor.fetchall()

        # Return messages in JSON format
        messages = [row[0] for row in rows]  # Extract message from each row
        return jsonify(messages)  # Return the messages as a JSON response
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return jsonify({"error": "Failed to fetch messages from the database"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
