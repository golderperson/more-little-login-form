from flask import Flask, request, render_template,redirect, url_for
import pymysql

app = Flask(__name__)

def getConnection():
  return pymysql.connect(
    host='localhost',
    port=int(3306),
    db='db name',
    user='yourusername',
    passwd='your db passwd',
    charset='utf8',
  )
@app.route("/")
def main_page():
    return "<p>This is the main page</p>"

@app.route("/htmlFile")
def index():
    return render_template('index.html')

@app.route("/ddd",methods=['GET','POST'])
def post_page():
    conn = getConnection()
    cur = conn.cursor()
    if(request.method == 'POST'):
        user_id = request.form['user_id']
        message=request.form['password']
    #    dt_now = datetime.datetime.now()
        sql = """
            insert into tablename (user_id,message)
            values (%s,%s)
            ;
        """
        cur.execute(sql, (user_id,message))
        print(user_id,message)
        conn.commit()
        return redirect(url_for('index'))
@app.route("/s",methods=['GET','POST'])
def super():
    conn = getConnection()
    cur = conn.cursor()
    sql ="""
    select*from table name;
    """
    cur.execute(sql)
    rows = cur.fetchall() 
    for t_rows in rows:
      print(t_rows[0], t_rows[1], t_rows[2])
      
    return render_template("d.html",data1=t_rows[0],data2=t_rows[1],data3=t_rows[2])
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)