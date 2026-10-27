from docx import Document
from docx.text.paragraph import Paragraph
from copy import deepcopy
from pathlib import Path
import json
src=Path('output/docx/RajendraPN_Azure_DevOps.docx')
d=Document(src);p=list(d.paragraphs)
def edit(i,text):
 p[i].runs[0].text=text
 for r in p[i].runs[1:]:r.text=''
changes={
8:'Azure DevOps and platform engineer with 10+ years of experience in cloud infrastructure, CI/CD, Kubernetes operations, and production support. Builds reusable Azure platform capabilities with Terraform, GitHub Actions, Python, Bash, and PowerShell.',
9:'Focuses on Azure platform engineering: repeatable environment provisioning, secure connectivity, shared deployment workflows, operational readiness, and developer enablement across development, security, and operations teams.',
10:'Creates and maintains CI/CD pipelines with GitHub Actions and Azure DevOps, combining reusable workflows, self-hosted execution, deployment controls, and versioned release artifacts.',
11:'Develops reusable Terraform and Ansible automation for Azure infrastructure and deploys containerized microservices with Helm and GitOps-style configuration management.',
12:'Supports Azure networking and application platforms, including VNets, NSGs, Private Link, DNS, Application Gateway, AKS, Key Vault, and Azure Databricks; understands hub-and-spoke, peering, Firewall, and route-table design patterns.',
13:'Troubleshoots Linux, container, network, and application failures using shell/Python automation and Azure telemetry; maintains runbooks and works with service owners on reliability improvements.',
17:'CI/CD\t: GitHub Actions, reusable workflows, self-hosted runners, Azure DevOps, Jenkins, GitLab, Argo CD',
18:'IaC\t\t\t\t: Terraform modules, plan validation, Azure ARM templates, Ansible; Azure Storage remote state and workspace concepts',
20:'Container Orchestration\t: Docker, Kubernetes, Helm; multi-stage Dockerfile and image-hardening practices',
21:'K8s Managed Service\t\t: Azure Kubernetes Service (AKS), OpenShift, Rancher',
27:'Cloud\t\t\t\t: Microsoft Azure, Azure networking, Private Link, DNS, Key Vault',
15:'Operating Systems\t\t: Linux, RHEL, Ubuntu, Windows Server; shell scripting, permissions, networking and service troubleshooting',
34:'Platform tools\t\t\t: Helm, Argo CD, Azure Container Registry, Vault, Istio; systemd service-management concepts',
51:'Skills used\t: Azure, Terraform, GitHub Actions, Azure DevOps, Python, Bash, AKS, Helm, Argo CD, Private Link, Azure Databricks, APIM, Application Gateway',
53:'Led Azure platform delivery by standardizing infrastructure changes, shared CI/CD workflows, environment configuration, and production release readiness with application teams.',
54:'Designed and operated AKS infrastructure with Terraform for Milvus and GPU workloads, troubleshooting scheduling, networking, resource capacity, and access controls.',
55:'Partnered with development, security, and operations teams to review platform designs, translate application dependencies into infrastructure requirements, and resolve delivery blockers.',
56:'Built reusable GitHub Actions and Azure DevOps workflows for application and infrastructure delivery, integrating automated validation, controlled promotion, and deployment approvals.',
57:'Developed modular Terraform configurations and CI plan-review checks, documenting environment inputs, access boundaries, and reviewed infrastructure changes.',
58:'Automated Azure Databricks workspace provisioning with Terraform across isolated subscriptions, standardizing network integration, RBAC, and data-platform environment configuration.',
59:'Published reusable platform examples, architecture diagrams, and operational runbooks, enabling developers to provision and support environments consistently.',
60:'Maintained self-hosted build infrastructure and Azure agent pools, troubleshooting Linux permissions, network access, dependencies, and failed pipeline execution.',
61:'Configured and troubleshot Azure private connectivity, including Private Endpoints, Private Link, VNet/subnet access, NSGs, and DNS dependencies for application services.',
62:'Reviewed AKS resource requests, scaling behavior, and Azure monitoring signals with application owners to improve capacity planning, reliability, and cost visibility.',
63:'Managed infrastructure and Helm configuration through Git pull requests, versioned changes, and deployment reviews to support traceable GitOps-style platform operations.',
64:'Standardized Docker packaging and Helm deployments for microservices, validating image inputs, application configuration, health checks, and rollback readiness.',
65:'Provisioned and supported Azure API Management infrastructure through Terraform and CI/CD, maintaining API routing, backend connectivity, and environment-specific configuration.',
66:'Troubleshot APIM gateway failures, authentication policies, and backend errors using platform diagnostics and application logs, documenting corrective actions with service owners.',
67:'Integrated Application Gateway with APIM, validating TLS, routing rules, and backend health probes to support secure, resilient API access.',
77:'Maintained Linux/Windows self-hosted agents and VMSS agent pools, troubleshooting execution capacity, permissions, dependencies, and connectivity.',
78:'Organized artifact feeds, views, and upstream sources to provide application teams with consistent, versioned build inputs.',
79:'Maintained Docker build and runtime configuration, diagnosing image and container failures during application delivery.',
80:'Operated Kubernetes Deployments, Services, and configuration, troubleshooting pod health and application connectivity during release promotion.',
81:'Migrated Jenkins pipelines to GitLab and configured runners, preserving build stages, artifacts, and deployment handoffs.',
82:'Established Git branching and review practices and coached developers on source control, pipeline ownership, and environment promotion.',
89:'Maintained self-hosted Linux/Windows runners and Azure agent pools, diagnosing build dependencies and execution failures.',
92:'Deployed Kubernetes microservices with Argo CD, versioning manifests and reviewing configuration changes through GitOps workflows.',
93:'Built Azure infrastructure with Terraform and ARM templates, integrating validation and reviewed changes into YAML pipelines.',
95:'Built GitHub Actions deployment workflows for AKS services, validating environment inputs and application health after release.',
96:'Maintained Dockerfiles and Kubernetes manifests for AKS applications, reviewing build dependencies, runtime settings, and deployment behavior.',
100:'Diagnosed build and release failures across application logs, pipeline execution, Linux hosts, and Azure resource dependencies.',
104:'Administered Kubernetes pods, Deployments, Services, and RBAC configuration; investigated scheduling and service-discovery failures.',
105:'Reviewed Kubernetes availability and recovery patterns with application teams, validating scaling requirements and upgrade readiness.',
110:'Configured Azure VNets, subnets, DNS, NSGs, VPN/ExpressRoute, load balancers, and Application Gateway; investigated routing and application-connectivity issues.',
118:p[118].text.replace('Azure, AWS,','Azure,'),
140:p[140].text.replace('Kubernetes, AWS,','Kubernetes, Azure,')
}
for i,text in changes.items():edit(i,text)
# Extend the short GlobalLogic project with distinct platform responsibilities.
anchor=p[82]
for text in [
'Maintained Terraform and environment configuration for Azure platform services, reviewing proposed changes with application owners.',
'Automated environment and deployment readiness checks with scripts, collecting diagnostic output for support handoffs.',
'Documented platform onboarding and recovery prerequisites, helping developers adopt shared deployment tooling.'
]:
 el=deepcopy(p[82]._p);anchor._p.addnext(el);q=Paragraph(el,anchor._parent);q.runs[0].text=text
 for r in q.runs[1:]:r.text=''
 anchor=q
out=Path('output/docx/RajendraPN_AzureDevOps_Remote_Platform.docx');d.save(out)
Path('tmp/azure-remote-word/manifest.json').write_text(json.dumps({'domain':'azure-devops','level':'Tailored','source':str(src.resolve()),'output':str(out.resolve()),'header':'Lead Azure DevOps Engineer | AI | K8s','latest_title':'Lead Azure DevOps Engineer','branch':'feature/rajendrapn-azure','focus':'Azure platform engineering, GitHub Actions, Terraform, networking, Linux, Docker, AKS'},indent=2))
print(out.resolve())
