from database.connection import execute_query, create_connection


def alter_table_heroes():
    query="""
    ALTER TABLE heroes
    ADD COLUMN likes VARCHAR,
    ADD COLUMN dislikes VARCHAR
    """
    execute_query(query)

alter_table_heroes()