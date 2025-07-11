import csv
import sys
import random
from collections import Counter

def main():
    while True:
        try:
            deck_filename = str(input("Welcome to Project Pylatro ! (This is an early/small version)\nWhat is the name of your 'deck' file ? (e.g., 'deck.csv')\n"))
            hands_filename = str(input("And what is the name of your 'hands' file ?\n"))

            ls_deck_filename = deck_filename.split(".")
            ls_hands_filename = hands_filename.split(".")

            if len(ls_deck_filename) == 2 and len(ls_hands_filename) == 2:
                ext_deck = ls_deck_filename[1]
                ext_hands = ls_hands_filename[1]

                if not ext_deck == "csv" or not ext_hands == "csv":
                    sys.exit("File(s) is not a CSV file. It needs to have the extension '.csv'\n")

                else:
                    deck = load_deck_csv(deck_filename)
                    poker_hands = load_poker_hands_csv(hands_filename)
                    dealt_hand = hand_dealing(deck)
                    dealt_cards = dealt_hand.copy()

                    print(f"\nDealt hand: {[card[1] for card in dealt_hand]}")

                    played_hand = user_choice(dealt_hand, deck, dealt_cards)
                    hand_name, hand_chips, hand_mult = hand_checking(dealt_hand, poker_hands)
                    score_hand = hand_counting(played_hand, hand_chips, hand_mult)

                    print(f"The hand is a {hand_name} and gives {hand_chips} chips with a multiplier of {hand_mult}")
                    print(f"Score from this hand: {score_hand}\n")
                    break

            elif len(ls_deck_filename) < 2 or len(ls_hands_filename) < 2:
                sys.exit("File(s) does not have an extension. File needs to be in the format 'name.csv'\n")

            elif len(ls_deck_filename) > 2 or len(ls_hands_filename) > 2:
                sys.exit("Too many extensions. File(s) needs to be in the format 'name.csv'\n")

        except FileNotFoundError:
            sys.exit("File(s) does not exist. Check the spelling\n")


def load_deck_csv(deck_filename):
    deck = []

    with open(deck_filename, "r") as csvdeck:
        deck_csv = csv.DictReader(csvdeck)

        for row in deck_csv:
            rank_value = int(row['Rank'])
            name = row['Name']
            suit = row['Suit'][0]
            chips = int(row['Chips'])
            card = (rank_value, name + suit, chips)
            deck.append(card)

    return deck


def load_poker_hands_csv(hands_filename):
    poker_hands = {}

    with open(hands_filename, "r") as csvhands:
        hands_csv = csv.DictReader(csvhands)

        for row in hands_csv:
            hand = row['Hand']
            chips = int(row['Base_chips'])
            mult = int(row['Base_mult'])
            poker_hands[hand] = {'chips': chips, 'mult': mult}

    return poker_hands


def hand_dealing(deck, hand_size=5):
    dealt_hand = random.sample(deck, hand_size)

    return dealt_hand


def user_choice(hand, deck, dealt_cards):
    while True:
        choice = input("Do you want to (1) play the hand or (2) discard some cards? Type 1 or 2: ")

        if choice == '1':
            print("You chose to play the hand.")

            return hand

        elif choice == '2':
            print("You chose to discard some cards.")

            print("Enter the card positions you want to discard (1-5), separated by spaces (e.g., '1 3 4').")
            discard_input = input("Positions to discard: ")

            try:
                discard_positions = [int(pos) - 1 for pos in discard_input.split()]

                if all(0 <= pos < len(hand) for pos in discard_positions):
                    new_hand = replace_cards(hand, discard_positions, deck, dealt_cards)
                    print(f"Your new hand: {[card[1] for card in new_hand]}")
                    pass

                else:
                    print("Invalid positions entered. Please try again.")

            except ValueError:
                print("Invalid input. Please enter numbers corresponding to the card positions (1-5).")

        else:
            print("Invalid choice. Please type '1' or '2'.")


def replace_cards(hand, discard_positions, deck, dealt_cards):
    discard_positions = sorted(discard_positions)

    remaining_deck = [card for card in deck if card not in dealt_cards]

    new_cards = random.sample(remaining_deck, len(discard_positions))

    for index, new_card in zip(discard_positions, new_cards):
        hand[index] = new_card

    dealt_cards.extend(new_cards)

    return hand


def hand_checking(hand, poker_hands_values):
    rank_values = [card[0] for card in hand]
    suits = [card[1][-1] for card in hand]
    rank_values = sorted(rank_values)

    rank_counts = Counter(rank_values)
    suit_counts = Counter(suits)

    is_flush = len(suit_counts) == 1
    is_straight = all(rank_values[i] + 1 == rank_values[i + 1] for i in range(4))

    if is_flush and is_straight:
        hand_name = "Straight Flush"
    elif 4 in rank_counts.values():
        hand_name = "Four of a Kind"
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        hand_name = "Full House"
    elif is_flush:
        hand_name = "Flush"
    elif is_straight:
        hand_name = "Straight"
    elif 3 in rank_counts.values():
        hand_name = "Three of a Kind"
    elif list(rank_counts.values()).count(2) == 2:
        hand_name = "Two Pair"
    elif 2 in rank_counts.values():
        hand_name = "Pair"
    else:
        hand_name = "High Card"

    hand_info = poker_hands_values.get(hand_name, {'chips': 0, 'mult': 1})
    poker_hand_chips = hand_info['chips']
    poker_hand_mult = hand_info['mult']

    return hand_name, poker_hand_chips, poker_hand_mult


def hand_counting(hand, hand_chips, hand_mult):
    total_hand_chips =  sum(card[2] for card in hand) + hand_chips
    score = total_hand_chips * hand_mult

    return score


if __name__ == "__main__":
    main()
