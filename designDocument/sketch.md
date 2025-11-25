## Types of users and their actions:

### Privileges:  
Organizer/Admin > Team Captains > Players > Spectators

#### Organizers/Admin
- Create tournament
- Input results
- Add teams to tournament / edit: delay or cancel
- Create clubs and edit

#### Team captains  
- Cannot be in more than one team
- Sign their team into the competition / tournament
- Creates his team
- modify team members (removing, adding and editing)
- When leaving a team then they choose a player to take their place as team captain (If no one left then the team is archived where it still holds the score and win information)

#### Player
- Register self
- Remove from team
- Edit self
- Create a team and promote them selves to the team captain

#### Spectators
- TO see matches and tournaments
- Get game schedule
- Get results
- See teams and clubs


# Prioritized Requirements
## Functional
### A
- Each Player is in 1 team
- Team Captains can add, change or modify Players in team
- ONLY ONE admin who can create tournament and clubs
- Admin can add teams to tournaments
- Admin can delay a tournament or cancel
- Tournaments automatically archive after they Play out
### B
- Switch captain
- Players can be in more than 1 team
- Clubs
### C
- Edit archive (like removing invalid tournaments) 
## NON-Functional
### A

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
- win counter
- Points (for Playing / winning?)

### Team
- List of Players 3 <= list <= 5
- Name: Unique
- Captain: Player handle
- Optional = usl homepage, ascii art
- Win counter
- points (for Playing / winning?)

### Club
- Win counter
- Teams associated
- Club colors
- Name
- created by the organizer

Club -> Team -> Player

### Competition
- Venues (location)
- Time: begin - end
- Teams

### Tournament
- Receives info from organizers
- Date: start date - end date
- Unique name
- Venue(location)
- Registered contact person (With e-mail and phone number) 

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
- At least 16 teams in a tournament
- Teams cannot Play in multiple matches at the same time
- The main interactions from the user is with shown steps like: 1) Login, 2) Sign Up, b) back ... something like that (can also have some commands)
- 
