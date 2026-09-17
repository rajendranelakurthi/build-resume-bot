import json, sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore, BundledHtmlResumeRenderer, build_aws_devops_profile
assets=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(assets/'people',assets/'static').load_person('rajendra-prasad-n')
p=build_aws_devops_profile(base)
p.page_title='Rajendra Prasad N - Lead AWS DevOps Engineer'
p.headline='Lead AWS DevOps Engineer | Ansible, Linux & Release Automation'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in AWS cloud operations, application deployments, release management, and infrastructure automation.</strong> Hands-on expertise with <strong>Ansible, Linux, Bash/Shell scripting, Jenkins, GitLab CI/CD, Terraform, and AWS deployment services</strong>. Builds reusable automation for server configuration, application installation, environment promotion, health validation, and recovery. Leads release readiness, production cutovers, troubleshooting, and cross-team coordination, with a focus on consistent configurations, traceable artifacts, and dependable deployment procedures.'
p.achievements_title='AWS DevOps & Release Delivery Highlights'
p.achievements=[{'tag':a+':','text':b} for a,b in [
('Deployment Automation','Standardized application delivery using reusable pipelines, Ansible roles, shell utilities, and versioned deployment artifacts.'),
('Linux & AWS Operations','Connected Linux administration, AWS infrastructure automation, monitoring, and incident response into repeatable operational workflows.'),
('Release Management','Coordinated release scope, dependencies, readiness checks, approvals, cutover execution, rollback plans, and post-release validation.')]]
p.skill_sections=[{'title':a,'content':b} for a,b in [
('AWS Cloud','EC2, VPC, IAM, ALB/NLB, Auto Scaling, S3, EBS, RDS, Route 53, CloudWatch, CloudTrail, Systems Manager, Secrets Manager'),
('Ansible & Configuration','Playbooks, reusable roles, inventories, variables, Jinja2 templates, handlers, tags, Ansible Vault, rolling updates, idempotent configuration'),
('Linux Administration','RHEL, Ubuntu, Amazon Linux, systemd, package management, users and permissions, SSH, filesystems, process and resource troubleshooting'),
('Shell Scripting & Automation','Bash, POSIX shell, Python, AWS CLI, sed, awk, grep, jq, cron, error handling, retries, logging, API-driven automation'),
('CI/CD & Application Delivery','Jenkins, GitLab CI/CD, GitHub Actions, CodePipeline, CodeBuild, CodeDeploy, Maven, Gradle, JFrog Artifactory, Nexus'),
('Release Management','Release calendars, change approvals, dependency tracking, go/no-go reviews, artifact promotion, cutover plans, rollback, release notes, retrospectives'),
('Infrastructure & Containers','Terraform, CloudFormation, Ansible, Docker, ECR, EKS, Kubernetes, Helm, ArgoCD, infrastructure as code'),
('Monitoring & Security','CloudWatch, Prometheus, Grafana, Splunk, ELK, SonarQube, Fortify, Black Duck, least-privilege IAM, secrets handling, audit evidence')]]
jobs=[
(['AWS','Ansible','Linux','Bash','Jenkins','GitLab CI/CD','Terraform','CodeDeploy','CloudWatch'],[
'Led AWS application and infrastructure delivery, translating release requirements into reusable deployment workflows, operational standards, and environment-specific implementation plans.',
'Built multi-stage Jenkins and GitLab pipelines for compilation, automated tests, security scans, artifact publication, approvals, deployment, and post-release verification.',
'Engineered reusable Ansible roles for Linux packages, service accounts, application directories, configuration templates, certificates, and systemd services; separated shared defaults from environment-specific variables.',
'Implemented staged application deployments with Ansible serial execution, load-balancer draining, service restarts, health checks, and failure thresholds to stop unsafe promotion.',
'Developed Bash deployment utilities with argument validation, explicit exit-code handling, bounded retries, execution locks, structured logs, and cleanup traps for repeatable production operations.',
'Owned release calendars, dependency reviews, change records, go/no-go checkpoints, cutover runbooks, stakeholder updates, and post-implementation validation across engineering and operations teams.',
'Automated AWS provisioning with Terraform and CloudFormation for EC2, networking, IAM, load balancing, storage, and monitoring, using reviewed plans and environment-specific configuration.',
'Configured CodeDeploy lifecycle hooks and deployment groups for EC2 application releases; integrated CloudWatch alarms and automatic rollback to the last known-good revision.',
'Administered Linux application hosts and investigated systemd failures, filesystem pressure, CPU and memory contention, permissions, DNS resolution, and application connectivity issues.',
'Standardized AWS Systems Manager maintenance workflows for patching and remote operations, coordinating prechecks, maintenance windows, reboot requirements, and post-patch service validation.',
'Promoted versioned artifacts across environments with checksum verification, release tags, configuration separation, and protected secrets; maintained traceability from source commit to deployed package.',
'Led deployment incident triage using CloudWatch logs, alarms, and application telemetry; documented root causes, recovery actions, and automation improvements in release retrospectives.'
]),
(['AWS','Ansible','Linux','Shell Scripting','GitLab CI/CD','Docker','Kubernetes'],[
'Developed reusable GitLab CI/CD templates for application builds, artifact publication, deployment approvals, and environment promotion.',
'Administered Linux build agents and runner pools, maintaining toolchains, workspace cleanup, dependency caches, permissions, and workload-specific execution settings.',
'Created Ansible playbooks to install application prerequisites, deploy versioned packages, render configuration files, and manage service startup across environments.',
'Automated deployment prechecks and smoke tests with shell scripts, validating disk capacity, package availability, service status, and endpoint responses.',
'Packaged applications as Docker images and deployed Kubernetes workloads with controlled configuration, readiness probes, and verified rollout status.',
'Coordinated application releases with development and QA teams, tracking defects, dependencies, approvals, and rollback readiness before production cutover.',
'Resolved pipeline, Linux, container, and network failures and converted recurring support tasks into documented automation and troubleshooting procedures.'
]),
(['AWS','Ansible','Linux','Bash','Terraform','GitHub Actions','EKS','CloudWatch'],[
'Provisioned AWS infrastructure with Terraform and CloudFormation, maintaining reusable modules and reviewed changes for compute, networking, storage, and monitoring.',
'Built GitHub Actions and Jenkins workflows for reproducible builds, versioned artifacts, controlled deployments, and automated release validation.',
'Automated Linux application configuration with Ansible roles and shell scripts, standardizing packages, runtime settings, file ownership, and service management.',
'Deployed microservices to EKS with Docker, Helm, and ArgoCD workflows; verified readiness, configuration changes, and rollback options during release promotion.',
'Developed Bash and Python utilities for environment checks, AWS resource inventory, artifact retrieval, deployment status reporting, and operational cleanup.',
'Maintained Linux build and deployment hosts, diagnosing dependency conflicts, process failures, network connectivity, and resource bottlenecks.',
'Established CloudWatch dashboards and alarms alongside backup and disaster-recovery procedures to support service restoration and deployment troubleshooting.',
'Partnered with distributed engineering teams on release schedules, production readiness, dependency sequencing, and operational handover documentation.'
]),
(['AWS','Ansible','Linux','Bash','Jenkins','Terraform','Prometheus','Grafana'],[
'Designed Jenkins and GitHub Actions pipelines for AWS application and infrastructure delivery, incorporating repeatable build, test, package, and deployment stages.',
'Developed resilient Ansible roles for highly available Prometheus, Grafana, and Node Exporter deployments, managing configuration templates, handlers, and service validation.',
'Authored Bash and Python automation for Linux health checks, log collection, service recovery, and recurring operational tasks with documented execution procedures.',
'Built Jenkins shared libraries to standardize image versioning, artifact publication, reusable deployment steps, and environment promotion.',
'Automated project onboarding through internal FastAPI services integrating Jenkins, Jira, and JFrog, reducing repeated manual setup across delivery workflows.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray; maintained artifact traceability and integrated quality and security checks into releases.',
'Created Python Prometheus exporters and operational dashboards to expose application-specific metrics and support incident investigation and capacity reviews.',
'Supported production deployments and incident response, coordinating health verification, rollback decisions, root-cause reviews, and improvements to release runbooks.'
]),
(['AWS','Ansible','Linux','Shell Scripting','Jenkins','Maven','Tomcat','JBoss','Helm'],[
'Built Jenkins delivery pipelines for Java applications and REST microservices across development, test, UAT, and production environments.',
'Automated Linux application setup and configuration with Ansible and shell scripts, including runtime dependencies, environment properties, access permissions, and service checks.',
'Managed Maven build outputs and deployment packages for Tomcat and JBoss services, preserving version traceability and environment-specific configuration.',
'Deployed Kubernetes applications with Helm and version-controlled manifests, validating configuration changes, pod health, and service connectivity.',
'Troubleshot AWS application dependencies involving EC2, load balancers, RDS, CloudWatch, certificates, and identity integrations during releases and migrations.',
'Coordinated multi-environment releases with application teams, tracking deployment prerequisites, change approvals, validation results, and recovery actions.',
'Implemented ELK-based logging and maintained deployment guides, architecture documentation, and operational runbooks for engineering and support teams.'
]),
(['AWS','Ansible','Linux','Shell Scripting','Python','Maven','Tomcat','JBoss','Nexus'],[
'Created Ansible deployment workflows to promote application packages from development through production using consistent installation and configuration steps.',
'Wrote shell and Python scripts for file handling, package extraction, configuration updates, service control, log inspection, and post-deployment checks.',
'Supported Linux build and application servers, resolving permission issues, failed processes, disk usage, missing dependencies, and connectivity problems.',
'Authored reusable Terraform modules and AWS CLI automation to provision infrastructure and maintain environment-specific service configurations.',
'Established Git branching, release tagging, and artifact repository practices to keep application versions and deployment inputs traceable.',
'Documented deployment sequences for infrastructure, API, database, and UI components, coordinating environment readiness, release execution, and handover to support teams.'
])]
for i,(skills,bullets) in enumerate(jobs):
 p.experience[i].title=base.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['AWS','Ansible','Linux','Shell Scripting','Release Management','Application Deployments','DevOps Automation','Bash','Jenkins','Terraform']
p.summary_html += ' Healthcare Payer experience supporting application deployments and release operations for member enrollment, eligibility, and claims-processing services within the Mphasis/HPE engagement.'
p.skills.append('Healthcare Payer')
p.skill_sections.append({'title':'Healthcare Payer Domain','content':'Member enrollment, eligibility and benefits, claims-processing applications, payer application deployments, batch-processing support, release validation'})
p.skill_sections=[s for s in p.skill_sections if s['title']!='Monitoring & Security']
p.experience[-1].skills_used.append('Healthcare Payer')
p.experience[-1].impact[0]='Supported Healthcare Payer application releases within the Mphasis/HPE engagement, using Ansible to promote enrollment, eligibility, and claims-processing service packages across environments.'
p.experience[-1].impact[1]='Developed shell and Python scripts for payer application configuration, service control, batch-job checks, log inspection, and post-deployment validation.'
p.experience[-1].impact[-1]='Coordinated payer application releases across API, database, batch, and UI components, validating dependencies, release sequencing, and handover with QA and support teams.'
p.experience[-1].impact.extend([
 'Supported Linux-hosted payer services by investigating failed batch jobs, missing inbound files, permission issues, and application connectivity; coordinated recovery and controlled job reruns with support teams.',
 'Partnered with application and QA teams on enrollment, eligibility, and claims workflow smoke tests after releases, documenting results, defects, and rollback readiness.'
])
p.notes=['Aggressive tailoring requested by user. Expanded responsibilities from AWS, configuration management, release engineering, and operations themes; no new numerical performance claims.']
assert p.email=='rajendran.scm@gmail.com'
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-aws-devops-ansible-release-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
stem.with_suffix('.jd.txt').write_text('AWS, Ansible, Linux, Shell Scripting, Release Management, Application Deployments, DevOps Automation.\nUser requested a robust Aggressive AWS DevOps resume with expanded responsibilities.\n')
html=BundledHtmlResumeRenderer(assets/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','variant':'AWS DevOps / Ansible / Linux / Release Management','experience_bullet_count':sum(len(j.impact) for j in p.experience),'html_path':str(stem.with_suffix('.html')),'pdf_path':str(out/'rajendra-pn-aws-devops.pdf'),'profile_path':str(stem.with_suffix('.profile.json')),'sources':['https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/transactions','https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html','https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html','https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
