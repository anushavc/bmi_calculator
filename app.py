from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/bmi',methods=['POST'])
def bmi_calc():
    mass=float(request.form['mass'])
    height=float(request.form['height'])
    height=height/100
    print(height)
    print(mass)
    bmi=(mass)/(height**2)
    bmi=round(bmi,2)
    return render_template('result.html',bmi=bmi)

if __name__=='__main__':
    app.run(debug=True)