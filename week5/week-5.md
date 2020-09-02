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
update `rbac.create` to `true` -- Line 85
update `rbac.clusterWideAccess` to `true` -- Line 92
update `runners.privileged` to `true` -- Line 168

Share runner-specific tags and the output of `k3d kubeconfig get mycluster` with the group


Default image
Default env vars
deploy to environment
Job using specific runner
Publish image to project registry

---

#### Additional Reading:
-

---

#### Gitlab

---

### Weekly Homework:

---

#### SPEAKER NOTES
