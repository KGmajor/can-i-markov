"""Generate Markov text from text files."""

from random import choice
from collections import defaultdict




def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path, encoding='utf-8')
    return open_file.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    
    chains = defaultdict(lambda: None)

    single_words = text_string.split()
    single_words.append(None)
    
    first_word = 0
    second_word = 0
    following_word = 0

    for i in range(len(single_words)-2):
        key = (single_words[i], single_words[i+1])
        value = single_words[i+2]

        chains.setdefault(key, []).append(value)
  
    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    word = choice(chains[key])
    words = []

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])


    return " ".join(words)

def random_tweet(random_text):

    find_captials = random_text.split()
    result = []
    i = None
    punk = ['.', '!']

    for word in find_captials:
        if word[0].isupper():
            i = find_captials.index(word)
            result.append(word)
            print(result)
            break
    
    print(find_captials[i:i+30])
            




input_path = ("ambitions.txt", encoding='utf-8')

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

random_tweet(random_text)
