import random
from models.event import Event
from models.game_state import GameState
from models import session

def check_id(patron, current_year, event):
    age = current_year - patron.birth_year
    if age < 18 or patron.sobriety == "Drunk" or patron.dress_code == "Scruffy":
        return False
    if event.name == "Celebrity Night" and patron.name == "VIP":
        return True
    return age >= 18

def exit_program():
    print("Goodbye!")
    session.close()
    exit()

def display_score(score):
    print(f"\nCurrent Score: {score}")

def generate_event(shift):
    events = ["Normal Night", "Theme Night", "Celebrity Night", "Ladies Night"]
    event_name = random.choice(events)
    event = Event(name=event_name)
    session.add(event)
    session.commit()
    return event

def save_game(score, shift):
    game_state = GameState(score=score, shift=shift)
    session.add(game_state)
    session.commit()
    print("Game saved successfully! ID:", game_state.id)

def load_game():
    save_id = input("Enter the ID of the save game to load: ")
    game_state = session.query(GameState).filter_by(id=save_id).first()
    if game_state:
        print(f"Game loaded successfully! ID: {game_state.id}, Score: {game_state.score}, Shift: {game_state.shift}")
        return game_state.score, game_state.shift
    else:
        print("No saved game found with that ID.")
        return 0, 1

def delete_save():
    save_id = input("Enter the ID of the save game to delete: ")
    game_state = session.query(GameState).filter_by(id=save_id).first()
    if game_state:
        session.delete(game_state)
        session.commit()
        print(f"Saved game with ID {save_id} deleted successfully!")
    else:
        print("No saved game found with that ID.")

def list_saves():
    saves = session.query(GameState).all()
    if saves:
        print("\nSaved Games:")
        for save in saves:
            print(f"ID: {save.id}, Score: {save.score}, Shift: {save.shift}")
    else:
        print("No saved games found.")
