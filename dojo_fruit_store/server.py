from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    strawberry = ['0', '1', '2', '3', '4']
    raspberry = ['0' ,'1', '2', '3', '4']
    apple = ['0', '1', '2', '3', '4']
    blackberry = ['0', '1', '2', '3', '4']
    return render_template("index.html", strawberry = strawberry, raspberry = raspberry, apple = apple, blackberry = blackberry)

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(f"number of Apples: {request.form ['apple']}")
    print(f"number of Strawberries: {request.form ['strawberry']}")
    print(f"number of Raspberries: {request.form ['raspberry']}")
    print(f"number of Blackberries: {request.form ['blackberry']}")
    count =int(request.form['apple'])+int(request.form['strawberry'])+int(request.form['blackberry'])+int(request.form['raspberry'])
    print(count)
    return render_template("checkout.html", apple=request.form['apple'], 
    strawberry=request.form['strawberry'], blackberry=request.form['blackberry'], 
    raspberry=request.form['raspberry'], student_id=request.form['student_id'], first_name=request.form['first_name'], last_name=request.form['last_name'],
    count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    