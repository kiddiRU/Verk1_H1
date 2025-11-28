## Types of users and their actions:

### Privileges:  
Organizer/Admin > Team Captains > Players > Spectators

#### Organizers/Admin
- Create tournament
- Input results
- Add teams to tournament: need to be >= 16
- Edit times in tournament: delay or cancel 
- Create / edit clubs
- Chooses who wins in each round -- If there are odd teams the last team sits by after shuffling the teams 

#### Team captains  
- Cannot be in more than one team
- Creates his team
- modify team members (removing, adding and editing)
- When leaving a team then they choose a player to take their place as team captain (If no one left then the team is archived where it still holds the score and win information)
- When creating a team needs to joins a club
- After creating a team he then can see his team and add or remove players

#### Player
- Register self
- Leave a team
- Edit self
- Create a team and promote them selves to the team captain IF they are not already in a team

#### Spectators
- Game schedule
- Games:
  - Results
  - Teams
  - PLayers
  - Tournament?

- Tournament
  - Date
  - Teams
  - Rounds
  - Clubs
  - Teams
  - Players

- TO see matches and tournaments
- Get game schedule
- Get results
- See teams and clubs


# Prioritized Requirements
## Functional
### A
- The User can login as Organizer / Admin
- The User can register themselves as a player
- The User can login as a player 
- Spectator does not need to sign in
- Organizer can create a tournament
- Organizer can add and kick teams for the tournament before the start
- Organizer can start a tournament
- Organizer can input results for the tournament for each round
- Player can create a team
- Player becomes a team captain when team is created
- Team captain can leave the team
- Team captain can modify players in team (add / remove)
- Anyone can see matches and tournaments
- Anyone can see match schedule
- Anyone can see teams
- Organizer can view created tournaments
### B
- Organizer can create clubs
- Organizer can edit clubs
- When creating a team the player assigns the team to a club
- Anyone can see clubs
- Organizer can modify the time of a tournament before it has started
- Organizer can delete a tournament before it has been published
- When Organizer creates a tournament he has to choose between double elimination and normal
### C
- Team captain can transfer his authority to a player in team
- Team captain can switch from clubs
- Organizer can cancel a tournament
- Team captain can add ascii art to his team

## NON-Functional
### A
- System automatically shuffles and arrange teams in a tournament match, based on quantity of teams and the time frame
- When team captain leaves a team he assigns a team member to be the new team captain
- Tournaments automatically archive after they play out
- When team captain leaves a team if he was alone then the team is archived
- Each Player is in 1 team
- The system should not crash due to invalid data
- The players personal data should not be visible to the spectator
- Only the team captain can modify the team
- Only the organizer can create tournaments
- Code must follow Python type_hinting everywhere
- Code must follow the snake casing naming convention
- Player handle should be the length of 3-12
- Tournaments have 16 teams
- Tournaments generate UUID on creation
### B
- Only the organizer can modify clubs
- Give users options to cancel 
- Tournaments can have 16 or more teams
### C
- The Club Name will be printed in its color
- Show tournaments brackets visually 

# Use cases for requirements


# Test requirements


# Class diagrams
## Model classes
### Player
- Name
- Date of Birth
- Home Address
- Phone Number
- Handle: Unique
- Win counter
- Points (for Playing / winning?)
- Teams played for
- Tournaments played
- Apart of clubs
- is_team_captain

### Team
- List of Players 3 <= list <= 5
- Name: Unique
- CaptaiN Player handle
- Optional = url homepage, ascii art
- Win counter
- points (for Playing / winning?)
- Tournaments played
- Club

### Club
- Win counter
- Teams associated
- Club colors
- Name
- Created by the organizer

The Club file should have **Empty Club / NO Club** hardcoded into the text file so that teams can be created (Teams always need to join a club when created)

Club -> Team -> Player

### Tournament
- Receives info from organizers
- Date: start date - end date
- Allowed Time Frame of games
- Unique name
- Venue (location)
- Registered contact person (With e-mail and phone number) 
- Is active
- IS over
- Teams playing

### Matches
- Server ID
- What teams are Playing and when = Team A + Team B; Time
  - Time is between the start and end date of the tournament

## 3-tier design


# State diagrams
Teams
A team needs to have at least 3 amount of players to join a tournament
A team can have a maximum of 5 players? If it has 5 players, the captain cannot add more.
A player can have 3 states (Captain, In Team, Not In Team)
  •	Captain: Can view team and add or remove players
  •	Player in team: Can view his team, and can leave his team
  •	Player NOT in team: Can create a team
If captain leaves his team there can be two outcomes
  •	Captain leaves and selects a new captain from the team
  •	If the team is empty the captain leaves but the team still exists and has all statistics
A player can NOT leave his team if the team is in a tournament

Tournament
A Tournament has 3 states, and organizers capability is dependent on the state
  1.	A  Tournament is created but not published: in this state the organizer can still edit some information about the tournament. Add or remove teams, change date, venue, name and has the option to publish the                 tournament.
  2.	A Tournament is published: in this  state the organizer can no longer change the teams, date, venue, but can still change the name. Now the organizer has the option to input match results and  after all the matches        of that round have gotten a result he can start the next round.
  3.	A Tournament is archived: After all the rounds are over in a tournament the tournament goes to be archived, when its archived the organizer can no longer have any input into it, but it is still available for               everyone to see.
A tournament cannot start unless it has at least 16 teams
When organizer is adding a team, only teams with at least 3 players can be listed


# User group analysis


# UI-Design = Happy Path / User Flow

## Start page
1 Login
2 Register
3 Spectate
q Quit

## Login
Input your handle: 
b Back

## Admin Page
1 Manage Tournaments
2 Manage Clubs
b Back

### Manage Tournaments

!! NEED TO ADD THE ACTUAL CONTROL OF THE GAME !!

1 Publish 
2 Create Tournament
3 Edit Tournaments
b Back

#### Publish
--> The list of available tournaments

What tournament do you want to publish?: 

--> you choose: this tournament
--> do you want to continue?
Y Yes
N No

#### Create Tournament
Name: unique name 
Venue: some location
Start Date: YYYY-MM-DD
End Date:  YYYY-MM-DD
Email: something@something.something
Phone Number: 0000000

--> You have created a Tournament

#### Edit Tournaments
--> LIST OF ALL TOURNAMENTS ---
Choose tournament: this_tournament

this_tournament
1 Add Teams
2 Remove Teams
3 Edit time of Date
b Back

##### Add a Teams
Enter Team name or l for the list of all team or q to quit: abcd

--> abcd was found, do you want to continue?
Y Yes
N No

##### Remove a Team
Enter Team name or l for the list of all teams in the tournament or q to quit: abcd

--> abcd was found, do you want to continue?
Y Yes
N No

##### Edit Time of Date
--> old date: 2025-09-11 -> 2025-12-24
new start date:
new end date:

--> The new date is: something -> something
--> Do you want to continue?
Y Yes
N No

### Manage Clubs
1 Create Club
2 See Clubs
b Back

#### Create a Club
Name: Unique name
Color: some color

--> You have created a Club

#### See Club
--> list out all clubs

## Player Page
--> Name: some name
--> Date of Birth: 
--> Home Address:
--> Phone Number:
--> ------Non editable----
-x-> Team: team name 
-x-> Club: club name
-x-> Handle: unique handle
-x-> IS team captain Bool
--> ------------STATS--------------
-x-> Wins:
-x-> Points:
-x-> Teams Played For: [list of teams?]
-x-> Tournaments Played: [List of tournaments]

1 Edit Self
2 My Team
3 Create a Team
b Back

### Edit Self
--> Leave empty to keep old settings
Name: 
Date of Birth: 
Home Address: 
Phone Number: 

--> Do you want to continue?
Y Yes
N No

### My Team 
{NOTE} If team is empty it should let the user know
{NOTE} If the player is not the captain it should just list the team and have button 2 and b

--> Team: Team name

--> C - captains name
--> some name
--> some name
--> some name

1 Edit Team
2 Leave Team
b Back

#### Edit Team
1 Add Player
2 Remove Player
b Back

##### Add Player
{NOTE} if the player is already in a team it should show that

Enter a player name or the first letter(s) to search or q to quit: some player handle

--> some player handle is available
--> Do you want to add them to your team?
Y Yes
N No

##### Remove Player
--> List of player in the team
Input player to remove or q to quit: 

#### Leave Team
{NOTE} IF Team Captain and there are still player in the team then promote new team captain
{NOTE} If Team Captain and he was last in the team then archive the team

--> You have successfully leaved {team_name}

### Create a Team
{NOTE} By creating a Team you will automatically be promoted to Team Captain

Input unique name:
{Maybe} URL / HOMEPAGE:
{Maybe} ASCII ART:

--> List All clubs
Join a club: 


## Register
Enter Name: any name
Date of Birth: YYYY-MM-DD
Home Address: address number
Phone Number: 0000000
Handle: unique_handle
c Continue
b Back

### Continue
->->->-> Directs the User to the ## Player Page

## Spectate Page
1 Game Schedule
2 Clubs
3 Teams
4 History of tournaments
b Back

### Game Schedule
"-----------------------------
Tournament name
"-----------------------------
Date: Start - End, Venue
"-----------------------------
Number of Teams, ?Number of Rounds?
"-----------------------------

### Clubs
--> list of all clubs or the search feature

### Teams
1 See all teams
2 Search for specific teams

#### See all teams
--> List of all TEAMS

#### Search for specific teams
Enter a TEAMS name or the first letter(s) to search or q to quit:
--> LIST OF TEAMS

### History of tournaments
--> some kind of list of all tournaments

# EXTRA NOTES:
### Players / Teams
- Color: simple length check
- Venue: simple length check
- Email: needs to go through a check
- Phone number: 7 Numbers
- Address: (strings)(space)(number)
- When taking input we will have a validator in the logic layer that returns whether it is valid or not
- Valid player handle: Just about the length (3-12) NEED TO HAVE **ADMIN** in the handle file
- Date stored YYYY-MM-DD
  - ValidatioN
    - All need to be numbers that are not the "-"
    - Year: 
    - Month: 01 <= month <= 12
- If the C color requirement will be used then there should only be options for the user (Can only choose color out of few chosen colors)
- Randomize team list for tournaments
- At least 16 teams in a tournament
- Teams cannot Play in multiple matches at the same time
- The main interactions from the user is with shown steps like: 1) Login, 2) Sign Up, b) back ... something like that (can also have some commands)
- Everyone should be able to see all active Teams (in an active tournament) 
##
### Archive = Split into Tournament and Team
#### Tournament Archive
- When the tournament is over then it is archived 

#### Team Archive
- The place that a team goes to when a team captain is alone in a team and leaves the team (AKA: IF a team becomes empty)
- Stores empty teams and their scores (Should be able to view it)

##
### Publish Tournament
When Managing the tournaments the Organizer has the option of publishing a tournament and by pressing that option he will get a list of available tournaments (AKA: Tournaments that have 16 or more teams and tournaments that aren't already published). Then he will input what tournament he wants to publish and that tournament 

##
### Search Bar
#### Example: Searching for available players for teams
- Can input the name of a player directly
- IF unsure about the player options then should be able to list every name or...
- The ability to search the for the first letters to narrow down the list

##
### Schedule
- Stored in file

##
### Logic to use for multiple instances
Selecting a date
- Date of birth (Player)
- Start/End date (Tournament)

Unique Name
- Name of Tournament
- Player Handle

Email and PhoneNr
- Email (Player)
- PhoneNr (Player)
- Contact email (Tournament)
- Contact PhoneNr (Tournament)

##
### Response to an error message or confirm message SHOULD MAYBE HAVE SPECIAL VALIDATOR FOR MOST ACTIONS

#### Add a Teams
Enter Team name or l for the list of all team or q to quit: abcd

--> abcd was found are you sure you want to continue
Y Yes
N No

#### Remove a Team
Enter Team name or l for the list of all teams in the tournament or q to quit:

--> abcd is not apart of the tournament, do you want to continue
Y Yes
N No

