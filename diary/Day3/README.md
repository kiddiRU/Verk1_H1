# Diary, 2025-11-26

## Andri Már
### Time: 8:40 - 16:30
### On site: Yes

## Elmar
### Time: 8:40 - 16:30
### On site: Yes

## Ísak Elí
### Time: 8:50
### On site: Yes

## Kristinn Hrafn
### Time: 9:15
### On site: Yes

## Kristján Hagalín
### Time: 9:10 - 16:30
### On site: Yes

## Sindri Freysson
### Time: 8:30 - 16:30
### On site: Yes


# Morning meeting (Briefing)
## State of project: 
Most of the preliminary design decisions have been made, and our group has now started to work on more specialized tasks. 

## State of group: 
Decided to split ourselves in more specialized divisions; UI / UX (TUI), System engineer (and functionality) and Quality control (documentation and coordination).

## Divisions: 
- UI / UX: Elmar
- System engineer: ísak, Kristján
- QC: Sindri, Kristinn, Andri
## ToDo-list:
- Ísak  and Kristján- functionality of classes
- Andir - finish github desktop guide 
- Elmar - Work on TUI
- Kristinn - converting design doc from Markdown to Latex
- Sindri - Quality control and work on diary
- Finish use cases
- Happy path
- Decide on implementation details
- Class Diagram
# Evening meeting (Diary)
## State of project:
- Decided Use JSON to store data
- Model class Player knows what team he is in (needs to be synced with Model class team list of players)
- Decided not to allow organizer to control when matches happen, matches schedule is controlled by tournament team quantity and tournament time frame. Organizer controlling schedule caused to many problems.
- An issue was brought up about viewing schedule information of tournaments. When the organizer starts a tournament, how is it possible to view the schedule before it starts? The issue was resolved by adding a publishing state, which blocked the organizer from modifying the tournament. Tournament states: unpublished → published → active → archived.
- Finished github desktop guide
- Completed diary skeleton rework.
- Completed latex compiler in GitHub.
- Use cases done
- Worked on class diagram
- Major work on model classes
- Began work on 3-tier design
- Happy tree almost compleated

## State of group: 
- We asked TA if publishing is permissible, they answered that it was permissible and pointed out that the Organizer should be able to change the name of a published tournament. This sparked a debate about changing unique names of players or teams. It was decided to allow changing unique names if the name was not in the system.
## Divisions:
- UI / UX: Elmar, Andri
- System engineer: Ísak, Kristján
- QC: Sindri, Kristinn
## ToDo-list:
- Ísak  and Kristján- functionality of classes
- Elmar - Work on TUI
- Kristinn - converting design doc from Markdown to Latex
- Sindri - Quality control and work on diary
- Finish use cases
- Happy path
- Decide on implementation details
- Class Diagram
- Finish git Desktop manual
- Design schedule layout 
- Design development plan


