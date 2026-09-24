import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform Azure SRE Kubernetes AKS migration on-premises')
p.headline='Lead Azure DevOps engineer | SRE & AKS/K8s'
p.page_title='Rajendra Prasad N - Lead Azure DevOps Engineer - SRE & AKS/K8s'
p.summary_html='<strong>Azure DevOps and Site Reliability engineer with 10+ years of enterprise cloud, production operations, deployment automation, and platform reliability experience.</strong> Hands-on expertise in <strong>Azure compute, networking, storage, IAM, AKS/Kubernetes, CI/CD, Terraform, and Python/Bash/PowerShell automation</strong>. Supports availability, latency, capacity, and security through actionable observability, incident response, and recovery planning. Experienced in <strong>migrating on-premises VM-hosted applications to Azure Kubernetes Service (AKS)</strong>, including legacy-service containerization, hybrid connectivity, phased cutover, and rollback planning. Collaborates within client engineering teams on production support, release validation, and cutover readiness.'
p.achievements_title='Azure SRE & Kubernetes Migration Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Production Reliability','Service-health monitoring, incident diagnostics, capacity reviews, and recovery runbooks support stable Azure production workloads.'),
('On-Premises-to-AKS Migration','Dependency discovery, Docker packaging, Kubernetes configuration, staged validation, and rollback planning enable controlled modernization.'),
('Portable Delivery','Reusable pipelines and Helm values separate application artifacts from cloud-specific configuration and support repeatable on-premises-to-AKS migration waves.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Azure Infrastructure','VMs, VM Scale Sets, Virtual Networks, subnets, NSGs, routing, DNS, load balancing, Azure Storage, managed disks, Entra ID, RBAC, Key Vault'),
('SRE & Production Support','Availability, latency, performance, SLI/SLOs, incident triage, escalation, root-cause analysis, capacity planning, on-call support, recovery runbooks'),
('Kubernetes & Containers','AKS, Kubernetes/K8s, Docker, Helm, Argo CD, Deployments, Services, ingress, probes, autoscaling, resource limits, disruption budgets'),
('On-Premises-to-AKS Migration','Legacy VM containerization, dependency mapping, Azure landing zones, hybrid connectivity, ACR, AKS storage/identity mapping, phased cutover and rollback'),
('CI/CD & Release Delivery','Azure DevOps, Jenkins, GitLab CI, GitHub Actions, YAML templates, automated tests, artifact promotion, environment approvals, deployment verification'),
('Infrastructure Automation','Terraform, ARM/Bicep, Ansible, Python, Bash, PowerShell, Azure CLI, kubectl, Linux, Windows, configuration and drift management'),
('Observability','Azure Monitor, Log Analytics, Application Insights, Prometheus, Grafana, dashboards, alerts, logging, health checks, synthetic probes'),
('Security & Collaboration','Least privilege, managed identities, workload identity, secrets management, vulnerability scanning, client-team collaboration, migration reviews, stakeholder updates')]]
specs=[
(['Azure','SRE','AKS','Kubernetes','Docker','Terraform','ARM/Bicep','Azure DevOps','Prometheus','Grafana','Python'],[
'Supported Azure-hosted production and nonproduction workloads, monitoring availability, latency, performance, capacity, and security risks with application and infrastructure teams.',
'Provisioned Azure VMs, networking, storage, identities, and access controls through Terraform and ARM/Bicep, maintaining reviewed changes and environment-specific configuration.',
'Led incident triage for service outages, elevated response times, resource exhaustion, DNS failures, and connectivity issues; coordinated containment, restoration, and root-cause follow-up.',
'Built Azure Monitor, Log Analytics, Application Insights, Prometheus, and Grafana dashboards to correlate user-facing health, infrastructure metrics, application logs, and release events.',
'Defined service indicators, alert thresholds, ownership, and escalation runbooks with engineers; reviewed noisy alerts and recurring incidents to prioritize reliability improvements.',
'Assessed on-premises VM-hosted applications for AKS migration, mapping ports, service dependencies, runtime requirements, scheduled tasks, local storage, and external integrations.',
'Containerized legacy services with Docker, externalizing configuration and secrets, moving persistent state to suitable storage, and adding readiness, liveness, and graceful-shutdown handling.',
'Implemented Helm deployment patterns for AKS with versioned values, Services, ingress, resource settings, and namespace controls; validated application behavior under restart and scale events.',
'Prepared Azure landing-zone and AKS migration configurations, mapping on-premises connectivity to Azure networking, images to ACR, persistent data to Azure storage, and application access to Entra identities.',
'Executed phased on-premises-to-AKS migration rehearsals, validating hybrid connectivity, application and data consistency, DNS/traffic cutover, go/no-go checks, and rollback to the source environment.',
'Designed Azure DevOps, Jenkins, and GitLab CI workflows with reusable build/test stages, scanned container images, approved promotion, and target-specific deployment parameters.',
'Tuned AKS resource requests, limits, replica counts, HPA settings, and node capacity using observed demand; validated disruption budgets and workload placement for maintenance resilience.',
'Automated health checks, environment inventories, release validation, and incident evidence collection with Python, Bash, and PowerShell to reduce repeated operational work.',
'Participated in on-call escalation and recovery exercises, maintaining support documentation and coordinating capacity, release, and migration decisions as part of the client engineering team.'
]),
(['Azure','Azure DevOps','GitLab CI','AKS','Docker','Terraform','Ansible','PowerShell'],[
'Maintained Azure DevOps and GitLab CI pipelines for application builds, automated tests, artifact promotion, approvals, and deployment-health verification.',
'Provisioned and configured Azure application environments with Terraform and Ansible, validating network access, runtime dependencies, secrets, and service startup.',
'Packaged services as Docker images and deployed AKS workloads through Helm, investigating configuration drift, image-pull failures, and rollout errors.',
'Supported migration readiness by documenting application dependencies, environment settings, health endpoints, and repeatable deployment and recovery steps.',
'Troubleshot Linux/Windows host, pipeline, identity, and container issues with developers and QA and communicated release risks and remediation progress.',
'Maintained operational dashboards, alerts, and runbooks to improve visibility into platform health and failed application releases.'
]),
(['Azure','Kubernetes','Terraform','Jenkins','GitHub Actions','Python','Azure Monitor'],[
'Operated Azure cloud infrastructure for application environments, monitoring service health, resource consumption, connectivity, and deployment-related failures.',
'Provisioned repeatable compute, network, storage, and monitoring resources with Terraform and pipeline-driven change reviews.',
'Supported on-premises-to-AKS modernization through Docker packaging, configuration separation, Helm deployment, hybrid dependency checks, and post-migration validation.',
'Built Jenkins and GitHub Actions delivery workflows with automated checks, versioned artifacts, and controlled environment promotion.',
'Automated diagnostics and environment checks with Python, PowerShell, and Bash, isolating networking, permissions, service, and container failures.',
'Supported backup and recovery checks, capacity reviews, and operational handover across distributed application and support teams.'
]),
(['Azure','SRE','Kubernetes','Jenkins','Ansible','Prometheus','Grafana','Python'],[
'Supported production reliability and incident response for cloud-hosted services, correlating application symptoms with infrastructure metrics and recent changes.',
'Built resilient Ansible roles for Prometheus, Grafana, and Node Exporter and custom Python exporters for application-specific operational metrics.',
'Designed Jenkins and GitHub Actions automation for infrastructure and application releases, maintaining health gates and recovery readiness.',
'Authored Helm charts for consistent Kubernetes deployments and investigated pod restarts, configuration errors, resource pressure, and service connectivity.',
'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog to automate onboarding, deployment status, and recurring operations.',
'Collaborated on capacity planning, incident reviews, alert tuning, and runbook updates to reduce repeated troubleshooting and improve support handover.'
]),
(['Azure','Docker','Kubernetes','Helm','Jenkins','Ansible','PowerShell','Linux'],[
'Supported cloud migration and release activities for enterprise applications, documenting dependencies, validating connectivity, and coordinating cutover readiness.',
'Deployed Docker and Kubernetes workloads with Helm and controlled manifests, managing application configuration, service exposure, and health checks.',
'Automated Azure application-host setup and operational checks with Ansible and PowerShell across development, test, and production environments.',
'Investigated platform and application incidents involving certificates, permissions, database access, network routing, and failed deployments.',
'Maintained centralized logging, release procedures, recovery instructions, and customer status updates with distributed engineering teams.'
]),
(['Azure','Ansible','Linux','Python','Shell','Jenkins','Healthcare Payer'],[
'Supported production operations and releases for Healthcare Payer enrollment, eligibility, and claims applications within the Mphasis/HPE engagement.',
'Automated application installation, configuration changes, service control, and post-deployment checks using Ansible, Python, and Shell.',
'Investigated Linux process failures, permission issues, batch-job errors, and service connectivity problems and coordinated approved recovery actions.',
'Maintained Git branches, release tags, and artifact traceability and documented dependencies and deployment sequences for application components.',
'Worked with developers, QA, and support teams on release validation, incident updates, and operational handover.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['Azure','SRE','AKS','Kubernetes','Docker','Terraform','ARM/Bicep','Azure DevOps','Jenkins','GitLab CI','Python','Bash','PowerShell','Prometheus','Grafana','Azure Monitor']
p.notes=['Aggressive Azure SRE variant. User-specified header. Migration focus updated by user to on-premises-to-AKS. Employment history retained.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-azure-sre-onprem-aks-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.section-title{margin-top:12px}.skills-grid{gap:6px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text('''Lead Azure DevOps engineer | SRE & AKS/K8s
SRE responsible for reliability, scalability, performance, availability, latency, security and capacity of Azure production infrastructure and on-premises workloads migrating to AKS. Monitor and resolve Azure incidents; provision VMs/networking/storage/IAM; containerize legacy VM services and support Kubernetes/AKS migration, cutover and rollback. Build CI/CD for Azure and AKS. Dashboards, alerts, logs and health checks across environments. Automate IaC and reduce toil. Collaborate on incident response, capacity planning and migration readiness as an embedded vendor resource in client engineering teams. On-call support as required. Azure DevOps/Jenkins/GitLab CI; Docker/Kubernetes/AKS or comparable platforms; Terraform/ARM/Bicep; Python/Bash/PowerShell; Grafana/Prometheus/Azure Monitor.''')
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability','https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview']}
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
