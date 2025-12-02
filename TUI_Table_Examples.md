# TUI Tables

- ~~~~~~~~~ = some string
- XX = some int

- The table formats are NOT law and can be changed if you deem neccisary but just inform others if you make big changes so that it can be consistant throughout the program
- This is also just a rough first draft and just let me know (Andri) if you have any thoughts or questions

### Start Page:

```

Main Menu
—————————————
1 Login
2 Register 
3 Spectate
q Quit
——————————————
Choose Action:
——————————————

```





### Login:

```

Login
——————————————————
Input Your Handle:

```






### Admin page:

```

Admin Page
————————————————————
1 Create Tournament
2 Manage Tournaments
3 Create Club
b Back
————————————————————
Choose Action:
————————————————————

```





### Create Tournament

```

Create Tournament
———————————————————————————
Enter Tournament Name:
Inputed TournamentName
———————————————————————————
Enter Venue:
123 placename, cityname
———————————————————————————
Enter Start Date:
yyyy mm dd
———————————————————————————
Enter End Date:
yyyy mm dd
———————————————————————————
Enter Contact Email:
something@something.com
———————————————————————————
Enter Contact Phone Number:
1234567
———————————————————————————
c Continue
b Back
———————————————————————————
Choose Action:
———————————————————————————

```





### Manage Tournament

```

Manage Tournaments
——————————————————————————————————
- - - -List Of Tournaments - - - -
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
——————————————————————————————————
Choose A Tournament To Manage:


```






### Create Club










### Manage Unactive Tournament

```

Manage Unactive Tournaments
—————————————————————————————
- - - - TorunamentName- - - -

1 Manage Teams
2 Publish
3 Edit Tournament
b Back
—————————————————————————————
Choose Action:
—————————————————————————————

```




### Manage Active Tournament

```

Manage Active Tournaments
—————————————————————————————
- - - - TournamentName- - - -

1 Input Results Of Match
2 Next Round
3 Cancel Tournament
b Back
—————————————————————————————
Choose Action:
—————————————————————————————

```




### Publish

```

Publish 
———————————————————————————————————————————
Do You Want To Publish TournamentName? Y/N:
Y
———————————————————————————————————————————
TournamentName Has Been Published
———————————————————————————————————————————
c Continue
b Back
———————————————————————————————————————————
Choose Action:
———————————————————————————————————————————


(If user inputs “N” it will go back to previous screen)

```


### Edit Tournament

```

* * * User Path * * *
AdminPage [b ap] -> ManageTournaments [b mt] -> ManageUnactiveTournament [b mut]
—————————————————————————————————————————————————————————————————————————————————
					             Edit Tournament
—————————————————————————————————————————————————————————————————————————————————
- - - - - - - - - - - - - - - - -TournamentName- - - - - - - - - - - - - - - - - 

Date: yyyy mm dd - yyyy mm dd
Venue: 123 placename, cityname
Contact Info:
	Email: somth@somth.com
	Phone number: 1234567

—————————————————————————————————————————————————————————————————————————————————
1 Edit Time / Date
2 Edit Info
b Back
—————————————————————————————————————————————————————————————————————————————————
Choose Action:
—————————————————————————————————————————————————————————————————————————————————

```






### Manage Teams

```

Manage Teams
———————————————————
- - —TeamName - -

1 Add Team
2 Remove Team
b Back
———————————————————
Choose Action:
———————————————————

```





### Add Team

```

Add Team
—————————————————————————————————————————————————
- - - - - - - - -TournamentName- - - - - - - - -

Enter Team Name or ‘l’ to list all:
Inputed TeamName
—————————————————————————————————————————————————
TeamName Was Found, Do You Want To Continue? Y/N:
Y
—————————————————————————————————————————————————
TeamName Has Been Added!
—————————————————————————————————————————————————
b Back
—————————————————————————————————————————————————
Choose Action:
—————————————————————————————————————————————————


(If user inputs “N” it goes to the search again)

```


### Remove Team










### Edit Time










### Edit Tournament Info










### Matches

```

Matches
—————————————————————————
- - -TournamentName- - -
 
* Unfinished Matches *

ID: ID
Teams: Team1 - Team2

ID: ID
Teams: Team3 - Team4

ID: ID
Teams: Team5 - Team6

ID: ID
Teams: Team7 - Team8

—————————————————————————
Select Match ID:

```





### Next Round










### Cancel Tournament









### Match Results

```

Match Results
———————————————————————
Match: Team1 vs Team2
———————————————————————
Select Team To Advance:

```




### Player Page

```

Player Page
————————————————————————————————————————————————————
Name: PlayerName
Date of Birth: yyyy mm dd
Home Address: 123 placename, cityname
Phone Number: 1234567
Email: somth@somth.com
Team: TeamName (can be “NONE”)
Club: ClubName (can be “NONE”)
Handle: PlayerHandle
Rank: Player / Captain

- - - - - - - - - - - STATS- - - - - - - - - - - - - 
Wins: X
Points: X
Teams Played For: TeamName (can be “NONE”)
Tournaments Played: TournamentName (can be “NONE”)
————————————————————————————————————————————————————
1 Edit Info
2 My Team
3 Create a Team
q Log Out
————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————

```





### Edit Player Info










### My Team

```

My Team
————————————————————————
Rank:	Handle:
- - - - - - - - - - - - 
Captain: PlayerHandle
Member: PlayerHandle
Member: PlayerHandle
Member: 
. . .
————————————————————————
1 Edit Team
2 Leave Team
b Back
————————————————————————
Choose Action:
————————————————————————

```





### My Team (not in a team)

```

My Team
————————————————————————
You Are Not In A Team!
————————————————————————
b Back
————————————————————————
Choose Action:
————————————————————————

```



### Create Team

```

Create Team
———————————————————————————————————————————————————————————————
By Creating A Team You Are Assigned As The Captain Of It!
———————————————————————————————————————————————————————————————
Enter Team Name:
Inputed TeamName
———————————————————————————————————————————————————————————————
Enter Team URL (Optional):

———————————————————————————————————————————————————————————————
Enter Team ASCII Art (Optional):

———————————————————————————————————————————————————————————————
- - - - - - - - - - - - -List Of Clubs- - - - - - - - - - - - -
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
———————————————————————————————————————————————————————————————
Choose A Club To Join:
Inputed ClubName
———————————————————————————————————————————————————————————————
b Back
———————————————————————————————————————————————————————————————
Choose Action:
———————————————————————————————————————————————————————————————


```





### Create team (already in team)

```

Create Team
————————————————————————————————
You Are Already In A Team!
————————————————————————————————
b Back
————————————————————————————————
Choose Action:
————————————————————————————————

```







### Edit Team

```

Edit Team
————————————————————————
Rank:	Handle:
- - - - - - - - - - - - 
Captain: PlayerHandle
Member: PlayerHandle
Member: PlayerHandle
Member: 
. . .
————————————————————————
1 Add Player
2 Remove Player
b Back
————————————————————————
Choose Action:
————————————————————————

```





### Leave Team (captain)
 









### Leave Team (player)









### Add Player

```

Add Player
———————————————————————————————————————————————————————————————————————————————
Enter A Players Name Or The First Letter(s) To Search:
Inputed PlayerHandle
———————————————————————————————————————————————————————————————————————————————
The Handle “PlayerHandle” Was Found, Do You Want To Add Them To Your Team? Y/N:
Y
———————————————————————————————————————————————————————————————————————————————
PlayerHandle Has Been Added To Your Team!
———————————————————————————————————————————————————————————————————————————————
b Back
———————————————————————————————————————————————————————————————————————————————
Choose Action:
———————————————————————————————————————————————————————————————————————————————

(If user Inputs “N” then it will just ask to search again)

```


### Remove Player









### Spectator Page

```

Spectate Page
——————————————
1 Players
2 Clubs
3 Teams
4 Tournaments
b Back
——————————————
Choose Action:

```




### Players - Spectator

```

Players
——————————————————————————————————————————————————————
- - - - - - - - - -List Of Players- - - - - - - - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
——————————————————————————————————————————————————————
Enter A Players Name Or The First Letter(s) To Search:
———————————————————————————————————————————————————
Choose Action:
———————————————————————————————————————————————————

```





### Clubs - Spectator

```

Clubs
————————————————————————————————————————————————————
- - - - - - - - - -List Of Clubs- - - - - - - - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
————————————————————————————————————————————————————
Enter A Clubs Name Or The First Letter(s) To Search:
———————————————————————————————————————————————————
Choose Action:
———————————————————————————————————————————————————

```




### Teams - Spectator

```

Teams
———————————————————————————————————————————————————
- - - - - - - - - -List Of Teams- - - - - - - - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
———————————————————————————————————————————————————
Enter A Teams Name Or The First Letter(s) To Search:
———————————————————————————————————————————————————
Choose Action:
———————————————————————————————————————————————————

```





### View Player Stats









### View Club Stats









### View Team Stats









### Tournaments

```

Tournaments
——————————————————————————
~~~~~~~, active / archived
~~~~~~~, active / archived
——————————————————————————
Select Tournament:
——————————————————————————

```







### Active Tournament









### Game Schedule









### Brackets









### Teams In Tournament









### Team Tournament Stats









### Archieved Tournament

```

Archived Tournament
—————————————————————————————————————————
- - - - - - -TournamentName- - - - - - -

Tournament date: yyyy mm dd - yyyy mm dd
Rounds Played: XX
Winner: TeamName
—————————————————————————————————————————
1 Game Schedule
2 Teams
3 Brackets
b Back
—————————————————————————————————————————
Choose Action:
—————————————————————————————————————————

```





### Register

```

Register
————————————————————————
Enter Name:
Inputed PlayerName
————————————————————————
Enter Date Of Birth: 
yyyy mm dd
————————————————————————
Enter Home Address:
123 placename, cityname
————————————————————————
Enter Email:
something@something.com
————————————————————————
Enter Gamer Handle:
inputed Playerhandle
————————————————————————
c Continue
b Back
————————————————————————
Choose Action:
————————————————————————

```


