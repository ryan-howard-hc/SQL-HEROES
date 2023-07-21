from database.connection import execute_query

def alter_table_frenemies():
    query = """
    ALTER TABLE heroes
    ADD COLUMN friends INT,
    ADD COLUMN foes INT
    """
    execute_query(query)

alter_table_frenemies()