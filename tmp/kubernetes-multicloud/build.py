import json,sys
from pathlib import Path
sys.path.insert(0,'plugins/resume-creator-plugin/scripts')
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer
base=Path('resume_data/people/rajendra-prasad-n.json')
p=json.loads(base.read_text())
p['headline']='Lead Platform Engineer | Cloud Infrastructure'
p['page_title']='Rajendra P N - Kubernetes & Multi-Cloud Platform Engineering'
p['summary_html']='<strong>Lead Platform Engineer with 10+ years of experience in DevOps, cloud engineering, and production reliability.</strong> Operates <strong>Kubernetes platforms, Helm deployments, Docker workloads, and Terraform/Ansible automation across AWS and Azure</strong>. Troubleshoots scheduling, container startup, storage, ingress, DNS, and application failures; builds reusable Jenkins and GitHub Actions pipelines with secure release controls. Combines Linux administration, Python/Bash automation, observability, incident response, and recovery planning to support scalable enterprise services. Based in Dallas, TX.'
p['certifications']=[c for c in p['certifications'] if 'mulesoft' not in c.lower()]
p['skills']=['Kubernetes','AWS EKS','Azure AKS','Docker','Helm','Terraform','Ansible','Linux','Python','Bash','Jenkins','GitHub Actions','Git','Prometheus','Grafana','ELK','CloudWatch','Azure Monitor','Argo CD','RBAC','Networking','Production support']
p['skill_sections']=[
{'title':'Kubernetes & Cluster Operations','content':'Pods, Deployments, Services, ConfigMaps, Secrets, namespaces, RBAC, Helm; StatefulSets, DaemonSets, PV/PVC and StorageClass troubleshooting; node lifecycle, readiness probes, HPA; VPA concepts'},
{'title':'AWS & Azure Infrastructure','content':'EKS, EC2, VPC, IAM, ALB/NLB, Route 53, EBS/EFS, S3, CloudWatch; AKS, VNETs, NSGs, Azure Load Balancer, Azure DNS, ACR, Key Vault, Azure Monitor'},
{'title':'CI/CD, IaC & GitOps','content':'Jenkins/CloudBees, Groovy shared libraries, GitHub Actions, GitLab pipeline patterns, Maven, Artifactory, Terraform, Ansible, Git, branch protections, Helm, Argo CD'},
{'title':'Linux, Automation & Networking','content':'Linux administration, Python, Bash, PowerShell; process, filesystem and network diagnostics; DNS, ingress, TLS, load balancing, private endpoints and firewall troubleshooting; RHEL/Ubuntu operational concepts'},
{'title':'Observability & Production Reliability','content':'Prometheus, Grafana, ELK/Elastic, Node Exporter, application logs, Kubernetes events, CloudWatch, Azure Monitor; capacity reviews, incident triage, root-cause analysis, recovery runbooks'},
{'title':'Security & Resilience','content':'RBAC, least privilege, network policies, Key Vault, IAM, secret handling, image scanning, vulnerability remediation, health checks, rollout/rollback, availability and recovery validation; OpenShift, Istio/Linkerd, Vault/Keycloak concepts'}]
p['achievements']=[{'tag':'Kubernetes Delivery','text':'Standardized Helm and Kubernetes deployment patterns, release health checks, and environment configuration for production services.'},{'tag':'AWS & Azure Automation','text':'Built reusable infrastructure and delivery tooling across cloud environments with Terraform, Ansible, Python, and shared CI/CD pipelines.'},{'tag':'Production Reliability','text':'Correlated workload events, application logs, and cloud telemetry to isolate failures and improve operational runbooks.'}]
p['experience'][0]['title']='Lead Platform/DevOps Engineer'
roles=[[
'Operated Kubernetes application platforms across AWS EKS and Azure AKS, coordinating workload deployment, production support, and environment readiness.',
'Built reusable Terraform infrastructure for AWS VPC, IAM, and EKS dependencies and Azure networking, identity, and AKS services.',
'Standardized Helm charts and environment values for microservices, reviewing Deployments, Services, ConfigMaps, and Secrets before release promotion.',
'Troubleshot pending pods, restart loops, failed image pulls, and probe failures using Kubernetes events, container logs, and node diagnostics.',
'Investigated ingress, DNS, load-balancer, and service-connectivity failures across AWS and Azure, tracing traffic between application and infrastructure layers.',
'Managed namespace access and RBAC, coordinating AWS IAM and Azure identity controls with least-privilege deployment permissions.',
'Reviewed persistent-volume claims, storage provisioning, and mount failures for stateful services, aligning storage configuration with workload recovery requirements.',
'Coordinated cluster and worker-node maintenance, validating version compatibility, drain readiness, and workload health during planned changes.',
'Reviewed requests, limits, autoscaling, and scheduling constraints with service owners to address capacity bottlenecks and unstable workload behavior.',
'Built reusable Jenkins and GitHub Actions workflows for container builds, automated tests, artifact publication, Helm releases, and deployment verification.',
'Integrated image and dependency checks, protected deployment credentials, and infrastructure validation into shared CI/CD workflows.',
'Correlated Prometheus/Grafana metrics, application logs, CloudWatch, and Azure telemetry during production incidents and root-cause investigations.',
'Automated Linux, cluster-readiness, and release diagnostics with Python and Bash, reducing repeated manual investigation and support effort.',
'Supported Milvus and GPU-enabled workloads on AWS/Azure infrastructure, reviewing service dependencies, resource utilization, and deployment readiness.',
'Mentored engineers and maintained production-readiness and recovery runbooks, coordinating rollback checks and cross-team incident follow-up.'
],[
'Partnered with application teams on Kubernetes delivery across AWS and Azure, reviewing deployment prerequisites and release verification.',
'Maintained Docker build tooling and Linux/Windows runners, diagnosing cache, credential, dependency, and execution-capacity failures.',
'Built reusable GitHub Actions workflows for container builds, test stages, artifact publication, and controlled environment promotion.',
'Maintained Terraform and Ansible automation for AWS/Azure environment configuration, reviewing infrastructure changes and Linux drift.',
'Validated Helm values, ConfigMaps, and Secrets for shared Kubernetes services, resolving environment differences before deployment.',
'Investigated pod startup and service-connectivity failures using workload events, logs, DNS checks, and application health endpoints.',
'Standardized protected branches, release approvals, and artifact retention, preserving source-to-release traceability.',
'Automated runner-readiness and Kubernetes release diagnostics with Python and shell scripts for developer self-service.',
'Protected cloud deployment access with scoped AWS/Azure credentials and documented required permissions and secrets prerequisites.',
'Coached developers on deployment health, rollback inputs, and shared pipeline ownership, documenting operational handoffs.'
],[
'Built Jenkins and GitHub Actions pipelines for Kubernetes microservices, integrating Maven tests, image publication, and deployment checks.',
'Provisioned Azure platform services and supporting AWS infrastructure with reusable Terraform modules and reviewed change plans.',
'Implemented Helm packaging and Argo CD GitOps for AKS workloads, versioning environment configuration and rollback inputs.',
'Maintained Linux runners and Ansible configuration, troubleshooting build dependencies, filesystem issues, and execution failures.',
'Investigated pod scheduling, image-pull, and service-connectivity failures, correlating Kubernetes events with application and cloud telemetry.',
'Published versioned binaries and Docker images to shared repositories and incorporated SonarQube feedback into delivery workflows.',
'Used Azure Monitor, Application Insights, and AWS operational telemetry to support production troubleshooting and recovery documentation.',
'Reviewed namespace configuration, infrastructure access, tagging, and network dependencies with application owners before releases.',
'Built Python/Bash checks for AWS/Azure endpoints and release prerequisites, producing consistent diagnostics across environments.',
'Coordinated AKS node maintenance and application upgrades, verifying workload readiness and recovery steps with service owners.'
],[
'Administered CloudBees CI, JFrog Artifactory, and Xray for SaaS engineering, supporting reliable builds and secure container artifacts.',
'Developed Groovy Jenkins libraries for Docker image versioning and artifact publication, standardizing reusable release steps.',
'Built Python/FastAPI services integrating Jenkins, Jira, and JFrog to automate onboarding and developer delivery workflows.',
'Provisioned application infrastructure on Azure and maintained AWS integrations with Terraform/Ansible and environment-specific configuration.',
'Standardized Docker and Helm deployments for Kubernetes services and payment workloads, validating health checks and production readiness.',
'Partnered with microservice developers on test stages, dependency resolution, and repeatable promotion of release artifacts.',
'Built Python Prometheus exporters and Grafana/Node Exporter monitoring stacks to expose Linux and application health.',
'Investigated production incidents across application, Kubernetes, and AWS/Azure dependencies, converting repeat issues into platform fixes.',
'Reviewed deployment credentials and artifact vulnerability findings, coordinating remediation with application teams before release.',
'Maintained Kubernetes troubleshooting and recovery guidance, coaching developers on shared release controls and operational ownership.'
],[
'Built Jenkins/Maven workflows for REST microservices across test, UAT, and production, coordinating release prerequisites with developers.',
'Supported Azure application infrastructure and AWS integrations, troubleshooting networking, database connections, and secrets access.',
'Packaged Kubernetes applications with Helm, maintaining namespaces, Services, and configuration for repeatable cluster deployments.',
'Investigated container startup, service discovery, and deployment failures using application logs, Kubernetes events, and Linux diagnostics.',
'Automated cloud configuration with Terraform, ARM templates, and Ansible, reviewing infrastructure changes alongside application releases.',
'Implemented ELK and Azure Monitor visibility and reviewed AWS environment diagnostics during application incidents.',
'Coordinated database and API release dependencies, verifying execution order and recovery readiness before production handoff.',
'Scripted Linux and application health checks with Python/Bash, capturing diagnostic evidence for support teams.',
'Reviewed AWS/Azure deployment permissions and protected secret inputs, maintaining validated release procedures and change records.',
'Checked certificate expiry, DNS, and service connectivity during release readiness reviews and coordinated fixes with infrastructure owners.'
],[
'Built CI/CD workflows for API, database, and web components, standardizing build dependencies and release promotion.',
'Provisioned Azure resources and maintained AWS infrastructure dependencies with Terraform and reviewed environment parameters.',
'Configured Linux environments with Ansible and automated build-agent maintenance with Python and shell scripts.',
'Packaged containerized services with Helm and Kubernetes manifests, checking deployment health before release.',
'Investigated build and deployment failures through agent logs, Linux diagnostics, and configuration comparisons with developers.',
'Validated AWS/Azure access, DNS, network connectivity, and application dependencies before deployments.',
'Defined Git branching and protected-branch checks, versioning artifacts and environment configuration for repeatable promotion.',
'Protected deployment credentials and reviewed cloud permissions, documenting access prerequisites for application teams.',
'Maintained deployment manifests and configuration baselines, helping support teams trace failures to source and release changes.',
'Documented Linux, cloud, and application recovery procedures, supporting repeatable operational handoffs and environment onboarding.'
]]
for e,bullets in zip(p['experience'],roles):
 e['impact']=bullets
 e['skills_used']=['AWS','Azure','Kubernetes','Helm','Terraform','Ansible','Python','Linux'] + (['Jenkins','GitHub Actions'] if e['company'] != 'Mphasis Ltd' else ['Git','Bash'])
p['notes']=['Aggressive Kubernetes-focused AWS/Azure variant. Preserve base profiles.','Latest project 15 bullets; other projects 10. No mobile content or MuleSoft badge.','Preferred technologies without direct source evidence labeled concepts; Dallas location preserved without asserting onsite availability.']
out=Path('output/kubernetes-multicloud/rajendra-kubernetes-multicloud-aggressive')
out.with_suffix('.profile.json').write_text(json.dumps(p,indent=2)+'\n')
profile=BundledJsonResumeStore(out.parent,Path('plugins/resume-creator-plugin/assets/static')).load_person(out.name+'.profile')
template=Path('plugins/resume-creator-plugin/assets/templates/base_resume.html').read_text().replace('repeat(5,minmax(0,1fr))','repeat(4,minmax(0,1fr))').replace('align-items:start;','align-items:stretch;')
template=template.replace('</style>', '@media print{.job-header{flex-direction:row}.job-meta{white-space:nowrap}.job-block{break-inside:auto;page-break-inside:auto;margin-bottom:7px}.job-header,.job-details{break-after:avoid}.cert-card{min-height:72px}.cert-badge-svg{max-width:46px}.section-title{margin-top:10px;margin-bottom:6px}.skill-card{padding:6px 9px}.summary-box{padding:8px 12px}li{break-inside:avoid}.education-card{padding:6px 9px}}\n</style>')
Path('tmp/kubernetes-multicloud/template.html').write_text(template)
out.with_suffix('.html').write_text(BundledHtmlResumeRenderer(Path('tmp/kubernetes-multicloud/template.html')).render(profile))
print([(e['company'],len(e['impact'])) for e in p['experience']])
