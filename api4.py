from flask import Flask

data = Flask(__name__)

students = {
    "uma": 534,
    "bhanu": 535,
    "devi": 536,
    "deepu": 537,
    "yashu": 538,
    "yoga": 539
}

#import mysql.connector
#from mysql.connector import Error

#connection = mysql.connector.connect(
#        host='localhost',           # Replace with your MySQL server host
#        user='test',                # Replace with your MySQL username
#        password='Test@123',    # Replace with your MySQL password
#        database='test_db'     # Replace with your database name
#   )

@data.route("/hello")
def hello():
    return "hello world"
    
@data.route("/mysql")
def mysql():
    if connection.is_connected():
        print("Successfully connected to MySQL")
        return "SUCCESS"
    return "FAILURE"
@data.route("/students", methods=["GET"])
def get_all_students():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")
    rows = cursor.fetchall()
    return rows
@data.route("/addstudent/<name>/<id>", methods=["POST"])
def add_students(name,id):
    cursor = connection.cursor()
    query = "INSERT INTO test (name, address) VALUES (%s, %s)"
    values = (name, id)
    cursor.execute(query,values)
    connection.commit()
    return "success"

if __name__ == "__main__":
    data.run(host="0.0.0.0",port = 5002)

