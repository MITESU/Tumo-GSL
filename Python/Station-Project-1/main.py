import random

def text_input(prompt):
    value = input(prompt).strip()
    while value == "":
        print(" empty input")
        value = input(prompt).strip()
    return value

def text_input(prompt):
    value = input(prompt).strip()
    while True:
        if value == "":
            print(" empty input")
        else:
            try:
                float(value)
                return value
            except ValueError:
                print(f" '{value}' invalid input")
        value = input(prompt).strip()


def first_template(number, time_measure, transport_mode, adjective, sec_adjective, noun, color, body_part, verb, sec_number, sec_noun, thrd_noun, sec_body_part, frth_noun, thrd_adjective, silly_word):
    print(f"""It was about {number} {time_measure} ago when
        I arrived at the hospital in a {transport_mode}. The
        hospital is a/an {adjective} place, there are a lot
        of {sec_adjective} {noun} here. There are nurses here
        who have {color} {body_part}. If someone wants to come
        into my room I told them that they have to {verb} first.
        I've decorated my room with {sec_number} {sec_noun}. Today
        I talked to a doctor and they were wearing a {thrd_noun} on
        their {sec_body_part}. I heard that all doctors
        {verb} {frth_noun} every day for breakfast. The most
        {thrd_adjective} thing about being in the hospital
        is the {silly_word} {noun} !""")


def second_template(person_name, number, time_measure, feeling, sec_feeling, animal, noun, color, adverb, verb, sec_number, sec_noun, sec_verb, thrd_verb, silly_word, sec_color):
    print(f"""This weekend I am going camping with {person_name}.
        I packed my lantern, sleeping bag, and {noun}. I am so
        {feeling} to {verb} in a tent.I am {sec_feeling}
        we might see a(n) {animal}, I hear they're kind of dangerous.
        While we're camping, we are going to hike, fish, and {sec_verb}.
        I have heard that the {color} lake is great for {thrd_verb}.
        Then we will {adverb} hike through the forest for {number}
        {time_measure}. If I see a {sec_color} {animal} while hiking,
        I am going to bring it home as a pet! At night we will tell
        {sec_number} {silly_word} stories and roast {sec_noun} around the campfire!!""")


def third_template(person_name, verb, adjective, sec_adjective, thrd_adjective, frth_adjective, fth_adjective, noun, sec_noun, thrd_noun, frth_noun, fth_noun, magic_creature, sec_magical_creature, time_measure, room, number, color, place, animal):
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
    print(f" '{story_number}' invalid input")
    story_number = input("Chose template (1-3) ")
template = random.choice([int(story_number), 1, 2, 3])
print(f"Chosen template: {story_number}")
print(f"Random template: {template}")

if story_number == "1":
    number = text_input("Input Number: ")
    sec_number = text_input("Input Number again: ")
    time_measure = text_input("Input Measure of time: ")
    transport_mode = text_input("Input Mode of transportation: ")
    adjective = text_input("Input Adjective: ")
    sec_adjective = text_input("Input Adjective again: ")
    thrd_adjective = text_input("Input Adjective last time: ")
    noun = text_input("Input Noun: ")
    sec_noun = text_input("Input Noun again: ")
    thrd_noun = text_input("Input Noun one more time: ")
    frth_noun = text_input("Input Noun last time: ")
    color = text_input("Input Color: ")
    body_part = text_input("Input Part of the body: ")
    sec_body_part = text_input("Input Part of the body again: ")
    verb = text_input("Input Verb: ")
    silly_word = text_input("Input Silly Word: ")
    first_template(number, time_measure, transport_mode, adjective, sec_adjective, noun, color, body_part, verb, sec_number, sec_noun, thrd_noun, sec_body_part, frth_noun, thrd_adjective, silly_word)

if story_number == "2":
    number = text_input("Input Number: ")
    sec_number = text_input("Input Number again: ")
    time_measure = text_input("Input Measure of time: ")
    person_name = text_input("Input Person name: ")
    feeling = text_input("Input Feeling: ")
    sec_feeling = text_input("Input Feeling again: ")
    animal = text_input("Input Animal: ")
    noun = text_input("Input Noun: ")
    sec_noun = text_input("Input Noun again: ")
    verb = text_input("Input Verb: ")
    sec_verb = text_input("Input Verb again: ")
    thrd_verb = text_input("Input Verb ending in ing: ")
    adverb = text_input("Input Adverb ending in ly: ")
    color = text_input("Input Color: ")
    sec_color = text_input("Input Color again: ")
    silly_word = text_input("Input Silly Word: ")
    second_template(person_name, number, time_measure, feeling, sec_feeling, animal, noun, color, adverb, verb, sec_number, sec_noun, sec_verb, thrd_verb, silly_word, sec_color)

if story_number == "3":
    person_name = text_input("Input Person name: ")
    verb = text_input("Input Verb: ")
    adjective = text_input("Input Adjective: ")
    sec_adjective = text_input("Input Adjective again: ")
    thrd_adjective = text_input("Input Adjective one more time: ")
    frth_adjective = text_input("Input Adjective one more time: ")
    fth_adjective = text_input("Input Adjective last time: ")
    noun = text_input("Input Noun: ")
    sec_noun = text_input("Input Noun again: ")
    thrd_noun = text_input("Input Plural noun: ")
    frth_noun = text_input("Input Plural noun again: ")
    fth_noun = text_input("Input Noun last time: ")
    magic_creature = text_input("Input Magical creature(Plural): ")
    sec_magical_creature = text_input("Input Magical creature(Plural) again: ")
    time_measure = text_input("Input Measure of time: ")
    room = text_input("Input Room: ")
    number = text_input("Input Number: ")
    color = text_input("Input Color: ")
    place = text_input("Input Place: ")
    animal = text_input("Input Animal: ")
    third_template(person_name, verb, adjective, sec_adjective, thrd_adjective, frth_adjective, fth_adjective, noun, sec_noun, thrd_noun, frth_noun, fth_noun, magic_creature, sec_magical_creature, time_measure, room, number, color, place, animal)