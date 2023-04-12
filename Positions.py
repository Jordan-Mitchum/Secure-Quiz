import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderHome():
    return render_template('home.html')

@app.route('/startOver', methods=['GET','POST'])
def startOver():
    session.clear()
    return redirect(url_for('renderHome'))
    
@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2', methods=['GET','POST'])
def renderPage2():
    if 'position1' in session: 
        session.clear()
        return render_template('home.html')
    else:
        session["position1"]=request.form['position1']
        return render_template('page2.html')
 
@app.route('/page3', methods=['GET','POST'])
def renderPage3():
    if 'position2' in session:
        session.clear()
        return render_template('home.html')
    else:
        session["position2"]=request.form['position2']
        return render_template('page3.html')
    
@app.route('/page4', methods=['GET','POST'])
def renderPage4():
    if 'position3' in session:
        session.clear()
        return render_template('home.html')
    else:
        session["position3"]=request.form['position3']
        return render_template('page4.html')
    
@app.route('/page5', methods=['GET','POST'])
def renderPage5():
    if 'position4' in session:
        session.clear()
        return render_template('home.html')
    else:
        session["position4"]=request.form['position4']
        return render_template('page5.html')
    
@app.route('/pageEnd', methods=['GET','POST'])
def renderPageEnd():
    if 'position5' in session:
        session.clear()
        return render_template('home.html')
    else:
        session["position5"]=request.form['position5']
    
    total = 0
   
    if session["position1"] == "1":
        total = total + 1
    if session["position2"] == "1":
        total = total + 1
    if session["position3"] == "2":
        total = total + 1
    if session["position4"] == "3":
        total = total + 1
    if session["position5"] == "4":
        total = total + 1 
        
    if total < 3:
        yn = "Failed"
    else:
        yn = "Passed"
        
    return render_template('pageEnd.html', total = total, YN = yn)
    





if __name__=="__main__":
    app.run(debug=True)