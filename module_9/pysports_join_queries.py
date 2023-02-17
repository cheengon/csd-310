import mysql.connector  # import the MySQL Connector Python module
from mysql.connector import errorcode  # import the error codes for handling MySQL errors

# database configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # inner join query to get player data along with their team name
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # fetch all player records
    players = cursor.fetchall()

    # display player records
    print("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"  Player ID: {player[0]}\n  First Name: {player[1]}\n  Last Name: {player[2]}\n  Team Name: {player[3]}\n")

    # pause execution and wait for user input
    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    # handle potential errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    # close database connection
    db.close()