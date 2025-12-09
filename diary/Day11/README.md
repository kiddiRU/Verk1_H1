# Diary, 2025-12-08

## Andri Már
### Time: 8:23 - 18:35
### On site: Yes

## Elmar
### Time: 9:10 - 18:15
### On site: Yes

## Ísak Elí
### Time: 9:10 - 18:35
### On site: Yes

## Kristinn Hrafn
### Time: 10:00 - 17:00
### On site: Yes

## Kristján Hagalín
### Time: 9:12 - 17:03
### On site: Yes

## Sindri Freysson
### Time: 8:20 - 18:00
### On site: Yes

# Morning meeting (Briefing)
## State of project: 
The project is starting to take shape. The datalayer is done, and only the logic and UI layers are left. The main is set up, which allows us to test functionality of the program. MainUI now uses dict instead of if else, to improve readability.
## State of group: 
Kristinn is now working on tournament logic with Elmar and kristján
## Divisions: 
- UI / UX: Andri, Ísak
- System engineer: Elmar, Kristinn, Kristján
- QC: Sindri

## ToDo-list:
- Tournament Logic
- Add error message to home address

# Evening meeting (Diary)
## State of project:
When Kristjan was running load tournaments it crashed, it was caused by passing int in a list of str. Kristinn resolved the issue by making the model class initialize server list which made creation easier for data layer.

Issue was found by Elmar when creating player after registering using main.py, caused by player not being saved after creation.  

- Decided to allow tournaments to publish with 2 or more teams
- Kristinn - Working on tournament publish logic
- Andri - Working on Admin UI
- Ísak - Working on spectator UI
- Kristján and Elmar - Working on General Logic
- Kristinn - tournament logic 

## State of group: 
Ísak - This is is endless
## Divisions:
- UI / UX:
- System engineer: 
- QC: 
## ToDo-list:
