import numpy as np
import math as mt

all_possible_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def game_intro():
    print("Welcome to the Blackjack Game!")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards are worth 10, Aces can be 1 or 11.")
    print("Good luck!\n")
hand_of_player = []
hand_of_dealer = []
dealer_busted = False
player_stopped = False
def full_game():
    def start_hand():
        hand_of_player.append(np.random.choice(all_possible_cards))
        hand_of_player.append(np.random.choice(all_possible_cards))
        hand_of_dealer.append(np.random.choice(all_possible_cards))
        hand_of_dealer.append(np.random.choice(all_possible_cards))
        print(f"Your hand: {hand_of_player}, current score: {calculate_hand_value(hand_of_player)}")
        if calculate_hand_value(hand_of_dealer) == 21:
            print(f"Dealer's hand: {hand_of_dealer}, dealer has Blackjack! You lose.")
            option = input("Type 'y' to play again, 'n' to exit: ")
            if option == 'y':
                hand_of_player.clear()
                hand_of_dealer.clear()
                full_game()
            else:
                return
        elif calculate_hand_value(hand_of_player) == 21:
            print(f"Your hand: {hand_of_player}, you have Blackjack! You win!")
            option = input("Type 'y' to play again, 'n' to exit: ")
            if option == 'y':
                hand_of_player.clear()
                hand_of_dealer.clear()
                full_game()
            else:
                return
        else:
            player_turn()
    

    def calculate_hand_value(hand):
        value = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                aces += 1
                value += 11
            else:
                value += int(card)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    def player_turn():
        while True:
            option = input("Type 'y' to get another card, type 'n' to pass: ")
            if option == 'y':
                hand_of_player.append(np.random.choice(all_possible_cards))
                player_value = calculate_hand_value(hand_of_player)
                print(f"Your hand: {hand_of_player}, current score: {player_value}")
                print(f"Dealer's cards expect first card: ['{hand_of_dealer[1:-1]}', '?']")
                if player_value > 21 or player_value == 21:
                    determine_winner()
                    return
                dealer_turn_after_player()
            elif option == 'n':
                player_stopped = True
                dealer_turn_after_player_stopped()
                return
    def dealer_turn_after_player_stopped():
        while calculate_hand_value(hand_of_dealer) < 17 and dealer_busted == False:
            hand_of_dealer.append(np.random.choice(all_possible_cards))
            print(f"Dealer's hand: {hand_of_dealer}, dealer's score: {calculate_hand_value(hand_of_dealer)}")
        if calculate_hand_value(hand_of_dealer) > 21:
            print("Dealer busts! You win!")
        elif calculate_hand_value(hand_of_dealer) == 21:
            print("Dealer has Blackjack! You lose.")
        elif calculate_hand_value(hand_of_dealer) > calculate_hand_value(hand_of_player) or calculate_hand_value(hand_of_dealer) == calculate_hand_value(hand_of_player) or calculate_hand_value(hand_of_dealer) < calculate_hand_value(hand_of_player):
            determine_winner()
    
    def dealer_turn_after_player():
        while calculate_hand_value(hand_of_dealer) < 17 and dealer_busted == False:
            hand_of_dealer.append(np.random.choice(all_possible_cards))
            print(f"Dealer's hand: {hand_of_dealer}, dealer's score: {calculate_hand_value(hand_of_dealer)}")
        if calculate_hand_value(hand_of_dealer) > 21:
            print("Dealer busts! You win!")
            option = input("Type 'y' to play again, 'n' to exit: ")
            if option == 'y':
                hand_of_player.clear()
                hand_of_dealer.clear()
                full_game()
            else:
                return
        elif calculate_hand_value(hand_of_dealer) == 21:
            print("Dealer has Blackjack! You lose.")
            option = input("Type 'y' to play again, 'n' to exit: ")
            if option == 'y':
                hand_of_player.clear()
                hand_of_dealer.clear()
                full_game()
            else:
                return
        else:
            player_turn()
        
        
    def determine_winner():
        player_value = calculate_hand_value(hand_of_player)
        dealer_value = calculate_hand_value(hand_of_dealer)
        if (dealer_value > 21 or player_value > dealer_value) and player_value <= 21:
            print("dealer lost You win!")
            print(f"Dealer's final hand: {hand_of_dealer}, dealer's final score: {dealer_value}")
            dealer_busted = True
        elif dealer_value < 21 and (player_value < dealer_value or player_value > 21):
            print("You lose.")
            print(f"Dealer's final hand: {hand_of_dealer}, dealer's final score: {dealer_value}")
        else:
            print("It's a draw.")
            print(f"Dealer's final hand: {hand_of_dealer}, dealer's final score: {dealer_value}")
        option = input("Type 'y' to play again, 'n' to exit: ")
        if option == 'y':
            hand_of_player.clear()
            hand_of_dealer.clear()
            full_game()
        else:
            return
    start_hand()
game_intro()
full_game()
        