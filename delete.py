import mysql.connector as msc
import json
from flask import Flask
import urllib as ul
import webbrowser
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/delete')
def mem_conn():
    name = request.args['id']
    cnx = msc.connect(host='localhost',user='root',passwd='',database='work')
    curA = cnx.cursor()
    curA = cnx.cursor(buffered=True)
    curA.execute("DELETE FROM data WHERE id=%d"%(int(name)))
    curA.execute("SELECT * FROM data")
    cnx.commit()
    row_headers=[x[0] for x in curA.description]
    rv = curA.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    print(json.dumps(json_data,indent=2))
    return 'item deletes succesfull'
app.run()
mem_conn()



