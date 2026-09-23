exec(compile(open('tmp/build-release/build.py').read(),'build.py','exec'))
p.page_title='Rajendra Prasad N - Azure DevOps .NET Build & Release Engineer'
p.headline='Lead DevOps Engineer | Build & Release'
p.summary_html='<strong>Build and Release Engineer with 10+ years of enterprise software delivery, CI/CD automation, and release governance experience.</strong> Focused on <strong>Azure DevOps, Jenkins, .NET/MSBuild, Git/Gerrit, Docker, and JFrog Artifactory</strong>. Designs repeatable build, package, and deployment workflows; administers Windows/Linux build agents; and automates release tasks with PowerShell, Python, and Bash. Coordinates dependencies, approvals, artifact promotion, and production releases with engineering, QA, and operations teams.'
p.certifications=[c for c in p.certifications if not c.startswith('AWS')]
p.achievements=[{'tag':t,'text':v} for t,v in [
('Azure DevOps & .NET Delivery','Standardized build and release workflows around Azure DevOps, MSBuild, controlled source changes, and environment-specific deployment configuration.'),
('Jenkins & Artifact Engineering','Administered CloudBees Jenkins and JFrog tooling; built shared libraries for image versioning and repeatable artifact publication.'),
('Release Governance','Aligned release scope, dependencies, change windows, approvals, stakeholder updates, and production support across engineering teams.'),
('Automation & Build Reliability','Automated release operations with PowerShell, Python, and Bash and supported consistent Windows/Linux agent execution.')]]
p.skill_sections=[{'title':t,'content':v} for t,v in [
('Azure DevOps & Jenkins','Azure DevOps, Azure Pipelines, Jenkins, CloudBees Jenkins, reusable pipelines, shared libraries, Windows/Linux agents, agent pools'),
('.NET Build & Release','MSBuild, .NET (C#), Windows builds, PowerShell, build configuration, package publication, release promotion, deployment troubleshooting'),
('SCM & Enterprise Governance','Git, Gerrit, branching strategies, merge standards, approvals, release dependencies, change windows, release reporting'),
('JFrog & Artifact Management','JFrog Artifactory, Xray, Nexus, package feeds, upstream repositories, image versioning, controlled artifact promotion, SonarQube'),
('Docker & Deployment','Docker builds, container administration, image validation, Ansible deployment automation, environment-specific configuration'),
('Automation & Operational Security','PowerShell, Python, Bash, API integrations, secrets handling, certificate troubleshooting, deployment guides, production release support')]]
p.experience[0].skills_used=['Azure DevOps','Azure Pipelines','.NET/MSBuild','Git','PowerShell','Build Agents','Release Governance']
p.experience[0].impact=[
'Led enterprise .NET build and release delivery with Azure DevOps, coordinating application dependencies, release scope, change windows, and production readiness.',
'Standardized Azure Pipelines build and release workflows around source checkout, MSBuild execution, package publication, and controlled environment promotion.',
'Automated Windows build and deployment tasks with PowerShell, separating build configuration from environment-specific release settings.',
'Established Git branching, approval, and artifact versioning standards to preserve traceability between source changes and released packages.',
'Managed self-hosted build agents and execution environments, resolving build-tool, access, configuration, and pipeline failures.',
'Led migration of Azure DevOps repositories and delivery pipelines to GitLab, defining phased cutovers, validation gates, and rollback procedures.',
'Integrated secure secrets handling and pre-deployment checks into enterprise release workflows.',
'Coordinated release schedules, dependency reviews, milestone reporting, risk escalation, and production support across engineering teams.',
'Authored deployment guides and recovery runbooks and automated recurring release support tasks with Python, Bash, and PowerShell.']
p.experience[1].impact[1]='Administered Windows and Linux build agents, agent pools, runner templates, and execution policies to keep enterprise builds consistent and reliable.'
p.experience[1].impact.insert(3,'Separated package feeds, upstream sources, and execution settings to support repeatable dependency consumption and controlled release packaging.')
p.experience[2].impact[1]='Configured Windows/Linux build agents and environment-specific release targets, isolating deployment settings from reusable pipeline logic.'
p.experience[2].impact.insert(4,'Troubleshot failed builds and package publication by tracing source revisions, dependency resolution, agent configuration, and repository access.')
p.experience[3].impact.insert(2,'Connected Jenkins automation to Artifactory publication workflows so application teams could consume consistently versioned release outputs.')
p.experience[4].skills_used=['Jenkins','PowerShell','Git','Ansible','Release Packaging','Certificate Support']
p.experience[4].impact.insert(3,'Troubleshot certificate-management and identity-integration issues affecting enterprise application availability and release readiness.')
p.experience[5].impact.insert(4,'Managed variable groups and environment-specific settings to keep release configuration separate from the versioned application artifact.')
p.skills=['Azure DevOps','Azure Pipelines','Jenkins','.NET','MSBuild','Git/Gerrit','Docker','JFrog Artifactory','PowerShell','Release Engineering']
p.notes=['Azure/.NET focus reflects user correction. Preserves employment titles and dates. NuGet, Electron/Rust-Tauri, Inno Setup, and code signing require confirmation before being claimed as hands-on experience. Certificate support is documented; signing-certificate ownership is not inferred.']
p.email='rajendran.scm@gmail.com'
p.contact_lines_html=[v.replace('rajendranelakurthi@gmail.com',p.email) for v in p.contact_lines_html]
s.with_suffix('.profile.json').write_text(json.dumps(asdict(p),indent=2))
html=BundledHtmlResumeRenderer(a/'templates/base_resume.html').render(p)
html=html.replace('repeat(5,minmax(0,1fr))','repeat(4,minmax(0,1fr))')
s.with_suffix('.html').write_text(html)
m=json.loads(s.with_suffix('.json').read_text());m['focus']='Azure DevOps / .NET Build & Release';s.with_suffix('.json').write_text(json.dumps(m,indent=2))
assert 'AWS' not in html
assert 'rajendranelakurthi@gmail.com' not in html
