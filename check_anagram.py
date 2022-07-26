Problem Statement

Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input                  Expected Output


eat, tea	                     True

backward,drawback              False 

(Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter           True
	
About, table                    False


#code


def check_anagram(data1,data2):
    first = data1.lower()
    second = data2.lower()

    d1 = []
    d2 = []

    d1 = list(first)
    d2 = list(second)
    
    for_check1 = sorted(d1)
    for_check2 = sorted(d2)
    if (for_check1 != for_check2):
        return False

    count = 0
    if (len(d1) == len(d2)):
        for i in d1:
            for j in d2:
                if(i == j):
                    a = d1.index(i)
                    b = d2.index(j)
                    if(a == b):
                        return False
                    else:
                        count += 1
    if(len(second) == len(first)):
        return True
    else:
        return False

    print(check_anagram("Schoolmaster", "Theclassroom"))
	




	




	

