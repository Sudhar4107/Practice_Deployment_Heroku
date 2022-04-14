from unittest import result
from flask import Flask, render_template, request
import joblib
#C:\Users\ELCOT\Desktop\VsCode_Practice\deployment_env

#initialize app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def Form_Submit():
    A = request.form.get('A')
    B = request.form.get('B')
    C = request.form.get('C')
    D = request.form.get('D')
    E = request.form.get('E')

    model=joblib.load('dib_1.pkl')

    result = model.predict([[A,B,C,D,E]])

    if(result==0):
        F="Fail"
    else:
        F="Pass"

    return render_template('predict.html',data=f'Prediction result is {F}')


@app.route('/contacts')
def contact():
    return('Contact Page!')

if(__name__=='__main__'):
    app.run(debug= True)