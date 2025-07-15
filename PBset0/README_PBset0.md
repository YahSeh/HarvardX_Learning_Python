# Problem Set 0 - Functions, Variables
<h1>Indoor Voice</h1>

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

<h3>How to test</h3>

  Here’s how to test your code manually. At the indoor/ $ prompt in your terminal:

<li>Run your program with python indoor.py. Type HELLO and press Enter. Your program should output hello.</li>
<li>Run your program with python indoor.py. Type THIS IS CS50 and press Enter. Your program should output this is cs50.</li>
<li>Run your program with python indoor.py. Type 50 and press Enter. Your program should output 50.</li>
<br>
If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your indoor folder and have saved your indoor.py file there. Remember how?

<h1>Playback Speed</h1>

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with "..." (i.e., three periods).

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output: This...is...CS50    </li>
<li>Run your program with python playback.py. Type This is our week on functions and press Enter. Your program should output: This...is...our...week...on...functions</li>
<li>Run your program with python playback.py. Type Let's implement a function called hello and press Enter. Your program should output: Let's...implement...a...function...called...hello</li>
<br>

<h1>Making Faces</h1>

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

<h3>How to test</h3>

  Here’s how to test your code manually. At the indoor/ $ prompt in your terminal:

<li>Run your program with python faces.py. Type Hello :) and press Enter. Your program should output: Hello 🙂</li>
<li>Run your program with python faces.py. Type Goodbye :( and press Enter. Your program should output: Goodbye 🙁</li>
<li>Run your program with python faces.py. Type Hello :) Goodbye :( and press Enter. Your program should output: Hello 🙂 Goodbye 🙁</li>
<br>

<h1>Einstein</h1>

Even if you haven’t studied physics (recently or ever!), you might have heard that E=mc², wherein E represents energy (measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.your own as an argument to input. Be sure to call main at the bottom of your file.

<h3>How to test</h3>

  Here’s how to test your code manually. At the indoor/ $ prompt in your terminal:

<li>Run your program with python einstein.py. Type 1 and press Enter. Your program should output: 90000000000000000</li>
<li>Run your program with python einstein.py. Type 14 and press Enter. Your program should output: 1260000000000000000</li>
<li>Run your program with python einstein.py. Type 50 and press Enter. Your program should output: 4500000000000000000</li>
<br>

<h1>Tip Calculator</h1>

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

def main():<br>
    dollars = dollars_to_float(input("How much was the meal? "))<br>
    percent = percent_to_float(input("What percentage would you like to tip? "))<br>
    tip = dollars * percent<br>
    print(f"Leave ${tip:.2f}")<br>


def dollars_to_float(d):<brW
    # TODO<br>


def percent_to_float(p):<br>
    # TODO<br>


main()<br>

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
<li>dollars_to_float, which should accept a str as input (formatted as "$##.##", wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.</li>
<li>percent_to_float, which should accept a str as input (formatted as "##%", wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.</li>

<h3>How to test</h3>

  Here’s how to test your code manually. At the indoor/ $ prompt in your terminal:

<li>Run your program with python tip.py. Type $50.00 and press Enter. Then, type 15% and press Enter. Your program should output: Leave $7.50    </li>
<li>Run your program with python tip.py. Type $100.00 and press Enter. Then, type 18% and press Enter. Your program should output: Leave $18.00</li>
<li>Run your program with python tip.py. Type $15.00 and press Enter. Then, type 25% and press Enter. Your program should output: Leave $3.75</li>
<br>
