from flask import Flask

app = Flask(__name__) #create instance of FLASK CLASS
                        #__name__ = resouces 

@app.route('/')
def index(): #even the event app route will occure this function will be called
    return "<h1>HELLO WORLD</h1>"

@app.route('/xyz') #another link
def hello():
    return "Hello choto world"

@app.route('/gree/<name>') #this <> takes as ? of html
def greet(name): #from ?<> it gets the variable
    return f"Hello {name}"

@app.route('/add/<number1>/<number2>') #takes two argument 
def free(number1,number2): #takes as string
    return f"{number1 + number2}" 



@app.route('/add_number/<int:number1>/<int:number2>') #takes two argument as integar
def free2(number1,number2): #takes as integar 
    return f"{number1} + {number2}" 


from flask import request #handles GET Request
@app.route('/handle_url_params')
def handle_params():
    #return str(request.args)  #shows the dictionary of all parameter
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name =request.args.get('name')
        return f' {greeting}: {name}'
    else:
        return "Params are missing"



if __name__ == '__main__': #when it is called directly 
    app.run(host='0.0.0.0',port=5555, debug=True) #host port debug = continuous debuiging
#added