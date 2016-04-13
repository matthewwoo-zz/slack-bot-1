from src.app import app

app.run(debug=app.config['DEBUG'], port=5000)
# the reason why you didn't need to import a config file is that there is a config attribute to a Flask object