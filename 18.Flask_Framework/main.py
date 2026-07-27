from flask import Flask, render_template
'''
it creates an instance of the flask class, which will be our WSGI application.
'''
### WSGI Application is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
app=Flask(__name__)
@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"


@app.route('/redirect')
def redirect():
    return render_template('redirect.html')

if __name__=='__main__':
    app.run(debug=True)