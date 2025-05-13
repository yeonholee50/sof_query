from config import mongo_uri
from pymongo import MongoClient
import json
import os
import time

def load_json_to_mongodb(file_path, collection_name):
    """
    Load JSON file into MongoDB collection one document at a time
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        return False
    
    try:
        # Load JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Connect to MongoDB with SSL options
        client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
        db = client["usul"]
        
        # Clear existing data in collection
        db[collection_name].delete_many({})
        print(f"Cleared existing data in {collection_name} collection")
        
        # Insert data one by one
        success_count = 0
        if isinstance(data, list):
            total = len(data)
            for i, item in enumerate(data):
                try:
                    result = db[collection_name].insert_one(item)
                    print(f"Loaded document {i+1}/{total}: {item.get('name', 'Unnamed')}")
                    success_count += 1
                    # Small delay to avoid overwhelming the server
                    time.sleep(0.1)
                except Exception as e:
                    print(f"Error loading document {i+1}: {str(e)}")
        else:
            result = db[collection_name].insert_one(data)
            print(f"Successfully loaded document into {collection_name} collection")
            success_count = 1
            
        print(f"Loading complete. Successfully loaded {success_count} documents into {collection_name} collection")
        return True
        
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    return False

if __name__ == "__main__":
    # Load sofweek_agenda.json
    load_json_to_mongodb("sofweek_agenda.json", "sofweek_agenda")

