# split-hardware

We're developing an Alexa based cost sharing app for roommates to split the cost of shared items.

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
