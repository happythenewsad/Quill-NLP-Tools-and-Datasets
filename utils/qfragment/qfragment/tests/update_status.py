import requests
from time import sleep

sentences = [
    ("According to his trusty servant Jeff.", False),
    ("Beautiful toy birds.",False),
    ("Dancing boys can never sing.",True),
    ("Dancing in the moonlight could rock.", True),
    ("Dancing in the moonlight makes me happy.", True),
    ("Dancing in the moonlight suck.", False),
    ("Dead as a door nail.",False),
    ("Dreaming of her long lost sheep, Katie's eye's fluttered peacefully.",True),
    ("Have mixed the potion.", False),
    ("Have run around the word.", False),
    ("He and the boy stir the potion.", True),
    ("He and the boy stirs the potion.", False),
    ("He is a great warrior.",True),
    ("He stir the potion.", False),
    ("He stirs the potion.", True),
    ("He will have a comfortable home now.", True),
    ("He, along with the boy, stir the potion.", False),
    ("He, along with the boy, stirs the potion.", True),
    ("I stir the potion.", True),
    ("I stirs the potion.", False),
    ("John, tired and needing sleep, continued toward the gate.",True),
    ("Jumping up and down could be exciting.",True),
    ("Katherine began cry.", False),
    ("Katherine began crying.", True),
    ("Katherine began to cry.", True),
    ("Katherine began.", True),
    ("Katherine cried.", True),
    ("Katherine crying.", False),
    ("Katherine start.", False),
    ("Katherine started cry.", False),
    ("Katherine started crying.", True),
    ("Katherine started.", True),
    ("Katherine, start.", True),
    ("Ran around the word.", False),
    ("Run around the word.", True),
    ("Running around the word.", False),
    ("Running is fun.",True),
    ("Running out of excuses.", False),
    ("Sick men are unpleasant.",True),
    ("Sleeping is one of the best parts of the day.",True),
    ("Swimming sucks.",True),
    ("The boy and I stir the potion.", True),
    ("The boy and I stirs the potion.", False),
    ("The boy and you stir the potion.", True),
    ("The boy and you stirs the potion.", False),
    ("The boy and you will stir the potion.", True),
    ("The boy and you will stirs the potion.", False),
    ("The boy, along with me, stir the potion.", False),
    ("The boy, along with me, stirs the potion.", True),
    ("The boy, along with you, stir the potion.", False),
    ("The boy, along with you, stirs the potion.", True),
    ("The boy, along with you, will stir the potion.", True),
    ("The boy, along with you, will stirs the potion.", False),
    ("The men will be irate.", True),
    ("The men will be jumpy.", True),
    ("The men will be worried about her.", True),
    ("The men will be worried.", True),
    ("The men will be worry.", False),
    ("The men will be worrying about her.", True),
    ("The men will be worrying.", True),
    ("The men will be.", True),
    ("The potion has been stirred.", True),
    ("The potion have been stirred.", False),
    ("The potions has been stirred.", False),
    ("The potions have been stirred.", True),
    ("The race has been run.", True),
    ("The race have been run.", False),
    ("The races has been run.", False),
    ("The races have been run.", True),
    ("The scientist and the boy has been stirring the potion.", False),
    ("The scientist and the boy have been stirring the potion.", True),
    ("The scientist and the boy stir the potion.", True),
    ("The scientist and the boy stirs the potion.", False),
    ("The scientist and the boy will be stirring the potion.", True),
    ("The scientist and the boy will be stirs the potion.", False),
    ("The scientist and the boy will stir the potion.", True),
    ("The scientist and the boy will stirs the potion.", False),
    ("The scientist has be stirring the potion.", False),
    ("The scientist has been stir.", False),
    ("The scientist has been stirred the potion.", False),
    ("The scientist has been stirring the potion.", True),
    ("The scientist has been stirring.", True),
    ("The scientist has been stirs the potion.", False),
    ("The scientist have been stirring the potion.", False),
    ("The scientist have been stirring.", False),
    ("The scientist is stirring.", True),
    ("The scientist stir the potion.", False),
    ("The scientist stirs the potion.", True),
    ("The scientist was stirring.", True),
    ("The scientist will be stir the potion.", False),
    ("The scientist will be stirred the potion.", False),
    ("The scientist will be stirring the potion.", True),
    ("The scientist will be stirs the potion.", False),
    ("The scientist will be worried the potion is not done.", True),
    ("The scientist will be worrying the potion.", True),
    ("The scientist will be.", True),
    ("The scientist will stir the potion.", True),
    ("The scientist will stirs the potion.", False),
    ("The scientist will.", True),
    ("The scientist, along with the boy, has been stirring the potion.", True),
    ("The scientist, along with the boy, have been stirring the potion.", False),
    ("The scientist, along with the boy, stir the potion.", False),
    ("The scientist, along with the boy, stirs the potion.", True),
    ("The scientist, along with the boy, will be stirred the potion.", False),
    ("The scientist, along with the boy, will be stirring the potion.", True),
    ("The scientist, along with the boy, will stir the potion.", True),
    ("The scientist, along with the boy, will stirs the potion.", False),
    ("The scientists are stirring.", True),
    ("The scientists has been stirring.", False),
    ("The scientists have been stir.", False),
    ("The scientists have been stirred.", True),
    ("The scientists have been stirring.", True),
    ("The scientists have been swam.", False),
    ("The scientists have been swimming.", True),
    ("The scientists have been worried.", True),
    ("The scientists stir the potion.", True),
    ("The scientists stir.", True),
    ("The scientists stirs the potion.", False),
    ("The scientists stirs.", False),
    ("The scientists were stirring.", True),
    ("The scientists will be run out of town.", True),
    ("The scientists will be stir.", False),
    ("The scientists will be stirred.", True),
    ("The scientists will be stirring the potion.", True),
    ("The scientists will be stirring.", True),
    ("The scientists will be worried.", True),
    ("The scientists will be worrying.", True),
    ("The scientists will stir the potion.", True),
    ("The scientists will stir.", True),
    ("The scientists will stirs the potion.", False),
    ("The scientists will stirs.", False),
    ("The scientists will.", True),
    ("There am just twelve little girls in her school.", False),
    ("There were just twelve little girls in her school.", True),
    ("They stir the potion.", True),
    ("They stir.", True),
    ("They stirs the potion.", False),
    ("They stirs.", False),
    ("They will have a comfortable home now.", True),
    ("Tired and needing sleep.",False),
    ("Tired and needing sleep, John continued toward the gate.",True),
    ("Tired and needing sleep, worried and wanting a friend.",False),
    ("Until Sam is full grown.", False),
    ("We stir the potion.", True),
    ("We stir.", True),
    ("We stirs the potion.", False),
    ("We stirs.", False),
    ("Will have mixed the potion.", False),
    ("Will have run around the word.", True),
    ("Will run around the word.", False),
    ("Worried about the world.", False),
    ("Worried about the world.", False),
    ("Worrying about the state of the world is no fun.",True),
    ("Worrying needlessly.", False),
    ("Worrying needlessly.", False),
    ("You stir the potion.", True),
    ("You stir.", True),
    ("You stirs the potion.", False),
    ("You stirs.", False),
    ("You will stir the potion.", True),
    ("You will stir.", True),
    ("You will stirs the potion.", False),
    ("You will stirs.", False),
    ("According to his trusty servant Jeff, who was very good at his"
        " job.",False),
    ("Sprawled on the hot dirt like a lost slug.",False),
    ("Thinking about her.",False),
    ("Wishing that the day would end soon so he could return to his"
        " dog.",False),
    ("In the distance was the three forts whose historic names were known"
            " to every child in Charleston.", False),
    ("In the distance were the three forts whose historic names were known"
            " to every child in Charleston.", True),
    ("In the distance was three forts.", False),
    ("In the distance were three forts.", True),
    ("And with her pretty soft black curls, her rosy cheeks and pleasant"
            " voice, no one could imagined a more desirable teacher than"
            " Miss Rosalie George.", False),
    ("And with her pretty soft black curls, her rosy cheeks and pleasant"
            " voice, no one could imagine a more desirable teacher than"
            " Miss Rosalie George.", True),
    ("And with her pretty soft black curls, her rosy cheeks and pleasant"
            " voice, no one could have imagined a more desirable teacher than"
            " Miss Rosalie George.", True),
    ("And with her pretty soft black curls, her rosy cheeks and pleasant"
            " voice, no one could have imagine a more desirable teacher than"
            " Miss Rosalie George.", False),
    ("Let us go back a week and record what passed at the last interview"
            " between Philip and his father before the latter passed into"
            " the state of unconsciousness which preceded death.", True),
    ("Dreaming of his long-lost sheep, John slept soundly.", True),
]

for s in sentences:
    try:
        payload = {'text':s[0]}
        if s[1]:
            payload['is_correct'] = 'correct'
        requests.post('http://maxwellbuck.com:5000', data=payload) 
        sleep(.25)
        print('Success...')
    except:
        pass


