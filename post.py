import mysql.connector as msc
import json
from flask import Flask
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/insert')
def mem_conn():
    email_id=request.args['email_id']
    password=request.args['password']
    #task_id=request.args['task_id']
    #task_name=request.args['task_name']
    cnx = msc.connect(host='localhost',user='root',passwd='',database='work')
    curA = cnx.cursor()
    curA = cnx.cursor(buffered=True)
    curA.execute("INSERT INTO e_v (email_id,password) VALUES (%s,%s)"%(str(email_id),str(password)))
    curA.execute("select * from e_v where email_id=%s"%(str(email_id)))
    row_headers=[x[0] for x in curA.description]
    rv = curA.fetchall()
    cnx.commit()
    print(row_headers)
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    print(json.dumps(json_data))
    return jsonify(json_data),print("inserted sucessfully")
app.run()
mem_conn()
