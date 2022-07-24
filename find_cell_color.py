
"""Above is the standard representation of a chessboard.

This could be imagined as a 2D cartesian plane, with the x axis being represented by the alphabets and y axis by the numbers.

Given coordinates in the form of string, print if that cell is white or black.

Input Format
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

char_list = list(s)[:2]

char_list[-1]=int(char_list[-1])
white_cell_char = [ 'a','c','e','g']

for i in range(1,9):
    if char_list[0] in white_cell_char:
        if char_list[-1]%2==0:
            color = "White"
        else:
            color = "Black"
    else:
        if char_list[-1]%2==0:
            color = "Black"
        else:
            color = "White"
print(color)
