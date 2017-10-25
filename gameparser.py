import string


skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'up']



def filter_words(words, skip_words):

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

    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):

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
    #
    # COMPLETE ME!
    #
