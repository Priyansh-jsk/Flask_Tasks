# Step1- import
from flask import Flask

# Step2- create the object
appdemo = Flask(__name__)

users = ['priyansh', 'Aniket', 'Vivek', 'Suhana', 'Sunil', 'Vandana']

# Step3 - Define a routes and bind it with function and route
@appdemo.route('/')   # decorators
def index():
    return "Welcome to this application."

@appdemo.route('/about')
def about_us():
    return 'This is About us page'

@appdemo.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in users:
        return "Welcome {}!".format(user_name)
    else:
        return "Please Register"

# Step4 - Run the app
if __name__ == '__main__':
    appdemo.run(debug=True)
#    appdemo.run()
