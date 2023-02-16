import mysql.connector
from mysql.connector import Error, errorcode

# database connection configuration
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

    # create a cursor object
    cursor = db.cursor()

    # execute a SELECT query on the team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    # print the team records
    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print(f"Team ID: {team[0]}\nTeam Name: {team[1]}\nMascot: {team[2]}\n")

    # execute a SELECT query on the player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    # print the player records
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam ID: {player[3]}\n")

    # wait for user input before closing the connection
    input("\n\nPress any key to continue...")

except Error as err:
    # handle any errors that occur
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # close the database connection
    db.close()