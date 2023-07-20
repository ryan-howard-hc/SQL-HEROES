##DELETE CHARACTER

def delete_hero(name, about_me, biography):
    query = """
        DELETE FROM heroes
        WHERE name, about_me, biography = (%s, %s, %s)
    """
    execute_query(query,(name, about_me, biography))