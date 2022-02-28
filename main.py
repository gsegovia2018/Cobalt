import re
import time

def regex_fun(searcha, lista):
    for i in lista:
        print(re.search(searcha, i, re.IGNORECASE))


def searching(search, lista):
    #Set the count to 0 with the length of the list of words
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
            count = contained_in_words(search, word, count, i)
            indexes = find_indexes(word, search)
            count = consecutive(indexes, count, i)
            count = right_order(indexes,count, i)
    return count

def contained_in_words(search, word, count, ind):
    letters = list(search)
    w = list(word)
    #Check how many letters in search are in list word
    for letter in letters:
        if letter in w:
            w.remove(letter)
        else:
            count[ind] += 1
    return count

def find_indexes(word, search):
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
    return indexes

def consecutive(indexes, count, ind):
    for j in range(len(indexes)-1):
        if indexes[j+1]-indexes[j] != 1:
            count[ind] += 1
    return count

def right_order(indexes, count, ind):
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
    return count
            
if __name__ == "__main__":
    start = time.time()
    lista = ["Adele", "Elaine", "Elizabeth", "Harriet", "Ingrid", "Michelle", "Isabella", "BELLAA", "Ella"]
    search = "Ella"

    #regex_fun(searcha, lista)
    a = searching(search, lista)
    for i in range(len(a)):
       print(lista[i], a[i])
    end = time.time()
    print(end-start)


   
