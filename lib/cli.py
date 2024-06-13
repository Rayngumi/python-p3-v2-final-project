from helpers import exit_program, check_id, display_score
from models.patron import Patron
import random
import datetime
import time

def main():
    print("Welcome to Night Club Bouncer Simulator!")
    score = 0
    level = 1
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            score += simulate_night(level)
            display_score(score)
            level += 1
        else:
            print("Invalid choice")

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. Start a new night")

def simulate_night(level):
    current_year = datetime.datetime.now().year
    patrons = generate_patrons(5 + level, current_year)
    night_score = 0
    for patron in patrons:
        print(f"\nPatron: {patron.name}, Birth Year: {patron.birth_year}, Sobriety: {patron.sobriety}, Dress Code: {patron.dress_code}")
        start_time = time.time()
        action = input("Allow entry (y/n)? ")
        decision_time = time.time() - start_time
        
        if decision_time > 5:  # Time limit for decision
            print("Too slow! You lost a point.")
            night_score -= 1
            continue
        
        if action.lower() == 'y':
            if check_id(patron, current_year):
                print(f"{patron.name} is allowed entry. Correct decision!")
                night_score += 1
            else:
                print(f"{patron.name} should not be allowed entry. Incorrect decision.")
                night_score -= 1
        else:
            if not check_id(patron, current_year):
                print(f"{patron.name} is denied entry. Correct decision!")
                night_score += 1
            else:
                print(f"{patron.name} should be allowed entry. Incorrect decision.")
                night_score -= 1
    return night_score

def generate_patrons(n, current_year):
    names = ["Marshial", "Lilly", "Ted", "Robin", "Barney", "Homer", "Marge", "Lisa", "Maggie", "Moe", "Bart", "Ned", "Peter", "Lois", "Brian", "Stewie", "Chris", "Meg"]
    sobriety_levels = ["Sober", "Tipsy", "Drunk"]
    dress_codes = ["Formal", "Casual", "Scruffy"]
    return [Patron(name=random.choice(names), birth_year=random.randint(current_year-25, current_year-18), 
                   sobriety=random.choice(sobriety_levels), dress_code=random.choice(dress_codes)) for _ in range(n)]

if __name__ == "__main__":
    main()
