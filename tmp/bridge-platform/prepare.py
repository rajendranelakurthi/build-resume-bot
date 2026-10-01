import json,shutil
from pathlib import Path
root=Path('tmp/bridge-platform/plugin')
shutil.copytree('tmp/azure-infrastructure/plugin/assets',root/'assets',dirs_exist_ok=True)
d=json.loads(next(Path('output/pdf/azure-infrastructure').glob('*.profile.json')).read_text())
d['page_title']='Rajendra P N - Senior Azure DevOps & Cloud Platform Engineer'
d['headline']='Senior Azure DevOps & Cloud Platform Engineer | AI'
d['summary_html']='<strong>Senior Azure DevOps & Cloud Platform Engineer with 10+ years of experience in CI/CD, infrastructure automation, and production operations.</strong> Builds enterprise delivery capabilities with <strong>Azure DevOps, Terraform, Bicep, PowerShell, Docker, and Kubernetes</strong>, combining reusable pipelines, secure deployment controls, and cloud-native operating practices. Brings Azure platform engineering depth, additional AWS cloud experience, and SaaS/payment-platform delivery experience. Partners with architecture, application, cloud, and security teams to standardize infrastructure provisioning, improve observability, automate developer workflows, and maintain reliable operational handoffs.'
d['achievements_title']='Enterprise DevOps & Cloud Platform Highlights'
d['achievements']=[{'tag':'Enterprise Delivery Standards','text':'Standardized reusable pipelines, protected branches, artifact promotion, environment approvals, and deployment validation across application and infrastructure delivery.'},{'tag':'Cloud Automation','text':'Built reusable Azure Terraform modules and automated infrastructure with ARM templates, Ansible, and PowerShell; aligned platform changes with application releases.'},{'tag':'Developer Enablement','text':'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog to automate onboarding and reduce manual release coordination.'}]
d['skills']=['Azure DevOps Administration','Azure Pipelines','Terraform','Bicep','ARM Templates','PowerShell','Azure CLI','Docker','Kubernetes / AKS','DevSecOps','AWS','Platform Engineering']
d['skill_sections']=[{'title':'Enterprise Azure DevOps','content':'Azure Pipelines, multi-stage YAML, reusable templates, Azure Repos, Git policies, Azure Artifacts, agent pools, service connections, deployment environments, approvals, platform administration'}, {'title':'Infrastructure Automation','content':'Terraform modules and remote state, Bicep, ARM templates, Azure CLI, PowerShell, Ansible, deployment plan reviews, lifecycle automation; AWS CloudFormation concepts'}, {'title':'Azure Cloud Platform','content':'AKS, Azure Container Registry, Key Vault, Azure Storage, Virtual Machines, networking, Entra ID, RBAC; deployment patterns for App Services, Functions, API Management, Service Bus, Azure SQL Database'}, {'title':'Containers & Developer Enablement','content':'Docker, Kubernetes, Helm, Argo CD, Linux agents, Jenkins shared libraries, Python FastAPI, REST APIs, automated onboarding, reusable deployment workflows'}, {'title':'DevSecOps & Release Governance','content':'SonarQube, JFrog Xray, vulnerability scanning, secrets management, least privilege, branch protections, policy validation, quality gates, release traceability, audit evidence'}, {'title':'Reliability & Operations','content':'Azure Monitor, Log Analytics, Application Insights, Prometheus, Grafana, ELK, alerting, incident response, root cause analysis, operational runbooks, Linux, Bash, Python'}, {'title':'AWS Supporting Knowledge','content':'AWS cloud experience; working knowledge of Lambda, API Gateway, ECS/EKS, S3, RDS, CloudWatch, IAM, SNS, SQS, CloudFormation, hybrid integration, cost and operational governance'}]
j=d['experience'][0]
j['impact'][-1]='Maintained Azure DevOps repositories, build agents, artifact feeds, service connections, and deployment environments; coordinated platform configuration and delivery handoffs across application teams.'
j['impact'].append('Published deployment standards and operational runbooks covering environment setup, release verification, rollback, and incident escalation; aligned platform changes with architecture and security partners.')
j['skills_used']=['Azure DevOps','Azure Pipelines','Terraform','AKS','Helm','Key Vault','Azure Monitor','PowerShell','Python']
j=d['experience'][1]
j['impact']=[b for b in j['impact'] if 'embedded' not in b.lower()]
j['impact']+=['Standardized agent setup and pipeline dependencies to keep build environments reproducible and support transitions between delivery teams.','Maintained Azure Repos pull-request validation and release approvals, connecting source changes to versioned build outputs and deployment evidence.','Documented pipeline onboarding and recovery procedures, enabling development teams to use shared delivery workflows and resolve common failures.']
j=d['experience'][2]
j['impact']+=['Integrated infrastructure plan review and application verification into release workflows, keeping environment changes traceable to source and approved artifacts.','Partnered with application and cloud teams on Azure deployment patterns, aligning service configuration, identity requirements, and network connectivity before promotion.','Maintained operational runbooks for deployment recovery and recurring support activities; shared troubleshooting practices with distributed engineering teams.']
j=d['experience'][3]
j['impact'][7]='Integrated SonarQube quality checks, JFrog Xray artifact scanning, and secure secrets handling into delivery workflows; preserved validation results for release reviews.'
d['notes']=['Bridge Specialty Group role-specific variant. Android/iOS and associated delivery content removed by user request.','AWS services listed as supporting knowledge; no insurance-specific work or new certifications claimed.']
# The user requested removing all related content; keep internal notes clean too.
d['notes'][0]='Bridge Specialty Group role-specific cloud platform variant.'
assert all(len(j['impact'])>=9 for j in d['experience'])
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(d,indent=2)+'\n')
Path('tmp/bridge-platform/jd.txt').write_text('''Bridge Specialty Group Senior Azure DevOps & Cloud Platform Engineer
Enterprise Azure DevOps platform ownership and administration; architecture collaboration; CI/CD standards and self-service automation.
Terraform, Bicep, ARM templates, AWS CloudFormation; Azure and AWS provisioning and lifecycle management.
Application, infrastructure, integration pipelines; automated builds, tests, release quality gates, compliance controls, deployment validation.
Azure Kubernetes Service AKS, API Management, Service Bus, Functions, App Services, SQL Database, Storage, Key Vault, Monitor, Application Insights.
AWS Lambda, API Gateway, ECS/EKS, S3, RDS, CloudWatch, IAM, SNS, SQS; hybrid-cloud integration, cost optimization and governance.
DevSecOps security scanning, vulnerability assessments, policy validation, audit and compliance support for insurance and financial services.
Monitoring logging alerting observability production support root cause analysis operational documentation platform reliability.
Bachelor degree; 7+ years DevOps cloud platform SRE; 5+ years Azure DevOps administration implementation.
Git Terraform Bicep PowerShell Azure CLI Docker Kubernetes; independently own DevOps, manage transitions, support multiple teams.
Preferred AWS production support, security automation, modernization, insurance financial services, Azure AWS certifications, internal developer platforms.
''')
