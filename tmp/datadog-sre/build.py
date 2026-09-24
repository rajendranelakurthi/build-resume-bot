import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
p,_=tailor_profile(b,'Azure DevOps GitHub Actions Terraform Datadog SRE observability AWS Rundeck Ansible AIOps')
p.headline='Lead SRE | Azure & AWS'
p.page_title='Rajendra Prasad N - Lead SRE - Azure & AWS'
p.summary_html='<strong>Lead Site Reliability and Observability engineer with 10+ years of enterprise experience across cloud infrastructure, application delivery, monitoring, and production operations.</strong> Builds <strong>Datadog observability for Azure and AWS</strong> spanning infrastructure, APM, logs, networks, and digital experience. Defines actionable monitors, SLIs/SLOs, service-health views, and telemetry standards; automates onboarding and remediation using <strong>Rundeck, Ansible, Python, PowerShell, APIs, and Terraform</strong>. Applies AIOps and reviewed GenAI-assisted diagnostics to improve incident investigation and reduce operational toil. Collaborates with globally distributed application, infrastructure, network, and cloud teams on reliable service delivery.'
p.achievements_title='Datadog, Observability & Automation Highlights'
p.achievements=[{'tag':t+':','text':s} for t,s in [
('Enterprise Visibility','Correlated metrics, logs, traces, events, and network signals connect infrastructure behavior to application and customer impact.'),
('Observability as Code','Versioned dashboards, monitors, integrations, and automation workflows standardize onboarding and configuration across environments.'),
('Actionable Operations','SLO alerts, anomaly reviews, event enrichment, and controlled runbooks focus responders on service-impacting issues.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Datadog Platform','Infrastructure Monitoring, APM, Log Management, Network Monitoring, RUM, Synthetic Monitoring, Agents, integrations, dashboards, monitors, service tagging'),
('SRE & Observability','Metrics, logs, traces, events, telemetry pipelines, distributed tracing, SLIs, SLOs, error budgets, burn-rate alerts, service-health views, incident response'),
('Azure Observability','Azure Monitor, Log Analytics, Application Insights, AKS, Azure VMs, App Service, Azure SQL, Entra ID, Key Vault, Azure platform integrations'),
('AWS Observability','Datadog AWS integration, CloudWatch metrics/logs, CloudTrail events, EC2, EKS, ALB, RDS, Lambda, S3, IAM role delegation, service-health dashboards'),
('Automation & IaC','Rundeck jobs and runbooks, Ansible roles, Python, PowerShell, Bash, REST APIs, webhooks, Terraform Datadog provider, Git/GitHub, CI/CD'),
('Telemetry Operations','Agent/collector troubleshooting, OpenTelemetry, parsing, enrichment, log routing, trace sampling, retention, tag cardinality, telemetry consumption reviews'),
('AIOps & GenAI','Watchdog, anomaly detection, event correlation, composite alerts, noise reduction, incident enrichment, AI-assisted diagnostics, human-reviewed remediation'),
('Platform & Collaboration','Linux, Windows, Docker, Kubernetes, Helm, Azure DevOps, Jenkins, GitHub Actions, APAC/AMER/EMEA handovers, stakeholder communication, mentoring')]]
specs=[
(['Azure','AWS','Datadog','APM','Rundeck','Ansible','Terraform','Python','PowerShell','AIOps'],[
'Led Datadog observability delivery across Azure infrastructure, AKS, application services, and enterprise networks, translating stakeholder needs into monitoring standards and onboarding plans.',
'Configured Datadog Agents, Cluster Agents, integrations, and collectors; resolved proxy, TLS, permissions, endpoint, buffering, and tagging issues affecting telemetry collection.',
'Instrumented services for APM and distributed tracing, standardizing service/environment/version tags and correlating traces, logs, dependencies, and deployment events during investigations.',
'Built stakeholder dashboards, availability and latency SLIs, SLOs, error-budget views, and burn-rate alerts with service owners to improve incident prioritization.',
'Implemented Datadog AWS integrations with delegated IAM roles and scoped collection for EC2, EKS, ALB, and RDS metrics, validating account/region coverage and ownership tags.',
'Integrated AWS CloudWatch logs and CloudTrail change events with Datadog investigations to correlate application failures with infrastructure and access changes.',
'Developed AWS service-health dashboards for Lambda errors/throttling, load-balancer latency, database connections, and Kubernetes capacity; investigated missing metrics and duplicate host visibility.',
'Configured network telemetry and application dependency views and partnered with frontend teams on RUM and synthetic browser/API checks to distinguish user-experience failures from backend issues.',
'Managed dashboards, monitors, SLOs, and integration settings as Terraform and Git-controlled configuration, using pull requests, validation, environment inputs, and reviewed promotion.',
'Automated observability onboarding and approved remediation through Rundeck, Ansible, Python, PowerShell, REST APIs, and webhooks, retaining execution logs and controlled credentials.',
'Applied Watchdog findings, anomaly monitors, composite conditions, and deployment-event correlation to enrich incidents, tune routing, and reduce duplicate or nonactionable alerts.',
'Used GenAI-assisted workflows to summarize incident timelines, propose diagnostic queries, and draft runbook changes; verified conclusions against telemetry and required review before operational changes.',
'Reviewed log volume, trace sampling, retention, and custom-metric cardinality with service owners; reduced unnecessary collection while preserving error visibility and incident investigation needs.'
]),
(['Azure','AWS','Datadog','Ansible','Python','GitHub','CI/CD'],[
'Onboarded Azure application environments to Datadog, applying standard Agent configuration, service tags, log sources, dashboards, and monitor ownership.',
'Built Ansible and Python automation for agent installation, integration checks, configuration updates, and repeatable observability validation.',
'Monitored AWS EC2 host health and CloudWatch service metrics through Datadog, investigating collection gaps, permissions, and resource saturation.',
'Created AWS application dashboards that combined load-balancer errors, database connectivity, and deployment events for release-health checks.',
'Integrated monitoring checks and release markers into CI/CD and coordinated failed-check investigation with application and QA teams.',
'Maintained alert-routing documentation and incident handovers and worked with distributed teams to resolve agent, pipeline, and application telemetry failures.'
]),
(['Azure','AWS','Datadog','Terraform','Python','Kubernetes','Grafana'],[
'Implemented monitoring and log collection for Azure and Kubernetes workloads, maintaining environment tags, health checks, and actionable dashboards.',
'Automated observability configuration and operational inventory through Terraform, Python, and Git-based change reviews.',
'Built Datadog and CloudWatch views for AWS EC2, EKS, and RDS workloads, correlating compute pressure, container restarts, database latency, and service errors.',
'Investigated AWS network and application performance using load-balancer metrics, flow-log evidence, and service logs with infrastructure and development teams.',
'Troubleshot collector connectivity, missing tags, log parsing, and metric gaps and documented recovery procedures for support teams.',
'Coordinated release-health reviews and operational handovers across APAC, AMER, and EMEA, maintaining clear ownership, escalation paths, and diagnostic evidence.'
]),
(['Azure','AWS','Datadog','Prometheus','Grafana','Rundeck','Ansible','Python'],[
'Supported SRE monitoring and incident response for Azure-oriented application services, correlating logs, platform metrics, and recent releases.',
'Built Ansible roles for Prometheus, Grafana, and Node Exporter and custom Python exporters for application-specific health and capacity signals.',
'Created AWS CloudWatch and Datadog dashboards for application and infrastructure health and used telemetry to investigate deployment-related degradation.',
'Developed Python REST integrations across Jenkins, Jira, and JFrog and Rundeck runbooks for repeatable checks and approved operational tasks.',
'Tuned thresholds, alert routing, and monitoring coverage with service owners and converted incident findings into actionable dashboards and runbooks.',
'Mentored engineers on diagnostic workflows and collaborated with application teams on capacity reviews, service readiness, and post-incident improvements.'
]),
(['Azure','AWS','Datadog','ELK','Jenkins','PowerShell','Ansible'],[
'Implemented centralized application logging and operational dashboards for Azure-hosted enterprise services and release environments.',
'Automated monitoring prerequisites and service checks using Ansible, PowerShell, and shell scripts across Linux and Windows hosts.',
'Used AWS CloudWatch metrics and logs to troubleshoot load-balancer, application-host, and database connectivity issues during releases.',
'Investigated application-server failures, certificate issues, slow requests, and infrastructure dependencies with development and network teams.',
'Presented service-health findings to customer stakeholders and maintained deployment checks, troubleshooting guides, and escalation documentation.'
]),
(['Azure','AWS','Splunk','Linux','Python','Shell','Healthcare Payer'],[
'Supported production monitoring and release validation for Healthcare Payer applications within Mphasis/HPE, investigating service and batch-processing failures.',
'Used AWS CloudWatch and application logs to verify deployment health and investigate host, connectivity, and scheduled-job issues.',
'Developed Python and shell utilities for service checks, log inspection, configuration validation, and operational evidence collection.',
'Maintained support runbooks and coordinated incident updates, release checks, and handover with application, QA, and infrastructure teams.'
])]
for i,(skills,bullets) in enumerate(specs):
 p.experience[i].title=b.experience[i].title
 p.experience[i].skills_used=skills
 p.experience[i].impact=bullets
p.skills=['Datadog','Azure','AWS','Rundeck','Ansible','Python','PowerShell','Bash','APM','SLIs','SLOs','AIOps','GenAI','Terraform','REST APIs','webhooks','GitHub','CloudWatch','Prometheus','Grafana']
p.notes=['Aggressive Datadog-focused Lead SRE variant. AWS observability is explicitly covered in 10 of 40 experience bullets (25%). Employment history and certifications retained; no Datadog certification added.']
out=Path('tailored_resume/rajendra-prasad-n').resolve()
stem=out/'rajendra-prasad-n-lead-sre-datadog-azure-aws-aggressive'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.section-title{margin-top:12px}.skills-grid{gap:6px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text('''Senior Observability Engineer: enterprise Datadog across infrastructure, applications, networks, clouds, logs and digital experience. Dashboards, monitors, alerts, integrations, SLIs/SLOs, service health. Agents, APIs, collectors and telemetry pipelines. Automation via Rundeck, Ansible, Python, PowerShell, REST APIs, webhooks, Git/GitHub and CI/CD. Observability as code; AIOps event correlation, anomalies, intelligent alerting, noise reduction and enrichment. GenAI-assisted troubleshooting and automation. Azure and AWS, GCP beneficial. Investigate metrics/logs/traces/events/network signals. Optimize unnecessary telemetry and platform consumption. Global APAC/AMER/EMEA collaboration. Relevant existing certifications. Header: Lead SRE | Azure & AWS. User asks for 20-30% AWS observability experience.''')
bullets=[x for j in p.experience for x in j.impact]
aws_count=sum('AWS' in x for x in bullets)
m={'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'experience_bullet_count':len(bullets),'aws_observability_bullets':aws_count,'aws_experience_percentage':round(100*aws_count/len(bullets),1),'sources':['https://docs.datadoghq.com/integrations/amazon-web-services/','https://docs.datadoghq.com/service_level_objectives/','https://docs.datadoghq.com/observability_pipelines/guide/strategies_for_reducing_log_volume/','https://docs.datadoghq.com/dashboards/graph_insights/investigate_anomalies/']}
assert 20 <= m['aws_experience_percentage'] <= 30
stem.with_suffix('.json').write_text(json.dumps(m,indent=2))
print(json.dumps(m,indent=2))
