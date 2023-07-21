from database.connection import execute_query, create_connection

def create_hero(name, about_me, biography, likes, dislikes):
    name = input ("Enter Name: ")
    about_me = input ("About: ")
    biography = input ("Give us your origin story: ")
    likes = input ("What does the hero like?: ")
    dislikes = input ("What does the hero dislike: ")
    query = """
        INSERT INTO heroes (name, about_me, biography, likes, dislikes)
        VALUES (%s, %s, %s, %s, %s)
        """
    execute_query(query,(name, about_me, biography, likes, dislikes))
    print(f"{name} CREATED!")
    
# create_hero("MadDog Ryan", "Daylight as a street magician, Moonlight as a mad pussycat" , "Became mad pussycat through cat scratch fever")
create_hero("","","","","")

