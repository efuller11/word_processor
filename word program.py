# Elijah Fuller
# Assignment 12.1

# count top words max 30

try:
    # This program will give a word count of all the words in the file
    # and give the top 30 words.
    # It has not been modified to do any stop wording


    # Open the input file
    filename = input("Please enter a filename: ")
    s = open(filename, 'r', encoding = 'utf-8').read()

    # count characters
    num_chars = len(s)

    # count lines
    num_lines = s.count('\n')

    words = s.split()
    d = {}
    for w in words:
        if w in d:  # seen w before?
            d[w] += 1
        else:
            d[w] = 1

    print("after we processed word " + str(w) + ", our dictionary is now:")
    print(d)

    num_words = sum(d[w] for w in d)

    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()

    print('Your input file has characters = ' + str(num_chars))
    print('Your input file has num_lines = ' + str(num_lines))
    print('Your input file has num_words = ' + str(num_words))

    print('\n The 30 most frequent words are \n')

    i = 1
    for count, word in lst[:30]:
        print('%2s.  %4s %s' % (i, count, word))
        i += 1

    # now let's delete some of the stop words
    # the word "to" is a junky stop word, so let's remove from dictionary
        print(d)
    if "to" in d:
        del d["to"]
    print("Here's the dictionary after we deleted 'to':")
    print(d)

    # I'm going to delete a few other junky stop words here
    punct = [".,/?')($#!&*<>|{}-+_=&"]
    for word in
    stop_words = ['and','our', 'for', 'if', 'is', 'by', 'as', 'bln', 'the', 'of', 'in', 'a', 'on',  ]
    if "and" in d:
        del d["and"]
    if "our" in d:
        del d["our"]
    if "from" in d:
        del d["from"]

    print("Here's the dictionary after we deleted 'and, our, from':")
    print(d)

    # Now let's get another summary of our dictionary and see how it goes:

    num_words = sum(d[w] for w in d)

    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()

    print('Your input file has characters = ' + str(num_chars))
    print('Your input file has num_lines = ' + str(num_lines))
    print('Your input file has num_words = ' + str(num_words))

    print('\n The 30 most frequent words are \n')

    i = 1
    for count, word in lst[:30]:
        print('%2s.  %4s %s' % (i, count, word))
        i += 1

except FileNotFoundError:
    print(f"Sorry could not find {filename}.")
    exit()


