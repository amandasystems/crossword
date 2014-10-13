'''
Here we'll have a few functions for sorting a database of words

weighChar(words)
    takes in a list of words and scores each character
    returns array indexed by letters
    NOTE: only accepts lowercase a-z in ascii

countLetters(words, scoretable)
    receives a word and a scoretable, counts the letters and updates it
    returns new array
    NOTE: only accepts lowercase a-z in ascii

weighWordList(words)
    receives a list of words
    outputs a dictionary scoring each word
'''

from array import array
baseScore = 120



def weighChar(words):
    '''
    will bring in a list of words and output an array scoring each letter
    '''
    
    #first we'll make an empty array with 26 slots
    charScore = array('B', [])
    emptyScore = array('B', [baseScore])
    i = 0
    j = 26
    while i < j:
        charScore += emptyScore
        i += 1
 
    #counts letters and updates charScore for every word in list
    for w in words:
        charScore = countLetters(w, charScore)        


    #prints scoretable
    i = 0
    while i < j:
        print charScore[i],
        i += 1
    
    return charScore


def countLetters(word, nCharScore):
    '''
    count the letters in any in string and update character score
    '''
    for l in word:
        i = ord(l) - 97
        if nCharScore[i] >= 0:
            nCharScore[i] -= 1
    
    return nCharScore



def weighWordList(words):
    '''
    receives list of words, words
    '''
    
    indexWords = words
    wordScore = []

    charScore = weighChar(words)
    
    for word in words:
        score = weighWord(word, charScore)
        wordScore.append(score)
    
    #scoredWords = dict(zip(indexWords,wordScore))
    scoredWords = [indexWords, wordScore]
    print scoredWords
    return scoredWords



def weighWord(word, charScore):
    score = 0
    for l in word:
        i = ord(l) - 97
        score += charScore[i]
    return score


def sortIndexList(scoredWords):
    
    i = 0
    j = len(scoredWords[1])
    sortedList = []
    index = 0
    while i < j:
        index = findTopWord(scoredWords)
        nextWord = scoredWords[0].pop(index)
        scoredWords[1].pop(index)
        sortedList.append(nextWord)
        i+=1
        
    return sortedList

def findTopWord(scoredWords):
    topScore = 0
    i = 0
    j = len(scoredWords[1])
    index = 0
    while i < j:
        score = scoredWords[1][i]
        if score > topScore:
            topScore = score
            index = i
        i+=1

    return index
    
    


#testing
w = ["hej","hoho","zoo","bu","nationalencyklopedi", "kontroll"]

i = weighWordList(w)
print sortIndexList(i)
