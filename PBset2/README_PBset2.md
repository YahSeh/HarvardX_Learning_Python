# Problem Set 2 - Loops
<h1>camelCase</h1>

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python camel.py. Type name and press Enter. Your program should output: name   </li>
<li>Run your program with python camel.py. Type firstName and press Enter. Your program should output: first_name</li>
<li>Run your program with python camel.py. Type preferredFirstName and press Enter. Your program should output: preferred_first_name</li>
<br>

<h1>Coke Machine</h1>

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter. Your program should output: Amount Due: 25 and continue prompting the user for coins.</li>
<li>Run your program with python coke.py. At your Insert Coin: prompt, type 10 and press Enter. Your program should output: Amount Due: 40 and continue prompting the user for coins.</li>
<li>Run your program with python coke.py. At your Insert Coin: prompt, type 5 and press Enter. Your program should output: Amount Due: 45 and continue prompting the user for coins.</li>
<li>Run your program with python coke.py. At your Insert Coin: prompt, type 30 and press Enter. Your program should output: Amount Due: 50 because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.</li>
<li>Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter, then type 25 again and press Enter. Your program should halt and display: Change Owed: 0</li>
<li>Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter, then type 10 and press Enter. Type 25 again and press Enter, after which your program should halt and display: Change Owed: 10</li>
<br>

<h1>Just setting up my twttr</h1>

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python twttr.py. Type Twitter and press Enter. Your program should output:Twttr   </li>
<li>Run your program with python twttr.py. Type What's your name? and press Enter. Your program should output: Wht's yr nm?</li>
<li>Run your program with python twttr.py. Type CS50 and press Enter. Your program should output: CS50</li>
<br>

<h1>Vanity Plates</h1>

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

<li>“All vanity plates must start with at least two letters.”
<li>“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
<li>“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
<li>“No periods, spaces, or punctuation marks are allowed.”
<br>
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python plates.py. Type CS50 and press Enter. Your program should output: Valid</li>
<li>Run your program with python plates.py. Type CS05 and press Enter. Your program should output: Invalid</li>
<li>Run your program with python plates.py. Type CS50P and press Enter. Your program should output: Invalid</li>
<li>Run your program with python plates.py. Type PI3.14 and press Enter. Your program should output: Invalid</li>
<li>Run your program with python plates.py. Type H and press Enter. Your program should output: Invalid</li>
<li>Run your program with python plates.py. Type OUTATIME and press Enter. Your program should output: Invalid</li>
<br>

<h1>Nutrition Facts</h1>

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

<h3>How to test</h3>

  Here’s how to test your code manually:

<li>Run your program with python nutrition.py. Type Apple and press Enter. Your program should output: Calories: 130   </li>
<li>Run your program with python nutrition.py. Type Avocado and press Enter. Your program should output: Calories: 50</li>
<li>Run your program with python nutrition.py. Type Sweet Cherries and press Enter. Your program should output: Calories: 100</li>
<li>Run your program with python nutrition.py. Type Tomato and press Enter. Your program should output nothing.</li>
<br>
Be sure to try other fruits and vary the casing of your input. Your program should behave as expected, case-insensitively.
