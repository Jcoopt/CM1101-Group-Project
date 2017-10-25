import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'up'] #These words are skipped when parsing the input.



def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:
    """
    initial_input = words
    new_input = []

    for s in initial_input:
        valid = True
        for s_w in skip_words:
            if(s == s_w):
                valid = False
        if (valid):
            new_input = new_input + [s]
    return new_input



    
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:
    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    word_temp = ""
    word_list = []

    for ch in no_punct:
        if(ch != ' '):
            word_temp = word_temp + ch
        elif(ch == ' '):
            if (word_temp != ""):
                word_list = word_list + [word_temp]
            word_temp = ""

    if (word_temp != ""):
        word_list = word_list + [word_temp]
        
    word_list = filter_words(word_list, skip_words)

    return word_list

