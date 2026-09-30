import json,copy
from pathlib import Path
root=Path('plugins/resume-creator-plugin/assets')
p=json.loads((root/'variants/rajendra-aws-python-kubernetes.json').read_text())
s=json.loads((root/'reference/rajendra-aws-source.json').read_text())
p['page_title']='Rajendra Prasad N | Lead AWS DevOps Engineer'
p['headline']='Lead AWS DevOps Engineer | Infrastructure, Security & Integration'
p['summary_html']='<strong>Lead AWS DevOps Engineer with 13+ years of overall IT experience spanning build and release engineering, enterprise cloud infrastructure, automation, and production operations.</strong> Delivers <strong>AWS infrastructure, Terraform and CloudFormation automation, secure CI/CD, and application integration</strong> across multiple environments. Combines VPC networking, IAM controls, Secrets Manager, EC2, managed databases, and EKS with Python/Bash tooling, observability, incident response, and recovery planning. Leads cross-team release coordination, technical coaching, and operational documentation.'
p['achievements_title']='AWS INFRASTRUCTURE & DELIVERY LEADERSHIP'
p['achievements']=[{'title':'Secure AWS Infrastructure','text':'Delivered VPC networking, private service connectivity, identity controls, and repeatable Terraform/CloudFormation provisioning for enterprise workloads.'},{'title':'Application & Platform Integration','text':'Built Python FastAPI integrations for delivery tooling and supported microservices, database connectivity, certificates, and environment readiness.'},{'title':'Reliable Delivery & Operations','text':'Standardized CI/CD controls, coordinated production releases, and implemented monitoring, backup, and disaster-recovery capabilities.'}]
# Match schema of highlights used by renderer.
print('highlight source',s['achievements'][0])
p['skill_sections']=[{'title':a,'content':b} for a,b in [
('AWS Infrastructure & Networking','EC2, VPC, Route 53, security groups, ALB/NLB, PrivateLink, VPC endpoints, VPN, Direct Connect, S3'),
('Security & Governance','IAM, role-based access, MFA, Secrets Manager, certificate management, policy controls, SonarQube, Fortify, Black Duck, JFrog Xray'),
('Infrastructure as Code','Terraform modules, CloudFormation, Ansible, configuration enforcement, infrastructure validation, environment provisioning'),
('CI/CD & Source Control','GitHub Actions, GitLab CI, Jenkins, CodePipeline, CodeBuild, CodeDeploy, Git branching, approvals, artifact versioning'),
('Application & Database Integration','REST APIs, FastAPI, Java/Node.js microservices, Amazon RDS, Amazon Aurora, PostgreSQL, environment configuration'),
('Automation & Linux','Python, Bash/Shell, PowerShell, AWS CLI, Linux, RHEL, Ubuntu, API-driven platform automation'),
('Containers & Reliability','Docker, Kubernetes, EKS, Helm, Argo CD, CloudWatch, CloudTrail, Prometheus, Grafana, ELK, AWS Backup, Elastic Disaster Recovery'),
('Technical Leadership','Release coordination, architecture documentation, technical coaching, incident response, production support, runbooks, Agile/Scrum')]]
indices=[[13,10,0,4,3,5,1,7,8],[7,5,9,8,0],[14,4,13,6,11,12],[2,3,9,11,12,10],[8,14,6,7,9,2],[1,9,10,4,7]]
calin=copy.deepcopy(p['experience'][-1]);p['experience']=[]
for job,ii in zip(s['experience'],indices):
 j=copy.deepcopy(job);j['impact']=[job['impact'][i] for i in ii];p['experience'].append(j)
p['experience'].append(calin)
p['notes']=[n for n in p['notes'] if 'Python/Kubernetes' not in n]+['AWS infrastructure/integration JD variant. Aurora and PostgreSQL retained as source-listed skills; Aurora PostgreSQL administration, KMS ownership, and automatic secret rotation are not claimed without candidate confirmation.']
(root/'variants/rajendra-aws-infrastructure-integration.json').write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n')
