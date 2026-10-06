import json,shutil
from pathlib import Path
root=Path('tmp/jenkins-sre/plugin');shutil.copytree('plugins/resume-creator-plugin/assets',root/'assets',dirs_exist_ok=True)
d=json.loads(Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json').read_text())
d['headline']='Senior Site Reliability Engineer | Jenkins | Production Operations'
d['page_title']='Rajendra P N - Senior DevOps / SRE Engineer'
d['summary_html']='<strong>Senior DevOps / Site Reliability Engineer with 10+ years of experience in enterprise application delivery and production operations.</strong> Specializes in <strong>Jenkins CI/CD, application observability, on-call support, incident management, troubleshooting, and root cause analysis</strong>. Builds reusable pipelines and operational tooling with Groovy, Python, Bash, and PowerShell; investigates application and infrastructure failures across Linux, containers, and Azure/AWS environments. Partners with developers and infrastructure teams to improve release readiness, reduce recurring operational work, and maintain reliable services.'
d['achievements_title']='Site Reliability & Jenkins Delivery Highlights'
d['achievements']=[{'tag':'Jenkins Engineering','text':'Standardized Jenkinsfiles, shared libraries, build agents, test gates, and artifact promotion for repeatable application deployments.'},{'tag':'Production Reliability','text':'Correlated application logs and platform metrics during incidents; maintained actionable alerts, recovery procedures, and root cause follow-up.'},{'tag':'Operational Automation','text':'Developed Python integrations and scripting utilities for onboarding, deployment checks, diagnostics, and recurring support tasks.'}]
d['skills']=['Jenkins','CloudBees Jenkins','CI/CD','Site Reliability Engineering','Production Support','On-Call','Incident Management','Root Cause Analysis','Prometheus','Grafana','ELK','Python','Bash','PowerShell','Groovy']
d['skill_sections']=[{'title':'Jenkins & CI/CD','content':'Jenkinsfiles, Declarative Pipeline, Groovy shared libraries, multibranch jobs, agent administration, credentials binding, build/test stages, artifact promotion, deployment gates, rollback'}, {'title':'Production Support & Incident Response','content':'On-call rotations, alert triage, incident management, service restoration, escalation, root cause analysis, post-incident actions, operational readiness, recovery runbooks'}, {'title':'Observability, Logging & Alerting','content':'Prometheus, Grafana, ELK, Azure Monitor, Log Analytics, Application Insights, CloudWatch, application health, latency/error monitoring, dashboards, actionable alerts'}, {'title':'Programming & Debugging','content':'Python, Bash, PowerShell, Groovy, REST APIs, FastAPI, Java/Maven build diagnostics, SQL checks, code review, automated tests, application log and stack-trace analysis'}, {'title':'Enterprise Application Operations','content':'Linux services, processes, permissions, resource diagnostics, DNS/TLS/connectivity, Docker, Kubernetes, deployment validation, database dependencies, capacity troubleshooting'}, {'title':'Cloud & Release Reliability','content':'Azure/AWS, Terraform, configuration management, Key Vault/IAM, secure pipeline credentials, SonarQube, JFrog Artifactory/Xray, release evidence, development/infrastructure collaboration'}]
bullets=[[
'Built Jenkins CI/CD pipelines with versioned Jenkinsfiles and Groovy shared libraries for application builds, automated tests, artifact publication, and controlled production releases.',
'Administered Jenkins agents, credentials, job configuration, and tool dependencies; resolved queue delays, workspace failures, and unreliable build execution.',
'Implemented application health dashboards and alerts with Azure Monitor, Application Insights, Prometheus, and Grafana, correlating latency, errors, and resource utilization.',
'Participated in on-call rotations, triaging alerts and coordinating incident escalation, mitigation, and recovery verification with development and infrastructure teams.',
'Performed root cause analysis using application logs, stack traces, deployment history, and Linux diagnostics; tracked corrective actions to address recurring failures.',
'Developed Python, Bash, and PowerShell utilities for health checks, deployment validation, and diagnostic collection; reviewed and tested automation before production use.',
'Added Jenkins release gates for test results, vulnerability checks, configuration validation, and rollback readiness, improving operational handoff to support teams.',
'Supported Azure/AWS application environments, diagnosing Kubernetes, networking, identity, and database-connectivity issues during production incidents.',
'Maintained recovery runbooks and support handoffs; coached engineers on Jenkins troubleshooting and incident analysis while coordinating release readiness.'
],[
'Created Jenkins pipelines for compilation, automated tests, package publication, and deployment approvals across development, QA, and production.',
'Maintained Jenkins Linux/Windows agents and build tooling; debugged dependency, credential, disk-capacity, and connectivity failures affecting delivery.',
'Supported enterprise application releases with health checks, environment validation, and rollback procedures before and after production deployment.',
'Participated in on-call support, assessing incident impact, escalating application failures, and verifying service restoration with engineering teams.',
'Configured application dashboards and alert rules using Azure Monitor and CloudWatch; correlated error logs with infrastructure events during investigations.',
'Debugged Jenkinsfile and script failures with Groovy, Bash, and PowerShell; validated fixes through test jobs and reviewed source changes.',
'Performed root cause reviews for failed releases and production issues, documenting evidence and preventive fixes with development and infrastructure owners.',
'Maintained Azure/AWS environment parameters and protected pipeline credentials, troubleshooting deployment permissions and runtime connectivity.',
'Published Jenkins onboarding and production-support runbooks, standardizing escalation paths, release checks, and operational handoffs.'
],[
'Built and supported Jenkins CI/CD workflows for application and infrastructure changes, incorporating tests, artifact versioning, and deployment verification.',
'Developed reusable Jenkins stages and Groovy helpers for environment configuration and release checks; investigated agent and pipeline failures.',
'Monitored service health with Azure Monitor, Log Analytics, Prometheus/Grafana, and CloudWatch; tuned alert thresholds against observed application behavior.',
'Participated in production on-call support, diagnosing application errors, deployment regressions, and network failures with developers and platform teams.',
'Correlated logs, metrics, configuration changes, and release history to identify root causes; documented corrective actions and verified recovery.',
'Wrote Python and PowerShell tools for API health checks, log collection, and recurring support tasks; debugged scripts and validated error handling.',
'Supported containerized applications on Azure AKS and AWS EKS, investigating restart loops, readiness failures, and CPU/memory pressure.',
'Maintained release readiness checks for configuration, identity, and database dependencies; verified rollback plans and post-deployment application behavior.',
'Updated incident playbooks and troubleshooting documentation; shared operational findings to improve deployment practices and service reliability.'
],[
'Administered CloudBees Jenkins and developed shared libraries for SaaS and payment-platform CI/CD, standardizing build, test, package, and release stages.',
'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog to automate onboarding, release coordination, and recurring operational workflows.',
'Integrated SonarQube, JFrog Artifactory, and Xray into Jenkins delivery, validating code quality, artifact versions, and security results before promotion.',
'Participated in on-call rotations for SaaS workloads, managing incident triage, escalation, recovery actions, and verified handoff to support teams.',
'Used Prometheus/Grafana and CloudWatch dashboards to monitor application health, investigate errors, and identify Kubernetes resource constraints.',
'Performed root cause analysis across application logs, Jenkins outputs, and infrastructure changes; partnered with developers on fixes and regression checks.',
'Automated Linux diagnostics and recovery tasks with Bash, Python, and Ansible, reducing repetitive production-support work.',
'Supported Azure/AWS application and database dependencies, validating connectivity, environment configuration, and release recovery procedures.',
'Maintained production-readiness checklists, incident runbooks, and release evidence; aligned engineering and infrastructure teams on operational improvements.'
],[
'Built Jenkins and Maven pipelines for Java REST microservices with automated tests, security validation, and gated UAT/production promotion.',
'Maintained Jenkins job configuration, agents, credentials, and deployment scripts; investigated failed builds and application-release errors.',
'Monitored application health using ELK, Azure Monitor, Log Analytics, and CloudWatch; correlated logs and alerts with recent deployment changes.',
'Provided on-call production support, triaging incidents, coordinating escalation, and validating restored application functionality.',
'Investigated Java application logs, stack traces, Linux services, and network connectivity to identify root causes with development teams.',
'Developed Bash and PowerShell automation for environment checks and deployment diagnostics; tested fixes to scripts and Jenkins pipeline logic.',
'Supported Azure/AWS infrastructure and Kubernetes-hosted services, resolving configuration, permission, and database-connectivity failures.',
'Validated artifacts, deployment parameters, health checks, and rollback steps before release; captured post-deployment verification evidence.',
'Documented incident findings, recovery procedures, and Jenkins troubleshooting guidance to improve operational readiness and team handoffs.'
],[
'Created Jenkins build and deployment pipelines for API, database, and UI components, promoting versioned artifacts across environments.',
'Configured Jenkins jobs, Git integration, and build agents; diagnosed compilation, dependency, credential, and deployment failures.',
'Developed Python, Bash, and PowerShell scripts for deployment checks and administration tasks; debugged failures and verified corrective changes.',
'Monitored application logs and Azure/AWS infrastructure telemetry, using CloudWatch and operational dashboards to investigate service degradation.',
'Participated in on-call production support, assessing alerts, escalating incidents, and coordinating recovery with development and infrastructure teams.',
'Performed root cause investigations using build logs, configuration comparisons, and Linux diagnostics; documented fixes and follow-up actions.',
'Supported Azure/AWS application environments, validating infrastructure readiness, access permissions, and database connectivity before releases.',
'Added Jenkins artifact validation and post-deployment checks, confirming application health and required configuration during environment promotion.',
'Maintained production-support runbooks and release handover records, preserving troubleshooting steps, recovery actions, and verification results.'
]]
for j,b in zip(d['experience'],bullets):
 j['impact']=b
 j['skills_used']=['Jenkins','CI/CD','Production Support','On-Call','Observability','Python/Bash','Azure/AWS']
d['notes']=['Aggressive SRE-specific variant. Every project emphasizes Jenkins, production support, observability, on-call incidents, RCA, scripting/debugging, and operational readiness.']
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(d,indent=2)+'\n')
Path('tmp/jenkins-sre/jd.txt').write_text('''DevOps SRE Engineer Jenkins CI CD Production Operations
We are seeking a hands-on DevOps/SRE Engineer to support enterprise application environments, CI/CD pipelines, and production operations.
Build and support CI/CD pipelines, with strong Jenkins experience.
Monitor application health and improve observability, logging, and alerting.
Participate in on-call rotations, incident management, troubleshooting, and root-cause analysis.
Support production environments and help drive operational readiness.
Apply software engineering concepts and perform some coding/debugging as needed.
Collaborate with development and infrastructure teams to improve reliability and deployment processes.
Strong DevOps/SRE experience. Hands-on Jenkins/CI-CD experience. Production support, incident management, and on-call experience. Observability/monitoring experience. Some programming/software engineering experience.
Strictly create SRE resume with major focus on these skills and roles, including Jenkins points in all projects.
''')
assert all(len(j['impact'])==9 and sum('Jenkins' in b for b in j['impact'])>=2 for j in d['experience'])
