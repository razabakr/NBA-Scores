
"""
This section of code has to do with opening a text file which contains 
all the nba teams. Purpose of for loop is to show the user a list of all the nba teams 
that are available as choices
"""

def listofNbaTeams():

	file2 = open("nbaTeams.txt", "r")
	nbaTeams = file2.readlines()

	for line in nbaTeams:
		eachNbaTeam = line.split("\n")				
		eachNbaTeam.pop()
		print(eachNbaTeam)

		"""


 ""Return a list of the nba teams"""
def teams():
	listofnbateams = []
	file2 = open("nbaTeams.txt", "r")
	nbaTeams = file2.readlines()

	for line in nbaTeams:
		eachNbaTeam = line.split("\n")				
		eachNbaTeam.pop()
		listofnbateams.append(eachNbaTeam[0])
	return listofnbateams


def scoresofTeams():
	listofGames = []
	file = open( "games.txt")
	nbaGames = file.readlines()
	file.close()

	for line in nbaGames:
		eachNbaGame = line.split("\n")		#each nba game is its own component of a list
		eachNbaGame.pop()
		listofGames.append(eachNbaGame)
	return listofGames

listofnbateams = teams()				#way to access a list of all the nba teams
listofGames = scoresofTeams()			#way to access the scores of both teams


def mainFunction():


	scoresBetweenTwoTeams = []				#list that will produce the scores of each time those two teams met
	file = open("games.txt")				#txt file which contains all the games
	games = file.readlines()				#parsing through the file
	file.close()							#close the file
				
	team1 = input("What is the first team? ")
	guess1 = type(team1)

	team2 = input("What is the second team? ")
	guess2 = type(team2)


	for line in games and if team1 and team2 in games:
			scoresBetweenTwoTeams.append(line)
	print(scoresBetweenTwoTeams)

mainFunction()


