import json,sys
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
base=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
jd='''Lead consultant – API Development & Cloud Migration. Design, develop, modernize, migrate and support enterprise APIs across Payments, Money Movement and Information Reporting. Java, Spring Boot, REST APIs and microservices; on-premises-to-AWS migration. API Gateway, Lambda, ECS, Step Functions, SQS, SNS, DynamoDB, RDS, S3, IAM, KMS, AWS Transfer Family. Kafka event-driven integration. OpenShift and Docker. Secure coding, authentication, authorization, encryption and secrets management. Terraform, CI/CD, automated tests, governance, performance optimization, legacy assessment, refactoring, production cutover, on-call support, incident resolution and RCA. Dynatrace, CloudWatch, X-Ray, Grafana, Splunk. Collaborate with architects, product owners, business partners and engineering teams; code reviews and technical design.'''
p,_=tailor_profile(base,jd)
p.headline='Lead AWS DevOps Engineer | API & Cloud Migration'
p.page_title='Rajendra Prasad N - AWS DevOps, API Modernization & Cloud Migration'
p.summary_html='<strong>Lead AWS DevOps Engineer with 10+ years of enterprise experience in cloud engineering, application delivery, automation, and production support.</strong> Combines <strong>API modernization, Java/Spring Boot microservices, and on-premises-to-AWS migration</strong> with Terraform, secure CI/CD, and container operations. Builds delivery platforms using API Gateway, Lambda, ECS, Step Functions, Kafka, SNS/SQS, and managed data services. Partners with architects and application teams on API contracts, security, testing, cutover readiness, observability, and resilient integration patterns relevant to Payments, Money Movement, and Information Reporting.'
p.achievements_title='API Modernization, AWS Migration & Delivery Highlights'
p.achievements=[{'tag':t+':','text':v} for t,v in [
('Modernization','Incremental API refactoring, dependency assessment, containerization, and reversible cutovers support migration from on-premises services to AWS.'),
('Secure Delivery','Terraform, automated API tests, vulnerability checks, and controlled promotion standardize cloud-native releases.'),
('Operational Resilience','Idempotent processing, bounded retries, dead-letter handling, and correlated telemetry improve integration reliability.')]]
p.skill_sections=[{'title':t,'content':v} for t,v in [
('API & Microservices','Java, Spring Boot, REST, JSON, OpenAPI, API versioning, validation, exception handling, integration and contract testing'),
('AWS Application Platforms','API Gateway, Lambda, ECS/Fargate, Step Functions, ECR, S3, AWS Transfer Family, VPC, load balancing'),
('Events & Data','Apache Kafka, Amazon SNS, SQS, DynamoDB, RDS, SQL, idempotency, retries, dead-letter queues, event schemas'),
('Migration & Architecture','Legacy assessment, dependency mapping, incremental refactoring, on-premises-to-AWS migration, cutover, rollback, data reconciliation'),
('DevOps & Automation','Terraform, Jenkins, GitHub Actions, Git, Maven, Python, Bash, Ansible, CI/CD, automated testing, release management'),
('Containers & Security','Docker, OpenShift, ECS, Kubernetes, OAuth 2.0/OIDC, JWT, IAM, KMS, Secrets Manager, TLS, SAST/SCA, image scanning'),
('Observability & Support','Dynatrace, CloudWatch, AWS X-Ray, Grafana, Splunk, distributed tracing, performance tuning, on-call support, incident response, RCA'),
('Integration & Collaboration','Transactional API patterns for Payments, Money Movement and Information Reporting; API governance, design reviews, stakeholder coordination; Healthcare Payer support')]]
specs=[
(['AWS','Java','Spring Boot','API Gateway','ECS','Terraform','Kafka','CI/CD'],[
'Led AWS DevOps and API modernization delivery, coordinating infrastructure, application releases, migration readiness, and production support with architects and engineering teams.',
'Assessed on-premises API dependencies, runtime requirements, network paths, and deployment constraints; organized migration waves with validation criteria and rollback procedures.',
'Developed and enhanced Java/Spring Boot REST service components with request validation, consistent error responses, externalized configuration, and versioned OpenAPI contracts.',
'Modernized legacy integrations incrementally behind API Gateway, maintaining backward-compatible interfaces while routing selected functionality to Lambda and ECS services.',
'Built Terraform modules for API Gateway, Lambda, ECS, IAM, KMS, queues, storage, and data-service dependencies with reviewed plans and environment-specific configuration.',
'Implemented Step Functions workflows with explicit error handling and bounded retries; used SNS/SQS for asynchronous integration and DynamoDB-backed request tracking.',
'Developed Kafka and SQS integration components with idempotency checks, correlation identifiers, dead-letter handling, and controlled replay to prevent duplicate business processing.',
'Containerized Spring Boot services with Docker and supported OpenShift-to-ECS deployment adaptation, including health checks, task roles, secrets, networking, and scaling policies.',
'Integrated OAuth 2.0/OIDC and JWT validation with scoped authorization; enforced TLS, least-privilege IAM, KMS encryption, and Secrets Manager-based credential retrieval.',
'Automated managed SFTP integration through AWS Transfer Family and S3, configuring scoped access, encryption, transfer monitoring, and downstream processing validation.',
'Built Jenkins and GitHub Actions pipelines for Maven builds, unit and API contract tests, dependency/image scans, artifact publication, and controlled AWS deployments.',
'Configured CloudWatch, X-Ray, Dynatrace, Grafana, and Splunk views to correlate API latency, errors, dependency calls, queue backlog, and deployment events.',
'Investigated API bottlenecks across JVM resources, database connection pools, RDS queries, Lambda concurrency, and downstream timeouts; verified changes through load tests.',
'Supported migration rehearsals and production cutovers using smoke tests, response comparisons, operational checks, and rollback triggers; led incident reviews and runbook improvements.'
]),
(['AWS','Spring Boot','Jenkins','Terraform','Docker','API Testing'],[
'Built CI/CD workflows for Java/Spring Boot services, integrating Maven builds, automated tests, artifact versioning, and environment promotion.',
'Automated AWS application infrastructure and configuration through Terraform and deployment scripts, validating service connectivity and permissions before release.',
'Supported REST API enhancements and integration testing, checking request/response contracts, authentication failures, and backward compatibility with application teams.',
'Deployed containerized services and investigated startup, configuration, networking, and downstream dependency failures across test and production environments.',
'Partnered with developers and QA on release readiness, defect triage, smoke tests, rollback procedures, and operational handovers.'
]),
(['AWS','Terraform','Docker','Kubernetes','API Gateway','CloudWatch'],[
'Provisioned AWS infrastructure and supported migration of application services from legacy environments using Terraform, containers, and automated release workflows.',
'Maintained CI/CD pipelines for microservices, implementing deployment checks, versioned configuration, security gates, and controlled production promotion.',
'Supported API Gateway routing and backend service connectivity, troubleshooting permissions, TLS, timeouts, and application-level errors.',
'Automated container deployments and runtime configuration, validating health probes, resource limits, service discovery, and rollout behavior.',
'Correlated CloudWatch metrics, application logs, and distributed traces to investigate latency, failed requests, and downstream service degradation.',
'Coordinated migration validation, recovery exercises, incident reviews, and support documentation with distributed application and infrastructure teams.'
]),
(['AWS','Python','REST APIs','Jenkins','Ansible','Grafana','Splunk'],[
'Developed Python FastAPI integrations for Jenkins, Jira, and JFrog, using REST/JSON interfaces to automate onboarding, deployment status, and operational workflows.',
'Built Jenkins and GitHub Actions pipelines for application and infrastructure changes with automated checks, artifact promotion, and post-deployment validation.',
'Supported asynchronous service integrations by investigating processing delays, failed requests, retry behavior, and application dependency issues with developers.',
'Automated Prometheus, Grafana, and Node Exporter deployment with Ansible; developed Python exporters for application-specific operational metrics.',
'Used centralized logs and dashboards to diagnose production incidents, improve alerting, and maintain release, escalation, and recovery runbooks.'
]),
(['AWS','Jenkins','Ansible','Java Deployments','Linux','Bash'],[
'Supported enterprise Java application deployments for Mercedes-Benz Research & Development India across Linux and AWS-hosted environments.',
'Maintained Jenkins jobs and Ansible automation for packaging, configuration, deployment, service restarts, and release validation.',
'Investigated REST integration errors, application logs, database connectivity, permissions, and infrastructure issues during production support.',
'Created Bash/Python checks and operational documentation for change readiness, rollback, incident triage, and repeatable environment maintenance.'
]),
(['Healthcare Payer','Jenkins','Linux','AWS','Shell','Release Management'],[
'Supported Healthcare Payer application releases within Mphasis/HPE, coordinating integration checks and deployment readiness with development, QA, and infrastructure teams.',
'Automated Linux deployment tasks and configuration updates through Jenkins, Ansible, and shell scripting with post-release service verification.',
'Investigated API connectivity, scheduled processing, application errors, and host issues using logs and AWS CloudWatch signals.',
'Maintained release procedures, incident handovers, and recovery runbooks for enterprise application and integration support.'
])]
for j,b,(skills,bullets) in zip(p.experience,base.experience,specs):
 j.title=b.title
 j.skills_used=skills
 j.impact=bullets
p.skills=['AWS','API Gateway','Lambda','ECS','Step Functions','SQS','SNS','DynamoDB','RDS','S3','IAM','KMS','AWS Transfer Family','Java','Spring Boot','REST APIs','Kafka','OpenShift','Docker','Terraform','CI/CD','Dynatrace','CloudWatch','AWS X-Ray','Grafana','Splunk']
p.notes=['Aggressive JD-aligned draft; expanded development and migration responsibilities require candidate review. Payments terminology describes transferable integration patterns, not an asserted banking client engagement. Employment history, education and certifications retained.']
stem=Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-aws-api-cloud-migration-aggressive').resolve()
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('</style>','@media print {.cert-card{min-height:90px}.cert-badge-svg{max-width:64px}.section-title{margin-top:12px}.skills-grid{gap:6px}.skill-card{padding:4px 8px}.job-block{break-inside:auto;page-break-inside:auto}.job-block ~ .job-block{break-inside:avoid;page-break-inside:avoid}.job-header,.job-details{break-after:avoid;page-break-after:avoid}li{break-inside:avoid;page-break-inside:avoid}}\n</style>')
stem.with_suffix('.html').write_text(html)
stem.with_suffix('.jd.txt').write_text(jd)
stem.with_suffix('.json').write_text(json.dumps({'person':'Rajendra','domain':'devops-cloud','level':'Aggressive','html_path':str(stem.with_suffix('.html')),'pdf_path':str(stem.with_suffix('.pdf')),'profile_path':str(stem.with_suffix('.profile.json')),'sources':['https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html','https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html']},indent=2))
print(stem)
