import pandas as pd
from flask import send_file

from flask import Flask, render_template, request
import os
from ranker import rank_resumes

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():

    rankings = None

    if request.method == "POST":

        job_description = request.form["job_desc"]

        files = request.files.getlist("resumes")

        for file in files:
            if file.filename.endswith(".pdf"):
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        rankings = rank_resumes(job_description, UPLOAD_FOLDER)

        # ⭐ Create CSV Report
        df = pd.DataFrame(rankings, columns=["Resume", "Score"])
        df.to_csv("ranking_report.csv", index=False)

    return render_template("index.html", rankings=rankings)


@app.route("/download")
def download():
    return send_file("ranking_report.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)