from flask import Flask
import pyodbc

app = Flask(__name__)

# SQL Server connection settings
server = 'YOUR-SQL-SERVER-IP'  # Replace with your SQL Server instance's public IP
database = 'myappdb'  # Your database name
username = 'sqlserver'  # Your SQL Server username
password = 'Haj@1600'  # Your SQL Server password
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string)
    print("Connected to SQL Server!")
except Exception as e:
    print(f"Error: {e}")


@app.route('/')
def index():
    return 'Flask app running and connected to SQL Server!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
