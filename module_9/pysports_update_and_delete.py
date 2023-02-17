import mysql.connector
from mysql.connector import errorcode

# Define the database configuration object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Define a function to show all the players in the player table
def show_players(cursor, title):
    # Execute an inner join query on the player and team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    # Get the results from the cursor object 
    players = cursor.fetchall()
    # Print the title
    print("\n  -- {} --".format(title))
    # Iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    # Try to connect to the pysports database 
    db = mysql.connector.connect(**config)
    # Get the cursor object
    cursor = db.cursor()

    # Define the query to add a new player
    add_player = ("INSERT INTO player(first_name, last_name, team_id) VALUES(%s, %s, %s)")
    # Define the data to be inserted into the player table 
    player_data = ("Smeagol", "Shire Folk", 1)
    # Execute the query to add the new player to the player table 
    cursor.execute(add_player, player_data)
    # Commit the insert to the database 
    db.commit()
    # Show all the records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # Define the query to update the newly inserted record
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    # Execute the update query 
    cursor.execute(update_player)
    # Show all the records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # Define the query to delete the record with the first name of "Gollum"
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    # Execute the delete query 
    cursor.execute(delete_player)
    # Show all the records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    # Handle any MySQL database errors 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    # Close the database connection 
    db.close()
