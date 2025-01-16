
type = ['gif','jpg','jpeg','png','txt','pdf','zip']
ext = ['gif','jpeg','jpeg','png','plain','pdf','zip']

def main():
    file = input("File name : ").lower().strip()
    i = 0
    while i < len(type) :
        if (file[-3:] == type[i]) or (file[-4:] == type[i]) :
            if i < 4 :
                print(f"image/{ext[i]}")
            elif i == 4:
                print(f"text/{ext[i]}")
            elif i > 4:
                print(f"application/{ext[i]}")
        elif (file[-3:] not in type) and (file[-4:] not in type) :
            print("application/octet-stream")
            break
        i += 1

main()

################################

"""def main():
    file = input("File name : ").lower()
    if file[-4:] == ".gif" :
        print("image/gif")
    elif file[-4:] == ".jpg" :
        print("image/jpeg")
    elif file[-5:] == ".jpeg" :
        print("image/jpeg")
    elif file[-4:] == ".png" :
        print("image/png")
    elif file[-4:] == ".pdf" :
        print("application/pdf")
    elif file[-4:] == ".txt" :
        print("text/plain")
    elif file[-4:] == ".zip" :
        print("application/zip")

main()
"""
