"""
The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

Assume that the following information are given:
Price per litre of fuel = 70
Mileage of the bus in km/litre of fuel = 10
Price(Rs) per ticket = 80

The bus runs on multiple routes having different distance in kms and number of passengers.
Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.
"""
# code:
  

def calculate(distance,no_of_passengers):
    milege = 10
    petrol_price = 70
    ticket_price= 80
    
    petrol_used = distance/milege
    total_petrol_cost = petrol_used*petrol_price
    
    money_acquire = ticket_price*no_of_passengers
    
    if money_acquire>total_petrol_cost:
        return money_acquire-total_petrol_cost
    else:
        return -1



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
