# Step1- import
from flask import Flask

# Step2- create the object
appdemo = Flask(__name__)

# Step3 - Define a routes and bind it with function and route
@appdemo.route('/')   # decorators
def index():
    return "Welcome to this application.."

@appdemo.route('/about')
def about_us():
    return 'This is About us page'

# Step3 - Run the app
if __name__ == '__main__':
    appdemo.run()