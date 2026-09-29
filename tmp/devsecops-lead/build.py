import sys,json
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
root=Path('plugins/resume-creator-plugin/assets')
base=BundledJsonResumeStore(root/'people',root/'static').load_person('rajendra-prasad-n')
p,matched=tailor_profile(base,Path('tmp/devsecops-lead/jd.txt').read_text())
p.page_title='Rajendra Prasad N - DevSecOps Lead'
p.headline='DevSecOps Lead | Secure Delivery & Cloud Operations'
p.summary_html='<strong>Engineer-leader with 10+ years of enterprise DevOps, cloud engineering, release management, and production operations experience.</strong> Builds secure, repeatable delivery across <strong>pipelines, environments, secrets and access, security controls, observability, and recovery</strong>. Combines Azure and AWS infrastructure automation with code-review governance, security scanning, application release validation, and Kubernetes operations. Coordinates competing delivery dependencies, change windows, and production readiness across engineering teams, with a focus on traceable changes, controlled access, and reliable releases for enterprise and payment-platform workloads.'
p.achievements_title='DevSecOps Leadership Highlights'
p.achievements=[
{'tag':'Secure Path to Production','text':'Standardized reusable pipelines, reviewed changes, versioned artifacts, security checks, environment approvals, and deployment verification.'},
{'tag':'Environment & Release Coordination','text':'Aligned team dependencies, change windows, environment configuration, and recovery plans across application, database, and infrastructure releases.'},
{'tag':'Security & Operations','text':'Combined secrets controls, identity governance, monitoring, incident response, and runbooks to support secure production delivery.'}]
p.skill_sections=[
{'title':'Secure CI/CD & Code Controls','content':'GitHub Actions, Azure DevOps, Jenkins, GitLab CI, Harness; branch protection, required reviews, reusable workflows, approval gates'},
{'title':'Code & Dependency Security','content':'SonarQube, Fortify, Black Duck, JFrog Xray; static analysis, dependency scanning, artifact checks, security validation'},
{'title':'Application & Release Security','content':'Container image validation, REST microservices, security-test environments, smoke tests, controlled promotion, Liquibase migration validation'},
{'title':'Secrets & Identity','content':'Azure Key Vault, AWS Secrets Manager, Entra ID, IAM, RBAC, MFA, federated pipeline authentication, least-privilege deployment access'},
{'title':'Infrastructure & Platform Controls','content':'Terraform, CloudFormation, ARM templates, Ansible, AKS/EKS, Kubernetes, Helm, private networking, security groups, policy checks'},
{'title':'Environment & Change Management','content':'Development, QA, security testing, UAT, production; environment configuration, release dependencies, change windows, versioned artifacts'},
{'title':'Observability & Production Operations','content':'Azure Monitor, CloudWatch, CloudTrail, Prometheus, Grafana, Splunk, ELK; incident diagnosis, backup, recovery, operational runbooks'},
{'title':'Automation & Delivery Tooling','content':'Python, Bash, PowerShell, AWS/Azure CLI, Git, Docker, JFrog Artifactory, Jira, FastAPI, SQL, Linux and Windows build agents'}]
impacts=[[
'Led application, database, and infrastructure release coordination across engineering teams, aligning dependencies, change windows, approvals, and production readiness.',
'Built reusable GitHub Actions and Azure DevOps pipelines with automated validation, versioned artifacts, environment approvals, deployment checks, and recovery planning.',
'Established branch protections, required reviews, merge controls, and artifact versioning to keep code changes and production promotions traceable to approved releases.',
'Integrated DevSecOps controls into delivery workflows through secure secrets handling, Terraform validation, pre-deployment policy checks, and application release verification.',
'Provisioned cloud infrastructure with Terraform and integrated Key Vault, federated pipeline authentication, and controlled deployment access to reduce credential exposure.',
'Implemented private service connectivity and environment isolation using private endpoints, cloud networking controls, and identity-based access for application workloads.',
'Managed environment-specific configuration and coordinated release sequencing across development, QA, and production to address shared dependencies and delivery risks.',
'Automated pre-deployment checks, database connectivity validation, deployment summaries, and post-release smoke tests with Python, Bash, and PowerShell.',
'Validated version-controlled database migrations and generated SQL before promotion, coordinating application compatibility, permissions, and recovery with service owners.',
'Configured Harness delivery workflows with reusable templates, approval gates, deployment health checks, failure handling, and rollback steps for Kubernetes applications.',
'Coordinated production incident response and release support, using deployment logs and cloud monitoring to diagnose failures and guide service restoration.',
'Authored deployment guides, architecture documentation, and operational runbooks to improve support readiness, release handover, and knowledge transfer.'
],[
'Standardized reusable CI/CD stages, build-agent configuration, environment settings, and release checks with development and QA teams.',
'Migrated Jenkins pipelines to GitLab CI and enforced branch protection, secure runner practices, container image validation, and controlled pipeline execution.',
'Administered Linux and Windows build agents, Docker delivery workflows, and Kubernetes deployments; diagnosed credential, pipeline, and runtime failures.',
'Maintained separate development, QA, and production configuration and used reviewed deployment stages to protect application and database releases.',
'Partnered with developers to investigate deployment defects, strengthen release checks, and document repeatable remediation procedures.'
],[
'Provisioned cloud infrastructure with Terraform and pipeline-driven deployment patterns, supporting repeatable configuration and controlled environment changes.',
'Built CI/CD workflows with GitHub Actions and Jenkins, publishing versioned artifacts and integrating SonarQube with engineering delivery tooling.',
'Deployed containerized microservices with Helm, Kubernetes, and ArgoCD, supporting consistent configuration and release promotion across environments.',
'Implemented secure VPC networking, security groups, private connectivity, DNS, and load balancing for enterprise application workloads.',
'Implemented CloudWatch observability, AWS Backup, and disaster-recovery controls; troubleshot infrastructure and deployment issues across distributed teams.'
],[
'Delivered CI/CD and Terraform automation for payment-platform workloads, aligning application releases, infrastructure changes, and operational readiness.',
'Integrated SonarQube and secure secrets handling into reusable Jenkins and GitHub Actions workflows for build, test, artifact publication, and promotion.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray to support controlled artifact delivery and dependency-security workflows.',
'Applied identity controls, MFA, role-based access, and custom policy checks across cloud environments to strengthen platform governance.',
'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog and built Prometheus exporters and Ansible-managed monitoring stacks for operational diagnosis.'
],[
'Built continuous delivery pipelines for REST microservices across development, security-validation, UAT, and production environments.',
'Coordinated release configuration and verification with engineering teams and supported deployment troubleshooting across shared enterprise environments.',
'Automated Linux and Windows cloud configuration and secure application/database connectivity using infrastructure templates, Ansible, and PowerShell.',
'Supported identity integration, privileged access, MFA, Kubernetes release packaging, and monitoring through ELK and cloud-native tooling.'
],[
'Created repeatable deployment pipelines with Ansible and Terraform and promoted consistent artifacts from development through production.',
'Implemented Git branching practices, environment-specific configuration, and controlled release parameters to improve deployment traceability.',
'Automated administrative and deployment tasks with Python, shell scripting, and cloud CLI workflows; maintained build agents and support documentation.'
]]
skills=[['Azure','AWS','GitHub Actions','Azure DevOps','Harness','Terraform','Key Vault','Kubernetes','Python'],['GitLab CI','Jenkins','Git','Docker','Kubernetes','Linux'],['AWS','Terraform','GitHub Actions','EKS','SonarQube','CloudWatch'],['Jenkins','SonarQube','JFrog Xray','Terraform','Python','Prometheus','Ansible'],['Jenkins','Kubernetes','Ansible','PowerShell','ELK'],['Terraform','Ansible','Git','Python','Shell']]
for job,bullets,used in zip(p.experience,impacts,skills):job.impact=bullets;job.skills_used=used
p.notes=['Aggressive JD tailoring. Employment titles, dates, education, and certifications retained. New internet-researched tools and unconfirmed shared-environment booking/refresh ownership are documented separately, not asserted as experience.']
out=Path('output/pdf/rajendra-prasad-n-devsecops-lead-aggressive')
h=BundledHtmlResumeRenderer(root/'templates/base_resume.html').render(p)
h=h.replace('</style>','@media print{.header-left{flex:1;min-width:0}.header-right{flex:0 0 51mm}.cert-badge-svg{max-width:46px}.cert-card{min-height:74px}.job-block{break-inside:auto;page-break-inside:auto}.job-header,.job-details{break-after:avoid}li{break-inside:avoid}.summary-box{font-size:11px}.section-title{margin-top:12px}}\n</style>')
out.with_suffix('.html').write_text(h)
out.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
print(out)
