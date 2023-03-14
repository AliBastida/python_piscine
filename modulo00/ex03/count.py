from ast import Break
from operator import le
import sys
import string

def main():
    if len(sys.argv) > 2:
        print("Error")
    elif len(sys.argv) == 1:
        text_analyzer(sys.argv[1])

def text_analyzer(text = None):
    """Este es el docstring de mi funcion"""
    if text is None:
        print("What do you want me to analyze?")
        text = input()
    elif not isinstance(text, str):
        print("Error")
        return
        
    mayusculas = 0
    minusculas = 0
    punctuation = 0
    space = 0
    print(f"The text contains {len(text)} characters")
    for char in text:
        if char.isupper():
            mayusculas += 1  
        elif char.islower():
            minusculas += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char in string.whitespace:
            space += 1
    print(f"{mayusculas} upper letter(s)")
    print(f"{minusculas} lower letter(s)")
    print(f"{punctuation} punctuation mark")
    print(f"{space} space(s)")

if __name__ == "__main__":
    main()