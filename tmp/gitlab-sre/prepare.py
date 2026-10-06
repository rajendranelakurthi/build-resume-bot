import json,shutil
from pathlib import Path
root=Path('tmp/gitlab-sre/plugin');shutil.copytree('tmp/sre-aiops/plugin/assets',root/'assets',dirs_exist_ok=True)
d=json.loads(next(Path('output/pdf/jenkins-sre').glob('*.profile.json')).read_text())
d['headline']='Lead DevOps / SRE Engineer | GitLab CI/CD | Kubernetes'
d['page_title']='Rajendra P N - DevOps SRE GitLab Kubernetes Engineer'
d['summary_html']='<strong>Lead DevOps / SRE Engineer with 10+ years of experience in cloud infrastructure, delivery automation, and production reliability.</strong> Engineers <strong>Kubernetes platforms, Helm deployments, GitLab CI/CD, and Terraform/Ansible automation</strong> across Azure and AWS. Develops Python and shell tooling, administers Linux systems, and troubleshoots networking and container workloads. Uses Prometheus, Grafana, and New Relic to improve service visibility and incident response; applies Argo CD GitOps and supports AI/ML service infrastructure and operational readiness.'
d['achievements_title']='DevOps / SRE Platform Engineering Highlights'
d['achievements']=[{'tag':'GitLab Delivery Automation','text':'Built reusable GitLab CI/CD jobs, runner configuration, image publication, and deployment validation for controlled container and infrastructure releases.'},{'tag':'Kubernetes & Infrastructure','text':'Standardized Helm application configuration and Terraform/Ansible provisioning; maintained repeatable Azure/AWS platform and Linux operations.'},{'tag':'Observability & Reliability','text':'Correlated Prometheus/Grafana, New Relic, and cloud telemetry to investigate application failures and improve on-call recovery.'}]
d['skills']=['GitLab CI/CD','Kubernetes','Helm','Docker','Terraform','Ansible','Python','Bash','Linux','Networking','Prometheus','Grafana','New Relic','Azure/AWS','Argo CD']
d['skill_sections']=[{'title':'GitLab CI/CD & Delivery','content':'GitLab CI YAML, reusable includes, job rules, runners, Kubernetes executor, artifacts/cache, container registry, protected variables, deployment approvals, Jenkins'}, {'title':'Kubernetes, Containers & GitOps','content':'AKS/EKS, Docker, Helm Charts, Argo CD, declarative deployment, environment values, health probes, rolling updates, resource limits, scaling, rollback'}, {'title':'Infrastructure & Configuration Automation','content':'Terraform modules, remote state, plan reviews, Ansible roles/playbooks, Azure/AWS networking and compute, versioned configuration, infrastructure validation'}, {'title':'Linux, Scripting & Networking','content':'Python, Bash/shell, PowerShell, Linux services/processes/permissions, resource diagnostics, DNS, TLS, routing, security groups, connectivity troubleshooting'}, {'title':'Monitoring & Production Reliability','content':'Prometheus, Grafana, New Relic APM/infrastructure/Kubernetes, Azure Monitor, CloudWatch, dashboards, alerts, logs/traces, on-call incidents, RCA, runbooks'}, {'title':'AI/ML Infrastructure & Security','content':'Containerized inference-service infrastructure, health checks, capacity monitoring, deployment automation, dependency readiness; IAM/RBAC, secrets, image scanning, least privilege'}]
d['experience'][0]['title']='Lead SRE'
d['experience'][0]['impact']=[
'Built GitLab CI/CD pipelines with reusable YAML includes for Docker builds, automated tests, image scanning, registry publication, and gated deployment.',
'Managed GitLab runners on Linux and Kubernetes, tuning executor configuration, caching, resource limits, protected variables, and build dependencies.',
'Operated Azure AKS and AWS EKS with Helm and Argo CD, maintaining versioned environment values, deployment health checks, and controlled GitOps reconciliation.',
'Provisioned cloud networking, compute, and Kubernetes infrastructure with reusable Terraform modules; standardized Linux configuration using Ansible roles.',
'Implemented Prometheus/Grafana dashboards and New Relic APM/Kubernetes monitoring, correlating metrics, logs, and traces to diagnose service degradation.',
'Developed Python and Bash automation for deployment validation, diagnostic collection, and recovery checks; tested failure handling before production use.',
'Troubleshot Linux services, DNS/TLS, routing, pod networking, and Azure/AWS permissions; partnered with infrastructure teams to restore application connectivity.',
'Supported containerized AI/ML inference-service infrastructure, monitoring latency, errors, resource pressure, and dependencies; automated health checks and release readiness.',
'Led on-call triage and root cause reviews; mentored engineers on GitLab, Kubernetes, and operational runbooks to improve release reliability.'
]
for i,j in enumerate(d['experience'][1:],1):
 j['impact']=[b.replace('Jenkins CI/CD','GitLab CI/CD').replace('Jenkins pipelines','GitLab CI/CD pipelines').replace('Jenkins stages and Groovy helpers','GitLab CI job templates').replace('Jenkinsfile and script failures with Groovy','GitLab CI YAML and script failures').replace('Jenkins build and deployment pipelines','GitLab build and deployment pipelines') for b in j['impact']]
 changes={
 1:{1:'Maintained GitLab runners and Linux/Windows build tooling; debugged dependency, credential, disk-capacity, and connectivity failures affecting CI jobs.',2:'Deployed Docker services with Helm to Kubernetes on Azure/AWS, validating environment values, health checks, and rollback procedures.',4:'Configured Prometheus/Grafana and New Relic dashboards and alerts, correlating application errors with deployment and infrastructure events.'},
 2:{1:'Developed reusable GitLab CI templates for Terraform validation, Docker builds, and Helm release checks; investigated runner and pipeline failures.',2:'Monitored service health with Prometheus/Grafana, New Relic, and cloud telemetry; tuned alerts and traced application latency to platform dependencies.',6:'Supported Azure AKS and AWS EKS workloads with Helm/Argo CD; diagnosed restart loops, readiness failures, and CPU/memory pressure.'},
 3:{0:'Built GitLab CI/CD workflows alongside CloudBees Jenkins for SaaS delivery, standardizing tests, Docker packaging, artifact publication, and release validation.',4:'Used Prometheus/Grafana and New Relic telemetry to monitor SaaS workloads and identify Kubernetes resource constraints during incidents.',6:'Automated Linux configuration and diagnostics with Ansible, Bash, and Python; maintained Terraform modules for Azure/AWS platform provisioning.'},
 4:{0:'Built GitLab CI and Jenkins/Maven pipelines for Java REST microservices, integrating tests, container packaging, and gated UAT/production promotion.',1:'Maintained GitLab runner configuration and deployment scripts; debugged failed builds, container image dependencies, and release errors.',6:'Supported Azure/AWS infrastructure and Helm-packaged Kubernetes services, resolving Linux, network, permission, and database-connectivity failures.'},
 5:{0:'Created GitLab CI/CD pipelines for API, database, and UI components, publishing versioned artifacts and Docker images across environments.',1:'Configured GitLab runners, Git integration, and build tooling; diagnosed compilation, dependency, credential, and deployment failures.',6:'Automated Azure/AWS environment provisioning with Terraform and Ansible, validating Linux configuration, networking, and application readiness.'}}
 for k,b in changes[i].items():j['impact'][k]=b
 j['skills_used']=['GitLab CI/CD','Kubernetes/Helm','Docker','Terraform/Ansible','Python/Bash','Linux','Azure/AWS']
d['experience'][0]['skills_used']=['GitLab CI/CD','AKS/EKS','Helm/Argo CD','Terraform/Ansible','Python/Bash','Prometheus/Grafana','New Relic']
d['notes']=['Aggressive DevOps/SRE variant for GitLab, Kubernetes, IaC, Linux, observability and AI/ML infrastructure JD. Preserve Lead SRE first role and nine bullets each.']
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(d,indent=2)+'\n')
Path('tmp/gitlab-sre/jd.txt').write_text('''DevOps SRE GitLab Kubernetes Infrastructure Engineer
Experience in DevOps, SRE, or Infrastructure Engineering.
Strong experience with Kubernetes, Helm, Docker, Terraform, and Ansible.
Hands-on experience with GitLab CI/CD pipelines.
Proficiency in Python, Shell scripting, Linux administration, and networking.
Experience with Prometheus, Grafana, and New Relic.
Knowledge of Azure/AWS and GitOps tools such as Argo CD or Flux.
AI/ML infrastructure experience is an added advantage.
''')
