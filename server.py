from flask import Flask, request, render_template, jsonify
import sys

app = Flask(__name__)

data = None
if len(sys.argv) > 1:
    print("Connecting to mongo instance..")
    from pymongo import MongoClient
    port = int(sys.argv[1])
    client = MongoClient('localhost', port)
    # connecting to database
    db = client[sys.argv[2]]
    # connection to collection
    data = db[sys.argv[3]]

# Hello World!
@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return "Hello World!"

# Basic Json example
@app.route("/json", methods=['GET', 'POST'])
def json_example():
    res_dict = request.args
    if request.method == 'POST':
        res_dict = request.form

    # return a python dictionary as a json string
    return jsonify(res_dict)

# Basic template example
@app.route("/template", methods=['GET', 'POST'])
def template_example():
    name = ''
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args['name']

    # respond with html web page through flask template
    return render_template('index.html', name = name)  

# Basic database example
@app.route("/add", methods = ['GET'])
def add_to_database():
    if db is None:
        return "Database function not supported!\n"

    name = request.args["name"]
    email = request.args["email"]

    post = { "name": name, "email": email }
    if data.find({"name": name}).count() > 0:
        data.update_one({"name": number},{"$set": post}, upsert=False)
    else:
        data.insert_one(post)

    return "posted"

@app.route("/get", methods = ['GET'])
def get_from_database():
    if db is None:
        return "Database function not supported!\n"

    name = request.args["name"]
    return data.find_one({"name": name})["email"]

if __name__ == "__main__":
    app.run(debug=True, port=8080)
