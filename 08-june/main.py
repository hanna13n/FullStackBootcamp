import psycopg2
from flask import Flask, request

app = Flask("PyJobs in Bnglr")


@app.route("/")  # decorator
def fetchjobs():
    dbconn = psycopg2.connect("dbname=naukri")
    cursor = dbconn.cursor()
    cursor.execute("select title, company_name,jd_url from openings")
    ret = []
    for title, company_name, jd_url in cursor.fetchall():
        item = f"<b>{title}</b> :  {company_name} </br> {jd_url}"
        ret.append(item)
    l = "<br/><br/><br/><br/>".join(ret)
    return f"""<h2 align=center>List of jobs : </h2>

    {l}"""

# http://127.0.0.1/add?item=x
# @app.route("/add")
# def add_item():
#   item = request.args.get("item")
#   items.append(item)
#   return f"No. of items is now {len(items)}"


# https://flask.palletsprojects.com/en/2.0.x/
