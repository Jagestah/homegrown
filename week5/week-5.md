## Week 5
#### Overview
Get added to the Homegrown group
Migrate in some form/fashion your homegrown project
Helm install gitlab runner with tags and runner token
let the group know about the runner tag

brew install k3d
k3d create cluster k3s
k3d kubeconfig merge k3s --switch-context
Get added to the devops-homegrown group
Create new project in the devops-homegrown group
git clone the project to the code folder
cd to the project folder
Create a `helm` folder
cd to the helm folder
helm repo add gitlab https://charts.gitlab.io
helm repo update
helm fetch gitlab/gitlab-runner --untar
Uncomment and change `gitlabUrl` to `https://gitlab.com/` - Line 19
Uncomment and add `KetaL5SnyWuqwzyoHz3X` to the `runnerRegistrationToken` - Line 25
Uncomment and add your arbitrary, runner-specific tags - Line 146
Check for your runner here: https://gitlab.com/groups/devops-homegrown/-/settings/ci_cd

---

#### Additional Reading:
-

---

#### Gitlab

---

### Weekly Homework:

---

#### SPEAKER NOTES
