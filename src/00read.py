from database.connection import execute_query, create_connection
import psycopg2
def read_hero(name):
    query = """
        SELECT *
        FROM heroes
        WHERE name = %s
    """
    try:
        cursor = execute_query(query, (name,))
        result = cursor.fetchall()
        cursor.close()  
        cursor.connection.close() 
        return result
    except psycopg2.InterfaceError as e:
        print(f"The error '{e}' occurred. The cursor might already be closed.")
        return None

hero_name = input("Which hero do you want to see? ")
hero_info = read_hero(hero_name)

if hero_info:
    print("Hero:")
    for hero in hero_info:
        print(hero)
else: print (f"Not a hero or hero was banished")