from helpers import exit_program, check_id, display_score, generate_event, save_game, load_game, delete_save, list_saves_by_id
from models.patron import Patron
from models.event import Event
from models.game_state import GameState
from models import session, init_db
import random
import datetime
import time

def main():
    init_db()
    print("Welcome to Night Club Bouncer Simulator!")
    score = 0
    shift = 1
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            event = generate_event(shift)
            print(f"\nEvent: {event.name}")
            score += simulate_shift(shift, event)
            display_score(score)
            shift += 1
        elif choice == "2":
            save_game(score, shift)
        elif choice == "3":
            load_game()
        elif choice == "4":
            delete_save()
        elif choice == "5":
            list_saves_by_id()
        else:
            print("Invalid choice")

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. Start a new shift")
    print("2. Save game")
    print("3. Load game")
    print("4. Delete saved game")
    print("5. List saved games")

def simulate_shift(shift, event):
    current_year = datetime.datetime.now().year
    patrons = generate_patrons(5 + shift, current_year, event)
    shift_score = 0
    for patron in patrons:
        session.add(patron)
        print(f"\nPatron: {patron.name}, Birth Year: {patron.birth_year}, Sobriety: {patron.sobriety}, Dress Code: {patron.dress_code}")
        start_time = time.time()
        action = input("Allow entry (y/n)? ")
        decision_time = time.time() - start_time
        
        if decision_time > 5: 
            print("Too slow! You lost a point.")
            shift_score -= 1
            continue
        
        if action.lower() == 'y':
            if check_id(patron, current_year, event):
                print(f"{patron.name} is allowed entry. Correct decision!")
                shift_score += 1
            else:
                print(f"{patron.name} should not be allowed entry. Incorrect decision.")
                shift_score -= 1
        else:
            if not check_id(patron, current_year, event):
                print(f"{patron.name} is denied entry. Correct decision!")
                shift_score += 1
            else:
                print(f"{patron.name} should be allowed entry. Incorrect decision.")
                shift_score -= 1
    session.commit()
    return shift_score

def generate_patrons(n, current_year, event):
    names = ["Marshial", "Lilly", "Ted", "Robin", "Barney", "Homer", "Marge", "Lisa", "Maggie", "Moe", "Bart", "Ned", "Peter", "Lois", "Brian", "Stewie", "Chris", "Meg"]
    sobriety_levels = ["Sober", "Tipsy", "Drunk"]
    dress_codes = ["Formal", "Casual", "Scruffy"]
    return [Patron(name=random.choice(names), birth_year=random.randint(current_year-25, current_year-15), 
                   sobriety=random.choice(sobriety_levels), dress_code=random.choice(dress_codes), event_id=event.id) for _ in range(n)]

if __name__ == "__main__":
    main()
