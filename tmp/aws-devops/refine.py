import sys,json
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
root=Path('plugins/resume-creator-plugin/assets')
p=BundledJsonResumeStore(root/'people',root/'static').load_person('rajendra-prasad-n')
source=p
p,keywords=tailor_profile(p,'AWS Cloud AWS Administration Databricks Terraform S3 EC2 CloudTrail CloudWatch DevOps CI/CD Python Bash PowerShell')
p.page_title='Rajendra Prasad N - Lead AWS DevOps Engineer'
p.headline='Lead AWS DevOps Engineer | Terraform & Cloud Administration'
p.summary_html='<strong>Lead AWS DevOps Engineer with 10+ years of enterprise cloud engineering, systems engineering, CI/CD, and production operations experience.</strong> Hands-on expertise in <strong>AWS administration, Terraform infrastructure as code, EC2, S3, CloudWatch, and CloudTrail</strong>, backed by Linux and Windows systems experience. Automated <strong>Databricks environments on AWS</strong> across isolated accounts with network integration and IAM controls. Builds repeatable delivery pipelines and automates provisioning, operational support, and recovery using <strong>Python, Bash, PowerShell, and AWS CLI</strong>.'
p.achievements_title='AWS Engineering Highlights'
p.achievements=[source.achievements[1],{'tag':'Databricks on AWS','text':'Automated Databricks environment provisioning across isolated AWS accounts with standardized networking, IAM controls, and environment configuration.'},{'tag':'Cloud Automation','text':'Automated provisioning, platform support, and recovery workflows with Python, Bash, and PowerShell.'},source.achievements[3]]
p.skill_sections=[{'title':'AWS Cloud & Administration','content':'AWS, EC2, S3, IAM, VPC, EKS, ECR, RDS, Lambda, Route 53, ALB/NLB, CloudFront, AWS CLI'},{'title':'Infrastructure as Code','content':'Terraform, reusable modules, CloudFormation, Ansible, Packer, infrastructure pipelines, configuration automation'},{'title':'Databricks on AWS','content':'Environment provisioning, isolated AWS accounts, network integration, IAM controls, environment consistency'},{'title':'Monitoring & Audit','content':'Amazon CloudWatch, AWS CloudTrail, Prometheus, Grafana, Splunk, ELK, production troubleshooting'},{'title':'DevOps & CI/CD','content':'AWS CodePipeline, CodeBuild, CodeDeploy, Jenkins, GitHub Actions, GitLab CI, Git, artifact versioning, deployment approvals'},{'title':'Scripting & Systems Engineering','content':'Python, Bash, PowerShell, Linux, RHEL, Ubuntu, Windows Server, Docker, Kubernetes, Helm'}]
selections=[[10,9,0,3,4,13,7,8],[6,0,3,4],[4,14,13,6,7,10],[0,7,9,3,11],[8,14,6,9,10,12],[1,4,0,9]]
for job,base,indices in zip(p.experience,source.experience,selections):
    job.impact=[base.impact[i] for i in indices]

p.experience[0].impact[1:1] = [
    "Provisioned and administered Databricks all-purpose and job clusters on AWS, configuring runtime versions, autoscaling, auto-termination, and workload-specific compute settings.",
    "Configured Databricks serverless compute for supported analytics workloads, managing access, usage monitoring, and connectivity to governed AWS data sources.",
    "Implemented Unity Catalog governance through catalogs, schemas, grants, and storage credentials to control access to shared data assets.",
    "Integrated Amazon S3 data stores with Databricks through IAM roles and external locations, supporting governed access to Delta tables and analytics datasets.",
    "Automated deployment and scheduling of Databricks data pipelines and jobs, managing task dependencies, parameters, failure notifications, and recovery workflows.",
    "Defined cluster policies to standardize runtime selection, instance types, autoscaling limits, tagging, and auto-termination across engineering teams."
]
p.experience[1].impact[0:0] = [
    "Supported Databricks clusters on AWS, maintaining compute configuration, runtime compatibility, libraries, and job execution settings across development and test environments.",
    "Supported serverless SQL warehouse access and query troubleshooting for analytics teams working with AWS-backed datasets.",
    "Administered Unity Catalog permissions for catalogs, schemas, and tables, aligning data access with team roles and environment requirements.",
    "Configured access to S3-backed data stores and supported Delta table availability by troubleshooting IAM permissions, storage paths, and data access failures.",
    "Integrated Databricks notebook and job changes into GitLab CI/CD workflows and supported scheduled pipeline execution, dependency checks, and failure diagnosis.",
    "Applied cluster policies for approved compute configurations, autoscaling limits, and idle termination to standardize resource usage across environments."
]
for job in p.experience[:2]:
    job.skills_used = list(dict.fromkeys(job.skills_used + ['Databricks on AWS', 'Unity Catalog', 'Amazon S3']))
p.skill_sections[2]['content']='Clusters, serverless compute, Unity Catalog, S3 data stores, Delta tables, jobs and data pipelines, cluster policies, IAM integration'

p.experience[0].impact = [b for b in p.experience[0].impact if not b.startswith("Authored technical documentation")]
p.certifications=sorted(p.certifications,key=lambda c:0 if c.startswith('AWS') else 1)
h=BundledHtmlResumeRenderer(root/'templates/base_resume.html').render(p)
h=h.replace('</style>','@media print{html,body{width:auto;} .header-left{flex:1;min-width:0;} .header-right{flex:0 0 51mm;} .job-header{flex-direction:row;} .cert-badge-svg{max-width:48px;} .cert-card{min-height:72px;} .summary-box{margin-bottom:8px;} .section-title{margin-top:12px;} .job-block{break-inside:auto;page-break-inside:auto;} .job-header,.job-details{break-after:avoid;} li{break-inside:avoid;} }\n</style>')
out=Path('output/pdf/rajendra-prasad-n-aws-devops-databricks-aggressive')
out.with_suffix('.html').write_text(h)
out.with_suffix('.json').write_text(json.dumps({'level':'Aggressive','profile':asdict(p)},indent=2))
print(out.with_suffix('.html'))
