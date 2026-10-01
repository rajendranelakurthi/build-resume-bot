import json,shutil
from pathlib import Path
root=Path('tmp/databricks-platform/plugin')
shutil.copytree('plugins/resume-creator-plugin',root,dirs_exist_ok=True)
p=json.loads((root/'assets/people/rajendra-prasad-n.json').read_text())
p['full_name']='Rajendra P N';p['page_title']='Rajendra P N - Databricks Platform Engineer';p['headline']='Databricks Platform Engineer | AWS | Terraform';p['certification_badges_alt']='Rajendra P N certification badges'
p['summary_html']='<strong>Databricks Platform Engineer with 10+ years of cloud infrastructure, DevOps, and platform automation experience.</strong> Specializes in <strong>AWS Databricks workspace provisioning, Terraform, IAM, Unity Catalog, and compute governance</strong>. Automates metastores, storage access, cluster policies, SQL warehouses, jobs, notebooks, and pipeline configuration with controlled infrastructure delivery. Supports serverless compute, Snowflake platform provisioning, and selected Azure Databricks environments, partnering with data teams on secure access, reliability, and cost management.'
p['skills']=['AWS','Databricks','Terraform','Unity Catalog','IAM','S3','Cluster Policies','SQL Warehouses','Snowflake','Python','Azure Databricks']
p['skill_sections']=[
{'title':'AWS Databricks Infrastructure','content':'Account/workspace provisioning, Terraform AWS and Databricks providers, VPC, subnets, security groups, S3, cross-account IAM, PrivateLink, KMS'},
{'title':'Unity Catalog & Access','content':'Regional metastores, workspace assignments, catalogs, schemas, storage credentials, external locations, grants, groups, service principals, least privilege'},
{'title':'Compute & Workspace Management','content':'Cluster policies, runtime controls, autoscaling, auto-termination, SQL warehouses, serverless compute, jobs, notebooks, pipeline configuration, permissions'},
{'title':'Terraform & Platform Delivery','content':'Reusable modules, remote state, environment isolation, plan/apply approvals, drift checks, GitHub Actions, Jenkins, GitLab CI, Python, Bash, Databricks CLI/APIs'},
{'title':'Snowflake Platform Automation','content':'Terraform Snowflake provider, databases, schemas, virtual warehouses, roles, grants, storage integrations, S3 external stages, resource monitors'},
{'title':'Azure Databricks & Operations','content':'Azure managed workspaces, VNet integration, ADLS Gen2, managed identities, Key Vault; CloudWatch, audit logs, access troubleshooting, cost controls, runbooks'}]
p['achievements_title']='Databricks Platform & Infrastructure Highlights'
p['achievements']=[{'tag':'AWS Workspace Automation','text':'Provisioned Databricks environments with reusable Terraform, integrating AWS networking, storage, IAM, and controlled workspace configuration.'},{'tag':'Governed Platform Access','text':'Standardized Unity Catalog, metastore assignments, storage access, and compute policies to support consistent enterprise platform controls.'},{'tag':'Operational Readiness','text':'Automated jobs, notebook and pipeline configuration, SQL warehouses, and Snowflake resources with release checks and support documentation.'}]
first=[[
'Automated AWS Databricks workspace provisioning with Terraform, separating account-level infrastructure from workspace configuration across isolated environments.',
'Configured VPCs, private subnets, security groups, S3 storage, and cross-account IAM roles; implemented PrivateLink connectivity for supported workspace access paths.',
'Provisioned regional Unity Catalog metastores and workspace assignments, organizing catalogs, schemas, and grants for controlled data-platform access.',
'Managed storage credentials and external locations backed by S3 and IAM trust policies, troubleshooting permissions and service-principal access.',
'Authored cluster policies controlling approved runtimes, instance families, autoscaling limits, tags, and auto-termination for classic compute.',
'Enabled serverless compute for supported notebooks, jobs, and pipelines; configured access and usage controls separately from classic cluster policies.',
'Provisioned Databricks SQL warehouses with sizing, scaling, auto-stop, and permission settings; supported serverless SQL for eligible workloads.',
'Automated jobs, notebook deployment, task dependencies, schedules, retries, and pipeline configuration through Terraform and Databricks APIs.',
'Provisioned Snowflake warehouses, databases, schemas, roles, grants, and S3 storage integrations with Terraform, including cost and access controls.',
'Supported Azure Databricks managed workspaces, ADLS Gen2 access through managed identities, and Key Vault integration for selected environments.',
'Integrated Terraform plan/apply approvals, state isolation, configuration checks, monitoring, and runbooks into platform delivery and incident response.'
],[
'Provisioned and maintained AWS Databricks workspaces with Terraform modules and environment-specific configuration for development and release environments.',
'Configured AWS IAM roles, S3 access, VPC networking, and security-group rules required for Databricks workspace connectivity.',
'Configured Unity Catalog metastore assignments, catalogs, schemas, and access grants to support consistent workspace governance.',
'Maintained storage credentials and external locations, validating IAM trust and S3 permissions with data-platform teams.',
'Standardized cluster policies for runtime versions, compute sizing, autoscaling, tags, and idle termination.',
'Managed SQL warehouse configuration, user access, startup behavior, and cost settings for shared analytics environments.',
'Configured Databricks jobs, notebook paths, task parameters, schedules, retries, and pipeline permissions for repeatable execution.',
'Automated Snowflake warehouse, schema, role, and grant configuration with Terraform to keep platform settings version-controlled.',
'Supported Azure Databricks workspace configuration, ADLS access, and secret integration alongside AWS platform delivery.',
'Integrated workspace changes with GitLab CI, reviewed Terraform plans, and maintained separate variables and credentials across environments.',
'Troubleshot workspace provisioning, cluster startup, job configuration, and access failures; documented corrective actions and release checks.'
],[
'Delivered AWS Databricks workspace infrastructure through Terraform, standardizing networking, storage, IAM, and environment configuration.',
'Established cross-account IAM trust and S3 access policies, resolving network and permission issues affecting workspace provisioning.',
'Supported Unity Catalog adoption and metastore-to-workspace assignments as governance capabilities became available during the engagement.',
'Configured catalog and schema permissions and external storage access, coordinating identity and ownership requirements with platform teams.',
'Maintained cluster policies covering runtime selection, node sizing, autoscaling, tags, and auto-termination.',
'Configured Databricks SQL warehouses and access permissions, supporting startup, capacity, and connectivity troubleshooting.',
'Automated notebook deployment and job configuration, including schedules, task parameters, dependencies, and failure notifications.',
'Managed pipeline environment settings, execution permissions, and storage dependencies to support controlled releases.',
'Provisioned Snowflake platform resources with Terraform, organizing warehouses, databases, schemas, and role-based grants.',
'Supported Azure Databricks managed workspace and storage configuration while delivering the majority of platform infrastructure on AWS.',
'Built Jenkins and GitHub Actions workflows for infrastructure validation and deployment; maintained Python automation and platform runbooks.'
]]
for e,bullets in zip(p['experience'],first):
 e['impact']=bullets;e['skills_used']=['AWS','Databricks','Terraform','Unity Catalog','IAM','S3','Snowflake','Azure Databricks']
extras=[
['Maintained Git controls and deployment approvals for infrastructure changes, coordinating release readiness with application and platform owners.'],
['Automated Linux server configuration with Ansible and scripts to keep environment dependencies consistent.', 'Maintained environment-specific infrastructure settings, secrets access, and deployment validation with application teams.', 'Coordinated production release readiness, recovery steps, and post-deployment checks across development and operations.', 'Investigated infrastructure and application failures through logs and monitoring, documenting corrective actions and support procedures.'],
['Authored reusable Terraform modules and promoted reviewed infrastructure changes through CI/CD workflows.', 'Automated cloud administration and deployment checks with Python and shell scripts.', 'Managed Ansible playbooks for repeatable Linux configuration and application release preparation.', 'Troubleshot build-agent, dependency, and environment failures with development and support teams.', 'Documented infrastructure dependencies, deployment procedures, and verification steps for operational handoffs.']]
for e,add in zip(p['experience'][3:],extras):e['impact']+=add
assert all(len(e['impact'])>=9 for e in p['experience'])
p['notes']=['Display name Rajendra P N; 10+ years; minimum nine points per role.','AWS-first Databricks platform variant with detailed responsibilities across first three roles, expanded as explicitly requested by user. Source PDF supports AWS Databricks provisioning; detailed governance/Snowflake/Azure scope added per request.','Use current serverless notebook/job/pipeline scope only in current role; preserve historical job titles and dates.']
(root/'assets/people/rajendra-prasad-n.json').write_text(json.dumps(p,indent=2)+'\n')
# Preserve the authored summary while using the packaged ranking and export workflow.
q=root/'scripts/plugin_core.py';s=q.read_text();needle='def build_summary(profile: PersonProfile, matched_keywords: list[str], missing_keywords: list[str]) -> str:\n';s=s.replace(needle,needle+'    if profile.summary_html:\n        return profile.summary_html\n',1);q.write_text(s)
for q in [root/'assets/templates/base_resume.html']:
 s=q.read_text().replace('@media (max-width:900px)','@media screen and (max-width:900px)').replace('@media (max-width:560px)','@media screen and (max-width:560px)');s=s.replace('.job-block{margin-bottom:12px;}','.job-block{margin-bottom:12px;break-inside:auto;page-break-inside:auto;}');q.write_text(s)
out=Path('tailored_resume/rajendra-prasad-n');out.mkdir(parents=True,exist_ok=True)
(out/'Rajendra-P-N-Databricks-Platform.profile.json').write_text(json.dumps(p,indent=2)+'\n')
