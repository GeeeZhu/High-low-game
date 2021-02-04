from game_data import data
from art import logo,vs

# import random to choose an element from a list
import random
from replit import clear

def generate_account():
  return random.choice(data)

def format_data(compare_x):
  name_x = compare_x["name"]
  description_x = compare_x["description"]
  country_x = compare_x["country"]
  return f"{name_x}, a {description_x}, {country_x}."

def compare(choice,follower_count_1,follower_count_2):
  if follower_count_1 > follower_count_2:
    answer = "A"
  else:
    answer = "B"

  if choice == answer:
    return True
  else:
    return False


def game():
  clear()
  compare_1 = generate_account()
  compare_2 = generate_account()
  if compare_2 == compare_1:
    compare_2 = generate_account()

  continue_to_play = True
  while continue_to_play:
    print(logo)

    print(f"Compare A: {format_data(compare_1)}.")
    print(vs)
    print(f"Against B: {format_data(compare_2)}.")

    choice = input("Who has more followers? Type 'A' or 'B':")
    follower_count_1 = compare_1["follower_count"]
    follower_count_2 = compare_2["follower_count"]

    result = compare(choice,follower_count_1,follower_count_2)

    score = 0
    if result == True:
      score += 1
      print(f"You're right! Current score: {score}.")
      continue_to_play = True
    else:
      print(f"Sorry, that's wrong. Final score: {score}.")
      continue_to_play = False


game()
