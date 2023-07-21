from database.connection import execute_query, create_connection

def update_hero(name, about_me, biography,):

    query = """
    UPDATE heroes
    SET about_me = %s, biography= %s
    WHERE name = %s
    """
    execute_query(query,(about_me, biography, name))
    print(f"{name} UPDATED!")
name = input ("Who's evolving?: ")
about_me = input ("Life changing moment?: ")
biography = input ("Updated origin: ")
update_hero(name, about_me, biography)

