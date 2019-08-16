import random
from country_capital_subregion import country_capital_subregion

def q_and_a():

    country, capital, subregion = random.choice(country_capital_subregion)
    incorrect_capitals = []

    for x, y, z in country_capital_subregion:
        if z == subregion:
            incorrect_capitals.append(y)

    incorrect_capital_1, incorrect_capital_2, incorrect_capital_3 = random.sample(incorrect_capitals, 3)
    answers = [incorrect_capital_1, incorrect_capital_2, incorrect_capital_3, capital]
    random.shuffle(answers)

    choice = {
            'a': answers[0],
            'b': answers[1],
            'c': answers[2],
            'd': answers[3]
        }

    correct_choice = ([k for k,v in choice.items() if v == capital])
    correct_choice_string = str(correct_choice[0])
    return capital, country, choice, correct_choice_string

def game():
    points = 1
    while points > 0:
        capital, country, choice, correct_choice_string = q_and_a()
        print("What is the capital of", country, "?")
        print("")
        print("Choice 'a' :", choice.get('a'))
        print("Choice 'b' :", choice.get('b'))
        print("Choice 'c' :", choice.get('c'))
        print("Choice 'd' :", choice.get('d'))
        print("")
        print("You have", points, "point(s).")
        response = input('\nHit \'a\', \'b\', \'c\' or \'d\' for your answer\n')
        if response == correct_choice_string:
            points = points + 1
            print("Yeah, you doin' well. Let's do another one.")
        else:
            points = points - 1
            if points == 0:
                print("You have", points, "points.")
                print("Study harder, dude.")
                print("Game Over. You are done.")
            else:
                print("You have", points, "point(s) left. Try harder.")

game()


