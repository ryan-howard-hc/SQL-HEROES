from database.connection import execute_query, create_connection

def update_hero(name, about_me, biography,):
    name = input ("Who's evolving?: ")
    about_me = input ("Life changing moment?: ")
    biography = input ("Updated origin: ")
    query = """
    UPDATE heroes
    SET about_me = %s, biography= %s
    WHERE name = %s
    """
    execute_query(query,(name, about_me, biography))
    print(f"{name} UPDATED!")
    
update_hero("", "", "")