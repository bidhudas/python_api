#!/usr/bin/python3

def main():
    while True:
        try:
            name = input("Enter the name of a file: ")
            with open(name, "w") as myfile:
                myfile.write("This worked\n")
        except Exception as err:
            print(f'Error trying to create file {name}.\nError: {err}')
        else:
            break

    print("Thanks for making that simple file")

if __name__ == "__main__":
    main()
