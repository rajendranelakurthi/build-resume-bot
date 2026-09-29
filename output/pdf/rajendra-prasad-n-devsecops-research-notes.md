# DevSecOps Lead tailoring notes

The résumé emphasizes demonstrated delivery leadership, code controls, application validation, secrets/access, infrastructure controls, and production operations. Employer names, role titles, dates, education, and certifications are preserved. No numerical improvements or regulatory certifications have been invented. Nova is the prospective employer's program and is not represented as prior experience.

## Public research informing the security coverage

- [OWASP DevSecOps Guideline](https://devguide.owasp.org/en/09-operations/01-devsecops/): integrate static analysis, dependency analysis, and dynamic testing into delivery.
- [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final): organize secure development around preparation, software protection, secure production, and vulnerability response. Used as a role-design reference, not a claim of compliance.
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html): centralize secrets, restrict access, and manage credential lifecycle.
- [CISA software supply-chain guidance](https://www.cisa.gov/news-events/alerts/2022/11/17/cisa-nsa-and-odni-release-guidance-customers-securing-software-supply-chain): assess software dependencies and supply-chain risk.

## Additional tools to add only after hands-on experience is confirmed

| Security area | Tool / control | Relevant DevSecOps responsibility |
|---|---|---|
| Code and credentials | [Gitleaks](https://github.com/gitleaks/gitleaks) | Run repository and pre-commit secret checks; coordinate credential revocation and remediation. |
| Infrastructure | [Checkov](https://www.checkov.io/) | Scan Terraform, Kubernetes, Helm, and ARM configuration before provisioning; track approved exceptions. |
| Containers and repositories | [Trivy](https://www.trivy.dev/docs/latest/guide/scanner/secret/) | Integrate vulnerability, misconfiguration, and secret scanning where supported; prioritize findings before promotion. |
| Running applications / APIs | [ZAP Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) | Automate authenticated dynamic security testing in authorized nonproduction environments. |
| Software supply chain | SBOM generation and artifact signing | Associate dependency inventories and provenance with releases; verify artifacts before promotion. |
| Security governance | Risk-based gates and exception expiry | Assign remediation owners, severity-based deadlines, and documented risk acceptance rather than silently bypassing controls. |

## JD-specific responsibilities requiring confirmation

The saved material supports release coordination and environment configuration. It does not establish sole ownership of booking or refresh calendars, authority to decide competing refresh requests, or a named regulatory control framework. Suggested wording to use if accurate:

- Owned a shared environment booking register and refresh calendar, arbitrating competing requests against release criticality, dependencies, and agreed priorities.
- Coordinated environment refreshes with application, data, and test owners; validated versions, access, test-data readiness, and post-refresh smoke tests before handover.
- Governed nonproduction data refreshes using approved masking, access, retention, and recovery controls for sensitive datasets.
- Partnered with security and risk teams to retain approval, scan, deployment, exception, and recovery evidence for regulated workloads.
- Defined production ownership, support escalation, service-health criteria, rollback decisions, and incident follow-up across delivery teams.

These are proposed additions, not verified career claims. The résumé does not claim tools or responsibilities solely because they appear in public documentation.
