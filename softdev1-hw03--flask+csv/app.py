from flask import Flask, render_template
import occutable.util

app = Flask(__name__)

@app.route('/')
def index():
    data = occutable.util.gSearch("brownmykolyk")
    return data["items"][0]["formattedUrl"]

@app.route('/1/')
def p1():
    return "go to /occupations lmao"

@app.route('/2/')
def p2():    
    return "go to /occupations lmao"

@app.route('/3/')
def p3():    
    return "go to /occupations lmao"


@app.route('/occupations/')
def occupations():
    jobsDict = occutable.util.parseCSV("static/occupations.csv")
    randJob = occutable.util.randKey(jobsDict)
    jobLink = occutable.util.gSearch(randJob)["items"][0]["formattedUrl"]
    title = "Randoccupation"
    return render_template("occupations.html", jobsDict=jobsDict, randJob=randJob, title=title, jobLink=jobLink)


if __name__ == "__main__":
    app.run(debug=True)
