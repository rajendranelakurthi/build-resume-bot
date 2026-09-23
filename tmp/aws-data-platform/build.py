import sys,json
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
jd='Senior AWS Infrastructure/DevSecOps Engineer. AWS Infrastructure + Terraform/IaC. Databricks on AWS: workspace, networking, Unity Catalog, security. Snowflake administration: accounts, warehouses, RBAC/security. CI/CD and DevSecOps. Python/Bash scripting and enterprise cloud environments.'
p,kw=tailor_profile(b,jd)
p.page_title='Rajendra Prasad N - Senior AWS Infrastructure / DevSecOps Engineer'
p.headline='Senior AWS Infrastructure / DevSecOps Engineer'
p.summary_html='<strong>AWS infrastructure and DevSecOps engineer with 10+ years of enterprise cloud, release automation, and production operations experience.</strong> Hands-on delivery of <strong>Terraform infrastructure, Databricks environments on AWS, secure networking, IAM controls, and CI/CD platforms</strong>. Automates multi-account provisioning and operational workflows with Python and Bash; integrates secrets handling, Terraform validation, and policy checks into delivery pipelines. Experienced with AWS PrivateLink, VPC endpoints, EKS, and enterprise reliability practices.'
p.skills=['AWS','Terraform','Databricks on AWS','DevSecOps','CI/CD','IAM','PrivateLink','Python','Bash','EKS']
p.achievements=p.achievements[:3]
p.achievements.insert(1,{'tag':'Databricks on AWS','text':'Automated provisioning across isolated AWS accounts with standardized network integration, IAM controls, and consistent environments.'})
p.skill_sections=[{'title':t,'content':s} for t,s in [
('AWS Infrastructure & Networking','AWS multi-account environments, EC2, VPC, IAM, S3, EKS, Route 53, ALB/NLB, PrivateLink, VPC endpoints, VPN, Direct Connect'),
('Infrastructure as Code','Terraform, reusable Terraform modules, CloudFormation, Ansible, AWS CLI, pipeline-driven provisioning'),
('Databricks on AWS','Environment provisioning, isolated AWS accounts, network integration, IAM controls, environment consistency'),
('CI/CD & DevSecOps','CodePipeline, GitHub Actions, GitLab CI, Jenkins, secure secrets handling, Terraform validation, policy checks, SonarQube, Fortify, Black Duck, JFrog Xray'),
('Scripting & Platforms','Python, Bash, PowerShell, Linux, Docker, Kubernetes, Helm, ArgoCD'),
('Security & Reliability','IAM, MFA, role-based access controls, private networking, CloudWatch, CloudTrail, Prometheus, Grafana, AWS Backup, AWS Elastic Disaster Recovery')]]
# Prioritize source-supported accomplishments for this role.
indices=[[10,13,9,4,3,0,7,8],[6,7,5,9],[4,14,6,13,7,10],[0,2,3,7,9,10,11],[6,8,9,11,14],[1,3,4,9]]
for job,source,idx in zip(p.experience,b.experience,indices):job.impact=[source.impact[i] for i in idx]
s=Path('output/pdf/rajendra-prasad-n-devops-cloud-aggressive-senior-aws-infrastructure-devsecops-engineer-hands-on-aws')
s.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
s.with_suffix('.jd.txt').write_text(jd)
s.with_suffix('.html').write_text(BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p))
