import json
from pathlib import Path
q=Path('tmp/databricks-platform/plugin/assets/people/rajendra-prasad-n.json');p=json.loads(q.read_text())
p['summary_html']='<strong>Databricks Platform Engineer with 10+ years of infrastructure engineering, DevOps, and production operations experience.</strong> Owns <strong>Terraform-driven Databricks deployment on AWS</strong>, from account-level workspace foundations and private networking to Unity Catalog governance, compute policies, and operational readiness. Designs reusable platform modules, separates infrastructure and workspace lifecycles, and governs changes through reviewed plans and controlled promotion. Partners with security and data engineering teams on least-privilege access, production incident resolution, capacity and cost controls, with supporting Snowflake and Azure Databricks experience.'
p['achievements']=[{'tag':'Platform Architecture','text':'Established modular AWS Databricks deployment patterns separating network, storage, account-level workspace provisioning, and workspace administration.'},{'tag':'Governance as Code','text':'Codified IAM trust, Unity Catalog storage access, catalog grants, compute policies, and service-principal permissions in reviewed Terraform changes.'},{'tag':'Production Ownership','text':'Connected infrastructure promotion, drift control, provisioning diagnostics, compute guardrails, and operational runbooks into a repeatable platform lifecycle.'}]
p['skill_sections']=[
{'title':'Databricks Deployment Architecture','content':'AWS/Databricks Terraform providers, account and workspace provider aliases, credential/storage/network configurations, reusable modules, workspace bootstrap'},
{'title':'AWS Network & Identity','content':'Customer-managed VPCs, private subnets, route tables, security groups, PrivateLink, DNS, cross-account IAM trust, S3 policies, KMS, service principals'},
{'title':'Unity Catalog & Storage Governance','content':'Regional metastores, workspace assignments, catalogs, schemas, grants, storage credentials, external locations, volumes, DBFS migration'},
{'title':'Compute & Workload Administration','content':'Cluster policies, access modes, runtime lifecycle, node/worker limits, autoscaling, auto-termination, SQL warehouses, serverless compute, jobs, notebooks, pipelines'},
{'title':'Terraform Delivery & Operations','content':'Remote state, state isolation, locking, provider pinning, plan/apply gates, imports, drift detection, CI/CD, Python, Databricks APIs, audit logs, cost controls'},
{'title':'Supporting Data Platforms','content':'Snowflake Terraform: warehouses, roles, grants, storage integrations; Azure Databricks: managed workspaces, VNet integration, ADLS Gen2, managed identities, Key Vault'}]
p['experience'][0]['impact']=[
'Owned the AWS Databricks platform deployment lifecycle, translating networking, security, data-access, and workload requirements into reusable Terraform modules and onboarding standards.',
'Separated AWS foundations, account-level workspace creation, and workspace resources into distinct Terraform stages with provider aliases and explicit bootstrap dependencies.',
'Provisioned workspace credential, storage, and network configurations; validated cross-account IAM trust, S3 policies, and deployment permissions before workspace creation.',
'Designed customer-managed VPC deployments with private subnets, route tables, security groups, and PrivateLink; diagnosed DNS, endpoint, and control-plane connectivity failures.',
'Governed Terraform changes with isolated remote state, locking, pinned providers, reviewed plans, and controlled applies; reconciled drift and imported existing resources safely.',
'Established regional Unity Catalog metastores and workspace assignments; defined catalog/schema ownership, group grants, storage credentials, and S3 external locations as code.',
'Designed classic compute policies enforcing access modes, approved runtimes and node families, worker limits, required tags, and auto-termination to control risk and spend.',
'Enabled serverless notebooks, jobs, and pipelines with separate access and connectivity checks; provisioned SQL warehouses with scaling, auto-stop, and workload permissions.',
'Automated job graphs, schedules, retries, run-as identities, notebook deployment, and pipeline settings; validated service-principal access and storage dependencies before promotion.',
'Led diagnosis of failed workspace deployments, compute startup, IAM/S3 access, and job execution using Terraform output, Databricks events, audit logs, and AWS telemetry.',
'Assessed legacy DBFS mounts and init-script dependencies; planned migration to Unity Catalog volumes and workspace files with path, access, and execution validation.',
'Codified Snowflake warehouses, roles, grants, and S3 storage integrations with Terraform; supported Azure Databricks VNet, managed-identity, ADLS, and Key Vault configuration.'
]
p['experience'][1]['impact']=[
'Implemented AWS Databricks environment onboarding through parameterized Terraform modules, mapping workspace requirements to approved network, IAM, and storage configurations.',
'Maintained account-level and workspace-level deployment stages, verifying workspace readiness before applying identities, compute policies, and workload resources.',
'Validated cross-account role trust, S3 bucket access, subnet settings, and security-group rules to resolve workspace provisioning failures.',
'Configured Unity Catalog metastore assignments and catalog/schema grants, coordinating workspace identity groups and data-owner access requirements.',
'Tested storage credentials and external locations against S3 permissions, distinguishing AWS authorization failures from Unity Catalog grant issues.',
'Implemented reusable cluster-policy definitions with runtime allowlists, worker bounds, tags, and termination settings; tested policy behavior before environment rollout.',
'Configured SQL warehouse sizing, scaling, auto-stop, and access rights; investigated startup and connectivity issues with consuming teams.',
'Managed notebook paths, job parameters, task dependencies, schedules, and pipeline permissions as version-controlled deployment configuration.',
'Integrated Terraform checks and reviewed plans into GitLab CI, protecting credentials and isolating environment variables and state across deployments.',
'Diagnosed DBFS mount and path failures affecting notebooks and jobs, tracing storage access through IAM roles and S3 policies.',
'Automated Snowflake warehouse, schema, role, and grant changes with Terraform, reviewing access impact and configuration consistency before release.',
'Supported Azure Databricks workspace and ADLS configuration; produced deployment checklists, support runbooks, and verification evidence for platform handoffs.'
]
p['experience'][2]['impact']=[
'Built repeatable AWS Databricks workspace infrastructure with Terraform, organizing VPC, IAM, storage, and workspace inputs into reusable environment configurations.',
'Managed workspace deployment dependencies across cross-account credentials, S3 storage, and network registration; resolved incomplete or failed provisioning operations.',
'Validated subnet routing, security groups, DNS, and service connectivity with infrastructure teams before handing environments to data engineers.',
'Supported Unity Catalog adoption as capabilities became available, establishing metastore assignments and coordinating catalog ownership and access requirements.',
'Configured external storage access and catalog/schema grants, validating IAM trust and S3 permissions against intended workspace use.',
'Standardized cluster policies for runtime selection, compute sizes, worker limits, tags, and idle termination; investigated policy-related startup failures.',
'Administered SQL warehouse capacity, auto-stop, and permissions, troubleshooting availability and connection issues for analytics users.',
'Automated notebook and job deployment parameters, schedules, retries, and pipeline configuration to make environment promotion repeatable.',
'Integrated Terraform plans and deployment validation into Jenkins and GitHub Actions, using Python and shell utilities for configuration and access checks.',
'Maintained DBFS mounts and file dependencies for existing workloads, documenting storage paths and resolving role, bucket-policy, and file-access failures.',
'Provisioned Snowflake warehouse and access resources with Terraform; supported Azure Databricks workspace and storage integration for selected environments.',
'Created platform runbooks covering provisioning failures, access checks, compute readiness, and release verification; coordinated incident resolution across distributed teams.'
]
for target in [q,Path('tailored_resume/rajendra-prasad-n/Rajendra-P-N-Databricks-Platform.profile.json')]:target.write_text(json.dumps(p,indent=2)+'\n')
assert all(len(e['impact'])>=9 for e in p['experience'])
