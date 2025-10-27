from flask import Flask,render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/submit',methods=['POST'])
def submit():
    name=request.form.get('name')
    email=request.form.get('email')
    year=request.form.get('year')
    rollno=request.form.get('rollno')
    return render_template('result.html',name=name,email=email,year=year,phone=phone)
if __name__ == "_main_":
    app.run(host='0.0.0.0',port="5000",debug=True)
