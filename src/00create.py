from database.connection import execute_query, create_connection

def create_hero(name, about_me, biography):
    name = input ("Enter Name: ")
    about_me = input ("About: ")
    biography = input ("Give us your origin story: ")
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))
    print(f"{name} CREATED!")
    
create_hero("", "" , "")