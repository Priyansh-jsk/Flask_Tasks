from urllib import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fun_1():
    if request.method == 'POST':
        email = request.form['in_1']
        return "Welcome {}".format(email)
        # return "POST Request Page"
    else:
        return render_template("index.html")

@app.route('/search', methods=['GET'])
def search_function():
    query = request.args['q']
    return "Search query entered = {}".format(query)

# @app.route('/', methods=['POST'])
# def fun2():
#     return "POST Request Page"

if __name__ == '__main__':
    app.run(debug=True)