'''
This functions returns the greeting message according to the tym
'''
from datetime import datetime
import random
def current_time():
    current_time = datetime.now()
    greeting="Good morning"
    if current_time.hour>12 and current_time.hour<17:
        greeting="Good afternoon"
    elif current_time.hour>=17 and current_time.hour<22:
        greeting="Good evening"
    elif current_time.hour>=22:
        greeting="Hi, its too late"
    return greeting
'''
This function gives the welcome message
'''

def welcome(name):
    message = [
        "How can I help you?",
        "Is there anything I can help with?",
    ]
    print(f"{current_time()}! {name}, {random.choice(message)}")

def problem_name():
    print("1.Type 1 Diabetes")
    print("2.Type 2 Diabetes")
    print("3.Overactive Thyroid")
    print("4.Underactive Thyroid")
    print("5.Chronic Kidney")
    print("6.Cardiac issues")
    print("7.Jaundice")
    print("8.Stomach Ulcers")
    print("9.Obesity")
    print("10.Exit")
    try:
        return(int(input("Enter your health issue : ")))
    except :
        print("Invalid input")
        return 0

def type1_diabetes():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Type 1 Diabetes are Brown rice, Whole Wheat, Fruits, Vegetables, Lentils, Sprouts, Beets and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Type 1 Diabetes are Sodas, White Bread, Chips, Fried Foods, Refined Grains, Juice Drinks and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def type2_diabetes():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Type 2 Diabetes are Fatty Fish, Eggs, Avocados, Beans, Chia Seeds, Broccoli, Garlic, Nuts, Strawberries and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Type 2 Diabetes are Sugar-Sweetened Beverages, Flavoured Coffee Drinks, Honey, Dried Fruit, Fruit Juice, Packaged snack Foods and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                 print("Sorry! Invalid input")
            option=food_list()
    print_food()

def overactive_thyroid():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Overactive Thyroid are Fresh Fruits, Egg whites, Red Meat, Mushrooms, Oats, Nuts, Cashews and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Overactive Thyroid are Fish, Prawns, Egg Yolk, Cheese, Processed Meats, Iodizes Salt and Water, Milk and Dairy Products and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def underactive_thyroid():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Underactive Thyroid are Eggs, Meat, Fish, Vegetables, All Dairy Products, Fruits, Non-Caffeinated Beverages,Gluten-Free Grains and Seeds and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Underactive Thyroid are Sweet Potatoes, Cabbage, Broccoli, Cauliflower, Spinach, Peaches, Strawberries, Peanuts, Soy Foods and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def chronic_kidney():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
       print("The foods which you can intake if you are suffering from Chronic Kidney are Low-Fat Dairy Products, Fruits, Fish, Red Meat, Nuts, Beans, Garlic, Bellpepper and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Chronic Kidney are Brown Rice, Packed Foods, Pickels, Wheat Bread, Chips, Oranges, Spinach, Tomato, Potato and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def cardiac_issues():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Cardiac issues are lots of fruits and Vegetables, Lean meats, Skinless Poultry, Nuts, Beans, Legumes, Fish, Whole grains, Plant-based oils, such as olive oil, Low-fat dairy products and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Cardiac issues are Butter, Gravy, non-dairy creamers, Fried foods, Processed meats, Pastries, Certain cuts of meat, Junk foods like potato chips, cookies, pies, and ice cream and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def jaundice():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
       print("The foods which you can intake if you are suffering from Jaundice are Coconut and Barley water, Fruit Juices, Breads, Oats, Almonds, Carrots, Kiwi, Honey and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Jaundice are Alcohol, Refined carbohydrates, Packaged, canned, and smoked foods, Saturated and trans fats, Raw or undercooked fish or shellfish, Raw or undercooked fish or shellfish, Beef, Pork and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
               print("Sorry! Invalid input")
            option=food_list()
    print_food()

def stomach_ulcers():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Stomach Ulcers are Apples, Pears, Ooatmeal, Soyabeans, Broccoli, Berries, Green tea, Honey, Garlic, Buttermilk and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Stomach Ulcers are Chocolates, Coffee, Spicy Foods, Alcohol, Acidic foods, Caeffinated drinks, Yoghurt and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def obesity():
    print("Select any one option from 1 to 3")
    def food_list():
        print("1.Foods to eat")
        print("2.Foods to avoid")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def food_to_eat():
        print("The foods which you can intake if you are suffering from Obesity are Nuts, Seeds, Beans, Fish, Plant oils such as olive oil and vegetable oils, Brown rice, Whole wheat and etc...")
    def food_to_avoid():
        print("The foods which you should not intake if you are suffering from Obesity are Sodas, Fruit Drinks, Refined Grains, Sweets, Baked or Fried Potatoes, Red meat and Processes meats and etc...")
    def print_food():
        option = food_list()
        while option != 3:
            if option == 1:
                food_to_eat()
            elif option == 2:
                food_to_avoid()
            else:
                print("Sorry! Invalid input")
            option=food_list()
    print_food()

def chatbot():
    print("This bot helps you to find which food to eat and which food to avoid for different health problems")
    name = input("Enter your name : ") 
    welcome(name)
    print("Select any one of the below health issues so that you can know which foods to eat and which foods to avoid for that particular health issue")
    choice = problem_name()
    while choice != 10:
        if choice == 1:
            type1_diabetes()
        elif choice == 2:
            type2_diabetes()
        elif choice == 3:
            overactive_thyroid()
        elif choice == 4:
            underactive_thyroid()
        elif choice == 5:
            chronic_kidney()
        elif choice == 6:
            cardiac_issues()
        elif choice == 7:
            jaundice()
        elif choice == 8:
            stomach_ulcers()
        elif choice == 9:
            obesity()
        else:
            print("Please enter the number between 1 to 10")
        choice = problem_name()
        
chatbot()
