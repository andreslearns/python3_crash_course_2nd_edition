def count_words(filename):
    try:
        with open (filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print (f"Sorry, the filename {filename} does not exist!")
    else:
        #count the number of approximate number of word in the file
        words = contents.split()
        num_words = len(words)
        print (f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'pi_digits.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)