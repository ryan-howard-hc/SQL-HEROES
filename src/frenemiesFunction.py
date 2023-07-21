from database.connection import execute_query, create_connection
import psycopg2

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

frenemies_data = eval(frenemies_json)

    # Step 2: Get the hero mapping from the JSON data
hero_mapping = match_heroes(frenemies_data)

try:
        # Step 3: Connect to the PostgreSQL database
        connection = create_connection("your_database_name", "your_database_user", "your_database_password")

        # Step 4: Create a cursor to interact with the database
        cursor = connection.cursor()

        # Step 5: Update the "friends" and "foes" columns in the "heroes" table
        for hero1_id, hero2_id in hero_mapping.items():
            # Update "friends" column for hero1
            query_update_friends = """
                UPDATE heroes
                SET friends = ARRAY_APPEND(friends, %s)
                WHERE id = %s
            """
            execute_query(query_update_friends, (hero2_id, hero1_id))

            # Update "foes" column for hero1
            query_update_foes = """
                UPDATE heroes
                SET foes = ARRAY_APPEND(foes, %s)
                WHERE id = %s
            """
            execute_query(query_update_foes, (hero2_id, hero1_id))

        # Step 6: Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Friends and foes updated successfully")

except psycopg2.Error as e:
        print(f"Error: {e}")

# Call the function to update friends and foes in the "heroes" table
update_friends_and_foes()


    
#Make a function that lists out each hero id, and their corresponding friends and enemies in a list 

#Create corresponding columns for friend and foe

#Attach function from id's to corresponding friend, foe, and have it list in the table
    
#Tie relationship_type_id on relationships table to the corresponding id values for friends
#and enemies in relationship_types table
