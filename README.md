# Split

We're developing an Alexa based cost sharing app for roommates to split the cost of shared items.

## To Run
`python FlaskApp/app.py`.

Navigate to `localhost:5000` and check it out.

## Information

We configured an Alexa Skill to send commands to an AWS Lambda function. The function sends cURL requests to access our webserver built with Flask over a Postgres DB. 

[To create a deployment package for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

[To review Alexa + Lambda set up](https://medium.com/crowdbotics/how-to-build-a-custom-amazon-alexa-skill-step-by-step-my-favorite-chess-player-dcc0edae53fb)
