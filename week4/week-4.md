## Week 4
#### Overview
Our focus for the week is going to be on utilizing Helm for implementing templates for our deployments and enforcing Infrastructure as Code. We're going to use Helm to build deployment manifests for multiple instances of our `swapi.py` script that accepts a number as an argument.

---

#### Additional Reading:
- [Gitlab's `auto-devops` Chart](https://gitlab.com/gitlab-org/cluster-integration/auto-deploy-image/-/tree/master/assets/auto-deploy-app)
- [Helm Documentation](https://helm.sh/docs)
- [Helm Getting Started Guide](https://helm.sh/docs/chart_template_guide/getting_started/)
- [Generally Available Helm Charts](https://github.com/helm/charts/tree/master/stable)
- [Sprig Functions](http://masterminds.github.io/sprig/)

---

#### Helm

Helm is a package manager for Kubernetes applications. Every manifest that is needed for an application should be contained in its Helm Chart.

Component | Description
--- | ---
Chart.yaml | Contains the metadata for the Helm Chart such as name and version.
values.yaml | Contains the customizable values that are used to build the templates in to Kubernetes manifests
templates/ | Contains all of the templates that build the manifests for the Kubernetes application

---

#### Helm Commands

Command | Description
--- | ---
`helm install` | Install a new Helm Chart
`helm upgrade` | Update a Helm Chart
`helm repo` | Manipulate the repos searched when referring to a Helm Chart
`helm uninstall` | Remove a Helm Chart from K8s
`helm template` | Verify the output of your Helm Charts

#### Commons Command Flags

Flag | Description
--- | ---
`--install` | Used with `helm upgrade`. Will install the Helm Chart if it doesn't already exist
`--create-namespace` | Creates the namespace specified in the `upgrade` or `install` command if it doesn't already exist. Default behavior in Helm 2 but must be explicit in Helm
`--debug` | Print the output of the templates.
`--dry-run` | Prevents the command from actually applying the manifests to the cluster. Usually used in conjunction with `--debug`

#### Context in the Templates

Helm maintains a notion of _context_. Meaning functions in our templates may behave differently depending on where they're invoked.

Typically looping functions such as `range` or `with` will change our context. Context is represent in the templates by the leading `.` we see in our object references.

If we want to use an absolute reference from within a different context we can refer to an object by preceding it with a `$`. IE `$.Values.image`. This is great for referencing global values that we don't want to change based on context.
