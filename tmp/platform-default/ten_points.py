import json,sys
from pathlib import Path
p=Path('resume_data/people/rajendra-prasad-n.json');d=json.loads(p.read_text())
points=[
'Automated deployment concurrency and smoke-test checks in GitHub Actions, preventing overlapping environment updates and capturing verification evidence for release decisions.',
'Validated reusable workflow changes in isolated test jobs, checking input contracts, artifact paths, and environment settings before adoption by application teams.',
'Coordinated AKS node maintenance and application upgrades, verifying workload readiness and recovery steps with service owners before production changes.',
'Managed artifact retention and dependency access for shared delivery services, troubleshooting repository failures and preserving approved build inputs for recovery.',
'Validated certificate expiry and service connectivity during release readiness checks, coordinating configuration fixes with application and infrastructure owners.',
'Captured deployment manifests and configuration baselines for environment handoffs, helping support teams trace runtime failures to source or release changes.'
]
for j,b in zip(d['experience'],points):
 if b not in j['impact']:j['impact'].append(b)
 assert len(j['impact'])>=10
 d['notes']=[n.replace('nine substantive bullets','at least ten substantive bullets') for n in d['notes']]
for q in [p,Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json')]:q.write_text(json.dumps(d,indent=2)+'\n')
for name in ['instructions.md','RESUME_WORKFLOW.md','plugins/resume-creator-plugin/skills/resume-creator/SKILL.md']:
 q=Path(name);s=q.read_text().replace('9+','10+').replace('nine or more substantive bullets','ten or more substantive bullets').replace('nine substantive bullets','ten substantive bullets');q.write_text(s)
q=Path('instructions.md');q.write_text(q.read_text()+'\n## Minimum Project Bullet Count (2026-10-06)\n\nEvery employer/project must contain at least 10 distinct, substantive experience bullets in the base and every future resume, at every tailoring level. Preserve this minimum when rewriting or removing content. The generator validates the minimum before writing artifacts; revise the structured profile when validation fails.\n')
q=Path('RESUME_WORKFLOW.md');q.write_text(q.read_text()+'\nEvery future resume must retain at least 10 substantive bullets per employer/project. Validate counts before rendering; do not satisfy the minimum with repeated filler.\n')
q=Path('README.md');q.write_text(q.read_text()+'\n## Resume content minimum\n\nAll base and future tailored resumes must contain at least **10 distinct, substantive bullets per employer/project**. The plugin validates this before generating output.\n')
q=Path('plugins/resume-creator-plugin/scripts/run_resume_request.py');s=q.read_text();s=s.replace('    request_slug = slugify(request.jd', '''    validate_project_bullets(output_profile)

    request_slug = slugify(request.jd''')
pos=s.index('def render_request(')
s=s[:pos]+'''MIN_PROJECT_BULLETS = 10


def validate_project_bullets(profile) -> None:
    short_projects = [f"{job.company}: {len(job.impact)}" for job in profile.experience
                      if len(job.impact) < MIN_PROJECT_BULLETS]
    if short_projects:
        raise ValueError("Every project requires at least 10 substantive bullets; revise "
                         + "; ".join(short_projects))


'''+s[pos:];q.write_text(s)
q=Path('tests/test_service.py');q.write_text(q.read_text().replace('at_least_nine_points','at_least_ten_points').replace('count >= 9','count >= 10'))
q=Path('tests/test_resume_creator_plugin.py');s=q.read_text()+'''

def test_project_minimum_rejects_short_variants():
    from dataclasses import replace
    import pytest
    module = _load_module("run_min_project_test", "run_resume_request.py")
    core = _load_module("core_min_project_test", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    module.validate_project_bullets(profile)
    short = replace(profile, experience=[replace(profile.experience[0], impact=profile.experience[0].impact[:9])])
    with pytest.raises(ValueError, match="at least 10"):
        module.validate_project_bullets(short)
''';q.write_text(s)
sys.path.insert(0,'plugins/resume-creator-plugin/scripts')
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer
profile=BundledJsonResumeStore(Path('plugins/resume-creator-plugin/assets/people'),Path('plugins/resume-creator-plugin/assets/static')).load_person('rajendra-prasad-n')
html=BundledHtmlResumeRenderer(Path('plugins/resume-creator-plugin/assets/templates/base_resume.html')).render(profile)
for q in [Path('examples/rajendra-prasad-n.html'),Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-platform-engineer-base.html')]:q.write_text(html)
print('Project counts:',[len(j.impact) for j in profile.experience])
