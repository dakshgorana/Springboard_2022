"""
            Problem Statement

            Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

            Rules:

                The word should have the largest frequency.

                In case multiple words have the same frequency, then choose the word that has the maximum length.

            Assumptions:

                The text has no special characters other than space.

                The text would begin with a word and there will be only a single space between the words.

            Perform case insensitive string comparisons wherever necessary.

            Sample Input
             "Work like you do not need money love like you have never been hurt and dance like no one is watching"
             "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
            
            Expected Output
             like 3
             fear 2
             
  #code:
  
  #lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0
    lst = data.split()
    d = {}
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i]=d[i]+1
   
    d2= {}
    
    for i in d:
        if d[i]>1:
            frequency = d[i]
            word = i
            d2[word] = frequency

    length = 0
    freq = 0
    word1 = ""
    for i in d2:
        if len(i)>length:
            length = len(i)
            freq = d2[i]
            word1 = i
    if freq >1:
        print(word1,freq,sep=" ")
  

    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Hands to clap and eyes to see "
max_frequency_word_counter(data)
             
             


            

            


            
