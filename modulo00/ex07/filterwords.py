import sys
import string

def main():

    try:
        assert len(sys.argv) == 3, "Wrong number of arguments"
        
    except AssertionError as msg:
        print (msg)
        sys.exit()
    try:
        str = sys.argv[1]
        num = int(sys.argv[2])
    except ValueError:
        print("Be sure you have write ther aguments properly")
        sys.exit()

    final_list = []

    for word in str.split():
        new_word = ""
        for letter in word:
            if not letter in string.punctuation:
                new_word += letter
        final_list.append(new_word)

    for word in final_list:
        if len(word) >= num:
            print(word)


if __name__ == "__main__":
    main()