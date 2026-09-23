import sys,json
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer,tailor_profile
a=Path('plugins/resume-creator-plugin/assets').resolve()
b=BundledJsonResumeStore(a/'people',a/'static').load_person('rajendra-prasad-n')
jd=Path('tmp/build-release/jd.txt').read_text()
p,keywords=tailor_profile(b,jd)
p.page_title='Rajendra Prasad N - DevOps Build & Release Engineer'
p.headline='DevOps Build & Release Engineer | Jenkins, SCM & Artifacts'
p.summary_html='<strong>Build and Release Engineer with 10+ years of enterprise software delivery, CI/CD automation, and release coordination experience.</strong> Hands-on with <strong>Jenkins/CloudBees, Git, Docker, JFrog Artifactory, build-agent administration, and deployment automation</strong>. Technical background includes Git/Gerrit, MSBuild, .NET (C#), Linux and Windows build environments, Python, Bash, and PowerShell. Standardizes build workflows, artifact versioning, branch controls, and environment promotion while coordinating release dependencies, change windows, and production support.'
p.achievements_title='Build & Release Engineering Highlights'
p.achievements=[{'tag':t,'text':s} for t,s in [
('CI/CD Engineering','Built and maintained enterprise pipelines, reusable Jenkins libraries, build agents, and automated deployment workflows.'),
('Artifact Management','Administered JFrog Artifactory and Xray and automated versioned image and package publication for downstream teams.'),
('Release Governance','Coordinated release schedules, dependencies, change windows, Git approvals, and stakeholder communications.'),
('Delivery Automation','Developed Python, Bash, PowerShell, and Ansible automation for repeatable builds, deployment, and release support.')]]
p.skill_sections=[{'title':t,'content':s} for t,s in [
('Jenkins & CI/CD Administration','Jenkins, CloudBees Jenkins, shared libraries, GitLab CI, GitHub Actions, self-hosted build agents, Linux/Windows runners'),
('Source & Release Governance','Git, Gerrit, GitHub, GitLab, Bitbucket, branching strategies, merge standards, approvals, release scheduling, dependency coordination'),
('Build Toolchains','MSBuild, .NET (C#), Maven, Gradle, ANT, Make, Java, Node.js, Windows and Linux build environments'),
('Artifacts & Quality Controls','JFrog Artifactory, JFrog Xray, Nexus, artifact feeds, upstream repositories, versioning, SonarQube, Fortify, Black Duck'),
('Docker & Deployment Automation','Docker image builds, image versioning, container delivery, Ansible deployment pipelines, environment promotion, configuration separation'),
('Scripting & Release Operations','Python, Bash, PowerShell, API integrations, YAML, build troubleshooting, release reporting, production support, operational runbooks')]]
specs=[
(['Git','CI/CD','Build Agents','Python','Bash','PowerShell','Release Governance'],[
'Led end-to-end release coordination across engineering teams, aligning schedules, dependencies, change windows, and risk mitigation plans.',
'Architected reusable build, test, and release workflows and standardized deployment pipelines for consistent enterprise delivery.',
'Established Git branching, approval, and artifact versioning standards to improve traceability and control over software changes.',
'Managed self-hosted runners, build agents, and distributed deployment infrastructure to support reliable pipeline execution.',
'Automated provisioning, release support, and recovery tasks with Python, Bash, and PowerShell.',
'Integrated secure secrets handling and pre-deployment checks into governed release workflows.',
'Published release communications, milestone reports, risk updates, deployment guides, and operational runbooks.',
'Coordinated production release support and incident response to restore service during high-priority delivery issues.']),
(['Jenkins','GitLab CI','Git','Docker','Linux/Windows Agents'],[
'Migrated Jenkins pipelines to GitLab CI, modernizing runner configuration and improving pipeline maintainability.',
'Administered self-hosted and autoscaling Linux and Windows build agents, agent pools, runner templates, and execution policies.',
'Created package views, artifact feeds, and upstream repository strategies for application-team delivery requirements.',
'Managed Docker image builds and container runtime administration to standardize application delivery.',
'Enforced GitLab branching and merge standards, reusable pipeline templates, secure runners, and image validation checks.',
'Troubleshot build, pipeline, and container failures with development teams to resolve release blockers.']),
(['Jenkins','Git','GitHub Actions','Docker','Maven','Ansible','PowerShell'],[
'Built and maintained Jenkins-based CI/CD workflows with Git, Maven, Ansible, and Docker for repeatable application delivery.',
'Configured Linux and Windows build agents and environment-specific deployment targets for controlled production rollouts.',
'Implemented GitHub Actions deployment workflows and standardized container image build and release processes.',
'Published versioned artifacts to enterprise repositories and package managers for downstream consumption and traceability.',
'Integrated Jenkins, GitHub, and SonarQube with engineering collaboration tools to support delivery and audit requirements.',
'Authored reusable shell and PowerShell scripts and resolved build, dependency, and deployment pipeline failures.']),
(['CloudBees Jenkins','JFrog Artifactory','Xray','Python','GitHub Actions','Ansible'],[
'Administered CloudBees Jenkins, JFrog Artifactory, and Xray enterprise services supporting secure software delivery.',
'Developed Jenkins shared libraries to automate image versioning and artifact publication to private JFrog repositories.',
'Standardized reusable GitHub Actions CI/CD patterns and designed application deployment pipelines.',
'Built Python FastAPI integrations connecting Jenkins, Jira, and JFrog to automate recurring delivery workflows.',
'Automated onboarding of new projects to the enterprise DevOps platform through API-driven processes.',
'Partnered with development teams to investigate defects and improve release quality through sprint retrospectives.']),
(['Jenkins','Maven','GitHub','Ansible','Shell','Tomcat','JBoss'],[
'Built continuous delivery pipelines for enterprise applications across Demo, Test, Pentest, Training, CTDEV, Sandbox, UAT, and production.',
'Standardized application release packaging and supported consistent deployment of REST-based microservices.',
'Presented CI/CD automation strategies and delivery improvements to engineering stakeholders.',
'Coordinated sprint commitments and delivery priorities while supporting application deployment and release troubleshooting.',
'Automated configuration tasks with PowerShell and maintained operational consistency across Linux and Windows application environments.']),
(['GitLab','Git','Maven','Ansible','Nexus','Python','Shell'],[
'Created Ansible deployment pipelines to promote application releases from development through production in a controlled, repeatable manner.',
'Built YAML-based build and release workflows with event-driven triggers for continuous integration on code changes.',
'Defined Git branching strategies and managed self-hosted build agents supporting release execution.',
'Promoted the same artifact set across environments using controlled selection and environment-specific configuration.',
'Documented build and deployment flows for API, database, UI, and supporting components to improve delivery consistency.'])]
for job,(skills,bullets) in zip(p.experience,specs):
 job.skills_used=skills
 job.impact=bullets
p.skills=['Jenkins','Git/Gerrit','Docker','JFrog Artifactory','MSBuild','.NET (C#)','Release Engineering','Python','Bash','PowerShell']
p.notes=['Pure Build & Release variant. Employment titles and dates preserved. NuGet, Electron/Rust-Tauri, Inno Setup and code signing are not claimed without experience confirmation.']
s=Path('output/pdf/rajendra-prasad-n-build-release-aggressive')
s.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
s.with_suffix('.jd.txt').write_text(jd)
s.with_suffix('.html').write_text(BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p))
s.with_suffix('.json').write_text(json.dumps({'person':'Rajendra','level':'Aggressive','focus':'Build & Release','email':p.email,'html_path':str(s.with_suffix('.html').resolve()),'pdf_path':str(s.with_suffix('.pdf').resolve())},indent=2))
