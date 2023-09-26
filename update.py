import mysql.connector as msc
import json
from flask import Flask
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/update')
def mem_conn():
    new_id=request.args['new_id']
    id_=request.args['id']
    cnx = msc.connect(host='localhost',user='root',passwd='',database='work')
    curA = cnx.cursor()
    curA = cnx.cursor(buffered=True)
    curA.execute("update data set task_id=%d where id=%d"%(int(new_id),int(id_)))
    curA.execute("select * from data where f_name=%d"%(int(new_id)))
    row_headers=[x[0] for x in curA.description]
    rv = curA.fetchall()
    cnx.commit()
    print(row_headers)
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    print(json.dumps(json_data))
    return jsonify(json_data)
app.run()
mem_conn()
