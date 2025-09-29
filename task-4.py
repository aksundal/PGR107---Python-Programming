
# Makes new string: Ignores high/low case letters, special characters and numbers
def is_palindrome(text):
    only_letters_lowercase = ""
    for ch in text:
        if ch.isalpha(): #check if character is a letter
            only_letters_lowercase += ch.lower() #Convert the letters to lowercase

#Reverses string: made with the new string
    reversed_text = ""
    for ch in only_letters_lowercase:
        reversed_text = ch + reversed_text
        #Checks if the new string and reverse string is the same
    return only_letters_lowercase == reversed_text


def main():
    print("Palindrome Checker")
    while True:
        user_input = input("PLease enter a string to check if it`s a palindrome or type 'exit' to quit: ") #Input from user
        #User can "Exit" the check
        if user_input.lower().strip() == "exit":
            print("End of Palindrome Checker.\nThank you for using the Palindrome Checker!")
            break
        # Check for empty input
        if len(user_input.strip()) == 0:
            print("You did not enter any text. ")#Message that lets user know that the input is empty
            continue
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is NOT a palindrome.")

if __name__ == "__main__":
    main()
