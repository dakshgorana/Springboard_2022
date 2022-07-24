"""Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input
"I like Python"
"Java is a very popular language"
	

Expected output
lieyon
"""

	
#code:-
def find_common_characters(msg1,msg2):
    common_char_list=[]
    for x in msg1:
        if x==" ":
            continue
        else:
            for y in msg2:
                if x == " ":
                    continue
                elif x == y:
                    if x in common_char_list:
                        break
                    else:
                        common_char_list.append(x)
                        break
    output="".join(common_char_list)
    if len(output)==0:
        return -1
    else:
        return output
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
