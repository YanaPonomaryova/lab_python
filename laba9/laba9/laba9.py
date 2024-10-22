def create_file_tf20_1():
    """Creates a text file TF20_1 with lines of varying lengths."""
    try:
        with open("TF20_1.txt", "w") as file:
            print("File TF20_1.txt was opened!")
            file.write("This is an example text with some words.\n")
            file.write("Let these words have different lengths.\n")
            file.write("Python is a great programming language.\n")
            print("Information was successfully added to TF20_1.txt!")
        print("File TF20_1.txt was closed!")
    except Exception as e:
        print(f"Error while creating the file: {e}")


def find_longest_words():
    """Reads the content of the file TF20_1, finds the longest words, and writes them to the file TF20_2."""
    try:
        with open("TF20_1.txt", "r") as file:
            print("File TF20_1.txt was opened!")
            content = file.read()
        print("File TF20_1.txt was closed!")
        
        # Remove punctuation and split the text into words
        words = [word.strip(",.!?;:") for word in content.split()]
        max_length = max(len(word) for word in words)
        
        # Find all words of the maximum length
        longest_words = [word for word in words if len(word) == max_length]
        
        # Write them to the file TF20_2, separated by spaces
        with open("TF20_2.txt", "w") as file:
            print("File TF20_2.txt was opened!")
            file.write(" ".join(longest_words))
            print("Information was successfully added to TF20_2.txt!")
        print("File TF20_2.txt was closed!")
    except FileNotFoundError:
        print("File TF20_1.txt not found.")
    except Exception as e:
        print(f"Error while processing the file: {e}")


def print_words_from_tf20_2():
    """Reads the content of the file TF20_2 and prints it with five words per line."""
    try:
        with open("TF20_2.txt", "r") as file:
            print("File TF20_2.txt was opened!")
            content = file.read()
        
        # Split the text into words
        words = content.split()
        
        # Print words, five per line
        print("New sequence:")
        for i in range(0, len(words), 5):
            print(" ".join(words[i:i+5]))
        print("File TF20_2.txt was closed!")
    except FileNotFoundError:
        print("File TF20_2.txt not found.")
    except Exception as e:
        print(f"Error while processing the file: {e}")


# Program execution
create_file_tf20_1()
find_longest_words()
print_words_from_tf20_2()
