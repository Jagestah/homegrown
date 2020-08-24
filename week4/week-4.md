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
