import json,sys
from pathlib import Path
extra=[
'Automated environment prerequisite checks for DNS resolution, service endpoints, and required configuration, catching deployment blockers before release execution.',
'Created reusable Python diagnostics to collect workload status and recent failures, giving developers consistent evidence for application troubleshooting.',
'Reviewed container resource requests and deployment settings with service owners, addressing capacity constraints and unstable application startup behavior.',
'Maintained release recovery checklists and verified rollback inputs in nonproduction environments, improving readiness for failed application deployments.',
'Published platform onboarding examples and troubleshooting documentation, helping application teams adopt shared pipelines and resolve common configuration issues.']
paths=[Path('resume_data/people/rajendra-prasad-n.json'),Path('plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json'),Path('tmp/java-platform/assets/people/rajendra-prasad-n.json')]+list(Path('output/java-platform').glob('*.profile.json'))
for p in paths:
 d=json.loads(p.read_text());e=d['experience'][0]
 for s in extra:
  if s not in e['impact']:e['impact'].append(s)
 d['notes']=[s.replace('at least ten substantive bullets per project','at least fifteen substantive bullets in the latest project and ten in every other project') for s in d.get('notes',[])]
 p.write_text(json.dumps(d,indent=2)+'\n')
for name in ['templates/base_resume.html','plugins/resume-creator-plugin/assets/templates/base_resume.html','tmp/java-platform/assets/templates/base_resume.html']:
 p=Path(name);s=p.read_text().replace('repeat(5,minmax(0,1fr))','repeat(4,minmax(0,1fr))').replace('align-items:start;','align-items:stretch;');p.write_text(s)
for name in ['src/resume_agents/renderers/html_resume.py','plugins/resume-creator-plugin/scripts/plugin_core.py']:
 p=Path(name);s=p.read_text()
 if name.startswith('src'):
  s=s.replace('for item in profile.certifications\n','for item in profile.certifications if "mulesoft" not in item.lower()\n')
 else:s=s.replace('for item in profile.certifications)','for item in profile.certifications if "mulesoft" not in item.lower())')
 p.write_text(s)
p=Path('plugins/resume-creator-plugin/scripts/run_resume_request.py');s=p.read_text().replace('MIN_PROJECT_BULLETS = 10','MIN_PROJECT_BULLETS = 10\nMIN_LATEST_PROJECT_BULLETS = 15');s=s.replace('\n\ndef render_request(', '\n    if profile.experience and len(profile.experience[0].impact) < MIN_LATEST_PROJECT_BULLETS:\n        raise ValueError("Latest project requires at least 15 substantive bullets")\n\n\ndef render_request(');p.write_text(s)
for name in ['instructions.md','RESUME_WORKFLOW.md','plugins/resume-creator-plugin/skills/resume-creator/SKILL.md']:
 p=Path(name)
 if p.exists():p.write_text(p.read_text()+'\nLatest project minimum: 15 distinct substantive bullets; all other projects minimum: 10. Hide MuleSoft certification badge in rendered resumes. Use four evenly aligned certification cards.\n')
sys.path.insert(0,'plugins/resume-creator-plugin/scripts')
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer
renderer=BundledHtmlResumeRenderer(Path('plugins/resume-creator-plugin/assets/templates/base_resume.html'))
base=BundledJsonResumeStore(Path('resume_data/people'),Path('plugins/resume-creator-plugin/assets/static')).load_person('rajendra-prasad-n')
for name in ['examples/rajendra-prasad-n.html','tailored_resume/rajendra-prasad-n/rajendra-prasad-n-platform-engineer-base.html']:Path(name).write_text(renderer.render(base))
for p in Path('output/java-platform').glob('*.profile.json'):
 profile=BundledJsonResumeStore(p.parent,Path('plugins/resume-creator-plugin/assets/static')).load_person(p.name[:-5])
 Path(str(p).replace('.profile.json','.html')).write_text(renderer.render(profile))
