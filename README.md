# split-hardware

We're developing an Alexa based cost sharing app for roommates to split the cost of shared items.

## To Run
`python FlaskApp/app.py`.

Navigate to `localhost:5000` and check it out.

Currently I have a simple template set up. Try going to `localhost:5000/some_string`.

Because the app is running in debug mode, updating the Python code will trigger a rebuild, so you don't need to manually restart the Flask process.

[To create a deployment package for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

[To review Alexa + Lambda set up](https://medium.com/crowdbotics/how-to-build-a-custom-amazon-alexa-skill-step-by-step-my-favorite-chess-player-dcc0edae53fb)

Things to do:
* Configure Alexa commands
  * Create endpoints with AWS Lambda for the Alexa commands
* Configure a webserver
  * Docker? :grimacing:
  * Flask
  * REST APIs
* Connect our webserver with our Lambda functions
