import json,shutil
from pathlib import Path
root=Path('tmp/release-deployment/plugin');shutil.copytree('plugins/resume-creator-plugin',root,dirs_exist_ok=True)
p=json.loads((root/'assets/people/rajendra-prasad-n.json').read_text())
p['full_name']='Rajendra P N';p['headline']='Release & Deployment Engineer | Azure DevOps | AWS';p['page_title']='Rajendra P N - Release & Deployment Engineer'
p['summary_html']='<strong>Release & Deployment Engineer with 10+ years of experience in software delivery, DevOps, and production support.</strong> Coordinates releases across development, test, staging, and production, combining <strong>Azure DevOps, Jenkins, Git, and deployment automation</strong> with environment readiness, change controls, validation, and rollback planning. Automates operational tasks with PowerShell, Python, and Bash; troubleshoots deployment failures and supports incident recovery. Partners with Development, QA, Infrastructure, Security, and business stakeholders to deliver controlled releases with clear communication and operational evidence.'
p['skills']=['Azure DevOps','Jenkins','Git','GitHub Actions','GitLab CI','PowerShell','Python','Bash','Terraform','Kubernetes','Docker','Release Management']
p['skill_sections']=[
{'title':'Release & Deployment Management','content':'Release calendars, dependency coordination, readiness reviews, implementation plans, change approvals, deployment sequencing, rollback plans, release notes'},
{'title':'CI/CD & Source Control','content':'Azure DevOps, Azure Pipelines, Jenkins, GitHub Actions, GitLab CI/CD, YAML, Git, pull requests, branch protection, release tags, pipeline maintenance'},
{'title':'Cloud & Environment Management','content':'Azure, AWS, Terraform, Ansible, Docker, Kubernetes, Helm, environment configuration, secrets, deployment targets, infrastructure validation'},
{'title':'Scripting & Automation','content':'PowerShell, Python, Bash, shell scripting, REST APIs, FastAPI, configuration checks, release status reporting, deployment verification'},
{'title':'Production Support & Observability','content':'Azure Monitor, CloudWatch, Splunk, ELK, AppDynamics, Prometheus, Grafana, smoke tests, incident triage, root cause analysis, recovery runbooks'},
{'title':'Artifacts, Quality & Governance','content':'Artifactory, Nexus, SonarQube, JFrog Xray, versioned packages, security checks, release evidence, access controls, audit readiness, operational documentation'}]
p['achievements_title']='Release Execution & Production Reliability Highlights'
p['achievements']=[{'tag':'Controlled Releases','text':'Coordinated environment readiness, deployment dependencies, validation steps, and recovery plans for application and infrastructure releases.'},{'tag':'Delivery Automation','text':'Built reusable CI/CD workflows and Python, PowerShell, and Bash utilities for repeatable deployments and operational checks.'},{'tag':'Production Support','text':'Investigated deployment failures, coordinated incident response, and converted recurring issues into documented fixes and improved release procedures.'}]
points=[[
'Coordinated release scope, schedules, dependencies, implementation steps, and production readiness with Development, QA, Infrastructure, Security, and business stakeholders.',
'Built and maintained Azure DevOps and Git-based delivery workflows with build, test, packaging, environment promotion, and post-deployment validation stages.',
'Prepared deployment plans covering artifact versions, environment prerequisites, execution order, owners, smoke tests, and rollback criteria.',
'Supported change reviews with technical risk assessments, dependency checks, test evidence, and recovery procedures before approved deployment windows.',
'Maintained release schedules and communicated readiness, blockers, approval status, and deployment progress to engineering and support teams.',
'Automated configuration checks, release preparation, deployment verification, and operational tasks using PowerShell, Python, and Bash.',
'Validated environment configuration, secrets access, infrastructure changes, and application dependencies before promoting releases into production.',
'Coordinated smoke tests and post-release monitoring; triaged deployment failures and production incidents with application and infrastructure owners.',
'Maintained Git branch protections, reviewed changes, artifact versioning, and security checks to preserve traceability throughout release execution.',
'Authored deployment guides and operational runbooks; documented root causes and incorporated incident lessons into release checks and recovery procedures.'
],[
'Supported releases across development, QA, staging, and production, coordinating build readiness and deployment handoffs with application teams.',
'Modernized Jenkins workflows into reusable GitLab CI pipelines while preserving build, test, packaging, and deployment requirements.',
'Administered Linux and Windows build agents, resolving runner capacity, workspace, dependency, and credential failures.',
'Maintained environment-specific variables and release configuration to keep deployment inputs consistent across stages.',
'Organized artifact feeds and package versions, ensuring teams promoted the intended release package and dependencies.',
'Applied branch protection, merge controls, and image-validation checks before application deployment.',
'Coordinated readiness checks and test evidence with QA and developers before environment promotion.',
'Troubleshot pipeline, container, and Kubernetes deployment failures and verified corrective actions with service owners.',
'Documented release procedures, known issues, and operational handoffs to support repeatable delivery.'
],[
'Built Jenkins and GitHub Actions pipelines for repeatable build, test, packaging, and application deployment workflows.',
'Configured deployment groups and environment-specific release targets for controlled production rollouts.',
'Coordinated infrastructure and application dependencies, deployment sequencing, and readiness checks with distributed engineering teams.',
'Published versioned artifacts and maintained package-consumption patterns for traceable release promotion.',
'Automated recurring deployment and operational checks with PowerShell, Python, and shell scripts.',
'Provisioned AWS environments with Terraform and integrated infrastructure validation into CI/CD execution.',
'Maintained release dashboards and defect-tracking visibility to communicate build health, blockers, and deployment status.',
'Investigated deployment failures using pipeline logs and platform telemetry; coordinated recovery and post-deployment validation.',
'Created release documentation and recovery guidance, incorporating monitoring and backup controls into operational readiness.'
],[
'Coordinated application and infrastructure delivery for SaaS and payment-platform workloads, aligning deployment dependencies and release readiness.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray to support controlled builds, secure packages, and production delivery.',
'Developed Groovy shared libraries for consistent image versioning and artifact publication across services.',
'Built Python FastAPI integrations between Jenkins, Jira, and JFrog to automate onboarding and release coordination.',
'Standardized CI/CD stages for build, testing, quality checks, and artifact promotion with development teams.',
'Provisioned deployment infrastructure using Terraform and Ansible and maintained environment configuration for Kubernetes workloads.',
'Used Prometheus and Grafana telemetry to assess platform health and investigate issues during production support.',
'Partnered with developers on defect isolation, incident recovery, and post-release reviews.',
'Documented corrective actions and reusable runbooks to reduce recurring support effort and improve release reliability.'
],[
'Built Jenkins and Maven delivery workflows for REST services across test, security-validation, UAT, and production.',
'Coordinated release configuration and deployment readiness with developers, QA, and infrastructure stakeholders.',
'Maintained Helm packages and Kubernetes configuration for repeatable deployment across environments.',
'Automated infrastructure provisioning and configuration with PowerShell, Ansible, and version-controlled definitions.',
'Validated application connectivity, credentials, and environment prerequisites before release execution.',
'Supported production deployment windows, application checks, and issue escalation with engineering teams.',
'Used ELK and cloud monitoring to investigate application and infrastructure failures affecting releases.',
'Documented deployment sequences, recovery procedures, and environment dependencies for operations handoff.',
'Communicated platform priorities and release improvements to distributed stakeholders through technical reviews.'
],[
'Created build and deployment workflows for API, database, and UI components across shared delivery environments.',
'Implemented Git branching practices and release versioning to control code promotion and package traceability.',
'Automated deployment tasks using Python, shell scripts, and Ansible to reduce manual release preparation.',
'Provisioned AWS infrastructure with Terraform and promoted reviewed infrastructure changes through pipelines.',
'Maintained build agents and resolved dependency and execution-environment failures.',
'Managed environment-specific variables and configuration for development, test, and production deployments.',
'Validated release artifacts and prerequisites before controlled environment promotion.',
'Investigated failed deployments with development and support teams and verified corrective actions.',
'Authored deployment guides and operational handoff documentation for application and infrastructure releases.'
]]
for e,b in zip(p['experience'],points):e['impact']=b
p['experience'][0]['skills_used']=['Azure DevOps','Git','AWS','Python','PowerShell','Bash','Terraform','Kubernetes']
p['experience'][1]['skills_used']=['Jenkins','GitLab CI','Git','Linux','Docker','Kubernetes']
p['experience'][2]['skills_used']=['Jenkins','GitHub Actions','AWS','Terraform','PowerShell','CloudWatch']
p['notes']=['Authored build-release branch profile; preserve its content during JD ranking.','Rajendra P N; 10+ years; minimum nine points per role.','ServiceNow, formal ITIL/CAB ownership, Datadog, and banking experience are not asserted without confirmation. Payment-platform experience retained.']
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(p,indent=2)+'\n')
out=Path('tailored_resume/rajendra-prasad-n');out.mkdir(parents=True,exist_ok=True)
(out/'Rajendra-P-N-Release-Deployment.profile.json').write_text(json.dumps(p,indent=2)+'\n')
q=root/'assets/templates/base_resume.html';s=q.read_text().replace('Build, Release & Automation Skills','Release, Deployment & Operations Skills').replace('@media (max-width:900px)','@media screen and (max-width:900px)').replace('@media (max-width:560px)','@media screen and (max-width:560px)');s=s.replace('.job-block{margin-bottom:12px;}','.job-block{margin-bottom:12px;break-inside:auto;page-break-inside:auto;}');q.write_text(s)
