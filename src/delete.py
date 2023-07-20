from database.connection import execute_query, create_connection


##DELETE CHARACTER

def delete_hero():
    name = input("Which hero would you like to delete: ")
    query = """
        DELETE FROM heroes
        WHERE name = %s
    """
    execute_query(query,(name,))
    print(f"{name} BANISHED!")
    
delete_hero()