import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(base,'Lead AWS DevOps Engineer CodePipeline CloudFormation Python AWS GCP Docker Kubernetes Jenkins Ansible Elasticsearch Solr Kibana Splunk Prometheus Grafana Couchbase JMeter JavaScript JSON SonarQube Agile')
p.page_title='Rajendra Prasad N - DevOps Cloud & Automation Engineer'
p.headline='Lead DevOps Engineer | AWS, GCP, Python & Kubernetes'
p.summary_html='<strong>Lead DevOps Engineer with 10+ years of enterprise experience in cloud infrastructure, CI/CD, application deployments, and production operations.</strong> Hands-on focus on <strong>Python automation, AWS and GCP, Docker, Kubernetes, Jenkins, Git, and Ansible</strong>. Supports search and data platforms using Elasticsearch, Solr, and Couchbase; builds observability with Kibana, Splunk, Prometheus, and Grafana. Integrates SonarQube quality gates and JMeter performance checks into delivery workflows, using JavaScript, JSON, and REST APIs for operational tooling. Collaborates with Agile teams on release readiness, troubleshooting, and reliability, including Healthcare Payer application support through Mphasis/HPE.'
p.achievements_title='Cloud, Automation & Platform Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Cloud & Automation','Reusable Python tooling, Ansible roles, and CI/CD pipelines standardize cloud provisioning and Kubernetes application delivery.'),
('Search & Observability','Operational monitoring connects search-cluster health, application logs, infrastructure metrics, and actionable alerts.'),
('Release Quality','Automated code analysis, API validation, and performance testing provide evidence for release and capacity decisions.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Cloud Platforms','AWS: EC2, S3, EKS, ECR, IAM, VPC, CloudWatch; GCP: Compute Engine, GKE, Cloud Storage, IAM, Cloud Monitoring'),
('Programming & Automation','Python, Bash, JavaScript, JSON, REST APIs, AWS CLI, gcloud CLI, operational tooling, deployment checks'),
('CI/CD & Source Control','Jenkins, Jenkinsfiles, shared libraries, Git, GitLab CI/CD, GitHub Actions, artifact promotion, approval gates, rollback'),
('Containers & Configuration','Docker, Kubernetes, EKS, GKE, Helm, Ansible roles and playbooks, Linux, Terraform, CloudFormation'),
('Search & Data Platforms','Elasticsearch, Solr / SolrCloud, Couchbase, index and collection operations, cluster health, backup and recovery'),
('Monitoring & Observability','Kibana, Splunk, Prometheus, Grafana, CloudWatch, Cloud Monitoring, centralized logging, metrics, dashboards, alerts'),
('Quality & Performance','SonarQube, JMeter, SAST, dependency and image scanning, REST/JSON validation, load tests, latency and throughput analysis'),
('Delivery & Domain','Agile, Scrum, Jira, release management, DevOps & Automation, incident response, root-cause analysis; Healthcare Payer application support')]]
specs=[
(['Python','AWS','GCP','EC2','S3','Jenkins','Ansible','Kubernetes','Elasticsearch','Solr','Couchbase','JMeter'],[
'Led DevOps automation across AWS and GCP environments, coordinating application delivery, platform changes, operational readiness, and production troubleshooting with Agile engineering teams.',
'Developed Python automation for AWS EC2 lifecycle operations, S3 artifact validation, resource inventory, environment checks, and deployment reporting using cloud APIs and structured JSON payloads.',
'Automated GCP Compute Engine and GKE environment setup with Terraform, Ansible, and gcloud workflows, managing service accounts, network configuration, and application deployment prerequisites.',
'Built Jenkins pipelines and shared libraries for Git-based builds, automated tests, SonarQube analysis, artifact publication, environment approvals, deployment, and rollback verification.',
'Containerized services with Docker and delivered workloads to Kubernetes on EKS and GKE using Helm, readiness probes, resource limits, autoscaling, and controlled rollout procedures.',
'Administered Elasticsearch cluster operations, including index templates, shard allocation, retention policies, snapshot validation, and investigation of indexing failures, disk pressure, and slow queries.',
'Supported SolrCloud deployments and collection administration, managing configuration sets, replicas, index updates, and query-health checks with application teams during upgrades and releases.',
'Supported Couchbase cluster maintenance through bucket configuration, resource monitoring, controlled rebalance operations, backup execution, and restore validation in coordination with database teams.',
'Implemented centralized logging with Elasticsearch/Kibana and Splunk, creating deployment-focused searches, dashboards, and alerts to diagnose application errors and infrastructure failures.',
'Built Prometheus and Grafana dashboards for Kubernetes, application, and search-service metrics, correlating latency, throughput, errors, and saturation with deployment events.',
'Integrated JMeter CLI load tests into Jenkins, parameterizing test data and concurrency, publishing reports, and comparing response-time percentiles and error rates against agreed release thresholds.',
'Created JavaScript utilities and Python REST integrations for JSON validation, deployment smoke tests, and status reporting; incorporated peer review and Agile retrospectives into automation improvements.'
]),
(['AWS','Python','Jenkins','Git','Ansible','Docker','Kubernetes','SonarQube'],[
'Built reusable Jenkins and GitLab CI/CD workflows for Git-based application builds, automated tests, versioned artifacts, and controlled environment promotion.',
'Configured Linux build agents and container runners, resolving toolchain, cache, dependency, permission, and capacity issues affecting delivery workflows.',
'Automated application installation and environment setup with Ansible roles and Python scripts, separating configuration values and secrets from deployable artifacts.',
'Integrated SonarQube quality gates and container checks into pipelines, coordinating defect remediation and exception reviews before production releases.',
'Deployed Docker-based Kubernetes services with versioned manifests, health probes, configuration validation, and rollout verification.',
'Partnered with developers and QA in Agile ceremonies to investigate deployment failures, refine smoke tests, and document rollback and support procedures.'
]),
(['AWS','GCP','Python','Terraform','Docker','Kubernetes','Jenkins','Prometheus','Grafana'],[
'Provisioned AWS and GCP application environments using reusable Terraform definitions and pipeline-driven changes for compute, networking, identities, and storage.',
'Automated EC2 and Compute Engine operational checks with Python and shell scripts, including inventory, configuration verification, service status, and resource cleanup.',
'Delivered Docker microservices to Kubernetes through Jenkins, GitHub Actions, Helm, and ArgoCD workflows with controlled promotion and post-deployment validation.',
'Managed S3 and Cloud Storage workflows for release artifacts, operational exports, and recovery inputs using scoped access and retention settings.',
'Implemented Prometheus and Grafana dashboards alongside cloud monitoring to track workload health, capacity, and deployment-related service degradation.',
'Investigated centralized application logs and cluster metrics to isolate network, container, resource, and dependency failures across cloud environments.',
'Supported backup and recovery procedures and collaborated with distributed development teams on release readiness, incident reviews, and operational documentation.'
]),
(['AWS','Python','Jenkins','Ansible','Prometheus','Grafana','Elasticsearch','Kibana','Splunk','JMeter'],[
'Designed Jenkins and GitHub Actions workflows for application and infrastructure deployments, standardizing build, test, package, and release stages.',
'Developed internal Python FastAPI integrations for Jenkins, Jira, and JFrog, using JSON-based APIs to automate onboarding, deployment status, and operational tasks.',
'Authored reusable Ansible roles to deploy highly available Prometheus, Grafana, and Node Exporter stacks with consistent configuration and service checks.',
'Built custom Python Prometheus exporters to expose application-specific metrics and improve incident diagnosis and capacity analysis.',
'Used Elasticsearch/Kibana and Splunk for centralized log analysis, correlating application errors with infrastructure signals and recent releases.',
'Partnered with QA on JMeter load-test execution and analyzed test results alongside Grafana metrics to investigate bottlenecks and validate configuration changes.',
'Administered Jenkins and JFrog tooling, built shared deployment libraries, and participated in Agile incident reviews and release retrospectives.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=base.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
prior=json.loads(Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-aws-devops-ansible-release-aggressive.profile.json').read_text())
for i in [4,5]:
 p.experience[i].title=prior['experience'][i]['title']
 p.experience[i].skills_used=prior['experience'][i]['skills_used']
 p.experience[i].impact=prior['experience'][i]['impact']
p.skills=['Python','AWS','GCP','S3','EC2','Docker','Kubernetes','Jenkins','Git','Ansible','Elasticsearch','Solr','Kibana','Splunk','Prometheus','Grafana','Couchbase','JMeter','JavaScript','JSON','SonarQube','Agile','DevOps & Automation']
p.notes=['Aggressive variant requested by user; expanded multicloud, search, database operations and performance-testing responsibilities. Employment history and certifications retained.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-aws-gcp-python-devops-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.section-title{margin-top:12px}.skill-card{padding:6px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text(', '.join(p.skills))
manifest={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':sum(len(j.impact) for j in p.experience),'sources':['https://solr.apache.org/guide/solr/latest/deployment-guide/metrics-reporting.html','https://docs.couchbase.com/server/current/manage/manage-backup-and-restore/manage-backup-and-restore.html','https://jmeter.apache.org/usermanual/get-started','https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics']}
stem.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
