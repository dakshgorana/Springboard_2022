"""Problem Statement

Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input
{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

Expected Output
[2, 2, 1]
"""
# code:


def find_correct(word_dict):
    #start writing your code here
    result = []
    exact = 0
    almost = 0
    wrong = 0
    for i in word_dict:
        
        list1 = list(i)
        list2 = list(word_dict[i])
        count = 0
        l=min(len(list1),len(list2))
        if len(i)!=len(word_dict[i]):
            wrong+=1
        else:
        
            for i in range(l):
                if list1[i] != list2[i]:
                    count+=1
            if count == 0:
                exact+=1
            elif 0<count<=2:
                almost+=1
            else:
                wrong+=1
    for i in (exact,almost,wrong):
        result.append(i)
    return result
        


	



 
