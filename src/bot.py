import os
import spacy
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Define the bot's functionality
def handle_message(message):
    # Parse the user's message using spaCy
    doc = nlp(message)

    # Extract the user's intent and parameters
    intent = None
    project1 = None
    project2 = None

    for token in doc:
        if token.text.lower() == "compare" or token.text.lower() == "differentiate":
            intent = "metadata_diff"
        elif token.text.lower() == "proj1":
            project1 = "proj1"
        elif token.text.lower() == "proj2":
            project2 = "proj2"

    # Perform the appropriate action based on the user's intent and parameters
    if intent == "metadata_diff" and project1 is not None and project2 is not None:
        # Launch the metaman CLI application to perform the metadata-diff between project1 and project2
        # ...

        # Return a message to the user with the results of the action
        return "The metadata difference between {} and {} is ...".format(project1, project2)
    else:
        return "I'm sorry, I didn't understand your request."

# Instantiate a Slack API client
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

# Instantiate a Slack Bolt app
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Define an event listener for messages sent to the bot
@app.event("app_mention")
def handle_mention(event, say):
    message = event["text"]
    response = handle_message(message)

    # Send the response back to the user
    try:
        say(response)
    except SlackApiError as e:
        print("Error sending message: {}".format(e))

# Start the app
if __name__ == "__main__":
    handler = SocketModeHandler(app_token=os.environ["SLACK_APP_TOKEN"], app=app)
    handler.start()
