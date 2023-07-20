from database.connection import execute_query, create_connection

def create_hero(name, about_me, biography):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))
create_hero("Ben", "Me Little Strong", "Grocery Manager")