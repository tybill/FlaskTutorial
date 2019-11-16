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

### ngrok
A great tool to expose your server running on localhost. To start, run
```
./ngrok http {port number}
```

If you did not change the default setting in server.py, {port number} should be 8080.
For more information, go to https://ngrok.com/

### templates
Here goes all the template HTMLs that we will use with flask templates