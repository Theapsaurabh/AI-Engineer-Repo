### Building URL Dynamically in Jinja2
### Jinja 2 template engine
from flask import Flask, render_template,request
'''
it creates an instance of the flask class, which will be our WSGI application.
'''
### WSGI Application is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
app=Flask(__name__)
@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"



@app.route('/get-post', methods=['GET', 'POST'])
def get_post():
    if request.method == 'POST':
        data = request.form['data']
        return f"Received POST request with data: {data}"
    else:
        return render_template('form.html')
    
# Variable Rule:

## here we are using a variable rule in the URL. The <int:score> part of the URL is a 
# variable that will be passed to the success function as an argument. 
# The int: part specifies that the variable should be treated as an integer.

@app.route('/success/<int:score>')
def success(score):
    res=""
    if(score>=90):
        res="A+"
    elif(score>=80):
        res="A"
    elif(score>=70):    
        res="B+"
    elif(score>=60):
        res="B"
    elif(score>=50):
        res="C"
    else:
        res="Fail"
    return render_template('result.html', grade=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if(score>=90):
        res="A+"
    elif(score>=80):
        res="A"
    elif(score>=70):    
        res="B+"
    elif(score>=60):
        res="B"
    elif(score>=50):
        res="C"
    else:
        res="Fail"
    exp={
        "score":score,
        "grade":res
    }
    return render_template('result1.html', result=exp)

if __name__=='__main__':
    app.run(debug=True)