import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(base,'Lead AWS DevOps Engineer CodePipeline CloudFormation Terraform Kubernetes DevSecOps monitoring observability reliability')
p.page_title='Rajendra Prasad N - Lead DevOps & Cloud Engineer'
p.headline='Lead DevOps & Cloud Engineer | IaC, DevSecOps & Kubernetes'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience building cloud infrastructure, automating software delivery, and supporting reliable production platforms.</strong> Hands-on expertise in <strong>AWS, Terraform, CloudFormation, CI/CD, Ansible, Kubernetes, and DevSecOps</strong>. Integrates security scanning, policy validation, quality gates, and operational telemetry into application and infrastructure delivery. Partners with developers to improve release readiness, troubleshoot distributed systems, and strengthen high availability, backup recovery, and deployment resilience. Additional Healthcare Payer application support experience through the Mphasis/HPE engagement.'
p.achievements_title='Cloud Engineering & Delivery Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Delivery Automation','Reusable CI/CD pipelines and infrastructure modules standardize environment provisioning, artifact promotion, and deployment validation.'),
('DevSecOps','Security scanning, configuration checks, protected approvals, and traceable release evidence embed controls throughout software delivery.'),
('Reliability','Application telemetry, actionable alerts, recovery runbooks, and tested rollback procedures support dependable production operations.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('CI/CD & Deployment','Jenkins, GitLab CI/CD, GitHub Actions, CodePipeline, CodeBuild, CodeDeploy, reusable pipelines, quality gates, release approvals, rollback'),
('Infrastructure as Code','Terraform modules, CloudFormation templates and change sets, remote state, plan review, drift detection, environment provisioning'),
('AWS & Cloud-Native Platforms','EC2, EKS, ECR, VPC, IAM, ALB/NLB, Auto Scaling, S3, RDS, Route 53, Secrets Manager, Systems Manager'),
('Kubernetes & Containers','Docker, Kubernetes, EKS, Helm, ArgoCD, readiness probes, resource limits, autoscaling, disruption budgets, rolling deployments'),
('DevSecOps & Compliance Automation','SonarQube, Fortify, Black Duck, SAST, SCA, image and secrets scanning, IaC policy checks, least privilege, approval evidence'),
('Configuration & Automation','Ansible roles and playbooks, Linux, Bash, Python, PowerShell, AWS CLI, YAML, JSON, configuration templates, service management'),
('Observability & Reliability','CloudWatch, Prometheus, Grafana, Splunk, ELK, metrics, logging, alerting, SLOs, root-cause analysis, multi-AZ availability, disaster recovery'),
('Release & Domain Experience','Change management, artifact promotion, smoke tests, recovery drills, developer collaboration; Healthcare Payer enrollment, eligibility and claims services')]]
specs=[
(['AWS','Terraform','CloudFormation','GitLab CI/CD','Jenkins','EKS','Ansible','CloudWatch','DevSecOps'],[
'Led cloud platform and CI/CD engineering, partnering with developers, security, and operations teams to standardize application delivery and improve production readiness.',
'Designed reusable Jenkins and GitLab pipelines for build, automated testing, security checks, artifact publication, environment promotion, deployment, and rollback verification.',
'Engineered Terraform modules and CloudFormation templates for AWS compute, networking, IAM, storage, EKS, and monitoring; enforced version control, reviewed plans, and environment-specific inputs.',
'Automated infrastructure provisioning and Linux configuration with Ansible, Bash, and Python, coordinating package installation, secrets retrieval, service startup, and post-provisioning validation.',
'Integrated SAST, dependency, container-image, and secrets scanning into CI/CD; configured severity-based quality gates and tracked approved exceptions through remediation.',
'Automated infrastructure policy checks for encryption, public exposure, IAM permissions, and resource tagging; retained scan results and approval records as release evidence.',
'Delivered containerized services to EKS using Helm and GitOps workflows, managing readiness checks, resource requests and limits, autoscaling, and controlled rollout settings.',
'Strengthened Kubernetes maintenance resilience with replica placement and disruption budgets; validated node-drain behavior separately from application rollout controls.',
'Implemented CloudWatch, Prometheus, Grafana, and centralized logging dashboards to correlate deployment events with latency, errors, saturation, and infrastructure health.',
'Established service health checks and actionable alerts with development teams; used SLO-oriented reviews to prioritize recurring failures and operational improvements.',
'Designed multi-AZ deployment patterns and backup recovery procedures; exercised restoration and failover runbooks against agreed recovery objectives and documented recovery gaps.',
'Troubleshot pipeline, Terraform state, IAM, DNS, network, and Kubernetes failures; converted root-cause findings into reusable automation, preventive checks, and support runbooks.'
]),
(['AWS','Terraform','GitLab CI/CD','Ansible','Linux','Docker','Kubernetes','DevSecOps'],[
'Built reusable CI/CD templates for application and infrastructure releases, integrating automated tests, artifact versioning, approvals, and smoke-test stages.',
'Automated cloud environment setup with Terraform and Ansible, standardizing configuration inputs, runtime prerequisites, and deployment credentials.',
'Administered Linux build agents and container runners, resolving toolchain, cache, permission, dependency, and resource-capacity issues.',
'Embedded code-quality, dependency, and image checks into delivery pipelines and enforced protected branches and controlled production access.',
'Deployed Docker and Kubernetes workloads with versioned manifests, configuration separation, readiness probes, and rollout verification.',
'Partnered with development and QA teams to investigate release failures, refine validation checks, and maintain tested rollback and support procedures.'
]),
(['AWS','Terraform','CloudFormation','EKS','GitHub Actions','Ansible','CloudWatch'],[
'Provisioned AWS environments through Terraform modules and CloudFormation templates, using change reviews, consistent tagging, and repeatable deployment parameters.',
'Implemented GitHub Actions and Jenkins workflows for application builds, automated tests, artifact publication, and multi-environment release promotion.',
'Deployed Kubernetes microservices with Docker, Helm, and ArgoCD, validating service readiness, configuration changes, and recovery options before cutover.',
'Automated Linux configuration and operational checks with Ansible, Python, and shell scripts to reduce environment drift and repeated manual setup.',
'Implemented IAM, VPC, security-group, and load-balancer configurations that supported private application communication and controlled operational access.',
'Built CloudWatch dashboards and alarms for application and infrastructure health; investigated capacity, network, container, and deployment failures.',
'Supported AWS Backup and disaster-recovery workflows, validating restored resources, application connectivity, and documented recovery sequences.'
]),
(['AWS','Jenkins','Terraform','Ansible','Kubernetes','Prometheus','Grafana','Python'],[
'Designed CI/CD pipelines and Terraform automation for AWS application and infrastructure delivery with repeatable validation and deployment stages.',
'Built Jenkins shared libraries for image versioning, artifact publication, deployment automation, and consistent promotion across environments.',
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray, integrating dependency and artifact checks into enterprise delivery workflows.',
'Developed Ansible roles for highly available Prometheus, Grafana, and Node Exporter monitoring stacks, including configuration templates and service verification.',
'Created Python Prometheus exporters and dashboards to expose application-specific health signals and improve incident diagnosis.',
'Developed internal FastAPI integrations across Jenkins, Jira, and JFrog to automate project onboarding and recurring operational tasks.',
'Supported production releases and incident response using health checks, log analysis, rollback decisions, and post-incident reviews with development teams.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=base.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
prior=json.loads(Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-aws-devops-ansible-release-aggressive.profile.json').read_text())
for i in [4,5]:
 p.experience[i].title=prior['experience'][i]['title']
 p.experience[i].skills_used=prior['experience'][i]['skills_used']
 p.experience[i].impact=prior['experience'][i]['impact']
p.skills=['CI/CD','Terraform','CloudFormation','DevSecOps','Kubernetes','Ansible','AWS','Observability','High Availability','Disaster Recovery']
p.notes=['Aggressive JD-tailored variant. Preserves employment history, certifications, updated contact email, and user-requested Healthcare Payer context.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-devops-cloud-devsecops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
jd='''DevOps Engineer: build and maintain modern cloud infrastructure, automate software delivery, strengthen DevSecOps, and improve application reliability.
Design CI/CD for automated build, testing, release and deployment. Implement IaC with Terraform and CloudFormation. Automate cloud provisioning, configuration management, environment setup and deployments. Integrate security scanning, compliance validation and quality gates. Support Kubernetes and cloud-native platforms. Implement monitoring, logging, alerting and observability. Partner with development to improve release quality, speed and reliability. Troubleshoot deployment and infrastructure issues. Optimize availability, resilience and disaster recovery.
Core skills: CI/CD; Terraform; CloudFormation; DevSecOps; Kubernetes; containers; cloud-native platforms; configuration management; security and compliance automation; monitoring and observability; logging and alerting; deployment automation; troubleshooting; reliability engineering; high availability and resilience.'''
stem.with_suffix('.jd.txt').write_text(jd)
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://developer.hashicorp.com/terraform/cli/test','https://kubernetes.io/docs/concepts/workloads/pods/disruptions/','https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-13.html']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
