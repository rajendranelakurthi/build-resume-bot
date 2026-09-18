import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform GitLab Jenkins Harness Argo CD Helm DevSecOps AWS AKS EKS ECS')
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in Azure and AWS cloud technologies, platform engineering, solution architecture, and release delivery.</strong> Designs governed <strong>Azure DevOps (ADO), GitLab, Jenkins, and Harness</strong> pipeline templates for secure deployments across cloud, on-premises, and hybrid environments. Leads migration planning and modernization using Terraform, Ansible, Docker, Kubernetes, Argo CD, and Helm. Integrates SDLC security controls, observability, and operational readiness while guiding engineers and coordinating customer stakeholders and multiple development teams.'
p.achievements_title='Enterprise Platform & Delivery Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Pipeline Governance','Versioned templates, protected approvals, service connections, and security gates standardize delivery across enterprise application teams.'),
('Migration & Modernization','Discovery, dependency mapping, target-state architecture, migration waves, and recovery planning connect cloud adoption to operational readiness.'),
('Engineering Leadership','Technical reviews, mentoring, customer communication, and cross-team release coordination align platform delivery with application priorities.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Azure & Platform Engineering','Azure DevOps / ADO, AKS, Azure VMs, Azure SQL, Key Vault, Entra ID, Virtual Networks, Azure Monitor, hybrid cloud architecture'),
('AWS Cloud','EC2, EKS, ECS, VPC, IAM, ALB/NLB, Auto Scaling, RDS, S3, CloudWatch, CloudTrail, enterprise network and database integration'),
('Enterprise CI/CD','Git, GitLab CI/CD, Jenkins, ADO YAML templates, Harness, template versioning, approvals, artifact promotion, release governance'),
('GitOps & Containers','Docker, Kubernetes, Argo CD, Helm, AKS, EKS, ECS, manifests, sync policies, readiness probes, rollout and rollback'),
('IaC & Configuration','Terraform, CloudFormation, Ansible, reusable modules and roles, remote state, provisioning, configuration management, drift checks'),
('SDLC & DevSecOps','SonarQube, SCA, SAST, DAST, Twistlock / Prisma Cloud, image scanning, secrets controls, policy gates, vulnerability remediation'),
('Operations & Observability','Splunk, Datadog, Prometheus, Grafana, Azure Monitor, AWS CloudWatch, Windows, Linux, SQL Server, Azure SQL, RDS'),
('Automation & Leadership','PowerShell, Shell/Bash, Python, REST APIs, microservices, migration planning, solution design, Agile, mentoring, customer and team coordination')]]
specs=[
(['Azure','AWS','ADO','GitLab','Jenkins','Harness','Terraform','AKS','EKS','Argo CD','Helm','Ansible'],[
'Led Azure-first platform engineering and solution-design discussions for hybrid enterprise workloads, translating customer requirements into infrastructure, identity, network, and deployment standards.',
'Designed versioned Azure DevOps YAML templates with typed parameters, approved tasks, service connections, environment checks, artifact promotion, and production approval controls.',
'Governed GitLab repositories, merge requests, protected branches, runner access, and reusable pipeline templates; aligned Jenkins workflows with common build and release requirements.',
'Built Harness deployment templates and environment definitions to standardize Kubernetes service delivery, controlled approvals, health verification, and rollback execution.',
'Led cloud migration planning through application discovery, dependency mapping, target-state Azure architecture, migration waves, cutover rehearsals, and post-migration service validation.',
'Engineered Terraform modules for Azure networking, identity, compute, AKS, secrets, and monitoring; maintained complementary AWS infrastructure for EC2, EKS, ECS, VPC, and RDS workloads.',
'Implemented Argo CD and Helm GitOps delivery for AKS and EKS, managing versioned values, sync policies, deployment sequencing, drift visibility, and Git-based recovery.',
'Standardized Docker builds and Kubernetes runtime configurations, including resource limits, readiness checks, autoscaling, namespace isolation, and controlled cluster maintenance.',
'Integrated SonarQube, SAST, SCA, DAST, and Twistlock/Prisma Cloud image checks into the SDLC, enforcing severity thresholds, approved exceptions, and remediation follow-up.',
'Automated Windows and Linux configuration with Ansible, PowerShell, Python, and Shell, covering application prerequisites, secrets, service controls, and REST endpoint validation.',
'Implemented Splunk, Datadog, Prometheus, Grafana, Azure Monitor, and CloudWatch dashboards to correlate deployment events with application errors, latency, capacity, and infrastructure health.',
'Guided engineers through design and code reviews, delegated delivery work, and coordinated customer updates and multi-team releases; led troubleshooting of pipeline, identity, network, cluster, and database failures.'
]),
(['Azure DevOps','Azure','GitLab','Jenkins','Terraform','Ansible','AKS','PowerShell'],[
'Developed reusable ADO and GitLab CI/CD templates for builds, automated tests, artifact publication, environment approvals, and deployment validation.',
'Configured Windows and Linux build agents, toolchains, caches, permissions, and service connections to support enterprise application delivery.',
'Provisioned Azure environments with Terraform and Ansible, standardizing network settings, application configuration, secrets retrieval, and service health checks.',
'Deployed Docker microservices to AKS with Helm, validating configuration, readiness, service connectivity, and rollback procedures.',
'Integrated SonarQube and dependency checks into pipelines and partnered with QA and security teams to resolve quality and vulnerability findings.',
'Coordinated release dependencies across development teams and resolved pipeline, authentication, runtime, and environment failures using PowerShell and Python diagnostics.'
]),
(['Azure','AWS','Terraform','GitHub Actions','Jenkins','Kubernetes','Argo CD','Python'],[
'Provisioned Azure platform resources and supporting AWS environments through reusable Terraform definitions and reviewed infrastructure changes.',
'Built Jenkins and GitHub Actions workflows for versioned builds, automated tests, artifact publication, and controlled application promotion.',
'Delivered Kubernetes microservices with Argo CD and Helm, separating shared configuration from environment values and tracking deployment health.',
'Supported migration and modernization activities by mapping service dependencies, validating connectivity, and documenting cutover and recovery procedures.',
'Automated Windows and Linux configuration checks with PowerShell, Python, and Shell, investigating service failures, permissions, and resource constraints.',
'Supported AWS EC2, VPC, EKS, and database integrations alongside Azure workloads, troubleshooting routing, DNS, security groups, and application access.',
'Developed cloud dashboards, alerting, backup checks, and operational runbooks with engineering and support teams to improve incident response.'
]),
(['Azure','AWS','Jenkins','Ansible','Terraform','Kubernetes','Prometheus','Grafana','Python'],[
'Standardized CI/CD workflows for Azure and supporting AWS application environments using Jenkins shared libraries and reusable deployment automation.',
'Developed Terraform and Ansible automation for environment provisioning, configuration consistency, and repeatable platform maintenance.',
'Built internal Python FastAPI integrations for Jenkins, Jira, and JFrog to automate onboarding, deployment status, and operational requests.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray, maintaining versioned artifacts and quality checks through release promotion.',
'Authored Ansible roles for Prometheus, Grafana, and Node Exporter stacks and created custom Python exporters for application-specific telemetry.',
'Partnered with developers on REST microservice releases, monitored production health, and coordinated incident recovery and post-release improvements.'
]),
(['Azure','AWS','Jenkins','Ansible','PowerShell','Linux','Windows','Docker','Helm'],[
'Built enterprise deployment pipelines for Java applications and REST microservices across development, test, UAT, and production environments.',
'Automated Azure application environment configuration with Ansible and PowerShell, managing Windows/Linux prerequisites, permissions, and service settings.',
'Deployed Docker and Kubernetes workloads with Helm and version-controlled manifests, validating configuration changes and application readiness.',
'Supported cloud migration cutovers with dependency mapping, connectivity checks, database access validation, and documented recovery procedures.',
'Implemented centralized logging and operational dashboards and troubleshot cloud networking, certificates, application servers, and database integrations.',
'Presented platform and delivery improvements to customer stakeholders and coordinated release priorities with distributed development teams.'
]),
(['Azure','AWS','Ansible','Linux','Shell','Python','Git','Jenkins','Healthcare Payer'],[
'Supported Healthcare Payer application releases within Mphasis/HPE, coordinating enrollment, eligibility, and claims-service deployments across enterprise environments.',
'Created Ansible workflows and Shell/Python scripts for installation, configuration changes, service control, and post-deployment checks.',
'Supported Azure-oriented application environments and AWS dependencies, validating server configuration, connectivity, and deployment prerequisites.',
'Administered Linux application and build servers, investigating permissions, failed processes, missing dependencies, and batch-processing issues.',
'Maintained Git branching, release tags, and versioned artifacts to make deployment inputs and application versions traceable.',
'Worked with development, QA, and support teams on release sequencing, smoke tests, defect follow-up, and operational handover.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['Azure','AWS','Platform Engineering','Solution Architecture','Git','GitLab','Jenkins','Terraform','ADO','Harness','Argo CD','Helm','Docker','Kubernetes','Ansible','PowerShell','Shell','Python','SonarQube','SCA','SAST','DAST','Twistlock','Windows','Linux','EC2','EKS','VPC','ECS','AKS','Splunk','Datadog','Prometheus','Grafana']
p.notes=['Aggressive Azure-focused enterprise platform variant. Preserves Multi-Cloud header, employment history, certifications and updated email.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-azure-platform-devops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
jd='''10+ years DevOps, AWS/Azure cloud, Platform Engineering, Solution Architecting. Enterprise CI/CD template design, implementation and governance for cloud, on-premises and hybrid deployments. Cloud migration leadership and modernization. Git, GitLab, Jenkins, Terraform, ADO, Harness. GitOps with Argo CD and Helm. Docker, Kubernetes. Ansible architecture automation. PowerShell, Shell, Python. SDLC and SonarQube, SCA, SAST, DAST, Twistlock. Windows, Linux and databases. Strong AWS EC2, EKS, VPC and database experience. ECS, EKS, AKS. Splunk, Datadog, Prometheus, Grafana, AWS-native observability. Microservices and REST. Team leadership, customer relationships, enterprise development-team coordination, debugging and troubleshooting.'''
stem.with_suffix('.jd.txt').write_text(jd)
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','variant':'Azure enterprise platform engineering','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates','https://developer.harness.io/docs/platform/Templates/template','https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/','https://docs.prismacloud.io/en/compute-edition/34/admin-guide/vulnerability-management/registry-scanning/configure-registry-scanning']}
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
