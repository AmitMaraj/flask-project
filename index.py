from flask import Flask, request
from datetime import datetime
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

mydb = mysql.connector.connect(
    host="localhost",
    user="amit",
    password="password",
    database="project"
)
if mydb.is_connected():
    db_Info = mydb.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = mydb.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

cursor = mydb.cursor(dictionary=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# get all projects from the database
@app.route('/projects')
def get_projects():
    global cursor
    cursor.execute('SELECT id, name, description, status, DATE_FORMAT(created_at, "%d/%m/%Y %h:%i %p") AS created_at FROM projects')
    results = cursor.fetchall()
    # print(results)
    return json.dumps({'status':'success', 'projects':results})   

@app.route('/project/create', methods = ['POST'])
@cross_origin(supports_credentials=True)
def create_project():

    data = request.get_json()
    global cursor,mydb

    if data['name'] is None:
        resp('error', None, 'Project name is required')

    if data['description'] is None:
        resp('error', None, 'Project description is required')

    name = data['name']
    description = data['description']
    status = data['status']

    curr_date = datetime.now().isoformat()
    try:
        results = cursor.execute(f"INSERT INTO projects (name, description, status, created_at) VALUES ('{name}','{description}','{status}','{curr_date}')")
        mydb.commit()
    except MySQLdb.IntegrityError:
        return json.dumps({'status':'error', 'msg':'Could not create project'})
    return json.dumps({'status':'success', 'msg':'Project created', 'created_at': curr_date})

# @app.route('/create/db')
# def create_db():
#     global cursor,mydb
#     results = cursor.execute("SELECT * FROM information_schema WHERE TABLE_NAME = 'projects' ")
#     print(results)
#     return 'done'

def resp(status, data, msg = None):
    return json.dumps({'status': status, 'data': data, 'msg': msg})