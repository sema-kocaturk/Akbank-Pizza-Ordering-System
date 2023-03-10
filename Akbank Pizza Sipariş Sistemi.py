# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:35:14 2023

@author: user
"""


import csv
import datetime

class Pizza:  #created a class as Pizza and get some properties
    def __init__(self,description,cost,size):
        self._description=description
        self._cost=cost
        self._size=size
    def get_description(self):
        return self._description
    def get_cost(self):
        return self._cost
    def get_size(self):
       return self._size
    
class Classic_Pizza(Pizza):   # created pizza types with encapsulation and enter properties
    def __init__(self):
       super().__init__("Classic materials: Sausage, Salami, Cheddar", 110,"standart")
       
       
class Margherita_Pizza(Pizza):
    def __init__(self):
       super().__init__("Margarita Ingredients: Tomato, Basil, Mozzarella", 100, "standart")


class Turk_Pizza(Pizza):
    def __init__(self):
       super().__init__("Turkish Ingredients: Ground Mince, Onion, Pepper, Garlic, Cheddar", 120,"standart")
   
       
class Dominos_Pizza(Pizza):
    def __init__(self):
       super().__init__("Dominos Ingredients: Salami, Sausage, Olive", 140,"standart")

class Decorator:
    def __init__(self,description,cost):   #created a class for extra Ingredients
        self._description=description
        self._cost=cost        
    def get_description(self):
        return self._description
    def get_cost(self):
        return self._cost
class Olive(Decorator):             #creted new class for all extra ingredients amd get some knowladge
    def __init__(self):
        super().__init__("Olive",4.99)
class Mushroom(Decorator):
    def __init__(self):
        super().__init__("Mushroom", 8.99)
class Goat_Cheese(Decorator):
    def __init__(self):
        super().__init__("Goat Cheese", 17.99)
class Meat(Decorator):
    def __init__(self):
        super().__init__("Meat", 25.99)
class Onion(Decorator):
    def __init__(self):
        super().__init__("Onion", 7.50)    
class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn", 6.5)
      
def main():       
        
    fıle= """
    Please Choose a Pizza: 
    1: Classic Pizza 110 ₺
    2: Margherita Pizza 100 ₺
    3: Turkish Pizza 120 ₺
    4: Dominos Pizza 140 ₺
    * and sauce of your choice: 
    11: Olives +5.50 ₺
    12: Mushrooms +7.90 ₺
    13: Goat Cheese +13.50 ₺
    14: Meat +15.00 ₺
    15: Onions +5.50 ₺
    16: Corn +3.90 ₺
    * Thank you!
    """
    
    dosya = open("menu_txt","w",encoding="utf-8")   #write menu on console for consumer and they will choose their order according to text
    dosya.write(fıle)
    total_cost=0    
    print(dosya)#printing the menu 
    number=int(input("How many pizza dp you want to order? : "))  #I learned how many pizzas to order from the user.
    number_order=0
    pizza_types=[]
    while number_order<number: # the loop will repeat up to the number of orders
        pizza_type = int(input("Please choose a pizza base: "))#getting the pizza type from the user
       
        if pizza_type == 1:
            pizza = Classic_Pizza()
            selected_pizza="Classic Pizza"
            number_order=number_order+1
            pizza_types.append(selected_pizza)
            total_cost=pizza.get_cost()+total_cost
        elif pizza_type == 2:
            pizza = Margherita_Pizza()
            selected_pizza="Margherita Pizza"
            number_order=number_order+1
            pizza_types.append(selected_pizza)
            total_cost=pizza.get_cost()+total_cost
        elif pizza_type == 3:
            pizza = Turk_Pizza()
            selected_pizza="Turk Pizza"
            number_order=number_order+1
            pizza_types.append(selected_pizza)
            total_cost=pizza.get_cost()+total_cost
        elif pizza_type == 4:
            pizza = Dominos_Pizza()
            selected_pizza="Dominos Pizza"
            number_order=number_order+1
            pizza_types.append(selected_pizza)
            total_cost=pizza.get_cost()+total_cost
        else:
            print("Invalid choice!")
    Toppings=[] #open list for all extra ingredients. This list will be used when giving knowladge consumer 
    number_decorator=0
    z=0
    while number_decorator< number_order:   #Extra ingredients can be entered separately for each pizza.
        decorator = int(input('Please choose topping if you dont want to  ad topping enter "0":'))#getting the pizza type from the user
        
        if decorator == 11:
            topping= Olive()
            Toppings.append("olive") 
            print("Olive added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator == 12:
            topping = Mushroom()
            Toppings.append("mushroom")  
            print("mushroom added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator == 13:
            topping = Goat_Cheese()
            Toppings.append("goat cheese")  
            print("goat chees added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator == 14:
            topping = Meat()
            Toppings.append("meat") 
            print("Meat added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator == 15:
            topping= Onion()
            Toppings.append("onion")  
            print("Onion added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator == 16:
            topping= Corn() 
            Toppings.append("corn")  
            print("Corn added the ", pizza_types[z])
            total_cost=total_cost+topping.get_cost()
        if decorator ==0:
           number_decorator=number_decorator+1 
           z=z+1
    x=0    
    extra=""        
    
    for i in Toppings:    # this part Toppings list change as a string to add information sentence for consumer
        extra=extra+i
        if x <len(Toppings)-1:
            extra=extra+", "
            x=x+1
            
    pizzas=""  
    y=0      
    for i in pizza_types:
        pizzas=pizzas+i
        if y <len(pizza_types)-1:
            pizzas=pizzas+", "
            y=y+1
            
    print("You order ",pizzas , "and you choosed extra ", extra,"and total cost is " "$" + str(total_cost))
    
    
    print("----------Enter Your Order Information----------\n")
    name = input("Name: ")
    ID = input("ID Number: ")
    credit_card_no = input("Enter Credit Card Number: ")
    credit_card_psw = input("Credit Card Password: ")

    now = datetime.datetime.now()    #giving now time as a date and clock
    order_date_and_time = datetime.datetime.strftime(now, '%c')

    print("Current Time =", order_date_and_time)
    
    order = [ name,pizzas,extra ,ID, credit_card_no, credit_card_psw, order_date_and_time]  
    with open('Orders_Database.csv', 'a', newline='',encoding="utf-8") as f:   # open a csv file to save information about consumer and order
        writer = csv.writer(f)
        writer.writerow(order)
    print("Your order has been successfully confirmed. Thanks!")

   


    


    
if __name__ == '__main__':
    main()

