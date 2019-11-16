from flask import Flask, request, render_template, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Hello World!
@app.route("/hello", methods=['GET', 'POST'])
def hello():
    resp = MessagingResponse()

    # Add a message
    resp.message("Hello World!\n");
    return str(resp)

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

if __name__ == "__main__":
    app.run(debug=True, port=8080)