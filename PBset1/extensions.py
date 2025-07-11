def main():
    extension = {"gif":"image/gif",
                 "jpg":"image/jpeg",
                 "jpeg":"image/jpeg",
                 "png":"image/png",
                 "pdf":"application/pdf",
                 "txt":"text/plain",
                 "zip":"application/zip"}

    input_file = input("File name: ").lower().strip().rsplit(".", 1)

    if len(input_file)>1 and input_file[1] in extension:
        print(extension[input_file[1]])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
