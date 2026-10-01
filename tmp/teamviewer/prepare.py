import json,shutil
from pathlib import Path
root=Path('tmp/teamviewer/plugin');shutil.copytree('tmp/bridge-platform/plugin/assets',root/'assets',dirs_exist_ok=True)
d=json.loads(Path('tmp/bridge-platform/plugin/assets/people/rajendra-prasad-n.json').read_text())
d['page_title']='Rajendra P N - Senior Azure DevOps & Platform Engineer'
d['headline']='Senior Azure DevOps & Platform Engineer | Kubernetes | GitOps'
d['summary_html']='<strong>Senior Azure DevOps & Platform Engineer with 10+ years of experience in cloud infrastructure, SaaS delivery, and production operations.</strong> Builds secure, highly available <strong>Azure platforms with Terraform/Bicep, AKS, Docker, Helm, and Argo CD GitOps</strong>. Automates CI/CD and operational tooling with Python, Bash, and PowerShell; improves reliability through observability, incident response, capacity planning, and cost optimization. Combines Azure and AWS platform experience with microservices delivery, identity controls, relational database operations, and cross-team engineering mentorship.'
d['achievements_title']='SaaS Platform Engineering Highlights'
d['achievements']=[{'tag':'Kubernetes & GitOps','text':'Standardized AKS/EKS deployments with Helm and Argo CD, using reviewed Git changes, health validation, and controlled reconciliation for repeatable releases.'},{'tag':'Reliability & Observability','text':'Correlated Azure Monitor, Application Insights, Prometheus, Grafana, and CloudWatch telemetry to troubleshoot incidents and guide capacity and scaling decisions.'},{'tag':'Automation & Enablement','text':'Built reusable delivery pipelines and Python operational integrations; published platform runbooks and coached engineers on secure cloud-native delivery.'}]
d['skills']=['Azure','Terraform','Bicep','AKS','Kubernetes','Docker','Helm','Argo CD','GitOps','Azure DevOps','Python','Bash','PowerShell','Observability','AWS']
d['skill_sections']=[{'title':'Azure Infrastructure & Availability','content':'AKS, virtual networks, NSGs, private endpoints, Azure Storage, Azure SQL Database, Key Vault, availability zones, resilient deployment patterns, capacity planning'}, {'title':'Kubernetes & GitOps','content':'Docker, AKS/EKS, Helm, Argo CD, GitOps reconciliation, drift correction, health checks, rolling updates, pod disruption budgets, HPA, cluster autoscaling'}, {'title':'Infrastructure & Delivery Automation','content':'Terraform modules, Bicep, ARM templates, Azure CLI, Azure DevOps YAML, Git policies, artifact promotion, security gates, CloudFormation, Jenkins'}, {'title':'Observability & Production Operations','content':'Azure Monitor, Log Analytics, Application Insights, Prometheus, Grafana, ELK, CloudWatch, dashboards, alerting, on-call support, incident response, root cause analysis'}, {'title':'Networking, Security & Identity','content':'Entra ID, Azure RBAC, managed identities, Key Vault, AWS IAM, network policies, TLS, secrets protection, vulnerability scanning; Keycloak/OIDC concepts'}, {'title':'Automation, Data & Enablement','content':'Python, Bash, PowerShell, Linux, REST APIs, FastAPI, SQL, relational database connectivity, Java/Maven delivery, runbooks, mentoring, developer self-service'}, {'title':'AWS Platform Engineering','content':'EKS/ECS, Lambda, API Gateway, VPC, S3, RDS, CloudWatch, IAM, SNS/SQS, Terraform/CloudFormation, resource rightsizing and cost governance'}]
d['experience'][0]['impact']=[
'Engineered secure Azure SaaS infrastructure with Terraform and Bicep, standardizing networks, private endpoints, storage, and AKS configuration across environments.',
'Operated AKS and AWS EKS platforms with Helm and Argo CD GitOps; controlled manifest promotion, drift correction, and deployment health through reviewed Git changes.',
'Improved AKS availability with zone-aware node pools, pod disruption budgets, readiness checks, and rolling-update safeguards; validated recovery procedures.',
'Built reusable Azure DevOps pipelines for container builds, automated tests, image scanning, IaC validation, and gated deployment to Azure and AWS workloads.',
'Implemented Azure Monitor, Application Insights, Prometheus/Grafana, and CloudWatch dashboards and alerts to track platform health and diagnose incidents.',
'Tuned pod resource requests, HPA settings, and node autoscaling against workload demand; reviewed Azure/AWS utilization to improve capacity and control cost.',
'Secured microservices with Entra ID, managed identities, Key Vault, AWS IAM, and Kubernetes network controls; partnered with Security on vulnerability remediation.',
'Developed Python, Bash, and PowerShell tooling for deployment checks and operational diagnostics; supported on-call incident response, root cause analysis, and runbooks.',
'Mentored engineers on Terraform, GitOps, and troubleshooting; partnered with Engineering, Product, Security, and Platform teams on service readiness and developer workflows.']
d['experience'][0]['skills_used']=['Azure','Terraform','Bicep','AKS/EKS','Argo CD','Helm','Azure DevOps','Prometheus/Grafana','AWS','Python']
d['experience'][1]['impact'][0]='Maintained AKS and AWS ECS deployment configuration, validating container health, environment settings, and protected inputs before release promotion.'
d['experience'][1]['impact'][6]='Automated Linux agent configuration and deployment diagnostics with Bash and PowerShell, reducing recurring setup work for development teams.'
d['experience'][2]['impact'][0]='Provisioned Azure AKS and AWS EKS with Terraform; managed Helm and Argo CD deployments with versioned configuration and controlled GitOps reconciliation.'
d['experience'][2]['impact'][6]='Improved Kubernetes performance through resource diagnostics and scaling reviews; investigated application latency, node pressure, and network connectivity.'
d['experience'][3]['impact'][2]='Used Prometheus/Grafana to diagnose Kubernetes capacity and service issues; automated Linux recovery tasks with Ansible and Bash during production support.'
d['experience'][3]['impact'][3]='Supported AWS RDS and Azure SQL Database release dependencies, validating SQL connectivity, database readiness, and application recovery procedures.'
d['experience'][3]['impact'][8]='Participated in on-call support for SaaS workloads, using CloudWatch logs and alarms to investigate AWS incidents and document root causes and recovery actions.'
d['experience'][4]['impact'][1]='Built Jenkins and Maven pipelines for Java REST microservices, integrating automated tests, security validation, and controlled promotion across UAT and production.'
d['notes']=['TeamViewer JD-specific Aggressive Azure DevOps variant. AWS platform responsibilities retained across all six projects; mobile content excluded.','No new certifications, employment history, or quantified outcomes added.']
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(d,indent=2)+'\n')
Path('tmp/teamviewer/jd.txt').write_text('''TeamViewer Senior Azure DevOps Platform Engineer
Design, build, and operate secure, scalable, highly available Azure infrastructure powering TeamViewer's global SaaS platform.
Manage and optimize Kubernetes platforms using GitOps practices and Infrastructure as Code.
Develop CI/CD pipelines, automation, and operational tooling to improve delivery speed, security, and developer productivity.
Implement monitoring, logging, and observability solutions to ensure platform reliability, performance, and visibility.
Drive platform performance, scalability, security, and cost optimization while supporting incident response and on-call operations.
Mentor engineers and partner across Engineering, Product, Security, and Platform teams to advance cloud-native best practices.
5+ years experience as a Senior DevOps, Platform, or Cloud Engineer in high-availability SaaS environments.
Strong expertise in Azure, Infrastructure as Code (Terraform/Bicep), Kubernetes, containers, and GitOps tools such as Argo CD.
Hands-on experience with CI/CD platforms, scripting (Python, Bash, PowerShell), and automation.
Knowledge of observability, cloud networking, microservices, infrastructure security, identity management (e.g., Entra, Keycloak), and relational databases.
Strong problem-solving, automation, and mentoring skills; experience with Java, Go, SQL, AWS, or GCP is a plus.
''')
assert all(len(j['impact'])==9 for j in d['experience'])
