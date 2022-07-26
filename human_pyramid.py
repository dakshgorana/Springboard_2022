"""
Problem Statement

Consider that the human tower is to be performed on a stage and the stage has a maximum weight limit. 

Write a python program to find the maximum number of people at the base level such that the total weight of tower does not exceed the maximum weight limit of the stage. 

Assume that:
1. Each person weighs 50 kg 
2. There will always be odd number of men at the base level of the human tower.

"""

#code:



def human_pyramid(no_of_people):
    if(no_of_people==1):
        return 1*(50)
    else:
        return no_of_people*(50)+human_pyramid(no_of_people-2)

def find_maximum_people(max_weight):
    no_of_people=0
    person_weight = 50
    number = max_weight / person_weight
    i=1
    while(1):
        if(sum(list(range(1,i+1,2)))*50 > max_weight):
            break
        i+=2
        print(i)
    i = i-2
    return i


max_people=find_maximum_people(1000)
print(max_people)
