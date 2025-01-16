import pytest
from unittest.mock import patch
from project import hand_counting, hand_checking, user_choice

def main() :
    test_hand_checking()
    test_hand_counting()
    test_replace_cards()


def test_hand_checking() :
    poker_hands_values = {
        "High Card": {"chips": 5, "mult": 1},
        "Pair": {"chips": 10, "mult": 2},
        "Two Pair": {"chips": 20, "mult": 2},
        "Three of a Kind": {"chips": 30, "mult": 3},
        "Straight": {"chips": 30, "mult": 4},
        "Flush": {"chips": 35, "mult": 4},
        "Full House": {"chips": 40, "mult": 4},
        "Four of a Kind": {"chips": 60, "mult": 7},
        "Straight Flush": {"chips": 100, "mult": 8},
    }

    hand = [(5, "FiveH", 5), (3, "ThreeD", 3), (10, "TenS", 10), (8, "EightC", 8), (12, "QueenH", 10)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "High Card"
    assert chips == 5  # Expected chips from "High Card"
    assert multiplier == 1  # Expected multiplier from "High Card"

    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (2, "TwoS", 2), (8, "EightC", 8), (10, "TenH", 10)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Pair"
    assert chips == 10
    assert multiplier == 2

    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (7, "SevenS", 7), (7, "SevenC", 7), (10, "TenH", 10)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Two Pair"
    assert chips == 20
    assert multiplier == 2

    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (5, "FiveS", 5), (8, "EightC", 8), (10, "TenH", 10)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Three of a Kind"
    assert chips == 30
    assert multiplier == 3

    hand = [(5, "FiveH", 5), (6, "SixD", 6), (9, "NineS", 8), (8, "EightC", 8), (7, "SevenH", 7)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Straight"
    assert chips == 30
    assert multiplier == 4

    hand = [(5, "FiveH", 5), (6, "SixH", 6), (2, "TwoH", 2), (8, "EightH", 8), (7, "SevenH", 7)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Flush"
    assert chips == 35
    assert multiplier == 4

    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (5, "FiveS", 5), (8, "EightC", 8), (8, "EightH", 8)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Full House"
    assert chips == 40
    assert multiplier == 4

    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (5, "FiveS", 5), (5, "FiveC", 5), (10, "TenH", 10)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Four of a Kind"
    assert chips == 60
    assert multiplier == 7

    hand = [(5, "FiveH", 5), (6, "SixH", 6), (9, "NineH", 8), (8, "EightH", 8), (7, "SevenH", 7)]
    hand_name, chips, multiplier = hand_checking(hand, poker_hands_values)
    assert hand_name == "Straight Flush"
    assert chips == 100
    assert multiplier == 8



def test_hand_counting() :
    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (2, "TwoS", 2), (8, "EightC", 8), (10, "TenH", 10)]
    hand_chips = 10
    hand_mult = 2
    assert hand_counting(hand, hand_chips, hand_mult) == 80


def test_replace_cards(capsys) :
    hand = [(5, "FiveH", 5), (5, "FiveD", 5), (2, "TwoS", 2), (8, "EightC", 8), (10, "TenH", 10)]
    deck = hand * 2
    dealt_cards = hand.copy()

    with patch("builtins.input", side_effect=["2", "a b c", "1"]):
        user_choice(hand, deck, dealt_cards)

        captured = capsys.readouterr()
        assert "Invalid input. Please enter numbers corresponding to the card positions (1-5)." in captured.out

if __name__ == "__main__":
    main()
