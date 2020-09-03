## Week 5
#### Overview
This week's focus is CI/CD and Gitlab by association. Gitlab is currently the industry leader in CI/CD and support free use of their platform; So it's the tool we're going to be using for this session.

---

#### Additional Reading:
> I refer to the Gitlab Configuration Reference as the Bible of Gitlab. If you have a question about how a particular part of their pipelines work; Chances are your answer lies in that document.

- [CI/CD Explained (video)](https://www.youtube.com/watch?v=scEDHsr3APg)
- [Gitlab Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/README.html)
- [Gitlab Predefined Environment Variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

---

#### Gitlab Repos
Gitlab repos operate in much the same way as any other Source Control git-based repo.
A couple high-level differences:
- Gitlab uses Merge Requests instead of Pull Requests
- Most importantly; We can run specific jobs depending on different states of the branch.

---

#### Gitlab Settings
Areas of interest:
- Settings-CI/CD -- This is where the environment variables are located.
- Settings-General -- Location for MR Approval behavior

---

#### Gitlab CI/CD
> I recently took a course on becoming a Gitlab Certified CI/CD Specialist so here's a list of things you need to know how to do in order to attain that certification:
- Implement a default image for all jobs
- Implement default environment variables for all jobs
- Overwrite default environment variables for specific jobs
- Dockerize code
- Build and push a Docker image to a repo's Container Registry
- Implement Job Policy rules to run jobs under different circumstances
- Deploy a Gitlab Runner
- Run jobs only on specific Gitlab Runners
- Deploy an application to a specific Gitlab environment

All the Gitlab CI/CD Pipeline rules are defined by the `.gitlab-ci.yml` located in the root of the repo. Refer to the [Gitlab Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/README.html) when writing this file.

At its most basic every `.gitlab-ci.yml` will contain at least:
``` yaml
stages:
  - a list
  - of stages
job-name:
  image: <the image the job uses goes here>
  stage: <the stage of the pipeline to run the job goes here>
  script:
    - <the steps to take for the job go here>
```

Gitlab Runners, like the one we installed via Helm to our k3d cluster, will constantly communicate back to the main server and ask if there's jobs that need to be ran. Once a job is found the Gitlab Runner will spin up a separate pod that runs the steps of the job using the configuration provided. The code repo will always get copied in to the job pod.

There are a ton of tools provided that allow us to keep our pipelines DRY. IE, `extends`, `includes`, and even using `git clone` from within a job.
Some common patterns for DRY pipelines I see are:
- Using `extends` to re-use code within the `.gitlab-ci.yml`
- Using `includes` to reference a separate template repo for deploy jobs

---

### Weekly Homework:

Homework Steps:
1. `brew install k3d`
1. `k3d create cluster mycluster`
1. `k3d kubeconfig merge mycluster --switch-context`
1. Get added to the devops-homegrown group
1. Create new project in the devops-homegrown group
1. `git clone` the new project to your `code` folder
1. `cd` to the new project folder
1. Create a `helm` folder
1. `cd` to the `helm` folder
1. `helm repo add gitlab https://charts.gitlab.io`
1. `helm repo update`
1. `helm fetch gitlab/gitlab-runner --untar`
1. Uncomment and change the value of `gitlabUrl` to `https://gitlab.com/` - Line 19
1. Uncomment and change the value of `runnerRegistrationToken` to `KetaL5SnyWuqwzyoHz3X` - Line 25
1. update `rbac.create` to `true` -- Line 85
1. update `rbac.clusterWideAccess` to `true` -- Line 92
1. Uncomment and add your arbitrary, runner-specific tags - Line 146
1. update `runners.privileged` to `true` -- Line 168
1. `helm upgrade --install gitlab-runner ./gitlab-runner --namespace gitlab --create-namespace`
1. Share runner-specific tags and the output of `k3d kubeconfig get mycluster` with the group
1. Have JJ check for your runner here: https://gitlab.com/groups/devops-homegrown/-/settings/ci_cd

---

#### SPEAKER NOTES
