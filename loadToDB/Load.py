
from pymongo import MongoClient

def connect_to_db():
    # connect to mongoDB host 27017 
    client = MongoClient("mongodb://localhost:27017")
    #use NBAstats database
    return client.NBAstats

def load_player_to_db(player_data, team_name):
    #insert player data into MongoDB
    db = connect_to_db()

    try:
        # Customize player stats in MongoDB
        db.players.insert_one({
            "first_name": player_data["First Name"],
            "last_name": player_data["Last Name"],
            "number": player_data["Number"],
            "position": player_data["Position"],
            "height": player_data["Height"],
            "weight": player_data["Weight"],
            "date_of_birth": player_data["Date of Birth"],
            "age": player_data["Age"],
            "experience": player_data["Experience"],
            "team": team_name
        })
        print("Player data loaded to MongoDB successfully")

    except Exception as e:
        print(f"Error loading player data to MongoDB: {e}")

def load_coach_to_db(coach_data, team_name):
    # insert coach data into MongoDB
    db = connect_to_db()

    try:
        # Custonmize coach stats in MongoDB
        db.coaches.insert_one({
            "first_name": coach_data["First Name"],
            "last_name": coach_data["Last Name"],
            "role": coach_data["Role"],
            "team": team_name
        })
        print("Coach data loaded to MongoDB successfully")

    except Exception as e:
        print(f"Error loading coach data to MongoDB: {e}")
