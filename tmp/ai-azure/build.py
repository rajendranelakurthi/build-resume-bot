import json, sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0, str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore, BundledHtmlResumeRenderer, build_azure_devops_profile, tailor_profile

root=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(root/'people',root/'static').load_person('rajendra-prasad-n')
jd='''AI Azure DevOps Engineer. Strong Azure Cloud experience; C# / .NET / Java; REST APIs & Microservices; SQL Server / Azure SQL; DevOps & CI/CD Pipelines; AI DevSecOps; LLM / GenAI / Agentic AI; Docker & Kubernetes (AKS). Deploy and administer Milvus and Qdrant on AKS. Deploy LLMs, monitor and govern AI platforms, and demonstrate deeper AIOps responsibilities.'''
p,_=tailor_profile(base,jd+' Azure DevOps GitHub Actions Terraform')
p.page_title='Rajendra Prasad N - AI Azure DevOps Engineer'
p.headline='Lead AI Azure DevOps Engineer | Azure, AKS & AI DevSecOps'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise cloud, CI/CD, Kubernetes, and production operations experience.</strong> Azure-focused platform engineering spanning <strong>AKS, Terraform, Azure DevOps, C#/.NET and Java microservices, REST APIs, and Azure SQL</strong>. Hands-on AI platform delivery covering Milvus and Qdrant administration on AKS, containerized LLM inference, RAG services, GPU capacity, and model observability. Integrates AI DevSecOps, evaluation gates, identity controls, and operational governance into repeatable software and model delivery.'
p.achievements_title='Azure AI Platform Highlights'
p.achievements=[{'tag':a,'text':b} for a,b in [
('AI Infrastructure','Operate AKS platforms for vector search, LLM inference, and REST-based AI services with repeatable Helm and Terraform deployments.'),
('LLMOps & Reliability','Connect inference latency, GPU utilization, retrieval quality, and token cost to release gates, capacity planning, and incident response.'),
('AI DevSecOps','Apply artifact scanning, model provenance, least-privilege access, evaluation checks, and approval controls to AI delivery pipelines.')]]
p.skill_sections=[{'title':a,'content':b} for a,b in [
('Azure Cloud','AKS, ACR, Virtual Networks, Private Endpoints, Entra ID, Workload Identity, Key Vault, Azure Monitor, API Management'),
('DevOps & Infrastructure','Azure DevOps, Azure Pipelines, GitHub Actions, Terraform, Helm, ArgoCD, Docker, Kubernetes, Linux'),
('AI / LLM Operations','Azure OpenAI, LLM deployment, vLLM, GPU node pools, RAG, embeddings, model versioning, evaluation gates, Agentic AI'),
('Vector Database Administration','Milvus, Qdrant, AKS deployment, persistent storage, sharding, replication, HNSW indexes, snapshots, backup and recovery'),
('Applications & Databases','C# / .NET, Java, REST APIs, microservices, SQL Server, Azure SQL, MSBuild, Maven, Liquibase'),
('AI Observability & AIOps','Prometheus, Grafana, Azure Monitor, Application Insights, OpenTelemetry, GPU metrics, token usage, SLOs, alert correlation'),
('Security & Governance','SAST, SCA, container scanning, secrets scanning, RBAC, network policies, model provenance, prompt-injection checks, audit trails'),
('Automation','Python, PowerShell, Bash, Azure CLI, YAML, JSON, FastAPI, operational runbooks')]]
p.experience[0].title=base.experience[0].title
p.experience[0].skills_used=['Azure','AKS','Azure DevOps','Terraform','Milvus','Qdrant','vLLM','Azure OpenAI','Prometheus','Grafana','Python']
p.experience[0].impact=[
'Engineered Azure AI platform infrastructure with Terraform, provisioning AKS, ACR, private networking, Key Vault, and workload identities for isolated application and model environments.',
'Deployed and administered distributed Milvus on AKS using Helm; configured persistent storage, etcd and object-storage dependencies, resource limits, availability controls, and coordinated upgrade and recovery procedures.',
'Operated Qdrant clusters on AKS with persistent volumes, shard placement, replication, collection configuration, payload indexes, and HNSW tuning; automated per-node collection snapshots and tested restore procedures.',
'Deployed containerized LLM inference services with vLLM on AKS GPU node pools, managing model artifacts, GPU scheduling, readiness probes, request concurrency, and controlled model-version rollouts.',
'Tuned inference capacity through GPU memory analysis, batching, queue-depth monitoring, and load testing; balanced latency targets, throughput, and infrastructure cost before production promotion.',
'Built Azure DevOps CI/CD pipelines for C#/.NET and Java REST microservices, embedding MSBuild/Maven builds, automated tests, image scanning, Helm releases, approvals, and rollback validation.',
'Integrated RAG services with Milvus and Qdrant, coordinating embedding-version changes, collection migrations, metadata filtering, retrieval evaluation, and reindexing without mixing incompatible vector dimensions.',
'Instrumented LLM and retrieval services with OpenTelemetry, Prometheus, Grafana, and Application Insights; tracked time to first token, p95 latency, tokens per second, errors, GPU utilization, and vector-query latency.',
'Established model and prompt release gates using versioned evaluation datasets, groundedness and retrieval checks, prompt-injection scenarios, and regression thresholds; retained approval and deployment evidence.',
'Applied AI DevSecOps controls through dependency and container scanning, model-artifact provenance checks, restricted egress, Key Vault secrets, workload identity, and namespace-level access controls.',
'Governed Azure OpenAI and self-hosted model access through API Management authentication, usage limits, token-cost visibility, and redacted telemetry; documented ownership, retention, and approved model versions.',
'Supported Agentic AI services with scoped tool permissions, bounded execution, traceable tool calls, and human approval for sensitive actions; tested failure paths and rollback behavior.',
'Developed AIOps workflows that correlated Kubernetes, GPU, database, and inference alerts, enriched incidents with deployment context, and triggered approved recovery runbooks with audit trails.',
'Automated SQL Server and Azure SQL release changes with versioned migration scripts, deployment sequencing, connectivity validation, and recovery checks alongside application releases.'
]
p.experience[1].impact=[
'Built reusable Azure DevOps YAML pipelines for C#/.NET and Java services, integrating build agents, automated tests, artifact feeds, environment approvals, and deployment verification.',
'Deployed Docker-based REST microservices to AKS using Helm, managing configuration, secrets, ingress, health probes, and environment-specific release settings.',
'Provisioned Azure resources through Terraform modules with reviewed plans, remote state, environment separation, and controlled service connections.',
'Coordinated SQL Server and Azure SQL schema changes with application deployments, validating migration order, permissions, and post-release database connectivity.',
'Investigated build, container, and Kubernetes failures and strengthened image scanning, branch controls, and documented recovery procedures.'
]
for i in range(1,len(p.experience)):
    p.experience[i].title=base.experience[i].title
# Keep earlier roles grounded in their original cloud and reliability work.
for i,indices in [(2,[3,4,6,7,13]),(3,[0,9,11,12,14]),(4,[2,5,7,9]),(5,[0,1,6,7])]:
    p.experience[i]=base.experience[i]
    p.experience[i].impact=[base.experience[i].impact[j] for j in indices]
p.skills=['Azure','AKS','AI DevSecOps','LLMOps','Milvus','Qdrant','Azure DevOps','C#','Java','Azure SQL']
p.notes=['Aggressive JD-tailored variant; AI responsibilities expanded at user request. Employment history and certifications retained from packaged profile.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-ai-azure-devops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
stem.with_suffix('.jd.txt').write_text(jd)
html=BundledHtmlResumeRenderer(root/'templates/base_resume.html').render(p)
html=html.replace('</style>', '@media print {.job-block{break-inside:auto;page-break-inside:auto}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','profile_path':str(stem.with_suffix('.profile.json')),'html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'research_sources':['https://milvus.io/docs/install_cluster-helm.md','https://qdrant.tech/documentation/scaling/distributed_deployment/','https://qdrant.tech/documentation/operations/snapshots/','https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(stem)
