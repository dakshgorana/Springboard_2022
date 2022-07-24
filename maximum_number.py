#lex_auth_01269441913243238467

def create_largest_number(number_list):
    max_num = ""
    while len(number_list)!=0:
        
        max_num=max_num+str(max(number_list))
        number_list.remove(max(number_list))
    return int(max_num)
    #remove pass and write your logic here

number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)
