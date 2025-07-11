import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

def main () :

    if len(sys.argv) == 1 :
        txt = str(input("Input : "))
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(txt))

    elif (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in fonts) :
        txt = str(input("Input : "))
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(txt))

    else :
        sys.exit("Invalid usage")

main()
