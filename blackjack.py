import numpy as np
import math as mt

all_possible_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
red_text = '\033[91m'
green_text = '\033[92m'
cyan_text = '\033[96m'
yellow_text = '\033[93m'

def game_intro():
    print(yellow_text +"***********************************************************")
    print(yellow_text +"|Welcome to the Blackjack Game!                           |")
    print(yellow_text +"|Try to get as close to 21 as possible without going over.|")
    print(yellow_text +"|Face cards are worth 10, Aces can be 1 or 11.            |")
    print(yellow_text +"|Good luck!\n                                             |")
    print(yellow_text +"***********************************************************")
hand_of_player = []
hand_of_dealer = []
dealer_busted = False
player_stopped = False
def start_hand():
    global hand_of_player, hand_of_dealer, dealer_busted, player_stopped
    hand_of_player = []
    hand_of_dealer = []
    dealer_busted = False
    player_stopped = False
    for _ in range(2):
        hand_of_player.append(str(np.random.choice(all_possible_cards)))
        hand_of_dealer.append(str(np.random.choice(all_possible_cards)))
        
def player_hit():
    global hand_of_player
    hand_of_player.append(str(np.random.choice(all_possible_cards)))
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
def dealer_play():
    global hand_of_dealer, dealer_busted
    while calculate_hand_value(hand_of_dealer) < 17 and not dealer_busted:
        hand_of_dealer.append(str(np.random.choice(all_possible_cards)))
    if calculate_hand_value(hand_of_dealer) > 21:
        dealer_busted = True
def check_winner():
    player_value = calculate_hand_value(hand_of_player)
    dealer_value = calculate_hand_value(hand_of_dealer)
    if player_value > 21:
        return red_text + "Player busts! Dealer wins."
    elif dealer_busted:
        return green_text + "Dealer busts! Player wins."
    elif (player_value > dealer_value or player_value == 21) and player_value <= 21:
        return green_text + "Player wins!"
    elif (dealer_value > player_value or dealer_value == 21) and dealer_value <= 21:
        return red_text + "Dealer wins!"
    else:
        return cyan_text + "It's a tie!"
    
def player_stand():
    global player_stopped
    player_stopped = True

def main():
    game_intro()
    start_hand()
    while not player_stopped:
        print(f"{green_text}Player's hand: {hand_of_player} (Value: {calculate_hand_value(hand_of_player)})")
        print(f"{yellow_text}Dealer's hand: [{hand_of_dealer[0]}, '?']")
        actions = input(yellow_text +"Do you want to 'hit' or 'stand'? ").lower()
        if actions == 'hit':
            player_hit()
            if calculate_hand_value(hand_of_player) > 21:
                break
        elif actions == 'stand':
            player_stand()
        else:
            print(red_text +"Invalid input. Please enter 'hit' or 'stand'.")
    dealer_play()
    print(f"{yellow_text}  Dealer's hand: {hand_of_dealer} (Value: {calculate_hand_value(hand_of_dealer)})")
    print(check_winner())
    play_again = input(yellow_text +"Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print(red_text +"Thanks for playing!")

main()

