from database.connection import execute_query, create_connection


##CREATE CHARACTER

# def create_hero(name, about_me, biography):
#     query =  """
#         INSERT INTO heroes (name, about_me, biography)
#         VALUES (%s, %s, %s)
#         ON CONFLICT (name) DO UPDATE 
#         SET about_me = excluded.about_me,
#             biography = excluded.biography
#         """
#     execute_query(query,(name, about_me, biography))
# create_hero("MadDog Ryan", "Daylight as a street magician, Moonlight as a mad pussycat" , "Became mad pussycat through cat scratch fever")


