from database.connection import execute_query, create_connection




##CREATE CHARACTER

def create_hero(name, about_me, biography):
    name = input ("Enter Name: ")
    about_me = input ("Enter friend name: ")
    biography = input ("Give us your origin story")
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))
create_hero("MadDog Ryan", "Daylight as a street magician, Moonlight as a mad pussycat" , "Became mad pussycat through cat scratch fever")

##DELETE CHARACTER

