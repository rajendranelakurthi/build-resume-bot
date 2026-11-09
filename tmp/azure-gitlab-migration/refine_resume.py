import json
import sys
from dataclasses import asdict
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root / 'plugins/resume-creator-plugin/scripts'))
from plugin_core import BundledJsonResumeStore, BundledHtmlResumeRenderer, tailor_profile

assets = root / 'plugins/resume-creator-plugin/assets'
base = BundledJsonResumeStore(assets / 'people', assets / 'static').load_person('rajendra-prasad-n')
jd = (root / 'tmp/azure-gitlab-migration/job-description.txt').read_text()
p, keywords = tailor_profile(base, jd)
p.summary_html = ('<strong>Lead DevOps Engineer with 10+ years of experience in CI/CD automation, Azure infrastructure, and production release delivery.</strong> Experience migrating Jenkins pipelines to <strong>GitLab CI</strong>, building reusable <strong>Azure DevOps</strong> workflows, and automating release and onboarding tasks with <strong>Python, Bash, and PowerShell</strong>. Partners with application developers and QA to manage build dependencies, versioned artifacts, environment configuration, deployment approvals, and production verification. GitLab Certified Associate with hands-on pipeline migration and build troubleshooting experience.')
p.skills = ['Azure DevOps', 'GitLab CI/CD', 'Jenkins', 'Python', 'Git', 'Maven', 'Azure', 'Terraform', 'AKS', 'Docker', 'PowerShell', 'Bash']
p.achievements = [
 {'tag': 'Pipeline Migration', 'text': 'Migrated Jenkins pipelines to GitLab CI and supported source review, automated validation, and release traceability.'},
 {'tag': 'Azure DevOps Delivery', 'text': 'Built reusable application delivery workflows with review checks, environment approvals, and versioned release artifacts.'},
 {'tag': 'Python Automation', 'text': 'Developed release checks and FastAPI integrations for Jenkins, Jira, and JFrog to automate onboarding and release coordination.'}
]
p.skill_sections = [
 {'title': 'CI/CD & Pipeline Migration', 'content': 'GitLab CI, Jenkins-to-GitLab pipeline migration, Azure DevOps (AZDO), GitHub Actions, reusable workflows, build automation, deployment approvals'},
 {'title': 'Python & Automation', 'content': 'Python, FastAPI, Bash, PowerShell, Azure CLI, onboarding automation, pre-deployment checks, smoke tests'},
 {'title': 'Source Control & Release Delivery', 'content': 'Git, pull requests, branch protection, merge controls, Maven, JFrog Artifactory, artifact versioning, SonarQube, SDLC'},
 {'title': 'Azure & Infrastructure', 'content': 'Azure, Terraform, ARM templates, Ansible, virtual networks, Key Vault, Microsoft Entra ID, RBAC; additional cloud experience: AWS'},
 {'title': 'Containers & Operations', 'content': 'AKS, Kubernetes, Docker, Azure Container Registry, Helm, ArgoCD, Linux, Azure Monitor, Log Analytics, Prometheus, Grafana'},
 {'title': 'Database Release Integration', 'content': 'Liquibase, Snowflake, SQL, version-controlled schema changes, validation, deployment history, rollback procedures'}
]
# Reuse documented work and bring the role-relevant responsibilities forward.
for job in p.experience:
    original = next(j for j in base.experience if j.company == job.company)
    job.impact = list(original.impact)
    job.skills_used = list(original.skills_used)
    if job.company == 'AT&T Services Inc.':
        job.impact = [original.impact[i] for i in [1, 0, 6, 5, 7, 8, 2]]
        job.skills_used = ['Azure', 'Azure DevOps', 'Python', 'PowerShell', 'GitHub Actions', 'Terraform', 'AKS', 'Key Vault']
    elif job.company == 'GlobalLogic':
        job.impact = [
            'Migrated Jenkins build and deployment pipelines to GitLab CI, adapting existing pipeline stages and supporting automated validation and release traceability.',
            original.impact[0],
            original.impact[3],
            original.impact[1],
        ]
        job.skills_used = ['Azure', 'GitLab CI', 'Jenkins', 'Git', 'Docker', 'Kubernetes', 'Liquibase', 'Snowflake']
    elif job.company == 'Turvo India Pvt Ltd':
        job.impact = [original.impact[i] for i in [1, 2, 4, 0, 5]]
    elif job.company == 'HCL Technologies':
        job.impact = [original.impact[i] for i in [0, 2, 3]]
    elif job.company == 'Mphasis Ltd':
        job.impact = [original.impact[i] for i in [0, 2, 3]]
p.notes = ['Tailored from saved Azure profile. No unverified GitLab tenure, Azure DevOps-to-GitLab migration ownership, or .NET development claims added.', 'Pipeline terminology reviewed against https://docs.gitlab.com/ci/migration/jenkins/ .']
out = root / 'output/pdf/azure-gitlab-migration'
stem = out / 'rajendra-prasad-n-azure-devops-gitlab-migration'
stem.with_suffix('.profile.json').write_text(json.dumps(asdict(p), indent=2) + '\n')
stem.with_suffix('.html').write_text(BundledHtmlResumeRenderer(assets / 'templates/base_resume.html').render(p))
print(stem.with_suffix('.html'))
