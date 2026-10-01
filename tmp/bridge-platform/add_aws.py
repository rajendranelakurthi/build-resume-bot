import json
from pathlib import Path
p=Path('tmp/bridge-platform/plugin/assets/people/rajendra-prasad-n.json')
d=json.loads(p.read_text())
d['summary_html']='<strong>Senior Azure DevOps & Cloud Platform Engineer with 10+ years of experience in enterprise CI/CD, cloud infrastructure, and production operations.</strong> Engineers <strong>Azure and AWS platforms</strong> with Terraform, Bicep, ARM templates, and CloudFormation. Builds reusable Azure DevOps pipelines for application, infrastructure, and integration delivery across AKS, EKS/ECS, serverless, and managed application services. Integrates DevSecOps controls, observability, and operational governance while partnering with architecture, application, cloud, and security teams to improve reliability and developer self-service.'
for s in d['skill_sections']:
 if s['title']=='AWS Supporting Knowledge':
  s['title']='AWS Platform Engineering'
  s['content']='Lambda, API Gateway, ECS, EKS, S3, RDS, CloudWatch, IAM, SNS, SQS, CloudFormation, VPC, hybrid integration, cost optimization, operational governance'
 if s['title']=='Infrastructure Automation': s['content']=s['content'].replace('; AWS CloudFormation concepts',', AWS CloudFormation')
 if s['title']=='Azure Cloud Platform': s['content']=s['content'].replace('; deployment patterns for',',')
d['achievements'][1]={'tag':'Azure & AWS Platform Automation','text':'Standardized Terraform, Bicep, ARM, and CloudFormation provisioning; automated container and serverless delivery with shared security and operational controls.'}
replacements={
0:{0:'Supported Azure/AWS connectivity, troubleshooting DNS, routing, NSGs, VPC security groups, and private service access with cloud and application teams.',
1:'Deployed Docker workloads to AKS and Amazon EKS/ECS, managing Helm values, image promotion, health validation, and rollback through gated pipelines.',
3:'Built Terraform modules, Bicep/ARM templates, and AWS CloudFormation stacks for network, compute, storage, and Kubernetes lifecycle management.',
4:'Implemented Azure Monitor, Application Insights, and Amazon CloudWatch dashboards and alerts; correlated application logs with platform telemetry for root cause analysis.',
6:'Integrated Key Vault, Entra ID, Azure RBAC, and AWS IAM controls into delivery; enforced least privilege, secrets protection, and security validation.',
8:'Established deployment standards for Azure App Services, Functions, and AWS Lambda/API Gateway; documented recovery, ownership transitions, and support handoffs.'},
1:{0:'Maintained AKS and AWS ECS deployment configuration, validating container health, environment settings, and protected release inputs before promotion.',
4:'Provisioned AWS platform resources with Terraform and CloudFormation, managing S3 artifacts, IAM deployment permissions, and environment-specific parameters.',
6:'Configured CloudWatch logs and alarms for AWS workloads; partnered with application teams to diagnose failed deployments and verify restored service.',
8:'Published reusable onboarding workflows and runbooks for Azure/AWS delivery, helping teams adopt shared pipelines and manage platform transitions.'},
2:{0:'Provisioned Azure AKS and AWS EKS infrastructure with Terraform; maintained Helm releases, node configuration, environment values, and deployment validation.',
3:'Correlated Azure Monitor, Log Analytics, and CloudWatch telemetry to isolate cloud service failures; tuned alerts and verified corrective actions.',
4:'Managed Azure Storage and AWS S3-backed Terraform state, environment configuration, and infrastructure plan reviews across release stages.',
7:'Supported Azure API Management, Service Bus, and AWS Lambda/API Gateway integrations, validating identity, connectivity, and deployment dependencies.',
8:'Reviewed AWS resource utilization and storage lifecycle settings with platform teams; supported rightsizing, tagging, and cost-governance improvements.'},
3:{1:'Built Terraform modules for Azure networking/AKS and AWS VPC/EKS, providing repeatable platform provisioning for SaaS and payment workloads.',
3:'Supported AWS RDS, S3, SNS, and SQS dependencies for application releases; validated database connectivity, queue permissions, and recovery readiness.',
4:'Secured Azure/AWS pipeline credentials with Key Vault and IAM-based access; separated environment permissions and protected production deployment inputs.',
8:'Used CloudWatch with Prometheus/Grafana to investigate AWS service and container incidents; maintained operational runbooks and release evidence.'},
4:{2:'Automated Azure infrastructure with ARM templates and AWS VPC, EC2, and S3 resources with Terraform/CloudFormation; configured Linux hosts using Ansible.',
3:'Managed Azure Key Vault and AWS IAM deployment access, securing application credentials, database connectivity, and environment permissions.',
4:'Investigated Azure and AWS deployment failures with ELK, Azure Monitor, and CloudWatch; coordinated fixes and verified restored application behavior.',
8:'Maintained AWS platform deployment parameters and CloudFormation update procedures, documenting validation, rollback, and production handoffs.'},
5:{2:'Provisioned Azure resources with Terraform/ARM and AWS EC2, VPC, S3, and RDS with Terraform/CloudFormation, standardizing repeatable environment setup.',
4:'Maintained AWS IAM roles, security groups, and environment parameters for controlled application access and automated platform deployments.',
5:'Troubleshot Azure/AWS release failures using build logs and CloudWatch metrics, isolating configuration, permission, and infrastructure issues.',
8:'Documented AWS provisioning and operational runbooks; coordinated infrastructure readiness, deployment scheduling, and verified support handoffs.'}}
aws_skills=[['AWS','CloudFormation','EKS/ECS','Lambda','CloudWatch','IAM'],['AWS','Terraform','CloudFormation','ECS','CloudWatch'],['AWS','EKS','Lambda','API Gateway','CloudWatch'],['AWS','EKS','RDS','SNS/SQS','CloudWatch'],['AWS','Terraform','CloudFormation','IAM','CloudWatch'],['AWS','CloudFormation','EC2','S3','RDS','IAM']]
for i,changes in replacements.items():
 j=d['experience'][i]
 for index,bullet in changes.items(): j['impact'][index]=bullet
 j['skills_used']=list(dict.fromkeys(j['skills_used']+aws_skills[i]))
d['notes']=['User requested AWS platform engineering responsibilities across every project for the Bridge Specialty Group JD.','Aggressive role-specific wording; no insurance employment or new certifications added.']
p.write_text(json.dumps(d,indent=2)+'\n')
assert all(len(j['impact'])==9 and sum('AWS' in b or 'Amazon' in b or 'CloudWatch' in b for b in j['impact'])>=3 for j in d['experience'])
print('Verified AWS platform responsibilities in all six projects; nine bullets per role.')
