"""
             Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

            Given a balanced string s, split it in the maximum amount of balanced strings and encapsulate them in ‘(’ and ‘)’. For example RRLL is balanced so you have to return “(RRLL)”.

            Return the string such that maximum amount of balanced encapsulated strings are there.

            Input Format
            Each Input has one line the string s which is a balanced string.

            Output Format
             return a string which is the enigma’s interpretation of the command.

            Constraints
            0<s.length<=2*10^6


            Sample Testcase 0
            Testcase Input
            RLRRLLRLRL

            Testcase Output
            (RL)(RRLL)(RL)(RL)
            
            Explanation
            s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
            
            Sample Testcase 1
            Testcase Input
            RLLLLRRRLR

            Testcase Output
            (RL)(LLLRRR)(LR)

            Explanation
             s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
             """

# Enter your code here. Read input from STDIN. Print output to STDOUT
def balance(s):
    r_count = s.count("R")
    l_count = s.count("L")
    result = []
    if r_count == l_count:
        r = 0
        l = 0
        i = 0
        start = 0
        end = 0
        while i<len(s):
            if s[i] =="R":
                r+=1
                i+=1
            else:
                l+=1
                i+=1
            if r== l:
                end = i
                result.append(s[start:end])
                start = i
                i =start
                
       return result
s = input()           
lst = balance(s)
for i in lst:
    print("("+i+")",end="")              

                    
               

    
