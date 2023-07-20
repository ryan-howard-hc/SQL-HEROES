from database.connection import execute_query, create_connection

def read_hero(name):
    query = """
        SELECT *
        FROM heroes
        WHERE name = %s
    """
    result = execute_query(query, (name))
    return result

hero_name = input("Which hero do you want to see? ")
hero_info = read_hero(hero_name)

if hero_info:
    for hero in hero_info:
        print(hero)
else: print (f"Not a hero or hero was banished")