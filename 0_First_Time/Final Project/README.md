# PYLATRO
#### Video Demo:  <https://youtu.be/4rCDQDNjuJ0>
#### Description:
## What is it ?
Pylatro is a little program inspired by the video game **Balatro**, which is a Roguelike Poker game.

In Pylatro, you get deat 5 cards, and you can either "play" them, or discard some cards in hopes to get better ones and form the best possible poker hand.
Each card gives "chips" based on thier rank (e.g.: Ace gives 14 chips, Ten gives 10 chips, Five gives 5 chips, etc), and each type of poker hand (Pair, Three of a kind, Flush, etc) gives additional *chips* and a *multiplier* that applies to the sum of all the chips.

This version of Pylatro is in a VERY early stage of development, because I underestimated the work load and complexity of the task, and I rather submit this early, functional version that meets the requirements rather than getting stuck and delaying everything.

## How does it work ?
You must "import" a *deck* and a *hands* files as CSV. Pylatro will ask you to give their name and extension like so: name.csv.

**Why ?** Because in the FULL game, you should be able to upgrade each poker hand type so that they give mùore chips and a higher multiplier, and you can have more or less cards, with different effects. Furthermore, I wouold like to implement a probability counter for each hand and cards in deck in the future. This is a simple foundation for the upcoming improvements.

If the files do not meet the expected format, an error message will pop up, exiting the program.

If the files DO meet the requirements, the program will read the files, and deal 5 random cards from the *deck* file in the format [rank][suit]. The suit is displayed as the first letter of said suit: Clubs = C | Diamonds = D | Hearts = H | Spades = S.

You will then have the choice to either play the cards straight away, or discard some for new cards from the same deck.

e.g.: If your dealt hand is like so:
[3C, JackS, 7C, 3D, JackH], You can discard cards at places 1, 3 and 4 (3C, 7C and 3D) for new cards. **New cards cannot be cards that have previously been dealt.**

The program will then sum all the chips **from the cards in hand**, then add the chips from the formed hand, and multiply it by the value of the multiplier from the poker hand.

e.g. If we keep the same hand: The poker hand formed is a **Two Pair** consisting of the two *Jacks* and two *3*. Each earns chips **equal to their rank**. A *Two Pair* earns **20 chips** and a **multiplier of 2**.

The score will then be : ((3 + 11 + 7 + 3 + 11) + 20) * 2 = **110 points**

## Testing the program
The *test_project* is kind of messy because of the way I made the main code. Because we're getting informations from CSV files, I had to "simulate" dealt hands for each type of poker hands, and create some sort of "mock deck" to be able to verify the *replace* function.

But in the end, *pytest* tests 3 functions and all of them pass it.

## Design choices
I've made this version because at first I wanted to make some sort of tool for Balatro to give me the probability of drawing a specific card from my deck. But I quickly realized that it was much more complex and intricate that what I was imagining. And so I made the basic functionnalities of a "playable game" to meet the requirements of CS50's course to be sure that I was able to code something that works, and finishing the full mod/game in my spare time will be a project of my own.
