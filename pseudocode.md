# MoSCoW

Must haves:
- Connect/Create to superhero database: Database for storage
- List superheroes and pals: For game to ask list of all heroes and their pals
- Ability to create new hero
- Update hero information if names/powers/friends change
- Be able to delete hero

Should haves:
- Abilities: Feature to add/show abilities of each hero
- Enemies: Keep track of villains and connected hero nemeses

Could haves:
- Mutual Friends: Instagram for heroes to determine mutual hero pals
- Likes and Dislikes: Details about heroes and their likes and dislikes
- Hero search: Feature that allows search by names/powers/mutual friends, etc

Wont haves: 
- Front end development?


# USER STORIES (AS ANONYMOUS USER...)
- Display tables to observe all these heroes and their connections
- Be able to add new heroes for display
- Be able to update and their heroes if something changes or delete them altogether


# Procedural
1. Connect to the database using Python and PostgreSQL
2. Follow the MoSCoW and CRUD(create,read,update,delete)to implement the desired tables and data for usage


# FUNCTIONAL
```
C: def create_heroes_table():
        create_table_query = """
        SELECT * from heroes(
            id int [pk]
            name VARCHAR
            about_me VARCHAR
            biography text
        );"""

   def create_heroes():
        name = input("Enter name: ")
        friend = input("Enter friend name: ")
        insert_query = f"INSERT INTO superheroes (name, friend) VALUES ('{name}', '{friend}');"
        cursor.execute(insert_query)
        connection.commit()
        print (f"{name} added to the superhero list with {friend} as a friend!")
```
R: 
```
    execute_query("Select name, power, friends FROM heroes;")
```
U:
```
    def add_hero():
        name = input("Enter superhero's name: ")
        friend = input("Enter superhero's friend's name: ")
        insert_query = f"INSERT INTO superheroes (name, friend) VALUES ('{name}', '{friend}');"
        cursor.execute(insert_query)
        connection.commit()
        print(f"{name} added to the superhero list with {friend} as a friend!")
    
```
D:
```
    def delete_hero():
        name = input("Enter superhero's name to delete: ")
        delete_query = f"DELETE FROM superheroes WHERE name = '{name}';"
        cursor.execute(delete_query)
        connection.commit()
        print(f"{name} has been removed from the superhero list!")
```