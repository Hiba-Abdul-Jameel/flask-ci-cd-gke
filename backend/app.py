from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)

# SQL Server connection settings
server = '35.243.252.245'  # Use the public IP and port explicitly
database = 'myappdb'  # Your database name
username = 'sqlserver'  # Your SQL Server username
password = 'Haj@1600'  # Your SQL Server password
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a connection to the database
try:
    conn = pyodbc.connect(connection_string)
    print("Connected to SQL Server!")
except pyodbc.Error as error:
    print(f"Error: {error}")
    conn = None  # Set connection to None in case of failure


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_messages', methods=['GET'])
def get_messages():
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        # Ensure connection is still open
        if conn.closed:
            return jsonify({"error": "Database connection is closed"}), 500

        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages")  # Query to get all messages
        rows = cursor.fetchall()

        # Return messages in JSON format
        messages = [row[0] for row in rows]  # Extract message from each row
        return jsonify(messages)  # Return the messages as a JSON response
    except Exception as fetch_error:
        print(f"Error fetching messages: {fetch_error}")
        return jsonify({"error": f"Failed to fetch messages: {fetch_error}"}), 500



@app.route('/test_connection', methods=['GET'])
def test_connection():
    if conn is None:
        return jsonify({"status": "failure", "message": "Failed to connect to the database"}), 500
    try:
        # Simple query to check the database connection
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  # Simple query to verify connection
        return jsonify({"status": "success", "message": "Database connection is successful"})
    except Exception as test_error:
        print(f"Error testing database connection: {test_error}")
        return jsonify({"status": "failure", "message": "Error while testing database connection"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
