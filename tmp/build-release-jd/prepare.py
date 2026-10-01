import json
from pathlib import Path
f=Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json');p=json.loads(f.read_text())
p['full_name']='Rajendra P N';p['page_title']='Rajendra P N - Lead Build & Release Engineer';p['headline']='Lead Build & Release Engineer | CI/CD & Developer Productivity';p['certification_badges_alt']='Rajendra P N certification badges'
p['summary_html']='<strong>Lead Build & Release Engineer with 10+ years of experience in software delivery, build automation, and production troubleshooting.</strong> Engineers <strong>Jenkins pipelines, Python automation, Git release workflows, and Linux build environments</strong> to improve developer productivity and release quality. Brings experience with reusable pipeline libraries, artifact repositories, Ansible configuration management, and cross-team issue resolution. Uses AI-assisted engineering with human review to support automation, troubleshooting, and technical documentation.'
p['skills']=['Jenkins','Groovy','Python','Linux','Git','Ansible','Maven','Gradle','Make','JFrog Artifactory','Nexus','CI/CD']
p['skill_sections']=[{'title':'Build & Continuous Integration','content':'Jenkins, CloudBees Jenkins, Groovy shared libraries, Jenkinsfile, GitLab CI/CD, GitHub Actions, Maven, Gradle, Make, ANT, MSBuild'}, {'title':'SCM & Artifact Management','content':'Git, branching strategies, merge reviews, release tags, versioned packages, JFrog Artifactory, Nexus, dependency management, reusable build components'}, {'title':'Automation & Linux','content':'Python, FastAPI, Bash, PowerShell, Linux, RHEL, Ubuntu, REST APIs, build agents, environment configuration, diagnostic scripts'}, {'title':'Infrastructure & Configuration','content':'Ansible roles and playbooks, Terraform, Docker, Kubernetes, Helm, version-controlled infrastructure, repeatable build environments'}, {'title':'Code Quality & Diagnostics','content':'SonarQube, JFrog Xray, automated tests, security checks, build logs, pipeline metrics, root cause analysis, defect tracking'}, {'title':'AI & Engineering Enablement','content':'GitLab Duo, AI-assisted code and test drafting, human review, data-handling controls, Jira integrations, release documentation, technical runbooks'}]
p['achievements_title']='Build & Release Engineering Highlights'
p['achievements']=[{'tag':'Build Automation','text':'Standardized reusable CI/CD workflows, build-agent configuration, artifact publication, and release checks across engineering teams.'},{'tag':'Developer Productivity','text':'Developed Python automation and service integrations to streamline project onboarding, pipeline administration, and recurring release tasks.'},{'tag':'Release Quality','text':'Combined Git controls, versioned artifacts, code-quality checks, troubleshooting, and technical documentation to strengthen repeatable delivery.'}]
# Retain historical employment designations and dates.
indices=[[1,2,3,4,5,7,12,13,14],[0,1,2,3,5,6,7,8,9],[0,1,2,5,8,9,10,11,12],[0,4,6,8,9,10,11,12,13],[0,1,2,3,4,5,7,9,14],[0,1,2,5,6,7,8,9,10]]
for e,ix in zip(p['experience'],indices):e['impact']=[e['impact'][i] for i in ix];e['skills_used']=[x for x in e['skills_used'] if x not in ['AWS','EKS','Linode']]
p['experience'][0]['impact'][0]='Administered source repositories, protected branches, merge approvals, access controls, and code ownership rules to support shared development and release governance.'
p['experience'][0]['impact'][2]='Architected reusable CI/CD templates with staged build execution, artifact retention, dependency caching, environment promotion, and controlled release approvals.'
p['experience'][0]['impact'][3]='Operated Linux build runners with workload-specific pools, isolated execution, and cache configuration; investigated queue time, capacity, and build failures.'
p['experience'][0]['impact'][4]='Integrated AI-assisted code explanation, test drafting, and documentation into engineering workflows, requiring human review and appropriate data handling.'
p['experience'][0]['impact'][6]='Developed Python and Bash tools for repository bootstrap, pipeline variables, runner setup, and release validation, reducing repetitive developer support work.'
p['experience'][3]['impact'][-1]='Developed Jenkins Groovy shared libraries for image versioning and artifact publication to private JFrog repositories, enabling reuse across application pipelines.'
p['notes']=['Authored build-release branch profile; preserve its content during JD ranking.','Preferred name Rajendra P N; 10+ years; minimum nine substantive points per role.','Specialist JD requirements Bazel, C/C++, Nix, QNX, monorepo ownership, thread-safe embedded development, and FDA experience require candidate confirmation.']
for target in [f,Path('resume_data/people/rajendra-prasad-n.json')]:target.write_text(json.dumps(p,indent=2)+'\n')
# Keep authored build/release data from being replaced by legacy five-bullet variants.
q=Path('plugins/resume-creator-plugin/scripts/plugin_core.py');s=q.read_text();needle='    lowered_jd = job_description.lower()\n';s=s.replace(needle,needle+'''    if "Authored build-release branch profile; preserve its content during JD ranking." in profile.notes:
        return replace(
            profile,
            achievements=rank_tagged_items(profile.achievements, keywords),
            skill_sections=rank_tagged_items(profile.skill_sections, keywords, content_key="content"),
            experience=[rank_experience(job, keywords) for job in profile.experience],
        ), matched_keywords
''',1);q.write_text(s)
for target in [Path('templates/base_resume.html'),Path('plugins/resume-creator-plugin/assets/templates/base_resume.html')]:
 s=target.read_text().replace('Core Technologies','Build, Release & Automation Skills');s=s.replace('<html lang="en">','<html lang="en">\n<!-- Build/release template: Rajendra P N; profile-driven headline; minimum nine substantive bullets per role. -->',1);target.write_text(s)
q=Path('instructions.md');s=q.read_text();s+='''\n## Build and release branch defaults
- Display name: Rajendra P N. Keep 10+ years experience wording.
- Use a build-and-release headline and content on feature/buildnrelease; preserve historical employer titles and dates.
- All future resumes and the standard base require at least nine substantive bullets per role.
- Prioritize build systems, Jenkins/Groovy, Python, Linux, Git, artifact management, Ansible, developer productivity, AI-assisted automation, and documentation.
- Do not infer Bazel, C/C++, Nix, QNX, thread-safe embedded application development, monorepo ownership, or FDA experience from the JD.
- Use the packaged workflow with --domain devops-cloud and outputs in tailored_resume/rajendra-prasad-n/.
- Leave work uncommitted for the user, following the established session preference.
''';q.write_text(s)
q=Path('README.md');s=q.read_text();s='''# Rajendra Build & Release Resume

This branch uses the Résumé Creator Plugin to tailor Rajendra P N's build and release engineering resume. The reusable base keeps 10+ years of experience, historical employment titles and dates, and at least nine substantive points for every role.

## Request command

```text
Use the Résumé Creator Plugin to create an Aggressive devops-cloud resume for Rajendra using this JD:
<paste the job description here>
```

## Generate HTML and PDF

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \\
  --person Rajendra \\
  --domain devops-cloud \\
  --level Aggressive \\
  --jd-file tmp/build-release-jd/jd.txt \\
  --output-dir tailored_resume/rajendra-prasad-n
```

The build/release base emphasizes build systems, CI, Jenkins/Groovy, Python, Linux, Git branching, artifact management, Ansible, developer productivity, AI-assisted automation, troubleshooting, and technical documentation. Add specialist tools or regulated-industry experience only when supported by the candidate's history.

The shared and plugin HTML templates render the name, headline, skills, and experience from structured profile data. Update both `resume_data/people/rajendra-prasad-n.json` and `plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json` when changing the reusable base. Final output belongs in `tailored_resume/rajendra-prasad-n/`.

---

'''+s;q.write_text(s)
