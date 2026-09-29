from pathlib import Path
p=Path('tmp/aws-devops/refine.py')
s=p.read_text()
insert='''
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
'''
s=s.replace('p.certifications=sorted',insert+'\np.certifications=sorted')
s=s.replace('.job-block{break-inside:avoid;} }', '.job-block{break-inside:auto;page-break-inside:auto;} .job-header,.job-details{break-after:avoid;} li{break-inside:avoid;} }')
p.write_text(s)
