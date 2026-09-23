import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform GHEC Jenkins JBoss WebLogic Python Shell')
p.headline='Lead DevOps Engineer | Azure, Independent Contributor'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in CI/CD, application deployments, middleware operations, and production support.</strong> Designs and administers <strong>GitHub Actions YAML workflows, GitHub Enterprise Cloud (GHEC), Jenkins, and Azure DevOps</strong> delivery platforms. Hands-on focus on <strong>JBoss EAP 7.4/8.1 and WebLogic 12c/14c</strong> configuration, administration, maintenance, and automated releases. Uses Unix/Linux, Bash, Python, PowerShell, and Ansible to standardize environments, troubleshoot application-server issues, and coordinate reliable production changes across development, QA, and operations teams.'
p.achievements_title='Workflow Automation & Middleware Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('GitHub Actions & GHEC','Reusable YAML workflows, runner governance, protected environments, and versioned artifacts standardize enterprise delivery.'),
('Middleware Operations','JBoss and WebLogic configuration, deployment automation, patch planning, and JVM diagnostics support stable application services.'),
('Release Reliability','Approval gates, health checks, recovery procedures, and cross-team coordination connect automated pipelines to production readiness.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('GitHub Actions & YAML','Reusable workflows, workflow_call, workflow_dispatch, composite actions, job dependencies, matrices, concurrency, caching, artifacts, workflow troubleshooting'),
('GitHub Enterprise Cloud','GHEC, organizations, teams, repository access, branch protection, CODEOWNERS, runner groups, Actions policies, environments, OIDC, secrets and variables'),
('CI/CD & Azure DevOps','Jenkins, Jenkinsfiles, shared libraries, Azure Pipelines, YAML templates, agent pools, service connections, Azure Artifacts, approvals and release promotion'),
('JBoss Administration','JBoss EAP 7.4 / 8.1, standalone and managed domains, management CLI, profiles, server groups, JDBC datasources, Elytron, WAR/EAR deployment, patching'),
('WebLogic Administration','WebLogic 12c / 14c, domains, Admin/Managed Servers, Node Manager, clusters, JDBC/JMS resources, WLST, deployment plans, patch maintenance'),
('Scripting & Platforms','Unix, Linux, Windows, Shell/Bash, Python, PowerShell, Ansible, Maven, Git, JSON, Azure VMs, Key Vault, Terraform, Docker, AKS'),
('Troubleshooting & Security','JVM heap and GC analysis, thread dumps, connection pools, SSL/TLS, logs, SonarQube, dependency scans, least privilege, Azure Monitor, Splunk'),
('Release Management & Operations','Change approvals, release calendars, cutover runbooks, smoke tests, rollback, incident response, root-cause analysis; Healthcare Payer application support')]]
specs=[
(['GitHub Actions','GHEC','Azure DevOps','Jenkins','JBoss EAP 7.4/8.1','WebLogic 12c/14c','Bash','Python','Ansible'],[
'Led GitHub Actions and Azure DevOps delivery automation for enterprise applications, aligning repository workflows, middleware deployments, and production change controls with engineering teams.',
'Designed reusable YAML workflows with workflow_call, typed inputs, explicit secrets, outputs, and versioned references so application teams could adopt shared build and deployment patterns.',
'Created composite actions for repeated setup and validation steps; configured job dependencies, conditional execution, matrix builds, timeouts, and concurrency controls for predictable pipeline behavior.',
'Implemented pull-request, branch, tag, scheduled, and manual triggers; standardized dependency caching, test-result publication, build summaries, artifact retention, and release-package checksums.',
'Administered GHEC organizations, teams, repository access, CODEOWNERS, protected branches, and Actions policies; applied least-privilege workflow tokens and reviewed third-party action references.',
'Managed self-hosted Linux and Windows runners, runner groups, labels, toolchains, proxy access, workspace cleanup, and capacity monitoring; isolated privileged deployment workloads.',
'Configured protected deployment environments, reviewer approvals, scoped variables and secrets, and GitHub-to-Azure OIDC federation to support controlled cloud access and production promotion.',
'Migrated Jenkins and ADO delivery stages into reusable GitHub Actions workflows, validating build parity, artifact naming, approval behavior, deployment checks, and recovery procedures.',
'Installed and administered JBoss EAP 7.4 and 8.1 in standalone and managed-domain modes, maintaining profiles, server groups, JVM settings, socket bindings, and environment-specific configuration.',
'Configured JBoss JDBC drivers and datasources, pool validation, Elytron security, TLS, and logging; diagnosed connection failures, classloading issues, memory pressure, and application startup errors.',
'Automated JBoss WAR/EAR deployments with management CLI, Ansible, and pipeline jobs, coordinating traffic draining, staged restarts, health verification, and restoration of prior application versions.',
'Planned JBoss maintenance and 7.4-to-8.1 migration activities with developers, assessing JDK and Jakarta compatibility, configuration changes, extension dependencies, and regression-test readiness.',
'Supported WebLogic 12c/14c domains, Admin/Managed Servers, Node Manager, clusters, JDBC/JMS resources, and WLST deployments; coordinated patches, configuration backups, and recovery checks.',
'Developed Bash, Python, and PowerShell diagnostics for release validation and incident response; led change reviews and troubleshooting using logs, thread dumps, GC behavior, and service-health evidence.'
]),
(['Azure DevOps','GitHub Actions','GHEC','Jenkins','Linux','Python','Ansible','JBoss'],[
'Built GitHub Actions and ADO YAML templates for Maven builds, automated tests, quality analysis, artifact publication, and controlled deployment stages.',
'Configured reusable workflow inputs, repository variables, deployment secrets, and approval gates to separate development, test, and production delivery.',
'Supported GHEC repository onboarding, branch protections, pull-request checks, and runner access with application teams.',
'Maintained Linux and Windows build agents and investigated checkout, dependency, permissions, network, and workflow-expression failures.',
'Automated JBoss application configuration and deployments with Ansible and shell scripts, validating datasources, service startup, and endpoint health.',
'Partnered with developers and QA on release readiness, failed-build analysis, smoke tests, and documented rollback procedures.'
]),
(['Azure','GitHub Actions','Jenkins','Python','PowerShell','JBoss EAP 7.4','WebLogic 14c'],[
'Developed GitHub Actions workflows for application builds, infrastructure validation, artifact publication, and approved multi-environment deployments.',
'Standardized job dependencies, reusable build steps, caching, and automated status reporting to improve workflow consistency across repositories.',
'Automated Azure environment configuration and operational checks with Terraform, Ansible, PowerShell, and Python.',
'Supported JBoss EAP 7.4 and WebLogic 14c releases, maintaining application settings, JDBC connectivity, deployment packages, and service verification.',
'Troubleshot Unix/Linux process failures, JVM resource pressure, certificate issues, and middleware connectivity using logs and diagnostic scripts.',
'Maintained release runbooks, backup checks, and recovery procedures and coordinated deployment windows with distributed engineering teams.'
]),
(['Azure','GitHub Actions','Jenkins','Python','Bash','Ansible','Prometheus','Grafana'],[
'Standardized GitHub Actions and Jenkins workflows for application and infrastructure delivery using shared build, test, and deployment patterns.',
'Built Jenkins shared libraries for artifact versioning, package publication, environment selection, and repeatable release execution.',
'Developed Python FastAPI integrations across Jenkins, Jira, and JFrog for project onboarding, deployment status, and operational requests.',
'Automated Linux service configuration and monitoring-stack deployment with Ansible, shell scripts, Prometheus, and Grafana.',
'Investigated production application and pipeline incidents, correlating logs and resource metrics with recent releases and coordinating service restoration.',
'Worked with developers and support teams on change readiness, rollback decisions, runbook improvements, and post-incident reviews.'
]),
(['Azure','Jenkins','Git','Ansible','Shell','WebLogic 12c','JBoss','Maven'],[
'Built Jenkins pipelines for Java applications and REST services across development, test, UAT, and production environments.',
'Administered JBoss and WebLogic 12c application configurations, managing JVM options, JDBC resources, service accounts, and environment properties.',
'Automated Maven package promotion and WAR/EAR deployment through Ansible, shell scripts, management CLI, and controlled release procedures.',
'Supported middleware maintenance through configuration backups, patch prechecks, service restarts, and post-change application validation.',
'Diagnosed deployment failures, blocked threads, database connection errors, TLS problems, and Unix permissions with development and infrastructure teams.',
'Coordinated release plans, change approvals, customer updates, and rollback readiness across distributed application teams.'
]),
(['Azure','Jenkins','Git','Ansible','Linux','Shell','Python','JBoss','Healthcare Payer'],[
'Supported Healthcare Payer enrollment, eligibility, and claims application deployments in the Mphasis/HPE engagement using repeatable release procedures.',
'Created Ansible and shell automation for application installation, JBoss configuration updates, service controls, and deployment verification.',
'Maintained Linux application servers and supported JBoss package deployments, datasource connectivity checks, log inspection, and batch-job troubleshooting.',
'Managed Git branching, release tags, and versioned artifacts and documented deployment sequencing for application, API, database, and UI components.',
'Worked with development, QA, and support teams on release windows, smoke tests, incident follow-up, and operational handover.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['GitHub Actions','YAML','GitHub Enterprise Cloud','GHEC','Jenkins','Azure DevOps','Unix','Shell','Bash','Python','PowerShell','WebLogic','JBoss','Ansible','release management']
p.notes=['Aggressive GitHub Actions and middleware variant; modern JBoss versions are concentrated in recent roles. Preserves Multi-Cloud header and updated email.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-github-actions-jboss-devops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text('GitHub Actions & YAML workflows; Jenkins / CI-CD; Unix / Shell / Bash; Python or PowerShell; GitHub Enterprise Cloud (GHEC); WebLogic 12c/14c; JBoss 7.4/8.1 strong plus; DevOps automation and deployment; production troubleshooting and release management; Azure nice to have. Expand GitHub Actions workflow responsibilities and JBoss configuration, administration, maintenance and deployments. Include regular DevOps with Azure DevOps.')
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments','https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/secure-your-work/security-harden-deployments/oidc-with-reusable-workflows','https://docs.redhat.com/en/documentation/red_hat_jboss_enterprise_application_platform/8.1/html-single/configuration_guide/index','https://docs.oracle.com/en/middleware/standalone/weblogic-server/14.1.1.0/nodem/']}
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
