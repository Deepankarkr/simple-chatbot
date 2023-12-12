import spacy
from spacy.matcher import PhraseMatcher
# Other libraries for intent recognition, search, and response generation

nlp = spacy.load("en_core_web_sm")


matcher = PhraseMatcher(nlp.vocab)

# Patterns for job, setup, access
patterns1 = [
    nlp("job"),
    nlp("setup"),
    nlp("access"),
]

# Patterns for time, timezone, schedule
patterns2 = [
    nlp("time"),
    nlp("timezone"),
    nlp("schedule"),
]

# Add patterns to the matcher
matcher.add("jobs", patterns1)
matcher.add("time", patterns2)


def process_message(message):
    doc = nlp(message)

    # Match the user's query with patterns
    matches = matcher(doc)

    # Get the first matched pattern (if any)
    if matches:
        intent = matches[0][1]
    else:
        intent = None

    # Check if the intent is an integer
    if isinstance(intent, int):
        # Handle recognized intents
        if intent == 5:
            # Provide link for jobs, setup, access
            response = "Here's the link for job information: [link-1]"
        elif intent == 4:
            # Provide link for time, timezone, schedule
            response = "Here's the link for time and schedule information: [link-2]"
    elif "roles" in doc:
        # Ask for further information about roles
        response = "Please specify which roles you're interested in."
    else:
        # Handle unknown intents
        response = "Sorry, I couldn't understand your question."

    return response


if __name__ == '__main__':
    # User input
    message = "How do I time set up access to my joobs?"

    # Process the message and get the response
    response = process_message(message)

    # Print the response
    print(response)
