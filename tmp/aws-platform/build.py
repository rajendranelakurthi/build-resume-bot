from pathlib import Path
exec(Path('tmp/aws-eks/build.py').read_text().split("stem=Path(")[0])
p.headline='Lead DevOps Engineer'
p.page_title='Rajendra Prasad N - AWS DevOps & Cloud Infrastructure'
jd='''Design, implement and maintain scalable cloud infrastructure and DevOps solutions. AWS/Azure, Kubernetes, Docker, Terraform, CI/CD. Jenkins, GitHub Actions, GitLab CI, Azure DevOps. EKS/AKS clusters, Helm, deployments, services, ingress. Terraform and CloudFormation. Prometheus, Grafana, Datadog, CloudWatch, ELK. Python, Bash, PowerShell automation. Cloud security, IAM, secrets management, vulnerability remediation and compliance. Production infrastructure, deployment, networking and performance troubleshooting. Agile collaboration with development, QA, security and architecture. GitOps, Argo CD/Flux, Ansible, cloud-native architecture.'''
p.summary_html='<strong>Lead AWS DevOps Engineer with 10+ years of enterprise experience designing, automating, and supporting scalable cloud infrastructure and production delivery platforms.</strong> AWS-focused expertise with additional <strong>Azure/AKS experience</strong>, combining Kubernetes, Docker, Terraform, CloudFormation, and Ansible with secure CI/CD across Jenkins, GitHub Actions, GitLab CI, and Azure DevOps. Builds GitOps delivery using Argo CD, automates operations with Python/Bash/PowerShell, and establishes observability through Prometheus, Grafana, Datadog, CloudWatch, and ELK. Partners with development, QA, security, and architecture teams on release reliability, vulnerability remediation, and production incident resolution.'
p.achievements_title='Cloud Infrastructure, DevOps & Reliability Highlights'
p.achievements=[{'tag':t+':','text':v} for t,v in [
('Scalable Platforms','Reusable infrastructure modules, resilient Kubernetes deployment patterns, and capacity controls support enterprise application growth.'),
('Delivery Automation','Pipeline templates, GitOps reconciliation, and configuration automation standardize provisioning, testing, and releases.'),
('Secure Operations','Identity controls, vulnerability gates, actionable telemetry, and recovery runbooks strengthen production reliability.')]]
p.skill_sections=[{'title':t,'content':v} for t,v in [
('AWS & Azure Cloud','AWS: EC2, EKS, VPC, IAM, S3, RDS, Route 53, ALB, ECR; Azure: AKS, VMs, VNets, Azure Monitor, Key Vault'),
('Kubernetes & Containers','EKS, AKS, Docker, Helm, Deployments, Services, Ingress, namespaces, RBAC, probes, HPA, node pools, cluster upgrades'),
('CI/CD & Source Control','Jenkins, GitHub Actions, GitLab CI, Azure DevOps, YAML templates, shared libraries, Git, build/test automation, promotion, rollback'),
('Infrastructure & Configuration','Terraform modules and remote state, CloudFormation stacks, Ansible roles/playbooks, configuration drift, reviewed infrastructure plans'),
('GitOps & Cloud-Native Delivery','Argo CD, Helm values, desired-state reconciliation, sync policies, drift detection, microservices, rolling and blue/green deployments'),
('Automation & Scripting','Python, Bash, PowerShell, AWS CLI, Azure CLI, REST APIs, provisioning, operational checks, reporting, deployment tooling'),
('Security & Governance','IAM, IRSA, OIDC, RBAC, KMS, Secrets Manager, Key Vault, TLS, SAST/SCA, image scanning, patching, compliance evidence'),
('Observability & Operations','Prometheus, Grafana, Datadog, CloudWatch, ELK, Azure Monitor, logs/metrics/traces, alerting, RCA, recovery, Agile collaboration')]]
updates=[
(['AWS','Azure','EKS/AKS','Terraform','CI/CD','Argo CD','Ansible'],[
'Led cloud infrastructure and DevOps delivery with AWS as the primary platform, partnering with architecture and application teams on scalability, security, release readiness, and production support.',
'Designed reusable Terraform modules and CloudFormation stacks for VPC, compute, IAM, storage, databases, and EKS dependencies with versioned inputs and reviewed infrastructure changes.',
'Administered production EKS and AKS clusters, planning upgrades, patching node images, validating add-ons, and recycling nodes with health checks and disruption controls.',
'Developed Helm charts and Kubernetes Deployments, Services, and Ingress resources with readiness probes, resource limits, topology placement, and autoscaling policies.',
'Troubleshot DNS, ingress routing, load-balancer health, pod connectivity, storage mounts, and scheduling failures across containerized application environments.',
'Built Jenkins shared libraries, GitHub Actions reusable workflows, GitLab CI templates, and Azure DevOps YAML pipelines for automated build, test, scan, deployment, and release verification.',
'Implemented Argo CD delivery from reviewed Git changes, managing environment-specific Helm values, sync policies, drift detection, health checks, and rollback through versioned configuration.',
'Automated provisioning and configuration with Ansible, Python, Bash, and PowerShell, including environment setup, inventory, deployment prerequisites, and operational reporting.',
'Hardened cloud access through scoped IAM roles, IRSA, OIDC federation, and Kubernetes RBAC; integrated Secrets Manager and Key Vault for controlled secret retrieval.',
'Embedded code, dependency, container, and IaC scanning into CI/CD gates; coordinated vulnerability remediation, patch deployment, and security evidence with compliance stakeholders.',
'Built Prometheus/Grafana dashboards, Datadog service views, and CloudWatch alerts for workload health, latency, errors, resource saturation, and deployment-related degradation.',
'Centralized application and platform logs through ELK and cloud logging services, standardizing metadata and retention to accelerate incident investigation.',
'Supported highly available deployments and recovery procedures, testing backup restoration, failover readiness, scaling limits, and application health after infrastructure changes.',
'Led production troubleshooting and root-cause reviews with development, QA, and security teams; translated Agile retrospectives into pipeline improvements and operational runbooks.'
]),
(['AWS','Jenkins','GitHub Actions','GitLab CI','Terraform','Docker'],[
'Built reusable Jenkins, GitHub Actions, and GitLab CI workflows for application builds, automated testing, security checks, and controlled environment promotion.',
'Automated AWS infrastructure and environment configuration through Terraform and Ansible with pull-request reviews and consistent deployment inputs.',
'Supported Docker-based Kubernetes applications using Helm charts, health probes, resource settings, and post-deployment verification.',
'Diagnosed pipeline, runner, artifact, permission, and service-connectivity failures with development and QA teams during release cycles.',
'Maintained monitoring checks, deployment documentation, and rollback procedures; contributed automation improvements through Agile planning and retrospectives.'
]),
(['AWS','Azure','EKS/AKS','Terraform','Argo CD','Prometheus','Grafana'],[
'Provisioned AWS and Azure application environments using Terraform definitions for networking, compute, identities, storage, and Kubernetes platform dependencies.',
'Supported EKS and AKS workload operations, including Helm deployments, service routing, node capacity, patching, and controlled cluster maintenance.',
'Maintained Jenkins, GitHub Actions, and Azure DevOps delivery workflows with automated validation, versioned artifacts, and environment promotion controls.',
'Implemented Argo CD reconciliation for container workloads, investigating configuration drift, failed synchronization, and deployment health issues.',
'Configured Prometheus, Grafana, CloudWatch, and Azure Monitor views to track application availability, capacity, and infrastructure performance.',
'Resolved networking, container, resource, and dependency incidents; coordinated recovery checks and operational handovers with distributed engineering teams.'
])]
for j,(skills,bullets) in zip(p.experience,updates):
 j.skills_used=skills
 j.impact=bullets
p.skills=['AWS','Azure','Kubernetes','EKS','AKS','Docker','Terraform','CloudFormation','Jenkins','GitHub Actions','GitLab CI','Azure DevOps','Helm','Argo CD','Ansible','Python','Bash','PowerShell','Prometheus','Grafana','Datadog','CloudWatch','ELK','IAM']
p.notes=['Aggressive JD-aligned draft with expanded cloud platform and automation responsibilities. Employment history, education, certifications and updated email retained.']
stem=Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-aws-cloud-kubernetes-devops-aggressive').resolve()
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.section-title{margin-top:12px}.skills-grid{gap:6px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text(jd)
stem.with_suffix('.json').write_text(json.dumps({'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'sources':['https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html','https://docs.aws.amazon.com/eks/latest/best-practices/security.html']},indent=2))
print(stem)
