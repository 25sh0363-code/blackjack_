import numpy as np
import math as mt
import streamlit as st
import random

#byyy omiii.                The best black game i made ;)


all_possible_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ["❤️","♦️","♣️","♠️"]


        
def deal_card():
    return (random.choice(all_possible_cards), random.choice(suits))   #simple deal card function nothing special

def get_card_html(card,hidden=False):
    if hidden:
        return"""
        <div style="border:5px white solid; border-radius:10px; width:80px; height:120px; background-color:black; display:flex; justify-content:center; align-items:center;">
            <div style="color:white; font-weight:bold; font-size:24px;">🂠</div>
        </div>
        """
    rank = card[0]

    if card[1] in ["❤️","♦️"]:
        color = "red"
    else:
        color = "black"
    
    return f"""
    <div style="border:1px solid black; border-radius:10px; width:80px; height:120px; display:flex; flex-direction:column; justify-content:space-between; padding:5px; background-color:white;">
        <div style="color:{color}; font-weight:bold;">{rank}{card[1]}</div>
        <div style="color:{color}; font-weight:bold; transform:rotate(180deg);">{rank}{card[1]}</div>
    </div>
    """

def display_hand(hand,hide_first_card=False):
    rand = ""
    for i,card in enumerate(hand):
        if i == 0 and hide_first_card:
            rand += get_card_html(card,hidden=True)
        else:
            rand += get_card_html(card)
    st.markdown(rand,unsafe_allow_html=True)
    


def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11                    #calculate hand function i learnt in kaggle
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def reset_game():
    st.session_state.player_hand = [deal_card(), deal_card()]
    st.session_state.dealer_hand = [deal_card(), deal_card()]
    st.session_state.gameover = False                                  #reset game function
    st.session_state.result = ""

st.title("🎶Streamlit Blackjack🤩")

if "player_hand" not in st.session_state:
    st.session_state.player_hand = [deal_card(),deal_card()]
    st.session_state.dealer_hand = [deal_card(),deal_card()]          #start hand function not a function but yea..🥀
    st.session_state.gameover = False
    st.session_state.result = ""

col1, col2 = st.columns(2)

with col1:
    st.subheader("your hand🖐️")
    display_hand(st.session_state.player_hand)
    player_score = calculate_hand_value(st.session_state.player_hand)
    st.metric("your score🙈",player_score)


with col2:
    st.header("dealer's hand🤚")
    if st.session_state.gameover:
        display_hand(st.session_state.dealer_hand)
        dealer_score = calculate_hand_value(st.session_state.dealer_hand)
        st.metric("dealer score🙉",dealer_score)
    else:
        display_hand(st.session_state.dealer_hand,hide_first_card=True)
        dealer_score = calculate_hand_value([st.session_state.dealer_hand[1]])
        st.metric("dealer score🙉",dealer_score)

st.divider()

if not st.session_state.gameover:
    col_1 ,col_2 =st.columns(2)

    with col_1:
        if st.button("hit!☝"):
            st.session_state.player_hand.append(deal_card())
            player_score = calculate_hand_value(st.session_state.player_hand)
            if player_score > 21:                                                 #button column 1 for hit button
                st.session_state.result = "you busted! dealer wins😵"
                st.session_state.gameover = True
            elif player_score == 21:
                st.session_state.result = "blackjack! you win!🥳"
                st.session_state.gameover = True
            st.rerun()
    with col_2:
        if st.button("stand!✋"):
            st.session_state.gameover = True
            dealer_score = calculate_hand_value(st.session_state.dealer_hand)
            while dealer_score < 17:
                st.session_state.dealer_hand.append(deal_card())
                dealer_score = calculate_hand_value(st.session_state.dealer_hand)
            player_score = calculate_hand_value(st.session_state.player_hand)               #button column 2 for stand button
            if dealer_score > 21:
                st.session_state.result = "dealer busted! you win!🥳"
            elif dealer_score > player_score:
                st.session_state.result = "dealer wins😵"
            elif dealer_score < player_score and player_score <= 21:
                st.session_state.result = "you win!🥳"
            else:
                st.session_state.result = "it's a draw!🤝"
            st.session_state.gameover = True
            st.rerun()
else:
    st.success(st.session_state.result)       #play again button
    if st.button("play again🔄"):
        reset_game()
        st.rerun()

                    







