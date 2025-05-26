import logging

from flask import Flask
from flask_apscheduler import APScheduler
import sqlite3

#app = Flask(__name__, static_folder="../frontend/build/", static_url_path="/")
app = Flask(__name__, static_folder="../frontend/dist/", static_url_path="/")
app.logger.setLevel(logging.INFO)

class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

@scheduler.task('interval', id='do_job_1', seconds=5, misfire_grace_time=900)
def job1():
    con = sqlite3.connect("./HD/analysis.db")

    data = con.execute("SELECT * FROM data").fetchall()
    print(data[0][0])
    
    KML = "<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>"
    # The row[2] and [1] are not an error. This is due to a flaw making the db
    for row in data:
        kml = (
            "<Placemark>\n"
            "<name>"+ row[0]+"</name>\n"
                "<Point>\n"
                    "<coordinates>"+ row[2] +","+ row[1] +",0</coordinates>\n"
                "</Point>\n"
            "</Placemark>\n"
        )
        KML += kml

    KML += "</Document></kml>"
    file = open("./HD/data.kml", "w")
    file.write(KML)
    file.close()




from .routes import *