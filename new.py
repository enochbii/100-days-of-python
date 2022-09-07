import random
from replit import clear

def deal_card():
    """Return the random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score from the calculated cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


#hint 13: create function called compare() and pass in the user_score and computer_score. if the computer and user both have same score, then it's a draw. if the computer has a blackjack (0), then the user losses. if the computer_score is over 21, then the computer loses. If none of the above, then the player with the highst score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a Blackjack "
    elif user_score > 21:
        return "you went over . you lose "
    elif computer_score > 21:
        return "your opponent went over . You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
      new_card = deal_card()
      user_cards.append(new_card)
      computer_cards.append(new_card)
  # hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  
  while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"Your cards: {user_cards}, current score:{user_score}")
      print(f" computer's first card:{computer_cards[0]}")
  
      if user_score == 0 or computer_score == 0 or user_score > 21:
          is_game_over = True
      else:
          user_should_deal = input(
              "Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == "y":
              user_cards.append(new_card)
          else:
              is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(new_card)
      computer_score = calculate_score(computer_cards)
  
  print(f" your final hand : {user_cards}, final score {user_score}")
  print(compare(user_score, computer_score))



while input("do you want to play a game of blackjack? Type 'y' or 'n': ")=='y':
  clear()
  play_game()
  