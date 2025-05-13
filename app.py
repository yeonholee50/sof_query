from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from typing import List, Dict, Any, Optional
from config import mongo_uri
import re
from bson import ObjectId
import json
import os

app = FastAPI(title="SOF Week API", description="API for querying SOF Week attendee data")

# Custom JSON encoder to handle MongoDB's ObjectId
class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

# Helper function to convert MongoDB document to JSON serializable dict
def mongo_doc_to_json(doc):
    if doc is None:
        return None
    doc_dict = dict(doc)
    for k, v in doc_dict.items():
        if isinstance(v, ObjectId):
            doc_dict[k] = str(v)
    return doc_dict

# Global client variable
client = None
db = None
collection = None

# Function to get MongoDB connection
def get_db():
    global client, db, collection
    if client is None:
        try:
            client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
            db = client["usul"]
            collection = db["sofweek_agenda"]
            # Test connection
            db.command('ping')
            print("Successfully connected to MongoDB")
        except Exception as e:
            print(f"MongoDB connection error: {str(e)}")
            raise
    return collection

# Connect on startup
@app.on_event("startup")
async def startup_db_client():
    get_db()

# Close connection on shutdown
@app.on_event("shutdown")
async def shutdown_db_client():
    global client
    if client:
        client.close()
        print("MongoDB connection closed")

# Function to get all documents
async def get_all_documents() -> List[Dict[str, Any]]:
    """
    Get all documents from the collection
    """
    try:
        collection = get_db()
        cursor = collection.find({})
        results = [mongo_doc_to_json(doc) for doc in cursor]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Generic search function to avoid repeating code (DRY principle)
async def search_collection(field: str, query: str) -> List[Dict[str, Any]]:
    """
    Generic search function that finds documents where the specified field contains the query string
    """
    # If query is empty, return all documents
    if not query:
        return await get_all_documents()
        
    try:
        collection = get_db()
        # Create case-insensitive regex pattern for partial matching
        regex_pattern = re.compile(f".*{re.escape(query)}.*", re.IGNORECASE)
        
        # Query the collection
        cursor = collection.find({field: regex_pattern})
        
        # Convert cursor to list and ensure ObjectId is properly converted to string
        results = [mongo_doc_to_json(doc) for doc in cursor]
        
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {"message": "SOF Week Agenda API", 
            "endpoints": ["/name/{query}", "/position/{query}", 
                         "/organization/{query}", "/filter/{query}",
                         "/name", "/position", "/organization", "/filter"]}

# Endpoints that handle both empty and non-empty queries
@app.get("/name/{query}")
@app.get("/name")
async def search_by_name(query: Optional[str] = ""):
    """Search for attendees by name (partial match). Empty query returns all records."""
    results = await search_collection("name", query)
    return {"count": len(results), "results": results}

@app.get("/position/{query}")
@app.get("/position")
async def search_by_position(query: Optional[str] = ""):
    """Search for attendees by position (partial match). Empty query returns all records."""
    results = await search_collection("position", query)
    return {"count": len(results), "results": results}

@app.get("/organization/{query}")
@app.get("/organization")
async def search_by_organization(query: Optional[str] = ""):
    """Search for attendees by organization (partial match). Empty query returns all records."""
    results = await search_collection("organization", query)
    return {"count": len(results), "results": results}

@app.get("/filter/{query}")
@app.get("/filter")
async def filter_by_bio(query: Optional[str] = ""):
    """Search for attendees by bio content (partial match). Empty query returns all records."""
    results = await search_collection("bio", query)
    return {"count": len(results), "results": results}

if __name__ == "__main__":
    import uvicorn
    # Get port from environment variable or use default
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
