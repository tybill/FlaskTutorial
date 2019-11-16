# FlaskTutorial
This is a quick starting guide for building a hackathon project with Python Flask

## Preliminaries

You should be able to use flask on your local machine. Follow the instructions here:
```
https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba
```

## About the tutorial
```
Flaskturotial
	|--------------- server.py
	|--------------- ngrok
	|--------------- templates
				|-------------------- index.html
```
### server.py
The server application written with flask. To start, run
```
python server.py
```

Default port is set to 8080.

The server also supports connection to a mongo db instance. To start the server with
connection to a particular db collection running on localhost, run
```
python server.py {port} {db_name} {collection_name}
```
port - The port your mongodb server is on (The default port for mongo is 27017)
db_name - Name of your db instance
collection_name - Name of the collection

There are several APIs supported by the server

##### /hello
Sample request:
```
{url}/hello
```

##### /json
Sample request:
```
{url}/json?firstname=Tommy&lastname=Trojan
```

Sample response:
```
{
	"firstname": Tommy,
	"lastname": Trojan
}
```

##### /template
Sample request:
```
{url}/json?name=Tommy
```

##### /add
Sample request:
```
{url}/add?name=Tommy&email=ttrojan@usc.edu
```

##### /get
Sample request:
```
{url}/get?name=Tommy
```

### ngrok
A great tool to expose your server running on localhost. To start, run
```
./ngrok http {port number}
```

If you did not change the default setting in server.py, {port number} should be 8080.
For more information, go to https://ngrok.com/

### templates
Here goes all the template HTMLs that we will use with flask templates