from flask import Flask, request, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "deadnuts"

@app.route('/',methods = ['GET','POST'])
def count():
    if 'count' in session:
        session['count']= session['count']+1
        return render_template("index.html", count = session['count'])
    else: 
        session['count']= 1
        return render_template('index.html', count = session['count'])

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return (redirect('/'))








if __name__ == "__main__":
    app.run(debug=True)