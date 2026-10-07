# AWS SRE default role guide

Researched 2026-10-07. Default target: Senior/Principal AWS Site Reliability Engineering and Cloud Architecture. This guide is the reusable role specification, not proof that the candidate has performed every responsibility.

## Core role scope

- Design AWS multi-AZ and multi-region architectures with fault isolation, dependency mapping, capacity planning, and documented availability tradeoffs.
- Define RTO and RPO with business owners; choose backup/restore, pilot light, warm standby, or active/active recovery patterns accordingly. Validate replication and restoration before relying on failover.
- Operate EC2, ECS, and Lambda; troubleshoot scaling, health checks, resource saturation, deployment failures, and service dependencies.
- Design VPC connectivity, Route 53 health checks and failover routing, and ALB/NLB traffic management.
- Support durable S3 and EFS storage, RDS availability and recovery, and SQS retry/dead-letter queue patterns.
- Maintain reusable Terraform and CloudFormation YAML; validate changes, review plans/change sets, manage drift, and keep recovery environments reproducible.
- Read, debug, and modify Python resiliency automation; make recovery actions observable, retry-safe, and testable.
- Own incident response, operational runbooks, post-incident analysis, troubleshooting across Linux/network/application layers, and corrective-action follow-through.

## Additional responsibilities from AWS guidance

- Define service-level indicators and objectives (SLIs/SLOs), measure availability and latency, and use error budgets and burn-rate alerts to prioritize reliability work. [AWS SRE overview](https://aws.amazon.com/what-is/sre/) and [CloudWatch SLOs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html).
- Exercise disaster recovery and failback, measure actual recovery against RTO/RPO, and test cross-service dependencies. [Multi-region operational readiness](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-4.html).
- Use controlled game days and fault injection with explicit scope, stop conditions, and recovery procedures; assess resilience gaps using AWS Resilience Hub and AWS Fault Injection Service where applicable. [Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html).
- Review customer responsibilities for redundancy and self-healing, including Auto Scaling and placement across fault boundaries. [Shared responsibility for resiliency](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/shared-responsibility-model-for-resiliency.html).
- Select recovery architectures against business recovery objectives and cost rather than assuming every workload requires active/active. [AWS recovery strategies](https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel_planning_for_recovery_disaster_recovery.html).

## Candidate evidence and certifications

The synchronized base uses existing repository AWS experience and the user's AWS SRE focus. Employment titles, organizations, dates, contacts, and education are preserved. Existing Aggressive outputs are framing references, not independent verification. Synthetic mock outputs are excluded as evidence.

AWS Certified Solutions Architect – Professional is a target qualification provided in the requested role specification. The recorded candidate credential is AWS Certified Solutions Architect – Associate; do not upgrade it without confirmation. Likewise, Principal is the target seniority, not a replacement historical title. New metrics, SLO ownership, ARC, Resilience Hub, and FIS experience require confirmation before being asserted in candidate bullets.

## Default execution

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py --person Rajendra --level Base
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py --person Rajendra --domain aws-sre --level Tailored --jd-file inputs/job-description.txt
```

`aws-sre` is the default domain. `devops-cloud` remains a compatibility alias. Base does not require a JD; other levels do. The main and bundled templates and JSON profiles must remain synchronized. Explicit Azure/DataOps requests can use the archived Azure variant; AWS or mixed AWS JDs must not implicitly select that variant. Historical generated resumes are retained as historical artifacts.
