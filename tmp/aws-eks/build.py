import json, sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore, BundledHtmlResumeRenderer, tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
jd='''Senior DevOps Engineer: AWS, production Kubernetes/EKS administration, upgrades, patching, node recycling, Karpenter, Cluster Autoscaler, HPA, VPA, Helm, VPC CNI, ALB, NGINX or Traefik. EC2, VPC, IAM, S3, Route53, RDS, IRSA. GitHub Actions reusable workflows and custom actions, automated testing, Secrets, Environments, deployment keys, variables, AWS OIDC, hosted and self-hosted runners. Terraform or AWS CDK, Python/Bash. ArgoCD or Flux, Docker multi-stage builds, ECR, vulnerability management. Enterprise Kubernetes runners and Actions Runner Controller (ARC). Required: 5+ years DevOps and AWS, 3+ years production EKS and GitHub Actions. Collaboration with software engineering teams and production support.'''
p,_=tailor_profile(base,jd)
p.headline='Senior DevOps Engineer | AWS & EKS'
p.page_title='Rajendra Prasad N - Senior AWS DevOps Engineer'
p.summary_html='<strong>Senior DevOps Engineer with 10+ years of enterprise experience in cloud infrastructure, automation, CI/CD, and production operations.</strong> Builds and supports <strong>AWS and production Kubernetes/EKS platforms</strong> with Terraform, Helm, GitOps, and Python/Bash. Designs reusable <strong>GitHub Actions workflows, AWS OIDC authentication, and Kubernetes-based self-hosted runners using ARC</strong>. Drives cluster lifecycle management, autoscaling, container security, observability, and reliable releases while partnering with software engineering teams on troubleshooting and operational readiness.'
p.achievements_title='AWS, EKS & Delivery Automation Highlights'
p.achievements=[{'tag':t+':','text':v} for t,v in [
('Production EKS','Cluster maintenance, workload scaling, networking, identity controls, and recovery procedures support reliable application delivery.'),
('Secure CI/CD','Reusable workflows, short-lived AWS credentials, protected environments, and isolated runners standardize enterprise releases.'),
('Infrastructure Automation','Terraform, GitOps, and Python/Bash tooling make provisioning and deployment repeatable and reviewable.')]]
p.skill_sections=[{'title':t,'content':v} for t,v in [
('AWS Infrastructure','EC2, VPC, IAM, S3, Route 53, RDS, EKS, ECR, ALB, CloudWatch, CloudTrail, Secrets Manager, multi-AZ architecture'),
('Kubernetes & EKS Operations','Cluster upgrades, patching, node recycling, managed node groups, Karpenter, Cluster Autoscaler, HPA, VPA, PDBs, probes'),
('GitHub Actions & CI/CD','YAML, reusable workflows, composite actions, matrix builds, caching, artifacts, Environments, Secrets, variables, deployment keys, Jenkins'),
('Identity & Runner Platforms','AWS OIDC, IAM trust policies, IRSA, RBAC, self-hosted runners, Actions Runner Controller (ARC), ephemeral runner scale sets'),
('GitOps & Containers','ArgoCD, Helm charts, Docker multi-stage builds, ECR image promotion, Git-based reconciliation, rollout validation and rollback'),
('IaC & Automation','Terraform modules, remote state, reviewed plans, AWS CDK familiarity, Python, Bash, Ansible, AWS CLI, REST APIs'),
('Networking & Security','VPC CNI, AWS Load Balancer Controller, ALB ingress, NGINX, DNS, TLS, security groups, NetworkPolicy, image scanning, SonarQube'),
('Observability & Reliability','CloudWatch, Prometheus, Grafana, Datadog, logs, alerts, capacity planning, incident response, root-cause analysis, runbooks')]]
specs=[
(['AWS','EKS','GitHub Actions','Terraform','Karpenter','ARC','ArgoCD','Python'],[
'Led AWS infrastructure and production EKS operations, partnering with software engineering teams on scalable platform design, secure delivery, release readiness, and incident resolution.',
'Administered EKS cluster upgrades, add-on compatibility checks, AMI patching, and managed node recycling using staged validation, cordon/drain procedures, and disruption budgets.',
'Configured Karpenter NodePools and capacity limits; maintained Cluster Autoscaler for separate managed node groups and tuned HPA with VPA recommendations to balance capacity and workload demand.',
'Developed Helm charts with environment values, probes, resource requests, affinity rules, and disruption budgets; validated manifests and application health before production promotion.',
'Troubleshot VPC CNI IP allocation, CoreDNS, service routing, and ingress failures; configured ALB ingress through AWS Load Balancer Controller, including TLS and target health checks.',
'Provisioned multi-AZ VPC, EC2, EKS, IAM, S3, Route 53, and RDS infrastructure using reusable Terraform modules, reviewed plans, remote state, and controlled environment promotion.',
'Implemented IRSA with service-account-scoped trust policies and least-privilege permissions so Kubernetes workloads could access AWS services using temporary credentials.',
'Designed GitHub Actions YAML pipelines for tests, security scans, Docker builds, ECR publication, and deployment verification; developed reusable workflows and custom composite actions.',
'Configured GitHub-to-AWS OIDC federation with repository and environment restrictions; managed protected Environments, Secrets, variables, approvals, and scoped deployment keys.',
'Operated ARC ephemeral runner scale sets on dedicated EKS build infrastructure, configuring runner groups, images, capacity limits, network access, and controller/runner log retention.',
'Optimized workflow matrix jobs, dependency caching, concurrency controls, artifact retention, and job permissions; diagnosed runner registration, queueing, and build-environment failures.',
'Implemented ArgoCD application delivery from reviewed Git changes, managing Helm values, sync health, drift detection, controlled promotion, and rollback through versioned configuration.',
'Hardened multi-stage Docker images and ECR workflows with minimal runtime layers, non-root execution, vulnerability checks, immutable image references, and remediation gates.',
'Automated EKS health checks and operational reporting with Python/Bash; correlated CloudWatch, Prometheus, and Grafana signals to resolve pod, node, network, and release incidents.'
]),
(['AWS','EKS','GitHub Actions','Terraform','Helm','Python','Bash'],[
'Built reusable GitHub Actions workflows for application builds, automated tests, image publication, and controlled AWS environment deployments.',
'Maintained hosted and self-hosted runners, resolving toolchain, dependency, cache, network, and permission issues that interrupted build and deployment jobs.',
'Automated AWS provisioning through Terraform modules and reviewed plans, separating environment configuration and sensitive values from source code.',
'Supported EKS workloads using Helm, health probes, resource limits, and rollout checks; investigated scheduling, image-pull, application startup, and service connectivity failures.',
'Integrated code and container scans into CI/CD gates and worked with developers and QA on release validation, rollback procedures, and deployment documentation.'
]),
(['AWS','EKS','Terraform','GitHub Actions','ArgoCD','Helm','Prometheus'],[
'Supported production AWS and EKS infrastructure, managing environment configuration, platform maintenance, operational readiness, and application delivery.',
'Built Terraform definitions for VPC networking, IAM, compute, and Kubernetes dependencies with pull-request reviews and pipeline-based provisioning.',
'Maintained GitHub Actions and Jenkins pipelines for Docker builds, test execution, ECR publishing, and Helm-based Kubernetes releases.',
'Supported ArgoCD reconciliation and versioned deployment manifests, diagnosing drift, failed syncs, and rollout issues with application teams.',
'Tuned pod resources and autoscaling, monitored node utilization, and investigated DNS, ingress, storage, and container failures through logs and metrics.',
'Developed Prometheus/Grafana and CloudWatch dashboards and alerts; maintained incident runbooks and coordinated production changes with distributed engineering teams.'
]),
(['AWS','Jenkins','GitHub Actions','Docker','Ansible','Python','Grafana'],[
'Designed Jenkins and GitHub Actions delivery workflows that standardized application builds, automated checks, artifact promotion, and release validation.',
'Developed Python REST integrations for Jenkins, Jira, and JFrog to automate onboarding, deployment reporting, and recurring operational tasks.',
'Automated Linux and monitoring platform configuration using Ansible roles for Prometheus, Grafana, and Node Exporter with repeatable service checks.',
'Supported Docker-based application delivery and AWS infrastructure operations, troubleshooting deployment failures, permissions, connectivity, and resource constraints.',
'Built custom Python exporters, reviewed production alerts, and partnered with developers on capacity analysis, incident reviews, and recovery documentation.'
]),
(['AWS','EC2','Jenkins','Ansible','Linux','Python','Bash'],[
'Supported AWS EC2 and Linux application environments for Mercedes-Benz Research & Development India, coordinating infrastructure changes and production releases.',
'Built Jenkins delivery jobs and Ansible playbooks for installation, configuration, application deployments, and environment validation.',
'Developed Python and Bash automation for service checks, artifact verification, log collection, and recurring maintenance activities.',
'Investigated application, network, permissions, and capacity issues; documented root causes and maintained release and rollback procedures.'
]),
(['AWS','Jenkins','Ansible','Linux','Shell','Healthcare Payer'],[
'Supported Healthcare Payer application releases within Mphasis/HPE, coordinating deployment readiness and operational checks with development, QA, and infrastructure teams.',
'Maintained Jenkins jobs and Ansible deployment tasks for Linux environments, versioned artifacts, configuration updates, and post-release validation.',
'Used AWS CloudWatch and application logs to investigate host, connectivity, batch-processing, and deployment issues across supported environments.',
'Created shell scripts and support runbooks for service validation, log collection, scheduled tasks, incident handovers, and recovery activities.'
])]
for j,(skills,bullets) in zip(p.experience,specs):
 j.skills_used=skills
 j.impact=bullets
for j,b in zip(p.experience,base.experience): j.title=b.title
p.skills=['AWS','EKS','Kubernetes','GitHub Actions','Terraform','Python','Bash','Karpenter','Cluster Autoscaler','HPA','VPA','Helm','IRSA','OIDC','ARC','ArgoCD','Docker','ECR','Ansible','CloudWatch']
p.notes=['Aggressive JD-aligned draft. Expanded responsibilities require candidate review before submission; original employers, dates, education and certifications retained.']
stem=Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-aws-eks-github-actions-aggressive').resolve()
data=json.dumps(asdict(p),indent=2).replace('rajendranelakurthi@gmail.com','rajendran.scm@gmail.com')
stem.with_suffix('.profile.json').write_text(data)
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p).replace('rajendranelakurthi@gmail.com','rajendran.scm@gmail.com')
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.section-title{margin-top:12px}.skills-grid{gap:6px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text(jd)
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html','https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html','https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws','https://docs.github.com/en/actions/how-tos/manage-runners/use-actions-runner-controller/deploy-runner-scale-sets']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
