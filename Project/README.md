# HR e-Sport Extravaganza

## General guide to running this program.
Youtube link: https://youtu.be/QDJU7cx0wmI

### Imports
All imports are in the Python Standard Library thus no requirements.txt is
provided. A list of imports used in the project is shown below.
- datetime
- enum
- json
- os
- uuid

### Python version
This program was tested on and guaranteed to work on python version 3.13,
other python versions 3.x > 3.4 should work but not guaranteed.

### Data
In the Project/DataLayer/Repository/ you should find the following files.
- clubs.json
- match.json
- players.json
- server.json
- teams.json
- tournament.json
Initially, these files should only contain "{}", as you use the program creating
clubs, players, teams, tournaments, etc, these files will store the information.
Tampering with these files manually could break the system and is strongly
advised against.

We provide dummy data for clubs, players, teams and tournaments for testing,
these files can be found in the DummyData/ directory and the contents of these
files can be copied to the other files in the Project/DataLayer/Repository.
The other files which do not receive dummy data should remain as described
above.

### Running the program
Running the program is as simple as moving to the Project/ directory in any
standard terminal and executing "python3 main.py" or however you interpret
python programs on your system.

### Admin
Admins can create and host tournaments as well as create clubs, to login in as
admin you open the login screen and when prompted for a handle, you input 
"admin".

