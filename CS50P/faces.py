def convert(text):
    # Replace the smiley face emoticon with the emoji
    text = text.replace(":)", "🙂😍")
    
    # Replace the frowny face emoticon with the emoji
    text = text.replace(":(", "🙁🥺")
    
    # Return the updated string
    return text

def main():
    # Prompt the user for input
    user_input = input()
    
    # Call the convert function and store the result
    converted_text = convert(user_input)
    
    # Print the final result
    print(converted_text)

# Call main at the bottom of the file
main()