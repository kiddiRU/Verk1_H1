## Types of users:

### Privelages: 
Organizers > Spectators
?Club Owner? > Team Captains > PLayers > Spectators

### Organizers
- Admin
- Create tournament
- Input results
- Add teams to tournamentss

### PLayers / Teams
- At least 16 teams in a tournament
- Teams cannot play in multiple matches at the same time

#### PLayer
- Regester self
- Remove from team
- Edit self
- Create a team and promote themself

#### Team captains  
- Canot be in more than one team
- Sign their team into the compatiotion / tournament
- Creates his team
- modify team memebers (removing and adding)
- !! IF we allow team captain to remove them self from team then what happenes??!!
- !! CLUB OWNER (IS THERE A CLUB OWNER) creates captian who then can create a team !!

### Spectators
- TO see maches and tournaments
- Get game schedule
- Get results
- See teams and clubs

# Prioritized Requirements
### A
- 
- TO arcive turnoments after they play out
- Each player is in 1 team
### B
- Swich captain
- Players can be in more than 1 team
- Clubs
### C
- Edit arcive (like removing invalid tournaments) 

# Use cases for requirements

# Test requirements

# Class diagrams

## Model classes
### PLayers
- Name
- Date of Birth
- Home Address
- Phone Number
- Handle: Unqie
- win counter
- Points (for playing / winning?)

### Team
- List of players 3 <= list <= 5
- Name: Uniqe
- Captain: player handle
- Optional = usl homepage, ascii art
- Win counter
- points (for playing / winning?)

### Club
- Win counter
- Teams associated
- Club colors
- Name
- 

Club -> Team -> PLayer

### Competition
- Venues (location)
- Time: begin - end
- Teams

### Tournament
- Receves info from organizers

### Matches
- Date time
- Server ID
- What teams are playing

## 3-tier design

# State diagrams

# User group analysis

# UI-Design
- Wireframe where we show "happy paths"




