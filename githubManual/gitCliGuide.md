# Basic git commands

## git clone
Copies all files of a git repository into your current directory.

## git pull
Pulls all commits made on the remote git repository to your local one.

## git add
Used to add changed files to your staging area.

## git commit -m "message"
Adds all the changes in your staging area to your local git repository.

## git push
Adds your local git commits to the remote repository.

# How git is set up.

When you clone a remote repository it sets up a git repository in your current directory, this system is split up into multiple layers.

## Your file system
Here you just make your changes to files like you normally do.

## Staging area
Here you can add changed files you want to commit with the add command, you can add specific files or directories or everything at once.
- git add . | Adds all changed files to the staging area in your current directory, recursively does the same to directories in your current directory.
- git add ./file | Adds the file to the staging area if the file has changed since the last commit.
- git status

## Local git repository
The git repository is just a collection of commits you have done, when you run git commit, all the changed files stored in the staging area get added
to a commit and the git repository keeps track of the commits so you can view or revert to them giving you good control of your past changes.

## Remote git repository
This is exactly the same as your local git repository but everyone in your group project has access to it, if you have made a commit on your local git
repository, no one can see it until you run git push which pushes all commits made on your local git repository to the remote one.
