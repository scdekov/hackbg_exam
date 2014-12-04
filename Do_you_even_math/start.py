from expression import Expression
from players import Player
from connection import *
import random


class Do_you_even_math:

    def __init__(self):
        Base.metadata.create_all(engine)

    def generate_random_expression(self):
        operator = random.choice(['+', '-', '*', '^'])
        if operator == '^':
            first_operand = random.randint(1, 5)
            second_operand = random.randint(1, 5)
        elif operator in '+*-':
            first_operand = random.randint(1, 20)
            second_operand = random.randint(1, 20)
        else:
            first_operand = random.randint(1, 20)
            second_operand = random.randint(1, 20)
            while first_operand % second_operand != 0:
                first_operand = random.randint(1, 20)
                second_operand = random.randint(1, 20)
        if operator == '-' and first_operand < second_operand:
            first_operand += second_operand

        return Expression(first_operand, second_operand, operator)

    def start_game(self):
        command = input("""Welcome to the "Do you even math?" game!
Here are your options:
- start
- highscores
>""")
        while True:
            if command == 'start':
                player_name = input("Enter your playername>")
                print("Welcome {}! Let the game begin!".format(player_name))
                expr_counter = 1
                right_answers = 0
                while(True):
                    print("=" * 10)
                    print("Question #{}:".format(expr_counter))
                    crr_expr = self.generate_random_expression()
                    answer = input(crr_expr)
                    if int(answer) == crr_expr.value():
                        print("Correct !")
                        right_answers += 1
                    else:
                        score = right_answers * right_answers
                        print("=" * 10)
                        print("Incorrect! Ending game. You score is: {}".format(score))
                        print("=" * 10)
                        session.add(Player(name=player_name, points=score))
                        break
                    expr_counter += 1
            elif command == 'highscores':
                highscores = session.query(Player).order_by(Player.points.desc())
                print("=" * 10)
                players_counter = 1
                for player in highscores:
                    print(players_counter, player)
                    players_counter += 1
                print("=" * 10)
            elif command == 'exit':
                break
            else:
                print("Wrong command!")
            command = input("""Here are your options:
- start
- highscores
>""")
        session.commit()


game = Do_you_even_math()
game.start_game()


