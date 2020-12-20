import os


def main():
    your_directory = input("Choose a directory to save your file to:")
    your_file = input("Enter the name of your file (include format):")
    your_name = input("Enter your name:")
    your_phonenum = input("Enter your phone number:")
    your_address = input("Enter your address:")
    if os.path.isdir(your_directory):
        write_file = open(os.path.join(your_directory, your_file), 'w')
        write_file.write(your_name+','+your_address+','+your_phonenum+'\n')
        write_file.close()
        print("\nFile contents:")
        read_file = open(os.path.join(your_directory, your_file), 'r')
        for lines in read_file:
            print(lines)
        read_file.close()
    elif not (os.path.isdir(your_directory)):
        os.system("mkdir " + your_directory)
        write_file = open(os.path.join(your_directory, your_file), 'w')
        write_file.write(your_name+','+''+your_address+','+''+your_phonenum+'\n')
        write_file.close()
        read_file = open(os.path.join(your_directory, your_file), 'r')
        print("\nFile contents:")
        for lines in read_file:
            print(lines)
        read_file.close()
    else:
        print("This directory does not exist. Please try again.")


main()
