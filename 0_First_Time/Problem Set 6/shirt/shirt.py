import sys, csv, glob
from os.path import splitext
from PIL import Image, ImageOps

def main() :
    check_args()
    try :
        img_input = Image.open(sys.argv[1])
    except FileNotFoundError :
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    img_bg = ImageOps.fit(img_input, size)
    img_bg.paste(shirt, shirt)
    img_bg.save(sys.argv[2])


def check_args() :
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")

    allowed = ['jpeg', 'jpg', 'png']
    name, ext = str(sys.argv[1]).split(".")
    name2, ext2 = str(sys.argv[2]).split(".")

    if not ext in allowed and not ext2 in allowed :
        sys.exit("Invalid output")
    elif ext != ext2 :
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
