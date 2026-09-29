from pathlib import Path
import json
root=Path('plugins/resume-creator-plugin')
p=root/'scripts/plugin_core.py';s=p.read_text();a=s.index('def tailor_profile(');b=s.index('def extract_keywords(',a)
s=s[:a]+'''def tailor_profile(profile: PersonProfile, job_description: str) -> tuple[PersonProfile, list[str]]:
    """Rank the branch's Azure profile without introducing unsupported JD claims."""
    keywords = extract_keywords(job_description)
    matched = [keyword for keyword in keywords if _profile_contains(profile, keyword)][:10]
    return replace(
        profile,
        achievements=rank_tagged_items(profile.achievements, keywords),
        skill_sections=rank_tagged_items(profile.skill_sections, keywords, content_key="content"),
        experience=[rank_experience(job, keywords) for job in profile.experience],
    ), matched


'''+s[b:]
a=s.index('def build_summary(');b=s.index('def rank_tagged_items(',a);s=s[:a]+s[b:];p.write_text(s)
p=root/'scripts/run_resume_request.py';s=p.read_text();a=s.index('def resolve_person_id(');b=s.index('def normalize_level(',a)
s=s[:a]+'''def normalize_domain(domain: str) -> str:
    """This branch supports Azure only; keep the old input as an alias."""
    normalized = domain.strip().lower()
    if normalized in {"azure-devops", "devops-cloud"}:
        return "azure-devops"
    raise ValueError(f"Unsupported domain {domain!r}; use azure-devops on this branch.")


def resolve_person_id(person: str, domain: str) -> str:
    normalize_domain(domain)
    if person.strip().lower() != "rajendra":
        raise ValueError(f"Unsupported person: {person!r}")
    return "rajendra-prasad-n"


'''+s[b:]
s=s.replace('    person_id = resolve_person_id(request.person, request.domain)','    domain = normalize_domain(request.domain)\n    person_id = resolve_person_id(request.person, domain)').replace('f"{request.person}-{request.domain}"','f"{request.person}-{domain}"').replace('{person_id}-{request.domain}-{level.lower()}','{person_id}-{domain}-{level.lower()}').replace('"domain": request.domain','"domain": domain').replace('choices=["devops-cloud"], help="Resume domain routing key"','type=normalize_domain, choices=["azure-devops"], help="Azure DevOps domain (legacy devops-cloud is an alias)"');p.write_text(s)
p=Path('src/resume_agents/tailor.py');s=p.read_text();a=s.index('def build_summary(');b=s.index('def rank_tagged_items(',a);s=s[:a]+'''def build_summary(profile: PersonProfile, matched_keywords: list[str], missing_keywords: list[str]) -> str:
    # Preserve the authored Azure summary. JD terms are ranking inputs, not evidence.
    return profile.summary_html or f"<strong>{escape(profile.headline)}</strong>"


'''+s[b:];p.write_text(s)
for path in [root/'assets/templates/base_resume.html',Path('templates/base_resume.html')]:
 s=path.read_text().replace('Approved Rajendra header: Lead DevOps Engineer | Multi-Cloud','Azure branch header is supplied by the structured profile')
 s=s.replace('#174a8b','#0067a8').replace('#0f3970','#004578')
 s=s.replace('</style>','''/* Azure branch print layout: retain readable role blocks and compact credentials. */
@media print{
.header-left{flex:1;min-width:0}.header-right{flex:0 0 51mm}
.cert-badge-svg{max-width:46px}.cert-card{min-height:76px}
.job-block{break-inside:auto;page-break-inside:auto}
.job-header,.job-details{break-after:avoid;page-break-after:avoid}
li{break-inside:avoid}.section-title{margin-top:12px}
}
</style>''');path.write_text(s)
p=root/'.codex-plugin/plugin.json';s=json.loads(p.read_text());s['description']='Create Azure DevOps resumes for Rajendra with CI/CD, Python, SSIS, Bicep, and secure Azure operations.';s['interface']['shortDescription']='Tailor Azure DevOps resumes and export HTML/PDF.';s['interface']['longDescription']='Azure-only branch workflow for Rajendra: select a tailoring level and JD to generate Azure DevOps, automation, SSIS, Bicep, security, and production-support resume content.';s['interface']['defaultPrompt']=['Use the Résumé Creator Plugin to create an Aggressive Azure-devops resume for Rajendra using this JD: <provide JD>','Create a Tailored Azure-devops resume for Rajendra.'];s['keywords']=list(dict.fromkeys(s['keywords']+['azure-devops','bicep','ssis']));p.write_text(json.dumps(s,indent=2)+'\n')
