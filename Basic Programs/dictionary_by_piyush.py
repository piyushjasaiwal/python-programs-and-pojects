def dictionary(word):
    dictionary_variable = {
        "A" : "apple",
        "B" : "ball",
        "C" : "cat",
        "D" : "what you are watching right now"
    }

    if word in dictionary_variable:
        return dictionary_variable[word]
    
    return "Word not found in the dictionary"