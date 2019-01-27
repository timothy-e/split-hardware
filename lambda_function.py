from botocore.vendored import requests

# Here we define our Lambda function and configure what it does when 
# an event with a Launch, Intent and Session End Requests are sent. # The Lambda function responds to an event carrying a particular 
# Request are handled by functions such as on_launch(event) and 
# intent_scheme(event).

def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()

# Here we define the Request handler functions
def on_start():
    print("Session Started.")

def on_launch(event):
    
    onlunch_MSG = "Hi there! Would you like to log an item that you have purchased?"
    reprompt_MSG = "Do you want to log an item?"
    card_TEXT = "Record an item"
    card_TITLE = "Log an item"
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def on_end():
    print("Session Ended.")

# The intent_scheme(event) function handles the Intent Request. 
# Since we have a few different intents in our skill, we need to 
# configure what this function will do upon receiving a particular 
# intent. This can be done by introducing the functions which handle 
# each of the intents.

def intent_scheme(event):
    intent_name = event['request']['intent']['name']

    if intent_name == "Log_Purchases":
        return log_purchases(event)  
    elif intent_name == "Amount_Owed":
        return amount_owed(event)
    elif intent_name == "Settle_Balance":
        return settle_balance(event)
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)

# Here we define the intent handler functions
def log_purchases(event):
    
    item = event['request']['intent']['slots']['item']['value']
    name = event['request']['intent']['slots']['name']['value']
    amount = event['request']['intent']['slots']['amount']['value']
    amountTwo = event['request']['intent']['slots']['amountTwo']['value']
    amountCents = int(amount) + int(amountTwo)/100
    
    theMSG = "{} has logged {}. They spent {} dollars and {} cents.".format(name, item, amount, amountTwo)
    reprompt_MSG = "Would you like to log purchases?"
    card_TEXT = name + ", you've logged " + item +  str(amountCents)
    card_TITLE = name + ", you've logged " + item 
    
    #Post Request for the three parameters for a purchased item
    path = "?name={}&cost={}&item={}".format(name, str(amountCents), item.replace(" ", "%20"))
    r = requests.post('http://167.99.186.234:5000/add_purchase/' + path)
    
    return output_json_builder_with_reprompt_and_card(theMSG, card_TEXT, card_TITLE, reprompt_MSG, False)
    
        
def amount_owed(event):
    
    name = event['request']['intent']['slots']['name']['value']
    
    #Get Request to retrieve what the {name} owes and how much
    path = "?name={}".format(name)
    r = requests.get('http://167.99.186.234:5000/get_balance'+path)
    
    theMSG = "Balances Displayed for {}".format(name)
    reprompt_MSG = "Would you like to know who you owe funds?"
    card_TEXT = "Outstanding balances displayed"
    card_TITLE = "Outstanding balances displayed" 
    
    return output_json_builder_with_reprompt_and_card(theMSG, card_TEXT, card_TITLE, reprompt_MSG, False)
    

def settle_balance(event):
    
    #Post Request for settling all debts
    r = requests.put('http://167.99.186.234:5000/settle_debts')
    
    theMSG = "All balances have been settled"
    reprompt_MSG = "Would you like to settle balances?"
    card_TEXT = "balances settled."
    card_TITLE = "balances settled." 
    
    return output_json_builder_with_reprompt_and_card(theMSG, card_TEXT, card_TITLE, reprompt_MSG, False)
    
        
def stop_the_skill(event):
    stop_MSG = "Thank you. Bye!"
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Goodbye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = ""
    reprompt_MSG = ""
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Can you restate your question?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

# The response of our Lambda function should be in a json format. That is why in this part of the code we define the
# functions which will build the response in the requested format

def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict

def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict
    
def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict    

def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict

def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict