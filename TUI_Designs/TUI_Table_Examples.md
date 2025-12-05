# Banner python format
```


print("\n" + banner_border + BOLD +
"————————————————————————————————————————————————————————————————————————————————" + RESET + BOLD +
"""
    ____  __  __              _____                  __ 
   / __ \/ / / /    __       / ___/____  ____  _____/ /_
  / /_/ / / / /   / _ \______\__ \/ __ \/ __ \/ ___/ __/
 / _, _/ /_/ /   /  __/_____/__/ / /_/ / /_/ / /  / /_  
/_/ |_|\____/    \___/     /____/ .___/\____/_/   \__/  
                                /_/                                                                      
    ______     __                                                               
   / ____/  __/ /__________ __   ______ _____ _____ _____  ____  ____ _         
  / __/ | |/_/ __/ ___/ __ `/ | / / __ `/ __ `/ __ `/ __ \/_  / / __ `/         
 / /____>  </ /_/ /  / /_/ /| |/ / /_/ / /_/ / /_/ / / / / / /_/ /_/ /          
/_____/_/|_|\__/_/   \__,_/ |___/\__,_/\__, /\__,_/_/ /_/ /___/\__,_/           
                                      /____/                                      
""" + REDHIGH +
"————————————————————————————————————————————————————————————————————————————————" + RESET + "\n")

```


# TUI Tables

- ~~~~~~~~~ = some string
- XX = some int
- All tables are 80 characters long
- The menu name is formatted in the middle, ish
- the tables print "Choose Action" when there are multiple possible inputs and "Enter SOMETHING" when prompting for one specific thing
- ALLCAPS = info that depends on user inputs and program info (not fully implemented)
- MISSING at the top of the table places means that it is unfinished or needs to be polished etc

- The table formats are NOT law and can be changed if you deem neccisary but just inform others if you make big changes so that it can be consistant throughout the program
- This is also just a rough first draft and just let me know (Andri) if you have any thoughts or questions







### Start Page:

```
————————————————————————————————————————————————————————————————————————————————
    ____  __  __              _____                  __ 
   / __ \/ / / /   ___       / ___/____  ____  _____/ /_
  / /_/ / / / /   / _ \______\__ \/ __ \/ __ \/ ___/ __/
 / _, _/ /_/ /   /  __/_____/__/ / /_/ / /_/ / /  / /_  
/_/ |_|\____/    \___/     /____/ .___/\____/_/   \__/  
                               /_/                                                                      
    ______     __                                                               
   / ____/  __/ /__________ __   ______ _____ _____ _____  ____  ____ _         
  / __/ | |/ / __/ ___/ __ `/ | / / __ `/ __ `/ __ `/ __ \/_  / / __ `/         
 / /___ >  </ /_/ /  / /_/ /| |/ / /_/ / /_/ / /_/ / / / / / /_/ /_/ /          
/_____/_/|_|\__/_/   \__,_/ |___/\__,_/\__, /\__,_/_/ /_/ /___/\__,_/           
                                      /____/                                      
————————————————————————————————————————————————————————————————————————————————



————————————————————————————————————————————————————————————————————————————————
                                 Start Page
————————————————————————————————————————————————————————————————————————————————
1 Login
2 Register 
3 Spectate
q Quit
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```





### Login:

```


StartPage -> Login
————————————————————————————————————————————————————————————————————————————————
                                    Login
————————————————————————————————————————————————————————————————————————————————
Input Your Handle:
PLAYERHANDLE

```






### Admin page:

```


StartPage -> AdminPage
————————————————————————————————————————————————————————————————————————————————
                                Admin Page
————————————————————————————————————————————————————————————————————————————————
1 Create Tournament
2 Manage Tournaments
3 Create Club
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Create Tournament

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program

- Will have an example at the bottom of the file in its own cattegory



```

AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
TOURNAMNENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 PLACENAME, CITYNAME
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
YYYY MM MM
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
Enter Contact Email:
SOMETHING@SOMWTHING.COM
————————————————————————————————————————————————————————————————————————————————
Enter Contact Phone Number:
PHONENUMBER
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Manage Tournament

```


AdminPage -> ManageTournaments
————————————————————————————————————————————————————————————————————————————————
                            Manage Tournaments
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Tournaments- - - -
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
————————————————————————————————————————————————————————————————————————————————
Choose A Tournament To Manage:


```






### Create Club

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


AdminPage -> CreateClub
————————————————————————————————————————————————————————————————————————————————
                                Create Club
————————————————————————————————————————————————————————————————————————————————
Input Club Name:
CLUBNAME
————————————————————————————————————————————————————————————————————————————————
Input Club Colour (club color options):
CLUBCOLOR
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————



```


### Manage Unactive Tournament

```


ManageTournaments -> ManageUnactiveTournaments
————————————————————————————————————————————————————————————————————————————————
                         Manage Unactive Tournaments
————————————————————————————————————————————————————————————————————————————————
- - - -TorunamentName- - - -

1 Manage Teams
2 Publish
3 Edit Tournament
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```




### Manage Active Tournament

```

ManageTournaments -> ManageActiveTournaments
————————————————————————————————————————————————————————————————————————————————
                        Manage Active Tournaments
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
1 Input Results Of Match
2 Next Round
3 Cancel Tournament
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```




### Publish

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```

ManageTournaments -> ManageUnactiveTournament -> Publish
————————————————————————————————————————————————————————————————————————————————
                                    Publish 
————————————————————————————————————————————————————————————————————————————————
Do You Want To Publish TOURNAMENTNAME? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
TOURNAMENTNAME Has Been Published
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


(If user inputs “N” it will go back to previous screen)

```


### Edit Tournament

```


ManageTournaments -> ManageUnactiveTournament -> EditTournament
————————————————————————————————————————————————————————————————————————————————
					             Edit Tournament
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -

Date: YYYY MM DD - YYYY MM DD
Venue: 123 PLACENAME, CITYNAME
Contact Info:
	Email: SOMTH@SOMTH.COM
	Phone number: PHONENUMBER

————————————————————————————————————————————————————————————————————————————————
1 Edit Time / Date
2 Edit Info
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```


### Manage Teams

```


ManageTournaments -> ManageUnactiveTournament -> ManageTeams
————————————————————————————————————————————————————————————————————————————————
                                Manage Teams
————————————————————————————————————————————————————————————————————————————————
- - — -TEAMNAME- - - -

1 Add Team
2 Remove Team
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Add Team

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


ManageTournaments -> ManageUnactiveTournament -> ManageTeams -> AddTeam
————————————————————————————————————————————————————————————————————————————————
                                Add Team
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -

Enter Team Name or "l" to list all:
TEAMNAME
————————————————————————————————————————————————————————————————————————————————
TEAMNAME Was Found, Do You Want To Continue? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
TEAMNAME Has Been Added!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


(If user inputs “N” it goes to the search again)

```


### Remove Team

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program

```


ManageTournaments -> ManageUnactiveTournament -> ManageTeams -> RemoveTeam
————————————————————————————————————————————————————————————————————————————————
                                Remove Team
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
Enter Team Name Or "l" To List All:
TEAMNAME
————————————————————————————————————————————————————————————————————————————————
TEAMNAME Was Found, Do You Want To Continue? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
TEAMNAME Has Been Removed!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————



```




### Edit Time

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


EditTournament -> EditTime
————————————————————————————————————————————————————————————————————————————————
                                Edit Time
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
Old Date: YYYY MM DD - YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
Enter New Start Date:
YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
Enter New End Date:
YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
The New Date Is: YYYY MM DD - YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————



```


### Edit Tournament Info

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


EditTournament -> EditTournamentInfo
————————————————————————————————————————————————————————————————————————————————
                            Edit Tournament Info
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Tournament Name:
TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Venue:
NEWVENUE
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Email:
NEWEMAIL
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Phone Number:
NEWPHONENUMBER
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```

### Matches

```


ManageTournaments -> ManageActiveTournament -> Matches
————————————————————————————————————————————————————————————————————————————————                        
                                    Matches
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
 
* Unfinished Matches *

ID: ID
Teams: TEAM1 - TEAM2

ID: ID
Teams: TEAM3 - TEAM4

ID: ID
Teams: TEAM5 - TEAM6

ID: ID
Teams: TEAM7 - TEAM8

————————————————————————————————————————————————————————————————————————————————
Select Match ID:

```





### Next Round
MISSING (Not Yet Implemented)
```


ManageTournaments -> ManageActiveTournament -> NextRound
————————————————————————————————————————————————————————————————————————————————





```

### Cancel Tournament

```


ManageTournaments -> ManageActiveTournament -> CancelTournament
————————————————————————————————————————————————————————————————————————————————
                                CancelTournament
————————————————————————————————————————————————————————————————————————————————
Are You Sure That You Want To Cancel TOURNAMENTNAME? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
TOURNAMENTNAME Has Been Cancelled


```

### Match Results

```


ManageTournaments -> ManageActiveTournament -> Matches -> MatchResults
————————————————————————————————————————————————————————————————————————————————
                                Match Results
————————————————————————————————————————————————————————————————————————————————
Match: TEAM1 vs TEAM2
————————————————————————————————————————————————————————————————————————————————
Select Team To Advance:

```




### Player Page

```


Login -> PlayerPage
————————————————————————————————————————————————————————————————————————————————
                                Player Page
————————————————————————————————————————————————————————————————————————————————
Name: PLAYERNAME
Date of Birth: YYYY MM DD
Home Address: 123 PLACENAME, CITYNAME
Phone Number: PHONENUMBER
Email: SOMTH@SOMTH.COM
Team: TEAMNAME (can be “NONE”)
Club: TEAMNAME (can be “NONE”)
Handle: PLAYERHANDLE
Rank: Player / Captain

- - - - STATS- - - -
Wins: X
Points: X
Teams Played For: TEAMNAME (can be “NONE”)
Tournaments Played: TOURNAMENTNAME (can be “NONE”)
————————————————————————————————————————————————————————————————————————————————
1 Edit Info
2 My Team
3 Create a Team
q Log Out
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Edit Player Info

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> EditPlayerInfo 
————————————————————————————————————————————————————————————————————————————————
                                Edit Player Info 
————————————————————————————————————————————————————————————————————————————————
- - - -PLAYERNAME- - - -
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Name:
NEWNAME
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Date Of Birth:
NEWDOB
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Address:
NEWHOMEADDRESS
————————————————————————————————————————————————————————————————————————————————
(Leave Field Empty If You Want To Leave Them Unchanged)
Enter New Phone Number:
NEWPHONEADDRESS
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————




```

### My Team

```

PlayerPage -> MyTeam
————————————————————————————————————————————————————————————————————————————————
                                My Team
————————————————————————————————————————————————————————————————————————————————
Rank:	    Handle:
- - - - - - - - - - - -
Captain:    PLAYERHANDLE
Member:     PLAYERHANDLE
Member:     PLAYERHANDLE
Member: 
. . .
————————————————————————————————————————————————————————————————————————————————
1 Edit Team
2 Leave Team
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### My Team (not in a team)

```


PlayerPage -> MyTeam
————————————————————————————————————————————————————————————————————————————————
                                My Team
————————————————————————————————————————————————————————————————————————————————
You Are Not In A Team!
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```



### Create Team

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> CreateTeam
————————————————————————————————————————————————————————————————————————————————
                               Create Team
————————————————————————————————————————————————————————————————————————————————
By Creating A Team You Are Assigned As The Captain Of It!
————————————————————————————————————————————————————————————————————————————————
Enter Team Name:
TEAMNAME
————————————————————————————————————————————————————————————————————————————————
Enter Team URL (Optional):

————————————————————————————————————————————————————————————————————————————————
Enter Team ASCII Art (Optional):

————————————————————————————————————————————————————————————————————————————————
- - - -List Of Clubs- - - -
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~
————————————————————————————————————————————————————————————————————————————————
Choose A Club To Join:
CLUBNAME
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```





### Create team (already in team)

```


PlayerPage -> CreateTeam
————————————————————————————————————————————————————————————————————————————————
                                Create Team
————————————————————————————————————————————————————————————————————————————————
You Are Already In A Team!
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```







### Edit Team

```


PlayerPage -> MyTeam -> EditTeam
————————————————————————————————————————————————————————————————————————————————
                                Edit Team
————————————————————————————————————————————————————————————————————————————————
Rank:	    Handle:
- - - - - - - - - - -
Captain:    PLAYERHANDLE
Member:     PLAYERHANDLE
Member:     PLAYERHANDLE
Member: 
. . .
————————————————————————————————————————————————————————————————————————————————
1 Add Player
2 Remove Player
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Leave Team (captain)

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> MyTeam -> LeaveTeam
————————————————————————————————————————————————————————————————————————————————
                                Leave Team
————————————————————————————————————————————————————————————————————————————————
Rank:	    Handle:
- - - - - - - - - - - -
Captain:    PLAYERHANDLE
Member:     PLAYERHANDLE
Member:     PLAYERHANDLE
Member: 
. . .
————————————————————————————————————————————————————————————————————————————————
Select A New Captain Before Leaving The Team:
PLAYERHANDLE
————————————————————————————————————————————————————————————————————————————————
You Have Succesfully Left The Team!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————




```

### Leave Team (player)

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> MyTeam -> LeaveTeam
————————————————————————————————————————————————————————————————————————————————
                                Leave Team
————————————————————————————————————————————————————————————————————————————————
Are You Sure That You Want To Leave TEAMNAME? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
You Have Succesfully Left TEAMNAME!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————




```

### Add Player

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> MyTeam -> EditTeam -> AddPlayer
————————————————————————————————————————————————————————————————————————————————
                                Add Player
————————————————————————————————————————————————————————————————————————————————
Enter A Players Name Or The First Letter(s) To Search:
PLAYERHANDLE
———————————————————————————————————————————————————————————————————————————————
The Handle "PLAYERHANDLE" Was Found, Do You Want To Add Them To Your Team? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
PLAYERHANDLE Has Been Added To Your Team!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

(If user Inputs “N” then it will just ask to search again)

```


### Remove Player

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program


```


PlayerPage -> MyTeam -> EditTeam -> RemovePlayer
————————————————————————————————————————————————————————————————————————————————
                                Remove Player
————————————————————————————————————————————————————————————————————————————————
Rank:	    Handle:
- - - - - - - - - - - -
Captain:    PLAYERHANDLE
Member:     PLAYERHANDLE
Member:     PLAYERHANDLE
Member: 
. . .
————————————————————————————————————————————————————————————————————————————————
Input Player To Reamove:
PLAYERHANDLE
————————————————————————————————————————————————————————————————————————————————
Are You Sure You Want To Remove PLAYERHANDLE? Y/N:
Y
————————————————————————————————————————————————————————————————————————————————
PLAYERHANDLE Has Been Removed!
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back 
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```

### Spectator Page

```


Login -> SpectatorPage
————————————————————————————————————————————————————————————————————————————————
                                Spectator Page
————————————————————————————————————————————————————————————————————————————————
1 Players
2 Clubs
3 Teams
4 Tournaments
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:

```




### Players - Spectator

```


SpectatorPage -> Players
————————————————————————————————————————————————————————————————————————————————
                                Players
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Players- - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
————————————————————————————————————————————————————————————————————————————————
Enter A Players Name Or The First Letter(s) To Search:
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```





### Clubs - Spectator

```


SpectatorPage -> Clubs
————————————————————————————————————————————————————————————————————————————————
                                Clubs
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Clubs- - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
————————————————————————————————————————————————————————————————————————————————
Enter A Clubs Name Or The First Letter(s) To Search:
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```




### Teams - Spectator

```


SpectatorPage -> Teams
————————————————————————————————————————————————————————————————————————————————
                                Teams
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Teams- - - -
~~~~~~
~~~~~~~~
~~~~
~~~~~~
————————————————————————————————————————————————————————————————————————————————
Enter A Teams Name Or The First Letter(s) To Search:
TEAMNAME
————————————————————————————————————————————————————————————————————————————————
TEAMNAME Was Found, Do You Want To Continue? Y/N:
Y

```





### View Player Stats
```


SpectatorPage -> Players -> ViewPlayerStats
————————————————————————————————————————————————————————————————————————————————
                            View Player Stats
————————————————————————————————————————————————————————————————————————————————
- - - -PLAYERHANDLE- - - -
Team: TEAMNAME
Wins: XX
Points: XX

Previous Teams: 
    TEAMNAME
    ...             (will just say "NONE" if there are not previous teams or clubs)?
Previous Clubs:
    CLUBNAME
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```

### View Club Stats

```


SpectatorPage -> Clubs -> ViewClubStats
————————————————————————————————————————————————————————————————————————————————
                                View Club Stats
————————————————————————————————————————————————————————————————————————————————
- - - -CLUBNAME- - - - (printed in the club color? or maybe the entire table???)
Wins: XX
Points: XX
Teams In CLUBNAME:
    TEAMNAME
    TEAMNAME
    ...
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:


```

### View Team Stats

```


SpectatorPage -> Teams -> ViewTeamStats
————————————————————————————————————————————————————————————————————————————————
                                View Team Stats
————————————————————————————————————————————————————————————————————————————————
- - - -TEAMNAME- - - -
Club: CLUBNAME (in color?)
Wins: XX
Points: XX
Players:
    Rank:	    Handle:
    - - - - - - - - - - - -
    Captain:    PLAYERHANDLE
    Member:     PLAYERHANDLE
    Member:     PLAYERHANDLE
    Member: 
    . . .
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```

### Tournaments

```

SpectatorPage -> Tournaments
————————————————————————————————————————————————————————————————————————————————
                                Tournaments
————————————————————————————————————————————————————————————————————————————————
~~~~~~~, active / archived
~~~~~~~, active / archived
————————————————————————————————————————————————————————————————————————————————
Select Tournament:
————————————————————————————————————————————————————————————————————————————————

```







### Active Tournament

```


SpectatorPage -> Tournaments -> ActiveTournament
————————————————————————————————————————————————————————————————————————————————
                            Active Tournament
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
————————————————————————————————————————————————————————————————————————————————
1 Game Info And Schedule
2 Teams
3 Brackets
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```

### Game Info And Schedule

```


SpectatorPage -> Tournaments -> ActiveTournament -> GameSchedule -> GameInfo
————————————————————————————————————————————————————————————————————————————————
                            Game Info And Schedule
————————————————————————————————————————————————————————————————————————————————
- - - -TOURNAMENTNAME- - - -
Date: YYYY MM DD - YYYY MM DD
Venue: VENUENAME
Contact Email: EMAIL@EMAIL.COM
Phone Number: PHONENUMBER
Nuber Of Teams: XX
Number Of Rounds: XX

- - - -Schedule- - - -
Match1: TEAMNAME vs TEAMNAME
Match2: TEAMNAME vs TEAMNAME
Match3: TEAMNAME vs TEAMNAME
Match4: TEAMNAME vs TEAMNAME
... 
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Actions:
————————————————————————————————————————————————————————————————————————————————


```

### Brackets (ACTIVE)
MISSING IMPLEMENTATION (visable brackets)
```


SpectatorPage -> Tournaments -> ActiveTournament -> Brackets
————————————————————————————————————————————————————————————————————————————————
                                Brackets
————————————————————————————————————————————————————————————————————————————————
T   T   T   T   T   T   T   T   T   T   T   T   T   T   T   T     (Only a possible way to show brackets)
E   E   E   E   E   E   E   E   E   E   E   E   E   E   E   E   (This does not account for odd numbered teams or >20 teams)
A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
M   M   M   M   M   M   M   M   M   M   M   M   M   M   M   M
N   N   N   N   N   N   N   N   N   N   N   N   N   N   N   N
A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
M   M   M   M   M   M   M   M   M   M   M   M   M   M   M   M
E   E   E   E   E   E   E   E   E   E   E   E   E   E   E   E
|---|   |---|   |---|   |---|   |---|   |---|   |---|   |---|
  |       |       |       |       |       |       |       |   
  T       T       T       T       T       T       T       T
  E       E       E       E       E       E       E       E
  A       A       A       A       A       A       A       A
  M       M       M       M       M       M       M       M
  N       N       N       N       N       N       N       N
  A       A       A       A       A       A       A       A
  M       M       M       M       M       M       M       M
  E       E       E       E       E       E       E       E
  |-------|       |-------|       |-------|       |-------|
      |               |               |               |       
      T               T               T               T
      E               E               E               E
      A               A               A               A
      M               M               M               M
      N               N               N               N
      A               A               A               A
      M               M               M               M
      E               E               E               E
      |---------------|               |---------------|
              |                                |
              T                                T
              E                                E
              A                                A
              M                                M
              N                                N
              A                                A
              M                                M
              E                                E
              |--------------------------------|        
                               |
                               T
                               E
                               A
                               M
                               N
                               A
                               M
                               E
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```

### Teams In Tournament (ACTIVE)

```


SpectatorPage -> Tournaments -> ActiveTournament -> TeamsInTournament
————————————————————————————————————————————————————————————————————————————————
                                Teams In Tournament
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Teams- - - -
TEAMNAME
TEAMNAME
TEAMNAME
TEAMNAME
TEAMNAME
...
————————————————————————————————————————————————————————————————————————————————
1 See More Team Details
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```

### Team Info In Tournament (ACTIVE)

```


SpectatorPage -> Tournaments -> ActiveTournament -> TeamsInTournament
————————————————————————————————————————————————————————————————————————————————
                                Teams In Tournament
————————————————————————————————————————————————————————————————————————————————
- - - -List Of Teams- - - -
TEAMNAME
TEAMNAME
TEAMNAME
TEAMNAME
TEAMNAME
...
————————————————————————————————————————————————————————————————————————————————
Enter Team Name For More Info:
TEAMNAME
————————————————————————————————————————————————————————————————————————————————



```

### Team Tournament Stats (ACTIVE)

```


ActiveTournament -> TeamsInTournament -> TeamTournamentStats
————————————————————————————————————————————————————————————————————————————————
                            Team Tournament Stats
————————————————————————————————————————————————————————————————————————————————
- - - -TEAMNAME- - - -
Rounds Won: XX
Rounds Lost: XX

Players:
    Rank:	    Handle:
    - - - - - - - - - - - -
    Captain:    PLAYERHANDLE
    Member:     PLAYERHANDLE
    Member:     PLAYERHANDLE
    Member: 
    . . .
————————————————————————————————————————————————————————————————————————————————
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————


```




### Register

- One input option appears at a time and the table gets bigger with each prompt?

- 
    ```
    ————————————————————————————————————————————————————————————————————————————————
    c Continue
    b Back
    ————————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————————
    ```

(Maybe appears after every prompt and user inputs "c" to save the last input and move onto the next one)?
makes the program more user forgiving and COULD be easier to save the information in the program

```


StartPage -> Register
————————————————————————————————————————————————————————————————————————————————
                                Register
————————————————————————————————————————————————————————————————————————————————
Enter Name:
PLAYERNAME
————————————————————————————————————————————————————————————————————————————————
Enter Date Of Birth: 
YYYY MM DD
————————————————————————————————————————————————————————————————————————————————
Enter Home Address:
123 PLACENAME, CITYNAME
————————————————————————————————————————————————————————————————————————————————
Enter Email:
SOMTH@SOMTH.COM
————————————————————————————————————————————————————————————————————————————————
Enter Gamer Handle:
PLAYERHANDLE
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————

```









## Example Table Flow For The Multiple Input Tables
```




AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
TOURNAMENTNAME








AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————
c





AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname







AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————
c







AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd





AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————






AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd






AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————






AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter Contact Email:
something@something.com





AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter Contact Email:
something@something.com
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————






AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter Contact Email:
something@something.com
————————————————————————————————————————————————————————————————————————————————
Enter Contact Phone Number:
1234567





AdminPage -> CreateTournament
————————————————————————————————————————————————————————————————————————————————
                              Create Tournament
————————————————————————————————————————————————————————————————————————————————
Enter Tournament Name:
Inputed TOURNAMENTNAME
————————————————————————————————————————————————————————————————————————————————
Enter Venue:
123 placename, cityname
————————————————————————————————————————————————————————————————————————————————
Enter Start Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter End Date:
yyyy mm dd
————————————————————————————————————————————————————————————————————————————————
Enter Contact Email:
something@something.com
————————————————————————————————————————————————————————————————————————————————
Enter Contact Phone Number:
1234567
————————————————————————————————————————————————————————————————————————————————
c Continue
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————
```











## Example For Bracket Options

T   T   T   T   T   T   T   T   T   T   T   T   T   T   T   T
E   E   E   E   E   E   E   E   E   E   E   E   E   E   E   E
A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
M   M   M   M   M   M   M   M   M   M   M   M   M   M   M   M
N   N   N   N   N   N   N   N   N   N   N   N   N   N   N   N
A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
M   M   M   M   M   M   M   M   M   M   M   M   M   M   M   M
E   E   E   E   E   E   E   E   E   E   E   E   E   E   E   E
|---|   |---|   |---|   |---|   |---|   |---|   |---|   |---|
  |       |       |       |       |       |       |       |   
  T       T       T       T       T       T       T       T
  E       E       E       E       E       E       E       E
  A       A       A       A       A       A       A       A
  M       M       M       M       M       M       M       M
  N       N       N       N       N       N       N       N
  A       A       A       A       A       A       A       A
  M       M       M       M       M       M       M       M
  E       E       E       E       E       E       E       E
  |-------|       |-------|       |-------|       |-------|
      |               |               |               |       
      T               T               T               T
      E               E               E               E
      A               A               A               A
      M               M               M               M
      N               N               N               N
      A               A               A               A
      M               M               M               M
      E               E               E               E
      |---------------|               |---------------|
              |                                |
              T                                T
              E                                E
              A                                A
              M                                M
              N                                N
              A                                A
              M                                M
              E                                E
              |--------------------------------|        
                               |
                               T
                               E
                               A
                               M
                               N
                               A
                               M
                               E
