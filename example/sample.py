#!/usr/bin/env python3

def main():
    # Print welcome message
    print("Hello, welcome to my simple Python script!")
    
    # Get user input
    name = input("What's your name? ")
    
    # Simple calculation example
    age = input(f"Hi {name}, how old are you? ")
    try:
        age = int(age)
        birth_year = 2024 - age
        print(f"You were born around {birth_year}!")
        
        # Fun fact about their age
        if age < 18:
            print("You're still a teenager!")
        elif age < 30:
            print("You're in your twenties!")
        else:
            print("You have lots of life experience!")
            
    except ValueError:
        print("That's not a valid age!")
    
    # Simple list manipulation
    favorite_things = []
    print("\nLet's create a list of your favorite things!")
    for i in range(3):
        thing = input(f"Enter favorite thing #{i+1}: ")
        favorite_things.append(thing)
    
    print("\nHere are your favorite things:")
    for i, thing in enumerate(favorite_things, 1):
        print(f"{i}. {thing}")
        
    print("\nThanks for using this script!")

if __name__ == "__main__":
    main()
