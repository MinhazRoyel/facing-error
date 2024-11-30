from flask import Flask

app = Flask(__name__) #create instance of FLASK CLASS
                        #__name__ = resouces 

@app.route('/')
def index(): #even the event app route will occure this function will be called
    return "<h1>HELLO WORLD</h1>"

if __name__ == '__main__': #when it is called directly 
    app.run(host='0.0.0.0',port=5555, debug=True) #host port debug = continuous debuiging
#added