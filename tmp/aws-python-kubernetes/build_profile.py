from pathlib import Path
import json
root=Path('plugins/resume-creator-plugin/assets')
p=json.loads((root/'reference/rajendra-aws-source.json').read_text())
p['page_title']='Rajendra Prasad N - Lead AWS DevOps Engineer'
p['headline']='Lead AWS DevOps Engineer | Python, Kubernetes & CI/CD'
p['summary_html']='<strong>Lead AWS DevOps Engineer with 10+ years of enterprise cloud engineering, release automation, and production operations experience.</strong> Develops <strong>Python tooling, FastAPI integrations, CI/CD platforms, and Kubernetes infrastructure</strong> across AWS environments. Hands-on expertise with GitHub Actions, GitLab CI/CD, Jenkins, Terraform, CloudFormation, Ansible, Docker, EKS, and Argo CD. Combines secure infrastructure automation with Prometheus/Grafana observability, incident troubleshooting, technical coaching, and cross-team release leadership.'
p['achievements_title']='AWS Automation & Engineering Leadership'
p['achievements']=[
{'tag':'Python Platform Tooling','text':'Developed FastAPI integrations for Jenkins, Jira, and JFrog and custom Prometheus exporters to connect delivery automation with operational visibility.'},
{'tag':'CI/CD Architecture','text':'Standardized reusable pipelines, runner infrastructure, source-control governance, artifact versioning, and controlled environment promotion.'},
{'tag':'Kubernetes & Reliability','text':'Delivered EKS workloads using Terraform, Helm, and GitOps workflows and integrated monitoring, security controls, and production support.'}]
p['skills']=['Python','Bash','AWS','EKS','Kubernetes','Docker','Terraform','Ansible','CloudFormation','GitHub Actions','GitLab CI/CD','Jenkins','Argo CD']
p['skill_sections']=[
{'title':'Python & Automation','content':'Python, FastAPI, REST API integrations, custom Prometheus exporters, Bash/Shell, PowerShell, AWS CLI, YAML, JSON'},
{'title':'CI/CD Architecture','content':'GitHub Actions, GitLab CI/CD, Jenkins, CloudBees, CodePipeline, CodeBuild, CodeDeploy, reusable workflows, runners, shared libraries'},
{'title':'AWS Cloud Engineering','content':'EC2, ECS, EKS, ECR, Lambda, S3, RDS, VPC, IAM, Route 53, ALB/NLB, CloudFront, private connectivity'},
{'title':'Infrastructure as Code','content':'Terraform, reusable modules, CloudFormation, Ansible roles/playbooks, Packer, reviewed infrastructure changes, environment configuration'},
{'title':'Containers & GitOps','content':'Docker, Kubernetes, EKS, Helm, Argo CD, OpenShift, Rancher, manifests, application configuration, cluster administration'},
{'title':'Observability & Reliability','content':'Prometheus, Grafana, ELK, CloudWatch, CloudTrail, Splunk, AWS Backup, Elastic Disaster Recovery, incident response, runbooks'},
{'title':'DevSecOps & Governance','content':'IAM, MFA, Secrets Manager, private endpoints, pipeline policy checks, branch protection, SonarQube, Fortify, Black Duck, JFrog Xray'},
{'title':'Engineering Leadership','content':'Technical coaching, release planning, architecture documentation, cross-team coordination, Agile/Scrum, knowledge transfer, Linux/Windows operations'}]
# Select supported work, preserving role titles, dates, employers and credentials.
indices=[[3,0,9,12,4,13,2,1,7,8],[6,7,8,0,4,5],[4,3,6,7,5,13,14],[9,11,7,12,6,10,13],[7,5,6,9,14,4],[1,9,4,0,6]]
for job,selection in zip(p['experience'],indices):
 job['impact']=[job['impact'][i].replace('ArgoCD','Argo CD') for i in selection]
job=p['experience'][0]
job['skills_used']=['AWS','Python','Bash','Terraform','EKS','GitHub Actions','CodePipeline','Helm']
job['impact'][0]='Developed Python, Bash, and PowerShell automation for provisioning, platform support, and recovery workflows, reducing manual operational effort.'
job['impact'][1]='Architected reusable CI/CD pipelines with AWS CodePipeline and GitHub workflows to automate build, test, and release execution across engineering teams.'
job['impact'][2]='Designed Terraform-based EKS infrastructure for high-throughput vector search and GPU-enabled workloads, integrating repeatable provisioning with container delivery.'
job['impact'][7]='Directed release planning across engineering teams, aligning dependencies, change windows, delivery risks, and production support.'
p['experience'][1]['skills_used']=['GitLab CI/CD','Jenkins','Docker','Kubernetes','Git','Linux','AWS']
p['experience'][3]['skills_used']=['Python','FastAPI','Jenkins','GitHub Actions','Terraform','Ansible','Kubernetes','Prometheus','JFrog']
p['certifications']=sorted(p['certifications'],key=lambda c:0 if c.startswith('AWS') else 1)
p['notes']=['JD-tailored AWS Python/Kubernetes variant. All six employers, titles, dates, education, and certifications preserved from the saved source.', 'Saved history begins August 2016: retain 10+ years, not the JD requirement of 12+. Do not claim CKA or AWS DevOps Engineer certification without evidence.', 'No new quantified outcomes or Kubernetes upgrade ownership inferred solely from the JD.']
(root/'variants/rajendra-aws-python-kubernetes.json').write_text(json.dumps(p,indent=2)+'\n')
