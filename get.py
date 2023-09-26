import mysql.connector as msc
import json
from flask import Flask
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/get')
def mem_conn():
    email_id=request.args['email']
    cnx = msc.connect(host='localhost',user='root',passwd='',database='work')
    curA = cnx.cursor()
    print(cnx.is_connected())
    curA.execute("SELECT * FROM e_v where email_id=%s"%(str(email_id)))
    row_headers=[x[0] for x in curA.description]
    rv = curA.fetchall()
    json_data=[]
    print(row_headers)
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
        print("email veXrified")
    print(json.dumps(json_data,indent=2))
    return jsonify(json_data)
app.run()
mem_conn()
