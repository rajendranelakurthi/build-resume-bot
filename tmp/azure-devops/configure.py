import json
from pathlib import Path
root=Path('plugins/resume-creator-plugin')
p=json.loads((root/'assets/people/rajendra-prasad-n.json').read_text())
p['page_title']='Rajendra Prasad N - Senior Azure DevOps Engineer'
p['headline']='Senior Azure DevOps Engineer | Python, SSIS & Bicep'
p['summary_html']='<strong>Senior Azure DevOps Engineer with 10+ years of enterprise application delivery, cloud infrastructure, automation, and production support experience.</strong> Builds <strong>Azure DevOps CI/CD pipelines, Python automation tools, SSIS packages, and Bicep infrastructure</strong> for repeatable application and data releases. Combines Azure engineering with certificate lifecycle management, secure credentials, encrypted database connections, and root cause analysis across software, infrastructure, and data workflows. Partners with architects and cross-functional teams to improve deployment verification, release reliability, and operational readiness.'
p['achievements_title']='Azure DevOps & Software Delivery Highlights'
p['skills']=['Azure','Azure DevOps','Azure Pipelines','Python','SSIS','Bicep','PowerShell','Azure SQL','Key Vault','Terraform','AKS']
p['achievements']=[{'tag':'Delivery Engineering','text':'Built reusable CI/CD workflows for application and database releases with code reviews, environment approvals, validation, and recovery planning.'},{'tag':'Automation & Data Integration','text':'Developed Python automation and SSIS integration workflows to support repeatable data processing, release checks, and operational troubleshooting.'},{'tag':'Secure Azure Operations','text':'Combined infrastructure automation, credential controls, certificate management, and monitoring to strengthen release readiness and production support.'}]
p['skill_sections']=[
{'title':'Azure DevOps & CI/CD','content':'Azure Pipelines, YAML templates, Azure Repos, Azure Artifacts, Git, pull requests, build agents, environments, approvals, deployment verification'},
{'title':'Software & Automation','content':'Python, PowerShell, Bash, C#/.NET, Java, REST APIs, FastAPI, Azure CLI, MSBuild, Maven, JSON, YAML'},
{'title':'SSIS & Database Delivery','content':'SSIS packages, control/data flows, connection managers, parameters, SSISDB deployment, execution logging, SQL Server, Azure SQL, Liquibase'},
{'title':'Azure Infrastructure as Code','content':'Bicep modules and parameters, validation, what-if reviews, ARM templates, Terraform, Ansible, virtual networks, compute, storage'},
{'title':'Security & Connectivity','content':'Azure Key Vault, certificates and renewal, TLS database connections, credential management, Entra ID, managed identities, RBAC, private endpoints'},
{'title':'Containers & Platforms','content':'AKS, Azure Container Registry, Docker, Kubernetes, Helm, ArgoCD, Linux, Windows Server, environment configuration'},
{'title':'Observability & Troubleshooting','content':'Azure Monitor, Log Analytics, Application Insights, Prometheus, Grafana, Splunk, ELK, incident diagnosis, root cause analysis, runbooks'},
{'title':'Engineering Quality & Governance','content':'SonarQube, JFrog Xray, code reviews, automated tests, release evidence, security documentation, technical knowledge sharing, recovery planning'}]
impacts=[[
'Built and maintained Azure DevOps CI/CD pipelines for application, database, and infrastructure releases, coordinating dependencies, environment approvals, and deployment verification.',
'Developed Python, PowerShell, and Bash automation for release checks, service integrations, database connectivity validation, and operational support.',
'Developed and supported SSIS packages with control flows, data transformations, parameterized connection managers, error handling, and execution logging.',
'Automated SSIS project deployment to SSISDB with environment-specific parameters and validated package execution and data-processing results after release.',
'Implemented Azure infrastructure as code with Bicep modules and parameter files, incorporating validation and what-if reviews into controlled pipeline deployments.',
'Managed certificate renewals and credential updates and configured encrypted SQL Server and Azure SQL connections, troubleshooting certificate trust, TLS, and authentication failures.',
'Integrated Azure Key Vault, federated pipeline authentication, and least-privilege deployment access to protect credentials used by application and data workflows.',
'Established Git branch protections, required reviews, merge controls, and versioned artifacts to improve code quality and release traceability.',
'Troubleshot application, infrastructure, pipeline, and data failures using Azure Monitor, deployment logs, and execution history; documented root causes and recovery procedures.',
'Coordinated schema changes, application compatibility checks, smoke tests, and rollback planning with development, QA, and data engineering teams.',
'Produced deployment evidence, environment specifications, and operational documentation to support security reviews, release decisions, and team knowledge transfer.'
],[
'Built reusable CI/CD stages for Azure-hosted applications, standardizing build-agent configuration, automated validation, environment settings, and release checks.',
'Supported .NET and Java delivery workflows with versioned artifacts, source-control reviews, container packaging, and deployment verification.',
'Administered Linux and Windows build agents and Kubernetes workloads, diagnosing pipeline, dependency, credential, and runtime failures.',
'Maintained separate development, QA, and production configuration and coordinated application and database releases with engineering teams.',
'Improved release reliability through secure runner practices, image validation, branch controls, and documented troubleshooting procedures.'
],[
'Built GitHub Actions and Jenkins pipelines for Azure application and database releases, coordinating service rollout and post-deployment validation.',
'Provisioned Azure infrastructure through Terraform and ARM templates and deployed containerized services to AKS using Helm and ArgoCD.',
'Developed Python, Bash, and PowerShell automation for release checks and operational tasks, publishing versioned artifacts for repeatable deployments.',
'Used Azure Monitor, Log Analytics, and pipeline telemetry to investigate deployment delays, infrastructure failures, and application connectivity issues.',
'Partnered with distributed engineering teams to resolve release blockers, improve delivery documentation, and strengthen production readiness.'
],[
'Delivered CI/CD automation for SaaS and payment-platform workloads, aligning application releases, database dependencies, and Azure infrastructure changes.',
'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog to automate project onboarding and reduce manual release coordination.',
'Standardized build, test, artifact publication, and promotion workflows with SonarQube and secure secrets handling.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray and maintained shared libraries for consistent artifact versioning.',
'Built Terraform modules for Azure networking and AKS and used Prometheus, Grafana, and Ansible automation to support operational diagnosis.'
],[
'Built Jenkins and Maven delivery pipelines for REST microservices across test, security-validation, UAT, and production environments.',
'Automated Azure virtual machines, virtual networks, and Linux configuration with ARM templates, Ansible, and PowerShell.',
'Managed Key Vault integration and secure database connectivity and coordinated release configuration and verification with developers and QA.',
'Packaged Kubernetes services with Helm and used ELK, Azure Monitor, and Log Analytics to troubleshoot deployment and application failures.'
],[
'Created repeatable build and deployment pipelines for API, database, and UI components, promoting consistent artifacts across environments.',
'Automated Azure infrastructure and application deployments with Terraform, ARM templates, Ansible, Python, and PowerShell.',
'Maintained Git branching practices, build agents, environment-specific release parameters, and deployment documentation.',
'Troubleshot failed releases with development and operations teams and documented corrective actions and verification procedures.'
]]
skills=[['Azure DevOps','Python','SSIS','Bicep','Key Vault','Azure SQL','AKS','PowerShell'],['Azure DevOps','Git','Docker','Kubernetes','Jenkins','PowerShell'],['Azure','Terraform','ARM templates','AKS','Python','Azure Monitor'],['Azure','Jenkins','FastAPI','JFrog','Terraform','AKS','Prometheus'],['Azure','Jenkins','ARM templates','Ansible','PowerShell','Helm'],['Azure','Git','Terraform','ARM templates','Ansible','Python']]
for job,bullets,used in zip(p['experience'],impacts,skills):job['impact']=bullets;job['skills_used']=used
p['certifications']=sorted(p['certifications'],key=lambda s:0 if 'Azure DevOps' in s else 1 if 'Azure Fundamentals' in s else 2)
p['notes']=['Azure-only branch profile. Preserve employment titles, dates, education, and certifications.', 'User confirmed hands-on SSIS, Bicep, certificate lifecycle and encrypted database connection experience. Recent-role placement assumed for tailoring; no quantified results or specific regulatory certification claimed.']
for path in [root/'assets/people/rajendra-prasad-n.json',Path('resume_data/people/rajendra-prasad-n.json')]:path.write_text(json.dumps(p,indent=2)+'\n')
