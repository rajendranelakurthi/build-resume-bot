import json
from pathlib import Path
# Branch-local default, retaining historical employer titles and approved identity.
p=Path('resume_data/people/rajendra-prasad-n.json');d=json.loads(p.read_text())
d['headline']='Lead Platform Engineer | Developer Experience | Cloud Infrastructure'
d['page_title']='Rajendra P N - Lead Platform Engineer'
d['summary_html']='<strong>Lead Platform Engineer with 10+ years of experience building cloud infrastructure, delivery automation, and reliable production platforms.</strong> Develops reusable <strong>Terraform/Ansible modules, Kubernetes/Helm deployment patterns, GitOps workflows, and CI/CD templates</strong> across AWS and Azure. Builds Python and API-based self-service automation for developer onboarding and operational tasks, integrating security controls and observability into shared platform capabilities. Partners with application, infrastructure, and security teams to improve developer experience, platform reliability, documentation, and operational readiness.'
d['skills']=list(dict.fromkeys(['Platform Engineering','Developer Experience','Self-Service Automation','Kubernetes','Terraform','Ansible','Helm','Argo CD','Python','AWS','Azure']+d['skills']))
d['achievements_title']='Key Platform Achievements'
d['skill_sections'].insert(0,{'title':'Platform Engineering & Developer Experience','content':'Reusable infrastructure modules, self-service onboarding, standardized deployment paths, shared CI/CD templates, platform APIs, operational runbooks, engineering enablement'})
d['achievements'].insert(0,{'tag':'Developer Enablement','text':'Built reusable delivery workflows and API-based onboarding automation, providing consistent platform capabilities and documented deployment standards for application teams.'})
# Reuse prior approved nine-bullet project variants where this branch has sparse older roles.
extra = [
    "Maintained reusable Terraform configuration and Ansible automation for consistent cloud environment setup and Linux operational tasks.",
    "Packaged containerized services with Helm and versioned environment values, validating deployment health and recovery before release.",
    "Developed Python and shell utilities for environment checks and platform diagnostics, publishing documented automation for engineering teams.",
    "Reviewed pipeline credentials, branch controls, and deployment permissions with application teams to support secure shared delivery workflows.",
    "Documented onboarding, platform configuration, and support procedures, helping developers adopt repeatable environment and release practices.",
]
for j in d['experience']:
    for bullet in extra:
        if len(j['impact']) >= 9: break
        j['impact'].append(bullet)
j=d['experience'][0];j['title']='Lead SRE'
j['impact'][0]='Built shared platform capabilities with reusable CI/CD templates, Terraform modules, and deployment standards, enabling consistent application delivery across AWS and Azure.'
j['impact'][1]='Automated developer onboarding and operational workflows with Python and REST APIs, documenting supported configuration and delivery patterns for engineering teams.'
d['notes']=['Platform Engineer is the default domain on feature/rajendrapn-platformengineer.','Preserve the platform headline and 10+ years wording; retain employment history, Lead SRE first role, certifications, and nine or more substantive bullets per project.','No Android/iOS delivery content. JD-specific changes belong in generated variants; leave changes uncommitted for the user.']
for q in [p,Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json')]:q.write_text(json.dumps(d,indent=2)+'\n')
# CLI domain normalization and structured output.
p=Path('plugins/resume-creator-plugin/scripts/run_resume_request.py');s=p.read_text().replace('from dataclasses import dataclass','from dataclasses import asdict, dataclass')
start=s.index('def resolve_person_id(');end=s.index('\n\ndef normalize_level',start)
s=s[:start]+'''def normalize_domain(domain: str) -> str:
    normalized = re.sub(r"[\\s_]+", "-", domain.strip().lower())
    if normalized in {"platform-engineer", "platform-engineering", "devops-cloud", "devops-sre"}:
        return "platform-engineer"
    raise ValueError(f"Unsupported domain: {domain!r}; use platform-engineer.")


def resolve_person_id(person: str, domain: str) -> str:
    normalize_domain(domain)
    if person.strip().lower() != "rajendra":
        raise ValueError(f"Unsupported person: {person!r}")
    return "rajendra-prasad-n"
'''+s[end:]
s=s.replace('person_id = resolve_person_id(request.person, request.domain)','domain = normalize_domain(request.domain)\n    person_id = resolve_person_id(request.person, domain)').replace('{request.domain}-{level.lower()}','{domain}-{level.lower()}').replace('"domain": request.domain','"domain": domain')
s=s.replace('    html_path.write_text(renderer.render(output_profile)', '    profile_path = html_path.with_suffix(".profile.json")\n    profile_path.write_text(json.dumps(asdict(output_profile), indent=2) + "\\n", encoding="utf-8")\n    html_path.write_text(renderer.render(output_profile)')
s=s.replace('"html_path": str(html_path),','"profile_path": str(profile_path),\n        "html_path": str(html_path),')
s=s.replace('required=True, choices=["devops-cloud"], help="Resume domain routing key"','default="platform-engineer", type=normalize_domain, choices=["platform-engineer"], help="Platform Engineer domain; devops-cloud/devops-sre remain aliases"')
p.write_text(s)
# Platform variants rank grounded content instead of dispatching to unrelated historical domain builders.
p=Path('plugins/resume-creator-plugin/scripts/plugin_core.py');s=p.read_text();needle='    tailored, keywords = _tailor_profile_content(profile, job_description)'
s=s.replace(needle,'''    if profile.headline.startswith("Lead Platform Engineer"):
        keywords = extract_keywords(job_description)
        matched = [word for word in keywords if _profile_contains(profile, word)][:10]
        return replace(profile,
            achievements=rank_tagged_items(profile.achievements, keywords),
            skill_sections=rank_tagged_items(profile.skill_sections, keywords, content_key="content"),
            experience=[rank_experience(job, keywords) for job in profile.experience]), matched
'''+needle);p.write_text(s)
p=Path('src/resume_agents/tailor.py');s=p.read_text().replace('tailored_summary = build_summary(profile, matched_keywords, missing_keywords)','tailored_summary = (profile.summary_html if profile.headline.startswith("Lead Platform Engineer")\n                        else build_summary(profile, matched_keywords, missing_keywords))');p.write_text(s)
# Active package docs and prompts.
for name in ['README.md','plugins/resume-creator-plugin/INSTALL.md','plugins/resume-creator-plugin/skills/resume-creator/SKILL.md','plugins/resume-creator-plugin/skills/resume-creator/agents/openai.yaml']:
 p=Path(name);s=p.read_text().replace('devops-cloud','platform-engineer').replace('DevOps / Cloud','Platform Engineer').replace('DevOps/Cloud','Platform Engineer').replace('Switch to the plugin branch:','Use the platform engineering branch:').replace('git switch plug-in','git switch feature/rajendrapn-platformengineer');p.write_text(s)
p=Path('plugins/resume-creator-plugin/skills/resume-creator/SKILL.md');s=p.read_text().replace('Notes:\n','Notes:\n- This branch defaults to `platform-engineer`; `Platform-Engineer`, `platform engineer`, `devops-cloud`, and `devops-sre` normalize to it.\n- Preserve the platform header, summary, historical job titles, and 9+ substantive bullets per project.\n- Rewrite the structured profile against each supplied JD before rendering; the deterministic engine ranks content and does not perform a full semantic rewrite.\n');p.write_text(s)
p=Path('plugins/resume-creator-plugin/.codex-plugin/plugin.json');d=json.loads(p.read_text());
def convert(x):
 if isinstance(x,str):return x.replace('devops-cloud','platform-engineer').replace('DevOps/Cloud','Platform Engineer')
 if isinstance(x,list):return [convert(v) for v in x]
 if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
 return x
p.write_text(json.dumps(convert(d),indent=2)+'\n')
for name in ['templates/base_resume.html','plugins/resume-creator-plugin/assets/templates/base_resume.html']:
 p=Path(name);p.write_text(p.read_text().replace('Lead DevOps Engineer | SaaS Platforms | AWS','Lead Platform Engineer | Developer Experience | Cloud Infrastructure'))
p=Path('instructions.md');s=p.read_text().replace('Always use **Lead DevOps Engineer**','Always use **Lead Platform Engineer**').replace('**Lead DevOps Engineer | SaaS Platforms | AWS**','**Lead Platform Engineer | Developer Experience | Cloud Infrastructure**');s+='\n## Platform Engineer Branch Defaults (2026-10-06)\n\n- On `feature/rajendrapn-platformengineer`, use `platform-engineer` for future requests; legacy DevOps domains normalize to this domain.\n- Use the synchronized platform base profiles and profile-driven templates. Prioritize developer experience, reusable infrastructure, self-service automation, Kubernetes/GitOps, CI/CD standards, security and reliability.\n- Preserve Lead SRE for the first employment role and 9+ substantive bullets per project; exclude mobile delivery content.\n- Leave changes uncommitted; the user commits. These branch-specific instructions supersede older header/domain instructions.\n';p.write_text(s)
p=Path('RESUME_WORKFLOW.md');p.write_text(p.read_text().replace('**Lead DevOps Engineer | SaaS Platforms | AWS**','**Lead Platform Engineer | Developer Experience | Cloud Infrastructure**')+'\n## Platform Engineer Default Workflow (2026-10-06)\n\nUse `python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py --person Rajendra --domain platform-engineer --level Aggressive --jd-file <JD>`. The default domain is platform-engineer. Legacy devops-cloud/devops-sre commands remain aliases. Both base profiles and templates use the platform designation. Platform tailoring preserves the summary/history and ranks JD-relevant content; perform structured JD rewriting before invoking the renderer. Never promote a JD variant to the base without user instruction.\n')
