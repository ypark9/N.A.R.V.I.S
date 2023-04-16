import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

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
