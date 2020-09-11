import sys
import re
import collections


# First, determine the files and handle stdin vs a list of CL arguments
def files_to_parse():
    argument_list = len(sys.argv)
    if argument_list == 1:
        try:
            actual_text = sys.stdin.read()  # Read from stdin if nothing is passed via CLI
        except Exception as e:
            print (e)
        stdin = True;
        return actual_text, stdin;
    else:
        list_of_files = []
        for i in range(1, argument_list):
            list_of_files.append(sys.argv[i])
        stdin = False;
        return list_of_files, stdin;


# Sanitize the text - we only care about words, not punctuation or case
def get_words(text_to_sanitize):
    pattern = re.compile(r"[^\s]+") # Match any non-whitespace characters
    non_alpha = re.compile(r"[^\w]", re.IGNORECASE) # Match anything that is not a letter or number
    for match in pattern.finditer(text_to_sanitize): # Find words
        next_word = non_alpha.sub("", match.group()).lower()  # Get rid of punctuation, convert to lowercase
        if next_word:  # Skip blank words with no letters (Punctuation, etc)
            yield next_word


# Now that text is sanitized, get the list of phrases
def phrases(words):
    phrase_list = []  # Each word is a list object
    for word in words:
        phrase_list.append(word)  # Start appending words to the first word in the list
        if len(phrase_list) > 3:  # If greater than three, remove the first word in the list
            phrase_list.remove(phrase_list[0])
        if len(phrase_list) == 3:  # If exactly three words, yield a tuple (generator function)
            yield tuple(phrase_list)


# Sequence the above two functions together and print the output
def run_sequence(data_to_process):
    phrases(get_words(data_to_process))  # Next, yield the phrases
    counts = collections.defaultdict(int)  # Init data structure that stores counts of phrases
    for phrase in phrases(get_words(data_to_process)):
        counts[phrase] += 1
    for results in sorted(counts, key=counts.get, reverse=True)[0:100]:
        print(counts[results], ": ", ' '.join(results))
    return counts


if __name__ == "__main__":
    text, stdin = files_to_parse()
    if stdin:
        run_sequence(text)
    else:
        for files in text:
            print("File: ", files)
            try:
                with open(files, 'r', encoding='utf-8') as file:
                    data = file.read()
                    run_sequence(data)
            except Exception as e:
                print(e)