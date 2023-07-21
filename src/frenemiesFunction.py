from database.connection import execute_query, create_connection

def match_heroes(data):
    hero_mapping = {}

    for item in data:
        hero1_id = item["hero1_id"]
        hero2_id = item["hero2_id"]
        relationship_type_id = item["relationship_type_id"]

        # Check if the relationship_type_id is 1 or 2 and match hero1 with hero2 accordingly
        if relationship_type_id == 1 or relationship_type_id == 2:
            hero_mapping[hero1_id] = hero2_id

    return hero_mapping

frenemies_json = """
[
  {
    "hero1_id": 4,
    "hero2_id": 1,
    "relationship_type_id": 2
  },
  {
    "hero1_id": 4,
    "hero2_id": 5,
    "relationship_type_id": 2
  },
  {
    "hero1_id": 4,
    "hero2_id": 3,
    "relationship_type_id": 2
  },
  {
    "hero1_id": 4,
    "hero2_id": 2,
    "relationship_type_id": 2
  },
  {
    "hero1_id": 3,
    "hero2_id": 1,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 3,
    "hero2_id": 5,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 3,
    "hero2_id": 2,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 2,
    "hero2_id": 1,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 2,
    "hero2_id": 3,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 6,
    "hero2_id": 1,
    "relationship_type_id": 1
  },
  {
    "hero1_id": 6,
    "hero2_id": 5,
    "relationship_type_id": 2
  },
  {
    "hero1_id": 6,
    "hero2_id": 2,
    "relationship_type_id": 1
  }
]
"""
    
#Make a function that lists out each hero id, and their corresponding friends and enemies in a list 

#Create corresponding columns for friend and foe

#Attach function from id's to corresponding friend, foe, and have it list in the table
    
#Tie relationship_type_id on relationships table to the corresponding id values for friends
#and enemies in relationship_types table
