from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return ('hello')


@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    exp = {
        'score': score,
        'result': res
    }
    return render_template('submit.html', success=exp)


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    total_marks = 0
    if request.method == 'POST':
        s1 = float(request.form['s1'])
        s2 = float(request.form['s2'])
        s3 = float(request.form['s3'])
        s4 = float(request.form['s4'])
        s5 = float(request.form['s5'])
        total_marks = (s1+s2+s3+s4+s5)/5
    else:
        return render_template('form1.html')
    return redirect(url_for('success', score=total_marks))


if __name__ == "__main__":
    app.run(debug=True)
