from flask import Flask, render_template, request, url_for, flash, redirect, session
from utils import auth, flaskUtils

app = Flask(__name__)
app.secret_key = "this is needed for msg flashing so..."



'''
ROOT ROUTE:
* Intended HTTP method: GET
* Intended referrer: ANY ('/*')
> If user is logged in, return welcome page
> If user NOT logged in, return login page
'''
@app.route("/", methods=['GET'])
def index():
    if "username" in session: #session hasn't expired
        return render_template("home.html", username=session["username"])
    return render_template("login.html")



'''
AUTHENTICATION ROUTE:
* Intended HTTP method: POST
* Intended referrer: ROOT ('/')
> If desired action is registration:
    > On success, redirect to index w/ success msg
    > On failure, redirect to index w/ error msg
> If desired action is login:
    > On success, redirect to index w/ success msg
    > On failure, redirect to index w/ error msg
'''
@app.route("/auth", methods=['GET','POST'])
def authenticate():
    if request.method == "GET": #shouldn't need to get this page
        flash("can't be GETtin' /auth around these parts", "error")
        return redirect( url_for("index") )
    
    assert request.method == 'POST', \
        "Unsupported Method: %s" % request.method
    if request.method == "GET":
        flash("Already logged in!", "error")
        return redirect( flaskUtils.redirect_url() )

    form_username = request.form.get('username')
    form_password = request.form.get('password')
    form_action = request.form.get('action')

    if form_action == "register":
        status = auth.register(form_username, form_password)
        if not(status): #if everything OK
            flash("just made ur acc c: now try logging in!", "success")
            return redirect( url_for("index") )
        
        flash(auth.regErrList[status - 1], "error")
        return redirect( url_for("index") )

    assert form_action == 'login', \
        "Unsupported Action: %s" % (form_action)
    status = auth.login(form_username, form_password)
    if not(status): #if everything OK
        flash("Login successful!", "success")
        session['username'] = form_username
        return redirect( url_for("index") )
    #if NOT everything OK:
    flash(auth.logErrList[status - 1], "error")
    return redirect( url_for("index") )



'''
LOGOUT ROUTE
* Intended HTTP method: POST
* Intended referrer: ROOT ('/')
> Pop username from session
> Redirect to index w/ success msg
'''
@app.route("/logout", methods=['GET','POST'])
def logout():
    if request.method == 'GET':
        flash("can't be GETtin' /logout around these parts", "error")
        return redirect( url_for('index')) 

    assert request.method == 'POST', \
        "Unsupported Method: %s" % (request.method)
    assert "username" in session, \
        "Session doesn't have key username: %s" % (session)

    session.pop('username')
    flash("Logged u out so u could log back in smh what's the point of all this .-.", "success")
    return redirect( flaskUtils.redirect_url() )


if __name__ == "__main__":
    app.run(debug=True)
