from flask import Flask
# Create the application instance
# __name__ is a special variable in Python 
# that is set to the name of the current module
app = Flask(__name__)

@app.route("/")

def hello():
    return "Welcome to HumanityGPT!"

# This conditional ensures that the Flask development server only runs if this script is executed directly
# (not imported as a module)
if __name__ == "__main__":
    # This conditional ensures that the Flask development server only runs if this script is executed directly
    # (not imported as a module)
    app.run(debug = True)