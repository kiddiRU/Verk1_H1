# Diary, 2025-12-02

## Andri Már
### Time: 8:30 - 16:35
### On site: Yes

## Elmar
### Time: 9:05
### On site: Yes

## Ísak Elí ---
### Time: 9:10 
### On site: Yes

## Kristinn Hrafn
### Time: 9:20 - 17:00
### On site: Yes

## Kristján Hagalín
### Time: 9:10 - 16:35
### On site: Yes

## Sindri Freysson
### Time: 8:30 - 16:35
### On site: Yes

# Morning meeting (Briefing)
## State of project:
Critical preparations and project set up are complete. We can now begin development.  
## State of group: 
Briefed Kristján and Kristinn about the current state of the project, about the coding standard that we are using, the changes we made to the model classes. Everyone has cloned the github repository and can start working after "Python gleði Rikka og Konna". Sindri decided to stay behind to work on the diary and latex doc.  
## Divisions: 
- UI / UX: Andri
- System engineer: Elmar, Ísak, Kristinn, kristján 
- QC: Sindri

## ToDo-list:
- UILayerAPI
- LogicLayerAPI
- DataLayerAPI
- Design user interface blueprint
- Test UI tree with users
- Setup of project
- Test happy path
- Convert word design doc into latex
- Create start page TUI
- Create data manager for DataLayer
- Create store function for player
- Create load function for player
- Create update function for player
- Create discard function for player
# Evening meeting (Diary)
## State of project:
- Finished filling out DataLayerAPI - Kristinn
- Almost finished TUI look - Andri
- Began work on LogicLayer - Kristján
- Major work on Model classes - Elmar and Ísak
- Created requirement list in latex desing doc - Sindri
## State of group: 
Issue found about how to keep track of data if model classes attributes don’t store UUID? 
The data Layer loads everything on file when requested by logic layer, which means we dont have to store a dict with handle as key and UUID as value in an auxiliary file. 
Logic layer loops over items in data dict until it finds a matching handle.
This also means that it is possible to store referances as UUID instead of class objects.

## Divisions:
- UI / UX: Andri
- System engineer: Elmar, Ísak, Kristinn, kristján 
- QC: Sindri
## ToDo-list:
- UILayerAPI
- LogicLayerAPI
- DataLayerAPI
- Design user interface blueprint
- Test UI tree with users
- Setup of project
- Test happy path
- Convert word design doc into latex - work in progress
- Create start page TUI
- Create data manager for DataLayer
- Create store function for player
- Create load function for player
- Create update function for player
- Create discard function for player