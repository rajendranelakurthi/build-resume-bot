from pathlib import Path
import json
root=Path('plugins/resume-creator-plugin')
p=json.loads((root/'assets/people/rajendra-prasad-n.json').read_text())
# Keep the complete source as reusable evidence; the default base is recruiter-focused.
archive=root/'assets/reference/rajendra-aws-source.json';archive.parent.mkdir(exist_ok=True)
if not archive.exists():archive.write_text(json.dumps(p,indent=2)+'\n')
p['page_title']='Rajendra Prasad N - Lead AWS DevOps Engineer'
p['headline']='Lead AWS DevOps Engineer | S3, VPC, IAM & Automation'
p['summary_html']='<strong>Lead AWS DevOps Engineer with 10+ years of enterprise cloud engineering, automated delivery, and production operations experience.</strong> Hands-on strength in <strong>Amazon S3, VPC networking, IAM, Terraform, CloudFormation, and CI/CD</strong>. Builds repeatable AWS infrastructure and release workflows with secure access, private service connectivity, monitoring, and recovery planning. Automates provisioning and operational support with Python, Bash, PowerShell, and AWS CLI while coordinating engineering teams through production releases and incident resolution.'
p['skills']=['AWS','S3','VPC','IAM','Terraform','CloudFormation','EKS','CodePipeline','Python','Bash','CloudWatch','CloudTrail']
p['achievements_title']='AWS Platform & Delivery Highlights'
p['achievements']=[{'tag':'Secure AWS Infrastructure','text':'Designed repeatable AWS provisioning with Terraform and CloudFormation, integrating IAM controls, VPC networking, and private service connectivity.'},{'tag':'Pipeline Automation','text':'Built reusable application and infrastructure delivery workflows with deployment checks, versioned artifacts, approvals, and environment promotion.'},{'tag':'Production Reliability','text':'Combined cloud monitoring, operational automation, incident response, and recovery runbooks to support enterprise application platforms.'}]
p['skill_sections']=[
{'title':'Amazon S3 & AWS Services','content':'Amazon S3, EC2, EKS, ECR, RDS, Lambda, AWS CLI, cloud resource administration'},
{'title':'VPC & Networking','content':'VPC, subnets, route tables, security groups, Route 53, ALB/NLB, VPN, Direct Connect, PrivateLink, VPC endpoints'},
{'title':'IAM & Security','content':'IAM roles and policies, least privilege, MFA, Secrets Manager, private networking, secure pipeline credentials, policy checks'},
{'title':'Infrastructure as Code','content':'Terraform, reusable modules, CloudFormation, Ansible, Packer, version-controlled infrastructure, environment configuration'},
{'title':'CI/CD & Workflow Automation','content':'AWS CodePipeline, CodeBuild, CodeDeploy, Jenkins, GitHub Actions, GitLab CI, job dependencies, approvals, deployment verification'},
{'title':'Observability & Recovery','content':'CloudWatch, CloudTrail, Prometheus, Grafana, Splunk, ELK, AWS Backup, Elastic Disaster Recovery, incident troubleshooting'},
{'title':'Scripting & Systems','content':'Python, Bash, PowerShell, AWS CLI, Linux, Windows Server, REST APIs, FastAPI, operational runbooks'},
{'title':'Containers & Delivery Quality','content':'Docker, Kubernetes, EKS, Helm, ArgoCD, Git, SonarQube, JFrog Artifactory, Xray, release governance'}]
indices=[[0,2,3,4,9,10,13,7,8],[0,3,4,5,6],[4,14,13,6,7,10],[0,7,2,3,9,10,11],[6,8,9,10,14],[1,4,0,8,10]]
for job,selection in zip(p['experience'],indices):job['impact']=[job['impact'][i] for i in selection]
p['certifications']=sorted(p['certifications'],key=lambda s:0 if s.startswith('AWS') else 1)
p['notes']=['AWS-only branch focus; retain all real employment titles, dates, education, and certifications.', 'Stonebranch and S3 landing/curated/archive ownership require confirmation before being added as employment claims. Source profile is retained in assets/reference.']
for f in [root/'assets/people/rajendra-prasad-n.json',Path('resume_data/people/rajendra-prasad-n.json')]:f.write_text(json.dumps(p,indent=2)+'\n')
