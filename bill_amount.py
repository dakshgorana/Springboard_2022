#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for gem in range(len(reqd_gems)):
        if reqd_gems[gem] in gems_list:
            ind = gems_list.index(reqd_gems[gem])
            bill_amount = bill_amount+price_list[ind]*reqd_quantity[gem]
        else:
            return -1
    if bill_amount>30000:
        bill_amount = 0.95*bill_amount
    
    return bill_amount
