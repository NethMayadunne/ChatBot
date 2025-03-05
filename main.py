import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def response(bot_response, list_of_words, single_response=False, required_words=[]):
    return {
        'response': bot_response,
        'probability': message_probability(list_of_words, list_of_words, single_response, required_words)
    }

def check_all_messages(message):
    highest_prob_list = {}

    def add_response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Add responses here
    add_response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    add_response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how']),
    add_response('You\'re welcome!', ['thank', 'you'], required_words=['thank']),
    add_response('I enjoy programming.', ['what', 'you', 'do'], required_words=['enjoy']),
    add_response('Have a great day!', ['good', 'day'], required_words=['day']),
    add_response('See you later!', ['bye', 'see', 'you'], required_words=['bye']),
    add_response('I am a chatbot.', ['who', 'are', 'you'], required_words=['who']),
    add_response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message)

# Testing the response system
while True:
    print('Bot:', get_response(input('You: ')))
