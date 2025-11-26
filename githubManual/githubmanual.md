# Basic git commands

* git clone
    - Copies all files of a git repository into your current directory.

* git pull
    - Pulls all commits made on the remote git repository to your local one.

* git add
    - Used to add changed files to your staging area.

* git commit -m "message"
    - Adds all the changes in your staging area to your local git repository.

* git push
    - Adds your local git commits to the remote repository.

## How these commands are executed with github desktop

### git clone

* In order to clone a repository, you first need to go to the overview of you repositories which can be found in the upper left corner

<img alt="cloning step 1" src="github_desktop_images/a_cloning1.png" width="50%"> 

* Next you need to select the "Add" dropdown menu and selct "clone repository"

<img alt="cloning step 2" src="github_desktop_images/a_cloning2.png" width="50%"> 

<img alt="cloning step 3" src="github_desktop_images/a_cloning3.png" width="50%">

* After copying the repository URL you can paste it in the menu that pops up and you can get a clone of the repository in your github desktop

<img alt="cloning step 4" src="github_desktop_images/a_cloning4.png" width="50%">


### git pull

* After someone has pushed a file, you can see how many files can be pulled in the far right button at the top of the screen, and you click it in order to pull those changes into your working directory

<img alt="pulling step 1" src="github_desktop_images/b_pulling1.png" width="50%">

* After pulling the changes you can see the change history by clicking on the "History" tab

<img alt="pulling step 2" src="github_desktop_images/b_pulling2.png" width="50%">


### git add

* After making any changes to a file in your working directory, the file will appear in the "changes" tab

<img alt="adding step 1" src="github_desktop_images/c_adding1.png" width="50%">

* You only need to select the files you want to add and they will be added to your staging area


<img alt="adding step 2" src="github_desktop_images/c_adding2.png" width="50%">


### git commit -m "message"

* After selecting the files to add, you can add a message to the commit at the bottom of the "changes" tab

<img alt="commiting step 1" src="github_desktop_images/d_commit1.png" width="50%">

* After writing the message you want to have with the commit, you only need to press the button at the bottom of the tab and the files will be commited

<img alt="commiting step 2" src="github_desktop_images/d_commit2.png" width="50%">


### git push

* After having commited a file you can push it by pressing the "Push origin" button that pops up on the screen or by pressing the far right button at the top of the screen

<img alt="pushing step 1" src="github_desktop_images/e_push1.png" width="50%">

# How git is set up.

When you clone a remote repository it sets up a git repository in your current directory, this system is split up into multiple layers.

## Your file system
Here you just make your changes to files like you normally do, this is called your working directory.

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

# Useful commands

* git status
    - Will show you which files have changed since last commit and whether they have been added to the staging area or not

* git diff
    - Shows which files are different from your working directory and staging area.

# Branches

Branches are workspaces which are independant from other branches, the default branch is the main branch, the final product should be all on the main branch.

When working on new features you should be creating a branch for that feature and developing it on that branch, when testing is done you should move the
changes to the main branch, this let's you work on changes for a certain feature which could break it's functionality temporarily while letting other people
work on other features which rely on that feature.

You shouldn't keep branches to long or you should rebase regularly to prevent coding against old implementations.

* git branch
    - Shows you a list of available branches and highlights your current branch.

* git branch [name]
    - This let's you create a branch with a certain name, this branch is only available on your local git repository.

* git checkout [name]
    - This let's you switch branches, all differences in files between those branches get changed on your working directory automatically.

* git merge [name]
    - This let's you merge all changes on the branch [name] to your current branch.

* git rebase [name]
    - This let's you move all commits made on branch [name] infront of all commits on your current branch, is recommended before merging for a cleaner commit tree.


## Using branches in github desktop

### Creating a branch

* In order to creater a brach in github desktop you need to select middle button at the top of the screen named "Current branch"

<img alt="opening branch menu" src="github_desktop_images/create_branch1.png" width="50%">

* A branch menu should open that has a button labeled "New Branch" near the top

<img alt="New branch" src="github_desktop_images/create_branch2.png" width="50%">

* Then you can name the branch and choose another branch to base the new branch from

<img alt="Naming and creating" src="github_desktop_images/create_branch3.png" width="50%">


### Merging branches

* In order to merge branches you need to go to the branch menu

<img alt="opening branch menu" src="github_desktop_images/create_branch1.png" width="50%">

* You need to select the branch that you want to merge INTO and then press the button at the bottom of the menu

<img alt="Select branch" src="github_desktop_images/merge1.png" width="50%">

* You can then select "Create a merge commit" to merge the branches

<img alt="" src="github_desktop_images/merge2.png" width="50%">


### Merge conflicts

* When trying to merge branches it is possible for there to be merge conflicts, if that is the case a warning will be shown before creating the merge commit

<img alt="conflicts warning" src="github_desktop_images/mergeconflict_warning.png" width="50%">

* If you decide to press "Create a merge commit" despite the warning another window will pop up that tells you what file has the conflict and gives you the option to open your tool so so you can go and solve the conflict manually

<img alt="conflict merging" src="github_desktop_images/mergeconflict_merging.png" width="50%">

* You will be able to see where the conflict is in the file between the "<<<<<<< HEAD" and ">>>>>>> branch-name" you will have to manually edit the files to keep the desired changes and remove all conflict markers (<<<<<<<, =======, >>>>>>>)

<img alt="conflict in file" src="github_desktop_images/mergeconflict_in_file.png" width="50%">

* After solving the merge conflict, you can go back to github desktop and you will now be able to continue the merge
 
<img alt="conflict solved" src="github_desktop_images/mergeconflict_solved.png" width="50%">


### Pull requests

* After finishing working on a branch you can create a pull request which will allow others on your team to add comments to the branch and view all the changes before the branch is merged
* You or another person on the team can then approve the pull request and the branch will then be merged

* To create a pull request, you have to go to your branch and press the "Preview Pull Request" button on the "Changes" tab

<img alt="creating a pull request" src="github_desktop_images/pull_request1.png" width="50%">

* You will then get a window over all the changes made on your branch and you can create the pull request

<img alt="submitting a pull request" src="github_desktop_images/pull_request2.png" width="50%">

* After creating the pull request you will be directed to github where you or a team member can leave a comment, close or approve your pull request

<img alt="viewing a pull request" src="github_desktop_images/pull_request3.png" width="50%">


# Common problems

## Pulling a file that you are editing 

* It sometimes happens that you are working on the same file at the same time as someone else, if he has pushed the file before you, you might run into a problem when trying to pull his version since it will overwrite your version. Github desktop shows an error when this happenes and gives you the option to "Stash changes and continue", this will stash your version of the file and pull the other version

<img alt="Editing the same file as someone else" src="github_desktop_images/pulling_a_file.png" width="50%">

* After pulling the other persons changes you will be able to go to the changes tab and recover the changed that were stashed and them combine them with the new version of the file

<img alt="recover your changes" src="" width="50%">


# Branching strategies

## Main-Only
* The Main-Only branching strategy revolves around using only the main branch for development and all changes are commited directly into it, so it uses no extra branches.

<img alt="Main-Only" src="github_desktop_images/main_only.png" width="50%">

## Feature Branching
* The Feature Branching branching strategy revolves around creating a new brnch for every feature and bug in the program 

<img alt="Feature Branching" src="github_desktop_images/feature_branching.png" width="50%">

## Gitflow
* 

<img alt="Gitflow" src="github_desktop_images/gitflow.png" width="50%">


## Github Flow
* 

<img alt="Github Flow" src="github_desktop_images/github_flow.png" width="50%">


## Trunk-Based Development
* 

<img alt="Trunk Based Development" src="github_desktop_images/trunk_based.png" width="50%">
* 

## Release Branching 
* 

<img alt="Release Branching" src="github_desktop_images/release_branching.png" width="50%">