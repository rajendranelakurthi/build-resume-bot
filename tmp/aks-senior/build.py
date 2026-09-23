import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform Kubernetes AKS CI/CD DevSecOps reliability')
p.headline='Senior DevOps Engineer with Kubernetes & Azure cloud'
p.page_title='Rajendra Prasad N - Senior DevOps Engineer with Kubernetes & Azure cloud'
p.summary_html='<strong>DevOps engineer with 10+ years of enterprise experience in Azure cloud, Kubernetes operations, CI/CD, deployment automation, and production support.</strong> Engineers <strong>AKS platforms, Azure DevOps and GitHub Actions pipelines, Terraform infrastructure, and Helm/GitOps delivery workflows</strong>. Integrates automated testing, vulnerability scanning, identity controls, observability, and release verification into application delivery. Develops PowerShell, Python, and Bash tooling; mentors engineers, coordinates cross-team releases, and serves as an escalation resource for critical platform and deployment incidents.'
p.achievements_title='Kubernetes, Azure & Delivery Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Kubernetes Operations','Node-pool maintenance, workload scheduling, secure configuration, scaling, and recovery procedures support resilient AKS services.'),
('Delivery Engineering','Reusable pipelines and Helm deployment patterns connect tests, security checks, approval gates, release promotion, and rollback readiness.'),
('Platform Reliability','Actionable telemetry, incident diagnostics, operational runbooks, and engineer mentoring strengthen production support and release consistency.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Azure Cloud & IaC','AKS, ACR, Azure VMs, Virtual Networks, Azure SQL, Key Vault, Entra ID, Azure Monitor, Terraform, Ansible, reusable infrastructure modules'),
('Kubernetes Administration','Node pools, upgrades, Deployments, StatefulSets, DaemonSets, Jobs/CronJobs, namespaces, quotas, RBAC, service accounts, rollout management'),
('Kubernetes Reliability','HPA, cluster autoscaler, resource requests/limits, taints/tolerations, affinity, topology spread, disruption budgets, startup/readiness/liveness probes'),
('Networking, Storage & Secrets','Services, ingress, DNS, network policies, TLS, persistent volumes/claims, StorageClasses, Azure Disk/Files CSI, Workload Identity, Key Vault CSI'),
('CI/CD & GitOps','Azure DevOps, GitHub, GitHub Actions, Jenkins, YAML templates, Git branching, pull requests, Docker, Helm, Argo CD, artifact promotion, release management'),
('DevSecOps & Access','SonarQube, SAST, SCA, image/secrets scanning, policy checks, compliance validation, least privilege, OIDC, managed identities, protected approvals'),
('Monitoring & Automation','Prometheus, Grafana, Azure Monitor, Log Analytics, Container Insights, alerts, logs, PowerShell, Python, Bash, Azure CLI, kubectl'),
('Production & Team Enablement','Troubleshooting, root-cause analysis, high availability, recovery drills, release runbooks, critical incident escalation, mentoring, technology evaluation')]]
specs=[
(['Azure','AKS','Kubernetes','Azure DevOps','GitHub Actions','Terraform','Helm','Argo CD','Python','Prometheus'],[
'Engineered Azure DevOps and GitHub Actions pipelines for enterprise builds, tests, scans, artifact publication, deployment approvals, release promotion, and post-deployment verification.',
'Designed reusable YAML templates and deployment automation frameworks with versioned inputs, standard checks, controlled credentials, and consistent rollback procedures for application teams.',
'Provisioned and administered AKS clusters with Terraform, managing system and user node pools, Azure networking, registry access, cluster identities, and environment configuration.',
'Planned AKS and node-image upgrades through compatibility checks, nonproduction validation, maintenance windows, drain testing, and post-upgrade workload verification.',
'Managed Kubernetes Deployments, StatefulSets, DaemonSets, Jobs, and CronJobs, troubleshooting scheduling, controller behavior, failed rollouts, and application configuration.',
'Standardized Helm charts and Argo CD delivery patterns with versioned values, manifest validation, sync sequencing, configuration-drift visibility, and Git-based recovery.',
'Tuned resource requests and limits, HPA settings, and cluster autoscaling from observed workload demand; used taints, tolerations, and affinity to isolate appropriate workloads.',
'Improved application resilience through multi-zone node placement, topology spread, startup/readiness/liveness probes, and disruption budgets for voluntary maintenance.',
'Configured Kubernetes Services, ingress routes, TLS, DNS, and network policies; diagnosed unreachable endpoints, service-discovery failures, and blocked pod-to-service traffic.',
'Administered persistent volumes, claims, StorageClasses, and Azure Disk/Files CSI integrations; investigated pending claims, mount failures, storage permissions, and recovery procedures.',
'Implemented Entra Workload Identity, Kubernetes RBAC, service accounts, and Key Vault CSI access, restricting secrets and cloud-resource permissions to required workloads.',
'Embedded automated tests, SonarQube analysis, dependency/image scanning, secrets detection, and infrastructure policy checks into delivery gates with approval and exception evidence.',
'Built Azure Monitor, Container Insights, Prometheus, and Grafana dashboards for node pressure, restarts, API errors, deployment duration, latency, and resource saturation.',
'Served as an escalation resource for CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending pods, and node-health failures; correlated events, logs, metrics, and recent changes during root-cause analysis.',
'Developed PowerShell, Python, and Bash tooling for deployment checks and incident diagnostics; mentored engineers, maintained runbooks, and evaluated platform improvements through focused proof-of-concepts.'
]),
(['Azure DevOps','GitHub Actions','AKS','Docker','Helm','Terraform','Ansible','PowerShell'],[
'Built reusable Azure DevOps and GitHub Actions workflows for application build, testing, artifact promotion, environment approvals, and release validation.',
'Automated Azure environment setup with Terraform and Ansible, standardizing network access, runtime prerequisites, configuration, and secure service connections.',
'Containerized services with Docker and deployed AKS workloads through Helm, validating manifests, probes, configuration values, and rollout status.',
'Configured namespaces, service accounts, resource quotas, and deployment permissions to separate team workloads and control environment access.',
'Diagnosed image-pull, pod-startup, readiness, and networking failures with kubectl, container logs, and application-team input.',
'Integrated quality and vulnerability checks into pipelines and partnered with developers and QA to improve smoke tests, deployment documentation, and rollback readiness.'
]),
(['Azure','Kubernetes','Argo CD','Helm','Terraform','GitHub Actions','Python','Azure Monitor'],[
'Provisioned Azure platform infrastructure through reusable Terraform definitions and reviewed changes for networking, identities, compute, and monitoring.',
'Delivered Kubernetes microservices through Argo CD and Helm, maintaining environment-specific values, deployment traceability, and service-health verification.',
'Built GitHub Actions and Jenkins workflows for reproducible builds, tests, container packaging, artifact publication, and controlled releases.',
'Supported Kubernetes workload scheduling and capacity reviews, adjusting resource settings and investigating pod restarts, node pressure, and failed deployments.',
'Implemented cloud dashboards, centralized logs, and actionable alerts to expose application health and deployment-related degradation.',
'Automated Linux/Windows checks with Python, PowerShell, and Bash and maintained recovery runbooks for platform, network, and application incidents.'
]),
(['Azure','Kubernetes','Jenkins','Ansible','Terraform','Prometheus','Grafana','Python'],[
'Designed CI/CD and infrastructure automation for enterprise applications using Jenkins, GitHub Actions, Terraform, and versioned deployment inputs.',
'Authored Helm charts for consistent Kubernetes application delivery, maintaining ConfigMaps, secrets references, Services, and workload health checks.',
'Developed Ansible roles for highly available Prometheus, Grafana, and Node Exporter stacks and Python exporters for application-specific metrics.',
'Built internal FastAPI tooling to integrate Jenkins, Jira, and JFrog onboarding, operational checks, and deployment status.',
'Supported container and platform incident response through log analysis, resource diagnostics, service verification, and recovery coordination.',
'Partnered with developers on release readiness and retrospectives, sharing troubleshooting practices and improving operational runbooks.'
]),
(['Azure','Kubernetes','Docker','Helm','Jenkins','Ansible','PowerShell','Linux'],[
'Built enterprise delivery pipelines for Java applications and REST microservices across development, test, UAT, and production environments.',
'Deployed Kubernetes workloads with Helm and version-controlled manifests, managing namespaces, configuration, Services, and environment promotion.',
'Automated Azure and application-host configuration with Ansible and PowerShell, validating runtime prerequisites, permissions, and connectivity.',
'Troubleshot failed deployments, application-server issues, certificates, database access, and container networking with development and infrastructure teams.',
'Implemented centralized logging and documented deployment sequences, change approvals, customer updates, and recovery procedures.'
]),
(['Azure','Jenkins','Git','Ansible','Linux','Shell','Python','Healthcare Payer'],[
'Supported Healthcare Payer enrollment, eligibility, and claims-service releases within Mphasis/HPE using controlled deployment and verification procedures.',
'Developed Ansible, Shell, and Python automation for application setup, configuration changes, service control, and post-release checks.',
'Maintained Linux application and build servers, investigating failed processes, permissions, deployment dependencies, and batch-job issues.',
'Managed Git branches, release tags, and versioned artifacts and coordinated application, API, database, and UI deployment sequencing.',
'Worked with development, QA, and support teams on release windows, smoke tests, incident follow-up, and operational handover.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['Azure','Kubernetes','AKS','Azure DevOps','GitHub Actions','Docker','Terraform','Helm','Argo CD','PowerShell','Python','Bash','DevSecOps','monitoring','release management','mentoring']
p.notes=['Aggressive Kubernetes/Azure variant. Exact header supplied by user; employment titles and chronology retained. Expanded cluster administration, delivery, security, observability and incident-response responsibilities.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-senior-devops-kubernetes-azure-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text('''Header: Senior DevOps Engineer with Kubernetes & Azure cloud
Design, implement and optimize DevOps, enterprise CI/CD, deployment automation, cloud-native delivery and release management. Administer Kubernetes/container platforms. Enable developers with improved build/test/deploy workflows. Integrate automated tests, validation, vulnerability scanning, compliance and DevSecOps controls. Monitor health, deployment performance and reliability. Troubleshoot incidents and perform root-cause analysis. Collaborate across cloud, infrastructure, security and applications. Develop PowerShell/Python/Bash automation and IaC. Maintain standards, release procedures and runbooks. Evaluate emerging technology and mentor engineers. Serve as a critical-incident escalation resource. Azure DevOps, GitHub, GitHub Actions, Git branching, distributed systems, observability, highly available systems, identity/secrets/access control. User requests additional Kubernetes responsibilities.''')
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability','https://kubernetes.io/docs/concepts/workloads/pods/disruptions/','https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/','https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview']}
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
