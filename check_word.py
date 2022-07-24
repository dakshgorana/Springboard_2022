"""


            Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to             be sent as SMS and returns the abbreviated sentence. 

            Rules are as follows: 
            a. Spaces are to be retained as is 
            b. Each word should be encoded separately

                If a word has only vowels then retain the word as is

                If a word has a consonant (at least 1) then retain only those consonants

            Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

            Sample Input
             I love Python
             MSD says I love cricket and tennis too
             I will not repeat mistakes
             
             
            Expected Output
             I lv Pythn
             MSD sys I lv crckt nd tnns t
             I wll nt rpt mstks
             """

#code:

#lex_auth_01269444961482342489
def check_word(msg):
    word = ""
    flag = True
    for i in msg:
        if i not in ["a","e","i","o","u","A","E","I","O","U"]:
            flag = False
            break
        
    if flag == False:
        for i in msg:
            if i not in ["a","e","i","o","u","A","E","I","O","U"]:
                word = word+i
    elif flag ==True:
        for i in msg:
            word = word+i
    return word
            


def sms_encoding(data):
    #start writing your code here
    word_list = data.split()
    print(word_list)
    sentence=""
    for i in word_list:
        result=check_word(i)
        sentence=sentence+result+" "
    return sentence.rstrip()

data="I love Python"
print(sms_encoding(data))
            


            

           


            

            


