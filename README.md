# Matt Breton - New Relic Coding Challenge

- Solution written using Python 3.7 and only built-in libraries (sys, re, collections) -- no need for pip here
- Execution follows requirements - `./main.py <file 1> <file2>` and so forth, or `cat <file> | ./main.py`
- Test file is `test.py`
- Origin of Species was used as a test file, but I also threw in the Star Wars Episode V script because Empire Strikes Back is the best Star Wars.


Thought process/notes:
- The text should be iterated through as few times as possible, for performance
- Generators seemed like the best way to iterate through large data sets
- If punctuation is ignored, it is therefore removed. The edge case I discovered for this was with '--'. Origin of Species uses these double dashes frequently, and in a refactor I would treat them as a space, rather than being removed entirely.
- If I were to refactor, I would also find a better way to handle stdin vs a list of files, and segregate out the print output into it's own function.
