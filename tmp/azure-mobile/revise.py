import json
from pathlib import Path
f=Path('tmp/azure-mobile/plugin/assets/people/rajendra-prasad-n.json'); p=json.loads(f.read_text())
p['full_name']='Rajendra P N';p['page_title']='Rajendra P N - Lead Azure DevOps Engineer';p['headline']='Lead Azure DevOps Engineer | AI | Android/iOS';p['certification_badges_alt']='Rajendra P N certification badges'
p['summary_html']='<strong>Lead Azure DevOps Engineer with 10+ years of experience in build automation, release engineering, and production delivery.</strong> Specializes in <strong>Azure Pipelines, Azure Repos, Azure Artifacts, and Bitrise for Android/iOS delivery</strong>, spanning reusable YAML workflows, signing, packaging, and publishing to Google Play and the App Store. Builds repeatable embedded software release workflows and coordinates versioned artifacts, verification, and release readiness. Automates operations with Python and PowerShell, using AI-assisted scripting selectively with review and testing.'
p['certifications']=[x for x in p['certifications'] if 'AWS' not in x]
p['skills']=['Azure DevOps','Azure Pipelines','Azure Repos','Azure Artifacts','Bitrise','Android','iOS','Google Play','App Store Connect','Terraform','Python','PowerShell']
p['skill_sections']=[
{'title':'Azure DevOps Engineering','content':'Multi-stage YAML pipelines, reusable templates, Azure Repos, branch policies, pull requests, Azure Artifacts feeds, build agents, deployment environments, approvals'},
{'title':'Android & iOS Delivery','content':'Bitrise workflows, Android Gradle builds, APK/AAB packaging, keystores, Xcode archives, iOS certificates, provisioning profiles, TestFlight, Google Play, App Store Connect'},
{'title':'Embedded Build & Release','content':'Automated compilation, build-toolchain configuration, versioned firmware artifacts, release manifests, checksums, build logs, integration verification, release baselines'},
{'title':'Azure Infrastructure & Deployment','content':'Terraform, Bicep, ARM templates, Azure CLI, AKS, Azure Container Registry, Helm, Argo CD, environment parameters, deployment validation'},
{'title':'Delivery Security & Quality','content':'Azure Key Vault, service connections, workload identity federation, secret variables, secure files, SonarQube, security scanning, automated tests, release evidence'},
{'title':'Automation & Diagnostics','content':'Python, PowerShell, Bash, REST APIs, Azure Monitor, Log Analytics, Application Insights, root cause analysis; AI-assisted scripting and documentation with review and testing'}]
p['achievements']=[{'tag':'Azure Pipeline Engineering','text':'Standardized reusable YAML pipelines, source-control policies, artifact promotion, environment configuration, and approval gates for repeatable software delivery.'},{'tag':'Android/iOS Publishing','text':'Automated mobile builds and release packaging with Bitrise, coordinating signing, provisioning, store submissions, and verification for Google Play and the App Store.'},{'tag':'Embedded Release Automation','text':'Organized embedded software builds into traceable release packages with versioned binaries, configuration baselines, build logs, and verification evidence.'}]
p['achievements_title']='Azure & Mobile DevOps Delivery Highlights'
p['experience'][0]['impact']=[
'Engineered multi-stage Azure Pipelines with reusable YAML templates for build, test, package, and deployment stages, standardizing environment parameters and approval gates.',
'Automated Android builds with Bitrise and Gradle, managed signing inputs and APK/AAB packaging, and published approved releases to Google Play with release verification.',
'Built iOS delivery workflows in Bitrise for Xcode archive/export, certificate and provisioning-profile handling, TestFlight distribution, and App Store submission and publishing coordination.',
'Automated embedded software build and release workflows, capturing toolchain configuration, versioned binaries, checksums, and release manifests for reproducible delivery.',
'Established Azure Repos branch policies and pull-request checks; published versioned packages and build artifacts for controlled promotion between environments.',
'Protected pipeline credentials with Azure Key Vault, secure files, and least-privilege service connections; troubleshot signing, provisioning, and authentication failures.',
'Integrated automated tests, static analysis, security checks, and deployment evidence into release gates; coordinated readiness and issue resolution with development and QA.',
'Developed Python and PowerShell release utilities; used AI-assisted script drafting and documentation with code review and test validation.',
'Diagnosed build, deployment, and application failures through Bitrise logs, Azure Monitor, and Log Analytics, coordinating fixes and post-release verification.'
]
p['experience'][0]['skills_used']=['Azure DevOps','Azure Pipelines','Bitrise','Android/iOS','Azure Artifacts','Key Vault','Python','PowerShell']
p['experience'][1]['impact']=[
'Built reusable Azure DevOps stages for compilation, automated tests, artifact publication, and release approvals across development, QA, and production.',
'Maintained Bitrise Android and iOS build workflows, resolving dependency, signing, provisioning, and packaging failures before release handoff.',
'Coordinated Google Play and App Store release preparation with application teams, validating build versions, environment settings, and published release status.',
'Integrated embedded software build outputs into versioned release packages and preserved configuration, build logs, and test evidence for integration handoff.',
'Administered Linux and Windows build agents, standardized tool dependencies, and diagnosed pipeline and credential failures.'
]
p['experience'][1]['skills_used']=['Azure DevOps','Bitrise','Android/iOS','Git','PowerShell','Build Agents']
p['experience'][2]['impact']=[
'Automated Azure application delivery with pipeline checks, versioned artifacts, environment-specific configuration, and post-deployment verification.',
'Supported Bitrise Android and iOS build and release pipelines, preparing signed packages and coordinating Google Play and App Store publishing activities.',
'Investigated mobile workflow failures using build logs, dependency configuration, signing inputs, and artifact metadata; documented fixes for repeatable releases.',
'Provisioned Azure infrastructure through Terraform and ARM templates and deployed services to AKS using Helm and Argo CD.',
'Created Python and PowerShell release-check utilities and used Azure Monitor and Log Analytics to diagnose deployment and service-connectivity issues.'
]
p['experience'][2]['skills_used']=['Azure','Bitrise','Android/iOS','Terraform','AKS','Python','Azure Monitor']
p['notes']=['Preferred display name for all future resumes: Rajendra P N. Preserve internal person ID.','User explicitly requested Azure-only content, exact header, embedded build/release points, and Bitrise Android/iOS build and store-publishing points; mobile experience placed under latest three employers as requested.','Keep 10+ years wording. No medical-device or IEC 62304 compliance claims.']
for target in [f,Path('resume_data/people/rajendra-prasad-n.json'),Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json')]:target.write_text(json.dumps(p,indent=2)+'\n')
q=Path('instructions.md');s=q.read_text(); start=s.index('## Persistent Rajendra preferences')
s=s[:start]+'''## Persistent Rajendra preferences (updated 2026-09-30)
- Display name in every future resume and template-generated output: **Rajendra P N**. Retain internal person ID for compatibility.
- Azure resume header: **Lead Azure DevOps Engineer | AI | Android/iOS**.
- Keep **10+ years** experience wording.
- On the Azure branch, focus exclusively on deep Azure DevOps and Android/iOS mobile delivery. Omit multi-cloud wording, AWS technologies, and AWS certification from the displayed resume.
- Emphasize Bitrise builds, signing, provisioning, packaging, Google Play and App Store publishing, and embedded software build/release workflows. Bitrise belongs under the latest three employers per user instruction.
- Keep AI usage modest and tied to reviewed, tested automation and documentation.
- Synchronize reusable profile data in resume_data/people and plugin assets/people. Templates render the display name from full_name; do not hardcode another name.
- The user will commit changes; leave this work uncommitted.
''';q.write_text(s)
for t in [Path('templates/base_resume.html'),Path('plugins/resume-creator-plugin/assets/templates/base_resume.html'),Path('tmp/azure-mobile/plugin/assets/templates/base_resume.html')]:
 s=t.read_text(); marker='<!-- Rajendra resume default: display name Rajendra P N; populated from profile full_name. -->\n'
 if marker not in s:s=s.replace('<html',marker+'<html',1)
 t.write_text(s)
