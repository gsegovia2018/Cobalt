import re
import time
from pwn import *

def regex_fun(searcha, lista):
    for i in lista:
        print(re.search(searcha, i, re.IGNORECASE))


def searching(search, lista):
    '''
    This function searchs for a word in a list of words and returns 
    a list with the matching values of each word from the list
    '''
    p = log.progress("Starting searching for matching word in list")
    #Set the count to 0 with the length of the list of words
    try:
        count = [0]*len(lista)
        #Convert the search word to lowercase
        search = search.lower()
        for i in range(len(lista)):
            #Convert the list word to lowercase
            word = lista[i].lower()
            #Check if the search word is contain in the list
            if search in word:
                if(search == word):
                    #if it's the same 0
                    count[i] = 0
                else:
                    #if it's contained 1
                    count[i] = 1
            else:
                p = log.progress(f"Checking if letters of {word.upper()} are in the list of words")
                time.sleep(0.5)
                count = contained_in_words(search, word, count, i)
                p.success("Count done\n")
                p = log.progress(f"Finding indexes in {word.upper()}")
                
                indexes = find_indexes(word, search)
                p.success("Indexes done\n")
                p = log.progress(f"Finding consecutives in {word.upper()}")
                count = consecutive(indexes, count, i)
                p.success("Consecutives done\n")
                p = log.progress(f"Right order in {word.upper()}")
                count = right_order(indexes,count, i)
                p.success("right order done")
        p.success("Searching function executed correctly")
        return count
    except Exception as e:
        p.error("Found error during searching process: ", e)


def contained_in_words(search, word, count, ind):
    '''
    Gets the search word and the word from the list and finds how
    many letters are contained in that word
    '''
    try:
        #p = log.progress("Checking if letters are in the list of words")
        letters = list(search)
        w = list(word)
        #Check how many letters in search are in list word
        for letter in letters:
            if letter in w:
                w.remove(letter)
            else:
                count[ind] += 1
        #p.success("Count done")
        return count
    except Exception as e:
        #p.error("Found error during contained_in_words: ", e)
        print("Error: ", e)

def find_indexes(word, search):
    '''
    Finds the indexes of the search letters in a word 
    and returns a list of indexes
    '''
    try:
        #p = log.progress("Finding indexes")
        indexes = []
        letters = list(search)
        word=list(word)
        for letter in letters:
            if letter in word:
                index = word.index(letter)
                indexes.append(index)
                word.remove(letter)
                word.insert(index, "1")  
            else:
                indexes.append(-2)
        #p.success("Indexes done")
        return indexes
    except Exception as e:
        #p.error("Found error during find_indexes: ", e)
        print("Error: ", e)
def consecutive(indexes, count, ind):
    '''
    Checks if the letters are consecutive in the word from the list
    '''
    try:
        #p = log.progress("Finding consecutive")
        for j in range(len(indexes)-1):
            if indexes[j+1]-indexes[j] != 1:
                count[ind] += 1
        #p.success("Consecutives done")
        return count
    except Exception as e:
        #p.error("Found error during consecutive: ", e)
        print("Error: ", e)
def right_order(indexes, count, ind):
    '''
    Checks if the letters are in the right order in the word
    from the list
    '''
    try:
        #p = log.progress("Finding right order")
        temp = None
        for j in range(len(indexes)-1):
            if temp == None:
                if indexes[j] >= indexes[j+1]: 
                    count[ind] += 1
                    if indexes[j+1] == -2:
                        temp = j
                else:
                    temp = j+1
            else:
                if indexes[temp] >= indexes[j+1]: 
                    count[ind] += 1
                    if indexes[j+1] == -2 and indexes[j] != -2:
                        temp = j
                    elif indexes[j+1] == -2 and indexes[j] == -2:
                        continue
                    else:
                        temp = j+1
                else:
                    temp = j+1
        #p.success("Right order done")
        return count
    except Exception as e:
        #p.error("Found error during right_order: ", e)
        print("Error: ", e)
            
if __name__ == "__main__":
    start = time.time()
    lista = ["Adele", "Elaine", "Elizabeth", "Harriet", "Ingrid", "Michelle"]#, "Isabella", "BELLAA", "Ella"]
    search = "Ella"

    #regex_fun(searcha, lista)
    a = searching(search, lista)
    for i in range(len(a)):
       print(lista[i], a[i])
    end = time.time()
    print(end-start)


   
