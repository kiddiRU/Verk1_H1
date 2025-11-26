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
- Sign their team into the competition / tournament
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
- Print out the match schedule
- The User can login as Admin / Organizer
- The User can register themselves as a player
- The User can login as a player 
- To be a spectator the user does not need to sign into anything
- Organizer can create a tournament
- Organizer can input results for the tournament for each round
- Organizer can add and kick teams for the tournament before the start
- Organizer can create clubs
- Player can create a team
- Player becomes a team captain when team is created
- Team captain can leave the team
- When team captain leaves a team he assigns a team member to be the new team captain
- When team captain leaves a team if he was alone then the team is archived
- When a team is created it is assigned to a club
- Team captain can modify players in team (add / remove)
- Each Player is in 1 team
- Tournaments automatically archive after they play out
- Spectator can see matches and tournaments
- Spectator can see teams and clubs
### B
- Organizer can modify the time of a tournament before it has started
- Organizer can cancel a tournament
- Switch captain
- Players can be in more than 1 team
- Clubs
- Player handle should be the length of 3-12
### C
- Edit archive (like removing invalid tournaments)
- Change team name
- Team captain can transfer his authority to a player in team
- Teams can switch from clubs
- Need password to login
- The Club Name will be printed in its color

## NON-Functional
### A
- Menus should have a "back" option when appropriate
- The system should not crash due to invalid data
- The players personal data should not be visible to the spectator
- Only the team captain can modify the team
- Only the organizer can create tournaments and clubs
- Code must follow Python type_hinting everywhere
- Code must follow the snake casing naming convention
### B

### C


# Use cases for requirements


# Test requirements


# Class diagrams
## Model classes
### Players
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

### Team
- List of Players 3 <= list <= 5
- Name: Unique
- Captain: Player handle
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

### Competition
- Venues (location)
- Time: begin - end
- Teams

### Tournament
- Receives info from organizers
- Date: start date - end date
  - j
- Unique name
- Venue (location)
- Registered contact person (With e-mail and phone number) 
- Is active

### Matches
- Date time
- Server ID
- What teams are Playing

## 3-tier design


# State diagrams


# User group analysis


# UI-Design


- Wireframe where we show "happy paths"

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
  - Validation:
    - All need to be numbers that are not the "-"
    - Year: 
    - Month: 01 <= month <= 12
- If the C color requirement will be used then there should only be options for the user (Can only choose color out of few chosen colors)
- Randomize team list for tournaments
- At least 16 teams in a tournament
- Teams cannot Play in multiple matches at the same time
- The main interactions from the user is with shown steps like: 1) Login, 2) Sign Up, b) back ... something like that (can also have some commands)
- 
#
### Archive = Split into Tournament and Team
#### Tournament Archive
- When the tournament is over then it is archived 

#### Team Archive
- The place that a team goes to when a team captain is alone in a team and leaves the team (AKA: IF a team becomes empty)
- Stores empty teams and their scores (Should be able to view it)

#
### Search Bar
#### Example: Searching for available players for teams
- Can input the name of a player directly
- IF unsure about the player options then should be able to list every name or...
- The ability to search the for the first letters to narrow down the list

#
### Schedule
- 
-

-
