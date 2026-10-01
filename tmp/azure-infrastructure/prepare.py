import json, shutil
from pathlib import Path
root=Path('tmp/azure-infrastructure/plugin')
shutil.copytree('plugins/resume-creator-plugin/assets',root/'assets',dirs_exist_ok=True)
p=root/'assets/people/rajendra-prasad-n.json'
d=json.loads(p.read_text())
d['page_title']='Rajendra P N - Azure Infrastructure & DevOps Engineer'
d['summary_html']='<strong>Lead Azure DevOps Engineer with 10+ years of experience in infrastructure automation, release engineering, and production operations.</strong> Engineers Azure cloud infrastructure with <strong>Terraform, Azure Pipelines, AKS, and Helm Charts</strong>, supporting cloud-native applications and hybrid infrastructure connectivity. Brings hands-on depth in Azure networking, identity, compute, storage, Linux administration, and observability with Azure Monitor, Log Analytics, Application Insights, Prometheus, and Grafana. Automates operations with PowerShell, Bash, and Python and collaborates with distributed development, security, and operations teams to troubleshoot incidents and deliver controlled releases.'
d['skills']=['Azure Cloud Infrastructure','Terraform','Azure DevOps','CI/CD','AKS / Kubernetes','Helm Charts','Azure Monitor','Log Analytics','Linux','PowerShell','Bash','Python']
d['achievements_title']='Azure Infrastructure & DevOps Highlights'
d['achievements']=[{'tag':'Infrastructure as Code','text':'Built reusable Terraform modules for Azure networking and AKS; maintained environment parameters and reviewed infrastructure changes through delivery pipelines.'},{'tag':'Kubernetes Delivery','text':'Deployed Azure-hosted containerized services using Helm and Argo CD, aligning application configuration, versioned artifacts, and release verification.'},{'tag':'Observability & Operations','text':'Correlated Azure Monitor, Log Analytics, Prometheus, and Grafana telemetry to diagnose platform failures and support reliable production releases.'}]
d['skill_sections']=[{'title':'Azure Infrastructure & Hybrid Connectivity','content':'Azure Virtual Machines, Virtual Networks, subnets, NSGs, routing, private endpoints, Azure Storage, Azure Container Registry, cloud-native services, hybrid network connectivity'}, {'title':'Infrastructure as Code','content':'Terraform modules, environment parameters, remote state, plan reviews, infrastructure validation, Bicep, ARM templates, Azure CLI'}, {'title':'CI/CD & Kubernetes','content':'Azure Pipelines, reusable YAML templates, Azure Repos, Azure Artifacts, Linux build agents, Docker, AKS, Kubernetes, Helm Charts, Argo CD, deployment approvals'}, {'title':'Monitoring & Observability','content':'Azure Monitor, Log Analytics, Application Insights, Prometheus, Grafana, ELK, dashboards, alerting, centralized logging, incident troubleshooting, root cause analysis'}, {'title':'Security & Identity','content':'Microsoft Entra ID, Azure RBAC, managed identities, Azure Key Vault, workload identity federation, secure service connections, SonarQube, artifact scanning'}, {'title':'Linux & Automation','content':'Linux system administration, services, permissions, process and resource diagnostics, networking fundamentals, PowerShell, Bash, Python, Ansible, REST APIs'}, {'title':'Mobile & Embedded Delivery','content':'Bitrise, Android/iOS signing and provisioning, Google Play, App Store publishing, embedded software release packages; reviewed and tested AI-assisted automation'}]
# Preserve employer history and mobile/embedded preferences while sharpening Azure operational scope.
j=d['experience'][0]
j['skills_used']=['Azure','Terraform','Azure Pipelines','AKS','Helm','Azure Monitor','Key Vault','Bitrise','Python','PowerShell']
j['impact'][0]='Engineered multi-stage Azure Pipelines for Terraform validation, infrastructure plan review, application builds, and gated deployment, standardizing reusable YAML templates and environment parameters.'
j['impact'][4]='Automated Azure infrastructure changes with reusable Terraform configuration for virtual networks, compute, storage, and AKS; reviewed deployment plans and validated environment readiness.'
j['impact'][5]='Secured Azure delivery with Key Vault, Microsoft Entra ID, Azure RBAC, managed identities, and least-privilege service connections; diagnosed access and authentication failures.'
j['impact'][6]='Deployed containerized services to AKS with Helm Charts, managing environment values, image versions, deployment health checks, and recovery procedures alongside automated security gates.'
j['impact'][8]='Investigated production and deployment incidents using Azure Monitor, Log Analytics, and Application Insights; tuned alerting and correlated logs with Linux resource and network diagnostics.'
j['impact'].append('Supported cloud-native and hybrid infrastructure connectivity by troubleshooting DNS, routes, NSGs, and private endpoint access with network and application teams; documented corrective actions and global support handoffs.')
j=d['experience'][1]
j['impact'][4]='Administered Linux and Windows build agents, managing services, permissions, tool dependencies, disk capacity, and network connectivity; resolved pipeline and credential failures.'
j['impact'][6]='Maintained Azure deployment configuration and Helm values across environments, validating Kubernetes service readiness and protected release inputs before promotion.'
j=d['experience'][2]
j['impact'][3]='Provisioned Azure networking, compute, and AKS infrastructure with Terraform and ARM templates; deployed Kubernetes applications through Helm Charts and Argo CD with environment-specific values.'
j['impact'][5]='Correlated Azure Monitor, Log Analytics, and application telemetry to isolate deployment failures and connectivity issues; maintained actionable alerts and verified recovery with engineering teams.'
j['impact'][6]='Maintained Terraform modules, environment parameters, and Azure Storage-backed state; reviewed planned changes before applying infrastructure updates across release stages.'
j=d['experience'][3]
j['impact'][4]='Built reusable Terraform modules for Azure virtual networks and AKS, standardizing network configuration and Kubernetes infrastructure alongside application delivery.'
j['impact'][5]='Used Prometheus and Grafana dashboards and alerts to investigate Kubernetes resource pressure and service failures; automated Linux operational tasks with Ansible and Bash.'
j=d['experience'][4]
j['impact'][1]='Automated Azure virtual machines, virtual networks, NSGs, and Linux configuration with ARM templates, Ansible, and PowerShell, standardizing infrastructure setup and connectivity checks.'
j['impact'][4]='Packaged Kubernetes services with Helm Charts, maintaining environment values, release versions, readiness checks, and deployment recovery procedures across Azure-hosted environments.'
p.write_text(json.dumps(d,indent=2)+'\n')
Path('tmp/azure-infrastructure/jd.txt').write_text('''This request has Plano or Richardson location as mandate and client interview will be there.
Required Skills & Qualifications
Strong experience with Azure Cloud Infrastructure and platform services.
Hands-on experience in Infrastructure as Code (IaC) using Terraform.
Experience with CI/CD automation, deployment pipelines, and DevOps practices.
Strong expertise in monitoring, alerting, logging, and observability tools and frameworks.
Experience with Helm Charts for Kubernetes application deployment and management.
Good understanding of Linux system administration and operating system fundamentals.
Experience managing and supporting cloud-native and hybrid cloud infrastructure environments.
Working knowledge of Azure networking, security, identity management, storage, and compute services.
Experience with containerized environments and Kubernetes platforms is preferred.
Knowledge of automation and scripting using PowerShell, Bash, or Python is desirable.
5+ years of experience in Azure Infrastructure, Cloud Engineering, or DevOps-related roles.
Azure certifications (AZ-104, AZ-305, or equivalent) are preferred.
Strong analytical, troubleshooting, and problem-solving skills.
Excellent communication and collaboration skills in a global delivery environment.
''')
