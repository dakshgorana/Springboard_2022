"""Problem Statement

Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

    Assume that the sentence would begin with a word and there will be only a single space between the words.

    Perform case sensitive string operations wherever necessary.

Sample Input
the sun rises in the east	

Expected Output
eht snu sesir ni eht stea

"""
# code:


def encrypt_sentence(sentence):
    #start writing your code here
    
    
    q = sentence.split()
   
    new_sentence = ""
    for i in range(len(q)):
        if (i+1)%2!=0:
            new_sentence=new_sentence+reverse(q[i])
        else:
            new_sentence= new_sentence+even_pos(q[i])
            
    return new_sentence.rstrip()
    
    
    
def reverse(msg):
        m  = list(msg)
        
        m.reverse()
        
        msg = "".join(m)
        
        return msg
        
        
def even_pos(msg):
        vowel = ""
        output = ""
        n = list(msg)
        for i in n:
            if i in ["a","e","i","o","u","A","E","I","O","U"]:
                vowel = vowel+i
            else:
                output = output+i
        output = " "+output+vowel+" "
        
        return output

    

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)

	



 
