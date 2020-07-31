### Week 1
#### Overview
This week's focus is on building out our development environments and an introduction to some of the key concepts that drive DevOps.

- Additional Resources:
  - [Bash cheat sheet for CLI commands](https://devhints.io/bash)
  - The 12 Factor App
  - DRY Principle
  - [Git Documentation](https://git-scm.com/docs/gitglossary)
  - Markdown Documentation


- Workstation Setup
  - Installing Command Line Interface (CLI)
  - Creating a code folder
  - Navigating the command line
  - Installing an Editor
  - Join Code Club Crew Slack Workspace
- Intro to Infrastructure as Code
- Intro to DevOps Methodology
- Git
  - branches
  - repos
  - commits
  - pull
  - push
  - checkout
  - pull requests
- Weekly Homework:
  - Create  aGithub account
  - Create Repo for the ongoing project
  - Create a README.md in the repo documenting why the student is interested in the course

### Workstation Setup

###### Installing a Command Line Interface (CLI)
- Recommendation for Mac: [iTerm2](https://www.iterm2.com)
- Recommendation for Linux: [Terminal](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

###### Creating a code folder
_Using your CLI_
1. Navigate to your `root` folder
  - `cd`
2. Create the `code` folder
  - `mkdir code`

###### Navigating the Command Line
_Refer to Additional-Resources.1 for a more complete list._

Quick callouts:
- `cd` = Change Directory, change the context of your CLI
  - `~` refers to your home directory
  - `cd` with no arguments takes you back to your home directory
  - `cd ~/code` takes you to your code repo
- `ls` = List, view the contents of your current CLI context(IE subdirectories and files)
  - `ll` is also a popular option

###### Installing an IDE
- Recommendation: [Atom](https://atom.io/)

###### Join the Code-Club-Crew (C3) Slack Workspace
In the Slack channel we have several industry professionals and other students who can help when you get blocked or need additional clarification.
- [Click here to join the Workspace](https://join.slack.com/t/code-club-crew/shared_invite/enQtNDQ3ODA2NTk0MTEyLTc1ODVhYTAwMDAyMTAwODlkMDAzYzNhMjIwOTcyMzA4MTY5NjExOTA2NjJiNGEzOTA5MDNlZGJiZTBjNzAzZjE)

### Goals of this bootcamp



###  Intro to DevOps Methodology
###### What is DevOps?
There's differing opinions on what is or is not DevOps. There's also some ambiguity between DevOps as a culture and DevOps as a job function. In my experience, in companies where DevOps exists only as a culture the Developers are responsible for building the tooling and standards around deploying their team's application in an automated way. The skillset around this tooling is complimentary to a Developer's traditional skillset but is broad enough by itself to warrant an entirely new breed of Engineer. Enter the DevOps Engineer.

DevOps as a role is an evolution of a company adopting a DevOps Culture. At a certain point the operational overhead of maintaining the company's pipelines, tooling and the skillset surrounding those tasks becomes so great that it makes sense to hire someone solely for that function. One of the main advantages of having a DevOps Engineering role is their ability to specialize in CI/CD best practices, technologies, and standards that can be be applied organization wide, transcending teams.

In fewer words; DevOps Engineers exist to increase the output of Developers, and thus the velocity of feature releases, by using automation to remove toil.

###### Why DevOps for Companies?
Companies that have moved from adopting a DevOps culture to hiring dedicated DevOps Engineers is looking for a person or team of people to be force multipliers for their Developers.

These companies are usually feeling the pain of manual and very slow deployments, manual testing, and rampant human error.

###### Who makes a good DevOps Engineer?
I've found that people who are passionate about DevOps have some common personality features:
- Industriously Lazy
- Able to see the beauty in efficiency
- A fascination with automation
- Clever not smart

This list isn't exhaustive or exclusive.

### Intro to Infrastructure as Code (IaC)
###### What is IaC?
Infrastructure as Code is a methodology that in its purest form would allow you to make any change necessary to the infrastructure via a change to source code. Thereby giving you access to all of the features of a source-controlled codebase. Such as; Versioned history and change control.

The idea that you could also leverage IaC to recover from any infrastructure failure or even spin up an exact replica of your infrastructure in a different geographical region or cloud provider is very lucrative to companies.

### Git
Familiarity with Git and by extension manipulating code source control is integral to someone within a development organization. Whether they're a Developer or DevOps Engineer. The cues from the source control is largely what will kick off our automation. Source control is also important as a way for multiple engineers to work on the same code base.

Manipulating the code in Git isn't always intuitive and it can be frustrating oftentimes when things go awry. Some pointers to make your life easier:
- When working with others, never commit to master. Write your code in a feature branch and merge it to master via an MR or PR.
- `git pull` often. Syncing your local machines files with the remote server is never a bad idea.

##### Some Vocabulary:

| Term              | Definition |
| :-----            | :----- |
| repo              | Synonymous with 'project'. A repo will include all the code for a specific application. |
| branch            | A logical separation of the code, meant to be eventually merged to a single branch, `master` |
| commit            | A save point in the code. Code must be committed before it can be pushed to the repo |
| pull              | Sync your local files with any changes in the repo |
| push              | Send your local changes to update the files on the repo |
| checkout          | Change which branch you're developing on |
| pull requests     | Sometimes called a Merge Request. Use these to combine branches. IE your branch to `master` |

### Weekly Homework:
- Familiarize yourself with the Additional Resources listed above.
- Create a Github account.
- Create Repo for the ongoing project.
- Create a README.md in the repo documenting why you're interested in this course.
