import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(base,'Lead AWS DevOps Engineer CodePipeline CloudFormation GitLab Lambda API Gateway SNS AWS Config Ansible Python Shell')
p.page_title='Rajendra Prasad N - AWS DevOps & Serverless Engineer'
p.headline='Lead AWS DevOps Engineer | GitLab, Serverless & DevSecOps'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in AWS cloud operations, CI/CD, infrastructure automation, and production delivery.</strong> Expertise in <strong>GitLab repository administration, AWS CodePipeline, Lambda, API Gateway, CloudFormation, and Python/Shell automation</strong>. Builds governed backend release workflows, automates frontend environments with Ansible, and integrates security scanning, AWS Config checks, and operational monitoring. Collaborates across large hybrid enterprise development, QA, security, networking, and operations teams. Brings working knowledge of GoCD concepts and mobile test-build distribution, with Healthcare Payer application support experience through Mphasis/HPE.'
p.achievements_title='AWS Serverless & Enterprise Delivery Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Serverless Delivery','Automated backend REST API releases using CodePipeline, Lambda, API Gateway, versioned infrastructure, and deployment health checks.'),
('GitLab & DevSecOps','Governed repositories, runners, merge workflows, security gates, and environment approvals to support traceable production releases.'),
('Enterprise Operations','Connected compliance evaluation, application telemetry, release coordination, and recovery runbooks across hybrid delivery teams.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('AWS Backend & Serverless','Lambda, API Gateway REST APIs, SNS, IAM, S3, CloudWatch, Secrets Manager, KMS, VPC integration'),
('CI/CD & GitLab','AWS CodePipeline, CodeBuild, CodeDeploy, GitLab CI/CD, repositories, runners, merge requests, protected branches, Jenkins; GoCD concepts'),
('Infrastructure as Code','AWS CloudFormation, AWS SAM, AWS CDK (Python), Terraform, change sets, stack parameters, reusable serverless infrastructure'),
('DevSecOps & Compliance','AWS Config rules, conformance packs, remediation workflows, SAST, dependency and secrets scanning, least privilege, pipeline quality gates'),
('Configuration & Scripting','Ansible, Python, Shell/Bash, Linux, AWS CLI, JSON, YAML, frontend provisioning, application configuration, deployment validation'),
('Monitoring & Alerting','AWS CloudWatch, Sumo Logic, Dynatrace, logs, metrics, traces, dashboards, SNS notifications, API latency, Lambda errors and throttling'),
('Enterprise Platforms','Hybrid cloud, EC2, VPC, VPN, DNS, load balancing, Docker, Kubernetes, Helm, controlled environment promotion'),
('Collaboration & Mobile','Agile, developer/QA collaboration, release readiness; Firebase App Distribution and TestFlight familiarity; Healthcare Payer application support')]]
specs=[
(['AWS','GitLab','CodePipeline','Lambda','API Gateway','CloudFormation','AWS CDK','SNS','AWS Config','Python','Ansible'],[
'Led AWS DevOps delivery within large hybrid enterprise teams, coordinating backend and frontend releases across developers, QA, security, networking, and production operations.',
'Administered GitLab projects, groups, repository permissions, protected branches, merge approvals, runners, and reusable CI/CD templates to standardize code governance and release execution.',
'Designed AWS CodePipeline workflows for backend services, integrating source changes, CodeBuild tests, security scans, versioned artifacts, approvals, and deployment validation.',
'Deployed backend REST APIs through API Gateway and Lambda, managing stages, function versions, aliases, execution roles, environment settings, and application secrets.',
'Defined serverless infrastructure using CloudFormation, AWS SAM, and Python-based AWS CDK constructs; reviewed synthesized templates and change sets before promoting environment-specific stacks.',
'Implemented gradual Lambda releases using aliases and deployment health alarms; validated API smoke tests and rollback paths before routing production traffic to new versions.',
'Integrated backend event notifications with SNS topics and subscriptions, configuring access policies, delivery-failure visibility, and alarm notifications for application and operations teams.',
'Embedded SAST, dependency, secrets, and infrastructure checks into delivery workflows; enforced quality thresholds, protected approvals, and traceable exceptions before deployment.',
'Configured AWS Config rules and conformance packs to evaluate resource settings, report noncompliance, and trigger controlled remediation workflows with revalidation and audit evidence.',
'Automated frontend service infrastructure and Linux configuration with Ansible roles for packages, web-server settings, application directories, certificates, service startup, and endpoint validation.',
'Implemented CloudWatch, Sumo Logic, and Dynatrace monitoring for backend health, correlating API latency, Lambda errors, throttling, logs, and traces with deployment events.',
'Developed Python and Shell utilities for release orchestration, API checks, configuration comparison, artifact validation, and incident diagnostics; used retrospectives to improve delivery workflows.'
]),
(['AWS','GitLab CI/CD','Jenkins','Ansible','Python','Shell','Linux','DevSecOps'],[
'Built GitLab CI/CD templates for application builds, tests, artifact publication, environment approvals, deployments, and post-release validation.',
'Managed Git repositories, branching policies, merge requests, protected variables, and runner pools to improve repository consistency and pipeline reliability.',
'Automated Linux and frontend runtime configuration with Ansible, Python, and Shell scripts, separating environment values and secrets from release packages.',
'Integrated code analysis, dependency checks, and deployment permissions into pipelines and worked with QA to resolve failed quality gates.',
'Troubleshot build-agent, credential, network, container, and application deployment issues across enterprise environments.',
'Coordinated release readiness, smoke-test evidence, defect follow-up, and operational handover with developers and support teams.'
]),
(['AWS','CloudFormation','Terraform','GitHub Actions','Jenkins','Python','CloudWatch','Docker'],[
'Provisioned AWS environments with CloudFormation and Terraform, maintaining reviewed infrastructure changes, environment parameters, and reusable resource definitions.',
'Built CI/CD workflows using GitHub Actions and Jenkins for repeatable builds, tests, artifact publication, and controlled application promotion.',
'Supported AWS application infrastructure spanning compute, IAM, networking, load balancing, storage, and monitoring for distributed engineering teams.',
'Developed Python and Shell automation for environment checks, AWS API operations, deployment diagnostics, and recovery procedures.',
'Deployed containerized services with Docker, Kubernetes, and Helm, validating runtime configuration, service health, and rollback options.',
'Implemented CloudWatch dashboards, logging, alarms, backup, and disaster-recovery checks to support incident response and service restoration.',
'Partnered with development, QA, network, and operations teams to resolve connectivity and deployment failures and document release dependencies.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=base.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
prior=json.loads(Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-devops-cloud-devsecops-aggressive.profile.json').read_text())
for i in [3,4,5]:
 p.experience[i].title=prior['experience'][i]['title']
 p.experience[i].skills_used=prior['experience'][i]['skills_used']
 p.experience[i].impact=prior['experience'][i]['impact']
p.skills=['AWS','GitLab','CodePipeline','Lambda','API Gateway','AWS CDK','CloudFormation','SNS','DevSecOps','AWS Config','Ansible','CloudWatch','Sumo Logic','Dynatrace','Python','Shell','GoCD','Firebase App Distribution','TestFlight']
p.notes=['Aggressive serverless JD variant. GoCD and mobile distribution are familiarity-level skills, not project ownership claims. Preserves employment history, certifications and Healthcare Payer context.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-aws-serverless-gitlab-devops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
jd='''Bachelor degree in Computer Science, Information Systems or related field. Minimum 8 years DevOps with AWS and CI/CD; large hybrid enterprise IT teams. GoCD or similar CI/CD tools. Strong GitLab repository and pipeline management. Backend CI/CD with AWS CodePipeline; REST API deployment with Lambda and API Gateway; serverless IaC with AWS CDK or CloudFormation; SNS integration and monitoring. DevSecOps security and compliance checks throughout pipelines. AWS Config resource compliance. Frontend infrastructure automation with Ansible. CloudWatch, Sumo Logic and Dynatrace monitoring. Collaboration with developers, QA and engineers. Python and Shell scripting. Knowledge of mobile testing distribution platforms.'''
stem.with_suffix('.jd.txt').write_text(jd)
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html','https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html','https://docs.gocd.org/current/introduction/concepts_in_go.html','https://firebase.google.com/docs/app-distribution']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
