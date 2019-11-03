def filebuilder(x):
    with open("file.txt", "a") as myfile:
        myfile.write(x + "\n")

def main():
    print("Zach is the instructor for the week")
    print("We should find youtube.com/user/alta3resarch and subscribe to his page!")
    filebuilder("Zach")

if __name__ == "__main__":
    main()
