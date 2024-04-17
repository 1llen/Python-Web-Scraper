from pymongo import MongoClient

def connect_to_db():
    """
    Connect to MongoDB. 

    Returns:
    client (MongoClient): A MongoClient object that can be used to connect to MongoDB.
    """
    # REPLACE WITH ENVIRONMENT VARIABLE
    connection_string = "mongodb+srv://allen:thisisthedumbpassword@mongonba.cnucra6.mongodb.net/?retryWrites=true&w=majority&appName=mongoNBA"
    database_name = "NBA"
    
    client = MongoClient(connection_string)
    database = client[database_name]
    
    return client, database

def load_player_to_db(player_data, team_name):
    """
    Insert or update player data in MongoDB to avoid duplicates.

    Args:
        player_data (dict): A dictionary containing player data.
        team_name (str): The name of the team.

    Returns:
        None
    """
    client, db = connect_to_db()

    try:
        # Access the players collection
        players_collection = db["players"]
        
        # filters through name to avoid duplicates
        filter_query = {"name": player_data["Name"]}
        update_query = {
            "$set": {
                "number": player_data["Number"],
                "position": player_data["Position"],
                "height": player_data["Height"],
                "weight": player_data["Weight"],
                "date_of_birth": player_data["Date of Birth"],
                "age": int(player_data["Age"]),
                "experience": player_data["Experience"],
                "team": team_name
            }
        }

        players_collection.update_one(filter_query, update_query, upsert=True)
        print("Player data loaded to MongoDB successfully")
        
    except Exception as e:
        print(f"Error loading player data to MongoDB: {e}")
        
    finally:
        # close the database connection
        client.close()

def load_coach_to_db(coach_data, team_name):
    """
    Insert or update coach data in MongoDB to avoid duplicates.

    Args:
        coach_data (dict): A dictionary containing coach data.
        team_name (str): The name of the team.

    Returns:
        None
    """
    client, db = connect_to_db()

    try:
        # Access the coaches collection
        coaches_collection = db["coaches"]
        
        # filters through first_name and last_name to avoid duplicates
        filter_query = {"first_name": coach_data["First Name"], "last_name": coach_data["Last Name"]}
        update_query = {
            "$set": {
                "role": coach_data["Role"],
                "team": team_name
            }
        }

        coaches_collection.update_one(filter_query, update_query, upsert=True)
        print("Coach data loaded to MongoDB successfully")

    except Exception as e:
        print(f"Error loading coach data to MongoDB: {e}")
        
    finally:
        # close the database connection
        client.close()
        
def check_URL_in_db(URL):
    """
    Check if URL exists in MongoDB.

    Args:
        URL (str): The URL to be checked.

    Returns:
        bool: True if URL exists in MongoDB, False otherwise.
    """
    client, db = connect_to_db()
    
    try:
        # Access the URLs collection
        URLs_collection = db["URLs"]
        
        # Check if URL exists
        filter_query = {"url": URL}
        result = URLs_collection.find_one(filter_query)
        
        # If URL exists, return True
        if result is not None:
            print("URL already exists in MongoDB")
            return True
        
        # If URL does not exist, return False
        print("URL does not exist in MongoDB")
        return False
    
    except Exception as e:
        print(f"Error checking if URL exists in MongoDB: {e}")
        
    finally:
        # close the database connection
        client.close()
        
def load_URL_to_db(URL):
    """
    Insert or update URL data in MongoDB to avoid duplicates.

    Args:
        URL (str): The URL to be inserted or updated.

    Returns:
        None
    """
    client, db = connect_to_db()
    
    try: 
        # Access the URLs collection
        URLs_collection = db["URLs"]
        
        # Check if URL already exists
        filter_query = {"url": URL}
        result = URLs_collection.find_one(filter_query)
        
        # If URL does not exist, insert it
        if result is None:
            URLs_collection.insert_one({"url": URL})
            print("URL loaded to MongoDB successfully")
            
            # Return false to indicate did not exist before
            return False
        
        # If URL exists, return true to indicate already exists
        print("URL already exists in MongoDB")
        return True
    
    except Exception as e:
        print(f"Error loading URL to MongoDB: {e}")
        
    finally:
        # close the database connection
        client.close()
        
        
        
        
        
        
        