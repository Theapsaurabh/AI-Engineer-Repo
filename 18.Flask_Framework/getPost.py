from flask import Flask, render_template,request
'''
it creates an instance of the flask class, which will be our WSGI application.
'''
### WSGI Application is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
app=Flask(__name__)
@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"


@app.route('/redirect', methods=['GET'])
def redirect():
    return render_template('redirect.html')


@app.route('/get-post', methods=['GET', 'POST'])
def get_post():
    if request.method == 'POST':
        data = request.form['data']
        return f"Received POST request with data: {data}"
    else:
        return render_template('form.html')
    
    
if __name__=='__main__':
    app.run(debug=True)