# lib/helpers.py

def check_id(patron, current_year):
    age = current_year - patron.birth_year
    if age >= 18 and patron.sobriety != "Drunk" and patron.dress_code != "Scruffy":
        return True
    return False

def exit_program():
    print("Goodbye!")
    exit()

def display_score(score):
    print(f"\nCurrent Score: {score}")
