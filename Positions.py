import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderHome():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderHome'))
    
@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2', methods=['GET','POST'])
def renderPage2():
    return render_template('page2.html')
 
@app.route('/page3', methods=['GET','POST'])
def renderPage3():
    return render_template('page3.html')
    
@app.route('/page4', methods=['GET','POST'])
def renderPage4():
    return render_template('page4.html')

if __name__=="__main__":
    app.run(debug=False)