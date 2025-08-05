############### Blackjack Project #####################


import random
import os
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    y_cards = random.choice(cards)
    return y_cards
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())



    def compare(u_score, c_score):
      """Compares the final score of user and computer"""
      if u_score == c_score:
        return "Draw"
      elif c_score =="0":
        return "User loses the game"
      elif u_score == "0":
        return "User wins the game"
      elif c_score >21:
        return "User wins the game"
      elif u_score >21:
        return "User loses the game"
      elif u_score > c_score:
        return "User wins the game"
      else:
        return "User loses the game"


    def calculate_score(cards):
      """Calculates the score of both the user and computer"""

      if sum(cards) == 21 and len(cards) == 2:
        return 0

      if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

      return sum(cards)

    while not is_game_over:
      user_score = calculate_score(user_cards)
      comp_score = calculate_score(computer_cards)
      print(f"User's cars: {user_cards} and score: {user_score}")
      print(f"Computer's First card: {computer_cards[0]}")
    
      if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
      else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
        if user_should_deal == "y":
          user_cards.append(deal_card())
        else:
          is_game_over = True


      while comp_score!=0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    
    print(f"Computer's cards were {computer_cards} and Computer's Final score is {comp_score}")
    print(compare(user_score,comp_score))


while input("Do you want to play the BlackJack game? 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()
    



