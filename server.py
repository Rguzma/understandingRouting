from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response



# import statements, maybe some other routescopy
@app.route('/success')
def success():
    return "success"
    
# app.run(debug=True) should be the very last statemen


@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return f"Hello, {name}"



@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/<string:word>/<int:num>')
def multiply(word, num):
    return f'test, {word*num}' 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.