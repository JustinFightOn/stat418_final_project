# MTCars Flask API

This is an API using simple linear regression to predict mpg using any other remaining variables as predictor in the mtcars.csv.

The environment is created through a `docker-compose` command, that references the corresponding Dockerfile and requirements.txt file, so make sure you have Docker and Python 3.7 installed.

To run this model, download or pull the repository using the link below:

`https://github.com/JustinFightOn/Mtcars-Flask-Api`

To run this API, change your directory to the docker folder and run:

`docker-compose up`

It should return:

`server is up - nice job!`

You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

`curl http://localhost:5000/`

Finally, to get mpg predictions, here is sample input into the model:

`curl -H "Content-Type: application/json" -X POST -d '{“name”: “Volvo 142E”, “cyl”: 4, “disp”: 121.0, “hp”: 109, “drat”:4.11, “wt”: 2.78, “qsec”: 18.6, “vs”: 1, “am”: 1, “gear”: 4, “carb”:2}' "http://localhost:5000/mpg"`

The result should be:

`{'MPG prediction': {'Volvo 142E': 24.36826768324378}}`