from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/', methods=['GET'])
def principal():

    if 'contador' in session:
        session['contador'] += 1
        texto = "times"
    else:
        session['contador'] = 1
        texto = "time"

    return render_template('index.html', texto=texto)


@app.route('/ByTwo', methods=['GET'])
def Incrementar():

    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    responseObj = {
        'contador': session['contador']
    }
    return responseObj


@app.route('/destroy_session', methods=['GET'])
def destroy():
    if 'contador' in session:
        session.clear()
    responseObj = {
        'contador': 1
    }
    return responseObj


@app.route('/prefCounterFrm', methods=['POST'])
def IncremenPersonal():

    cant = request.form['increaseNumber']
    print(cant)

    if 'contador' in session:
        session['contador'] += (int(cant)-1)
    else:
        session['contador'] = 1

    responseObj = {
        'contador': session['contador']
    }
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
