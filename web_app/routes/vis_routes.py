# web_app/routes/vis_routes.py

from flask import Blueprint, render_template

vis_routes = Blueprint("vis_routes", __name__)

import os
import sqlite3
import pandas as pd

DEV_DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sis_vis_dev.db")

@vis_routes.route("/visuals")
def visuals():
    #FilePath
    dev_conn = sqlite3.connect(DEV_DB_FILEPATH)
    # print("Connection:", dev_conn)
    cursor1 = dev_conn.cursor()
    # print("CURSOR:", cursor1)
    gradebook_query = "SELECT t.student_name, s.assignment_name, s.score, c.course_name, r.teacher_name FROM scores s LEFT JOIN student t ON s.student_id = t.id LEFT JOIN courses c ON s.class_id = c.id LEFT JOIN teachers r ON c.teacher_id = r.id;"
    gradebook_result = cursor1.execute(gradebook_query).fetchall()
    gradebook_df = pd.DataFrame(gradebook_result)
    return render_template("index.html")