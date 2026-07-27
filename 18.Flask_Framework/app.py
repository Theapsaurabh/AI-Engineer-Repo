from flask import Flask
'''
it creates an instance of the flask class, which will be our WSGI application.
'''
### WSGI Application is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello World"




if __name__=='__main__':
    app.run(debug=True)