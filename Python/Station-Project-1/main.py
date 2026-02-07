import random

def first_template(number, time_measure, transport_mode, adjective, sec_adjective, noun, color, body_part, verb, sec_number, sec_noun, thrd_noun, sec_body_part, frth_noun, thrd_adjective, silly_word):
    print(f"""It was about {number} {time_measure} ago when
        I arrived at the hospital in a {transport_mode}. The
        hospital is a/an {adjective} place, there are a lot
        of {sec_adjective} {noun} here. There are nurses here
        who have {color} {body_part}. If someone wants to come
        into my room I told them that they have to {verb} first.
        I’ve decorated my room with {sec_number} {sec_noun}. Today
        I talked to a doctor and they were wearing a {thrd_noun} on
        their {sec_body_part}. I heard that all doctors
        {verb} {frth_noun} every day for breakfast. The most
        {thrd_adjective} thing about being in the hospital
        is the {silly_word} {noun} !""")

def second_template(person_name, time_measure, feeling, sec_feeling, animal, noun, color, adverb, verb, sec_number, sec_noun, sec_verb, thrd_verb, silly_word, sec_color, number):
    print(f"""This weekend I am going camping with {person_name}.
        I packed my lantern, sleeping bag, and {noun}. I am so
        {feeling} to {verb} in a tent.I am {sec_feeling}
        we might see a(n) {animal}, I hear they’re kind of dangerous.
        While we’re camping, we are going to hike, fish, and {sec_verb}.
        I have heard that the {color} lake is great for {thrd_verb}.
        Then we will {adverb} hike through the forest for {number}
        {time_measure}. If I see a {sec_color} {animal} while hiking,
        I am going to bring it home as a pet! At night we will tell
        {sec_number} {silly_word} stories and roast {sec_noun} around the campfire!!""")
    
def third_template(person_name, verb, adjective, sec_adjective, thrd_adjective, frth_adjective, fth_adjective, noun, sec_noun, thrd_noun, frth_noun, fth_noun, magic_creature, sec_magical_creature, time_measure, room, number, color, place, animal ):
    print(f"""Dear {person_name}, I am writing to you
        from a {adjective} castle in an enchanted forest. I found myself
        here one day after going for a ride on a {color} {animal} in {place}.
        There are {sec_adjective} {magic_creature} and {thrd_adjective}
        {sec_magical_creature} here! In the {room} thereis a pool full of {noun}.
        I fall asleep each night on a {sec_noun} of {thrd_noun} and dream of {frth_adjective} {frth_noun}.
        It feels as though I have lived here for {number} {time_measure}.
        I hope one day you can visit, although the only way to get here now is
        {verb} on a {fth_adjective} {fth_noun}!!""")

story_number = input("Chose template (1-3) ")
while story_number not in ["1", "2", "3"]:
    story_number = input("Chose template (1-3) ")
template = random.choice([int(story_number), 1, 2, 3])
print(f"Chosen template: {story_number}")
print(f"Random template: {template}")
if story_number == "1":
    number = input("Input Number: ")
    sec_number = input("Input Number again: ")
    time_measure = input("Input Measure of time: ")
    transport_mode = input("Input Mode of transportation: ")
    adjective = input("Input Adjective: ")
    sec_adjective = input("Input Adjective again: ")
    thrd_adjective = input("Input Adjective last time: ")
    noun = input("Input Noun: ")
    sec_noun = input("Input Noun again: ")
    thrd_noun = input("Input Noun one more time: ")
    frth_noun = input("Input Noun last time: ")
    color = input("Input Color: ")
    body_part = input("Input Part of the body: ")
    sec_body_part = input("Input Part of the body again: ")
    verb = input("Input Verb: ")
    silly_word = input("Input Silly Word: ")
    first_template(number, time_measure, transport_mode, adjective, sec_adjective, noun, color, body_part, verb, sec_number, sec_noun, thrd_noun, sec_body_part, frth_noun, thrd_adjective, silly_word)
if story_number == "2":
    number = input("Input Number: ")
    sec_number = input("Input Number again: ")
    time_measure = input("Input Measure of time: ")
    person_name = input("Input Person name: ")
    feeling = input("Input Feeling: ")
    sec_feeling = input("Input Feeling again: ")
    animal = input("Input Animal: ")
    noun = input("Input Noun: ")
    sec_noun = input("Input Noun again: ")
    verb = input("Input Verb: ")
    sec_verb = input("Input Verb again: ")
    thrd_verb = input("Input Verb ending in ing: ")
    adverb = input("Input Adverb ending in ly: ")
    color = input("Input Color: ")
    sec_color = input("Input Color again: ")
    silly_word = input("Input Silly Word: ")
    second_template(person_name, number, time_measure, feeling, sec_feeling, animal, noun, color, adverb, verb, sec_number, sec_noun, sec_verb, thrd_verb, silly_word, sec_color)
if story_number == "3":
    person_name = input("Input Person name: ")
    verb = input("Input Verb: ")
    adjective = input("Input Adjective: ")
    sec_adjective = input("Input Adjective again: ")
    thrd_adjective = input("Input Adjective one more time: ")
    frth_adjective = input("Input Adjective one more time: ")
    fth_adjective = input("Input Adjective last time: ")
    noun = input("Input Noun: ")
    sec_noun = input("Input Noun again: ")
    thrd_noun = input("Input Plural noun: ")
    frth_noun = input("Input Plural noun again: ")
    fth_noun = input("Input Noun last time: ")
    magic_creature = input("Input Magical creature(Plural): ")
    sec_magical_creature = input("Input Magical creature(Plural) again: ")
    time_measure = input("Input Measure of time: ")
    room = input("Input Room: ")
    number = input("Input Number: ")
    color = input("Input Color: ")
    place = input("Input Place: ")
    animal = input("Input Animal: ")
    third_template(person_name, verb, adjective, sec_adjective, thrd_adjective, frth_adjective, fth_adjective, noun, sec_noun, thrd_noun, frth_noun, fth_noun, magic_creature, sec_magical_creature, time_measure, room, number, color, place, animal )