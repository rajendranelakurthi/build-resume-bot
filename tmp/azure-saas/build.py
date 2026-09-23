import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform Azure SaaS Cloud Operations Databricks monitoring security')
p.headline='Lead DevOps Engineer | Cloud & SAAS Operations'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in Cloud Operations, Software as a Service (SaaS) delivery, and production support, with a focus on Microsoft Azure.</strong> Operates cloud-hosted microservices, background processes, and managed services with an emphasis on uptime, scalability, secure releases, and proactive monitoring. Hands-on with <strong>Azure DevOps, GitHub Actions, Azure Monitor, Datadog, Azure Databricks as a managed service, and Python/Bash/PowerShell automation</strong>. Partners with development, product, and security teams on performance, incident response, access controls, vulnerability remediation, and audit evidence supporting SOC 2 and HIPAA initiatives. Healthcare Payer application experience through Mphasis/HPE.'
p.achievements_title='Cloud Operations & SaaS Reliability Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('SaaS Operations','Health checks, capacity reviews, and recovery runbooks support customer-facing services and background jobs.'),
('Secure Delivery','Reusable pipelines connect automated tests, vulnerability checks, controlled approvals, deployment validation, and rollback readiness.'),
('Operational Visibility','Dashboards, automated reports, actionable alerts, and audit records make service health and security work visible.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Azure Cloud Operations','Azure VMs, AKS, App Service, Azure SQL, Storage, Virtual Networks, Key Vault, Entra ID, resource health, scaling, backup and recovery'),
('SaaS Infrastructure','Software as a Service (SaaS), microservices, REST APIs, background workers, scheduled jobs, dependency health, release support, availability and capacity'),
('Monitoring & Reporting','Azure Monitor, Application Insights, Log Analytics, Datadog, Prometheus, Grafana, dashboards, alert routing, synthetic checks, service-health reports'),
('CI/CD & Deployment','Azure DevOps, GitHub Actions, Jenkins, Git, YAML templates, test automation, artifact promotion, security gates, approvals, rollback'),
('Managed Data Services','Azure Databricks managed service, workspace operations, job monitoring, compute policies, permissions, runtime maintenance, Azure SQL, storage integration'),
('Security & Compliance Support','SOC 2, HIPAA, access reviews, RBAC, MFA, least privilege, audit evidence, vulnerability remediation, patch management, encryption and secrets controls'),
('Automation & Configuration','Python, Bash, PowerShell, Azure CLI, Terraform, Ansible, Linux, Windows, Docker, Kubernetes, Helm, operational runbooks'),
('Incident & Team Operations','Production troubleshooting, root-cause analysis, on-call escalation, change management, recovery validation, developer/product collaboration, Healthcare Payer support')]]
specs=[
(['Azure','Cloud Operations','SaaS','Azure DevOps','GitHub Actions','Databricks','Azure Monitor','Datadog','Python'],[
'Led Azure Cloud Operations for SaaS application environments, coordinating uptime, capacity, service health, maintenance, and production support across microservices and background processes.',
'Monitored customer-facing APIs, scheduled jobs, and asynchronous workers, investigating failed executions, queue backlogs, dependency timeouts, and recurring application errors before wider service disruption.',
'Built Azure Monitor, Application Insights, Log Analytics, and Datadog dashboards to correlate availability, latency, error rates, resource saturation, and deployment events.',
'Automated daily service-health and release reports with Python and PowerShell, consolidating failed jobs, incidents, capacity trends, patch status, and outstanding remediation actions.',
'Maintained Azure DevOps and GitHub Actions pipelines with automated tests, code and dependency scanning, versioned artifacts, environment approvals, and post-deployment health validation.',
'Operated Azure Databricks as a managed service, administering workspace access, compute policies, job schedules, runtime maintenance, storage connectivity, and operational ownership.',
'Monitored Databricks job failures, run duration, resource usage, and retry behavior; coordinated diagnostics, safe reruns, and workload optimization with data engineering teams.',
'Strengthened access management with Entra ID, MFA, RBAC, managed identities, and Key Vault; supported periodic access reviews and controlled privileged changes.',
'Coordinated patching and vulnerability remediation across virtual machines, container images, application dependencies, and managed-service runtime versions, validating service health after maintenance.',
'Partnered with security, leadership, and audit contacts to assemble access-review records, release approvals, scan results, patch evidence, and recovery-test records for SOC 2 and HIPAA control reviews.',
'Supported secure handling of healthcare-related workloads through restricted log access, secrets separation, encryption settings, retention controls, and approved evidence-sharing procedures.',
'Automated Azure provisioning and configuration with Terraform, Ansible, Bash, and Python, reducing repeated manual setup and making environment changes reviewable.',
'Validated backups, restoration procedures, and rollback runbooks; coordinated incident response and root-cause reviews with developers and product leaders to prioritize recurring reliability issues.'
]),
(['Azure','Cloud Operations','SaaS','Azure DevOps','GitHub Actions','Ansible','Azure Monitor','Python'],[
'Supported Cloud Operations for Azure-hosted SaaS services, performing daily health checks, release support, incident triage, and environment maintenance.',
'Maintained CI/CD templates for application builds, automated tests, artifact promotion, approvals, and deployment verification across SaaS environments.',
'Configured service dashboards and alerts for application errors, resource pressure, and failed background jobs, documenting ownership and escalation paths.',
'Automated configuration and operational checks with Ansible and Python, validating application settings, service startup, credentials, and connectivity.',
'Applied access restrictions and security checks to build agents and deployment workflows and coordinated patch and vulnerability follow-up with engineering teams.',
'Worked with developers and QA to resolve failed releases, improve smoke tests, and maintain rollback and service-support procedures.'
]),
(['Azure','Cloud Operations','SaaS','Terraform','Jenkins','GitHub Actions','Databricks','Azure Monitor'],[
'Managed cloud infrastructure and production support for Azure-oriented SaaS application environments, monitoring service availability, capacity, and dependency health.',
'Provisioned repeatable environments with Terraform and pipeline-driven changes, maintaining consistent network, identity, compute, and monitoring configuration.',
'Built Jenkins and GitHub Actions delivery workflows for SaaS microservices with controlled artifact promotion, approvals, and post-release checks.',
'Supported Azure Databricks managed-service operations, investigating scheduled-job failures, compute startup issues, workspace permissions, and storage access with data teams.',
'Implemented dashboards, centralized logs, and alerts for workload failures and performance degradation and automated diagnostics with Python and PowerShell.',
'Maintained backup checks, recovery documentation, and patch procedures and coordinated incidents and release windows across distributed engineering teams.'
]),
(['Azure','Cloud Operations','SaaS','Jenkins','Ansible','Prometheus','Grafana','Python'],[
'Supported Cloud Operations and reliability for SaaS application services, coordinating release health, incident response, and operational improvements with development teams.',
'Standardized Jenkins and GitHub Actions pipelines for software and infrastructure releases, maintaining artifact traceability, health gates, and recovery readiness.',
'Developed Ansible roles for Prometheus, Grafana, and Node Exporter and Python exporters that exposed application-specific availability and performance signals.',
'Built internal FastAPI automation linking Jenkins, Jira, and JFrog for onboarding, deployment status, and recurring SaaS support activities.',
'Investigated application, container, and infrastructure incidents through logs and metrics, translating recurring failures into actionable alerts and runbooks.',
'Collaborated with developers and product stakeholders on release readiness, capacity concerns, maintenance schedules, and reliability priorities.'
]),
(['Azure','Cloud Operations','SaaS','Jenkins','Ansible','PowerShell','Linux','Monitoring'],[
'Supported cloud-hosted application and SaaS delivery environments, managing service configuration, release execution, environment readiness, and operational handover.',
'Built Jenkins pipelines for Java applications and REST services, integrating build validation, versioned packages, controlled promotion, and smoke tests.',
'Automated Azure application-host configuration with Ansible and PowerShell, validating permissions, runtime dependencies, credentials, and service connectivity.',
'Implemented centralized logging and health checks and investigated application-server failures, certificates, database connectivity, and resource bottlenecks.',
'Coordinated patch windows, release approvals, incident updates, and recovery procedures with customer stakeholders and distributed support teams.'
]),
(['Azure','Cloud Operations','SaaS','Ansible','Linux','Python','Shell','Healthcare Payer'],[
'Supported Cloud Operations and SaaS application delivery for Healthcare Payer enrollment, eligibility, and claims services within the Mphasis/HPE engagement.',
'Performed application and batch-service health checks, investigated failed jobs and missing files, and coordinated approved recovery with support teams.',
'Created Ansible, Shell, and Python automation for installation, configuration updates, service control, and post-deployment verification.',
'Supported secure Linux operations through permission reviews, controlled credentials, log-access restrictions, and scheduled maintenance checks.',
'Coordinated release sequencing, smoke tests, defect follow-up, and operational handover with development, QA, and healthcare application support teams.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['Azure','Cloud Operations','SaaS','Azure Databricks','Azure DevOps','GitHub Actions','Jenkins','Azure Monitor','Datadog','SOC 2','HIPAA','Python','Bash','PowerShell']
p.notes=['Aggressive Azure SaaS Operations variant. Every role emphasizes Cloud Operations and SaaS. Compliance wording describes operational controls and audit support, not certification ownership. Preserves employment history and updated email.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-azure-saas-cloud-operations-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.skills-grid{gap:6px}.section-title{margin-top:12px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text('''SaaS Operations Engineer | Cloud Infrastructure, CI/CD, & Security. Healthcare technology SaaS company supporting a home-care management platform. Manage Azure uptime, scalability, reliability across microservices and background processes. Automate reporting, logs and alerts. Maintain secure CI/CD. Support leadership and external audits for SOC 2, HIPAA and security frameworks. Access management, patching, vulnerability prevention. Automate infrastructure and deployments. Collaborate with developers and product leaders on performance and system visibility. 5+ years Cloud Operations/DevOps/SaaS Infrastructure; Azure; Azure DevOps/GitHub Actions/Jenkins; monitoring tools such as Datadog/New Relic/Azure Monitor; Python/Bash/PowerShell; troubleshooting and communication. Healthcare preferred. Include Azure Databricks as a managed service. Main focus in ALL projects: Cloud Operations and Software as a Service (SaaS).''')
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','variant':'Azure SaaS Cloud Operations','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://learn.microsoft.com/en-us/azure/databricks/jobs/monitor','https://learn.microsoft.com/en-us/azure/databricks/admin/system-tables/jobs-cost','https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us','https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2']}
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
