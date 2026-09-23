exec(compile(open('tmp/aws-data-platform/build.py').read(), 'build.py', 'exec'))
p.headline='Senior AWS Infrastructure / DevSecOps Engineer | Terraform & IaC'
p.summary_html='<strong>Terraform-focused AWS infrastructure and DevSecOps engineer with 10+ years of enterprise cloud, delivery automation, and production operations experience.</strong> Builds repeatable AWS infrastructure using <strong>Terraform modules, pipeline-driven provisioning, environment-specific configuration, and infrastructure validation</strong>. Experience spans EKS platforms, enterprise AWS environments, payment-platform infrastructure, and automated environment promotion. Combines infrastructure as code with Databricks provisioning, private networking, IAM controls, and Python/Bash automation to support secure enterprise delivery.'
p.achievements_title='Terraform & AWS Infrastructure Highlights'
p.achievements=[{'tag':t,'text':v} for t,v in [
('Reusable AWS Infrastructure','Authored Terraform modules and automated infrastructure deployments to standardize provisioning across environments.'),
('Terraform Delivery Controls','Integrated Terraform validation, secrets handling, and pre-deployment policy checks into AWS release workflows.'),
('Platform Infrastructure','Delivered Terraform-based EKS infrastructure for vector-search workloads and Terraform/Kubernetes solutions for payment-platform deployments.'),
('AWS Data Platforms','Automated Databricks environment provisioning across isolated AWS accounts with consistent networking and IAM controls.')]]
p.skill_sections[0],p.skill_sections[1]=p.skill_sections[1],p.skill_sections[0]
p.skill_sections[0]={'title':'Terraform & Infrastructure as Code','content':'Terraform modules, AWS infrastructure provisioning, CI/CD-driven Terraform deployments, Terraform validation, environment-specific configuration, CloudFormation, Ansible'}
p.skills=['Terraform','AWS','Infrastructure as Code','EKS','CI/CD','DevSecOps','Databricks on AWS','IAM','Python','Bash']
p.experience[0].impact=[
'Engineered Terraform-based AWS and EKS infrastructure for high-throughput Milvus vector-search platforms and GPU-enabled workloads.',
'Standardized AWS infrastructure provisioning with Terraform as part of repeatable platform delivery across enterprise environments.',
'Integrated Terraform validation and pre-deployment policy checks into AWS release workflows to strengthen infrastructure change governance.',
'Combined secure secrets handling, Git approvals, and artifact versioning standards with infrastructure delivery controls.',
'Automated Databricks provisioning across isolated AWS accounts, standardizing network integration, IAM controls, and environment consistency.',
'Implemented AWS PrivateLink, VPC endpoints, and private networking controls to secure application connectivity.',
'Automated AWS provisioning, support, and recovery workflows with Python, Bash, and PowerShell.',
'Built AWS CodePipeline and GitHub delivery workflows and supported production releases, incident response, and operational runbooks.']
p.experience[1].impact=[
'Supported AWS delivery environments using Terraform, GitLab CI, and Kubernetes as part of the enterprise DevOps toolchain.',
'Migrated Jenkins pipelines to GitLab CI and standardized reusable pipeline templates and controlled branch-based execution.',
'Enforced protected branches, secure runner standards, container image validation, and pipeline checks across delivery environments.',
'Administered Linux and Windows build agents and resolved pipeline, container, and Kubernetes failures with development teams.']
p.experience[2].impact=[
'Provisioned AWS infrastructure with Terraform and CloudFormation through pipeline-driven infrastructure-as-code workflows.',
'Standardized repeatable AWS infrastructure delivery using version-controlled Terraform configuration and automated deployment pipelines.',
'Designed secure AWS VPC networking, security groups, load balancing, Route 53 DNS, VPN, and Direct Connect connectivity for enterprise workloads.',
'Integrated infrastructure provisioning with EKS application delivery using GitHub Actions, Jenkins, Helm, and Kubernetes manifests.',
'Implemented AWS Backup, Elastic Disaster Recovery, and CloudWatch controls to support infrastructure recovery and operational visibility.',
'Authored reusable shell and PowerShell automation for cloud operations and release support.']
p.experience[3].impact=[
'Designed and delivered Terraform infrastructure and Kubernetes orchestration for AWS payment-platform deployments.',
'Used Terraform-based provisioning to make payment-platform infrastructure repeatable across deployment environments.',
'Built CI/CD workflows for AWS application and infrastructure changes, aligning provisioning with controlled software delivery.',
'Authored policy controls for AWS accounts and implemented MFA, identity controls, and role-based access management.',
'Automated enterprise platform onboarding and developed Python FastAPI integrations across Jenkins, Jira, and JFrog.',
'Administered CloudBees Jenkins, Artifactory, and Xray; developed Jenkins shared libraries for image versioning and artifact publication.',
'Built Python Prometheus exporters and Ansible monitoring roles for production observability.']
# HCL source documents CloudFormation, not Terraform; preserve that distinction.
p.experience[4].impact=[
'Provisioned AWS resources with CloudFormation and PowerShell, applying repeatable, auditable infrastructure-as-code practices.',
'Automated configuration enforcement for Linux and Windows EC2 fleets and managed secure access and database connectivity.',
'Supported EC2, CloudWatch, RDS, load balancing, auto scaling, Secrets Manager, and CloudFront for enterprise applications.',
'Planned AWS workload migrations and validated post-migration configuration through cutover and failover testing.',
'Integrated enterprise identity controls and strengthened privileged access, identity protection, and MFA.']
p.experience[5].impact=[
'Authored and maintained reusable Terraform modules for infrastructure provisioning and executed changes through automated CI/CD workflows.',
'Ran Terraform deployments through pipelines, using controlled environment selection to promote infrastructure changes across stages.',
'Managed environment-specific configuration and variable groups to separate deployment settings across development and production workflows.',
'Combined Terraform infrastructure automation with AWS CLI scripts to standardize cloud configuration and administrative operations.',
'Documented infrastructure, API, database, and UI deployment flows and applied Git branching standards for controlled release promotion.']
for i in [0,1,2,3,5]:
 job=p.experience[i]
 job.skills_used=['Terraform']+[v for v in job.skills_used if v!='Terraform']
p.notes.append('Terraform-focused revision; HCL retains source-documented CloudFormation experience. Snowflake and Unity Catalog remain unclaimed.')
s.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
s.with_suffix('.html').write_text(BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p))
