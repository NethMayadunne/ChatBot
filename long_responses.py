import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
def unknown():
    response = ['Could you please re-phrase that?', "What does that mean?"][random.randrange(4)]
    return response
