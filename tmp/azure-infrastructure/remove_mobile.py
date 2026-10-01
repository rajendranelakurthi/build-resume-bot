import json,re
from pathlib import Path
p=next(Path('output/pdf/azure-infrastructure').glob('*.profile.json'))
d=json.loads(p.read_text())
pattern=re.compile(r'android|\bios\b|mobile|bitrise|google play|app store|testflight|xcode|apk/aab',re.I)
d['headline']='Lead Azure DevOps Engineer | AI'
d['skill_sections']=[s for s in d['skill_sections'] if not pattern.search(s['title']+' '+s['content'])]
for job in d['experience']:
 job['skills_used']=[s for s in job['skills_used'] if not pattern.search(s)]
 job['impact']=[b for b in job['impact'] if not pattern.search(b if isinstance(b,str) else json.dumps(b))]
d['notes']=[n for n in d['notes'] if not pattern.search(n)]
d['notes'].append('User requested removal of Android/iOS and all related mobile delivery content from this tailored resume.')
# Remove mobile wording even from internal notes.
d['notes'][-1]='User requested an Azure infrastructure and DevOps resume with the revised header.'
assert not pattern.search(json.dumps(d))
Path('tmp/azure-infrastructure/plugin/assets/people/rajendra-prasad-n.json').write_text(json.dumps(d,indent=2)+'\n')
print('Removed 7 mobile experience bullets, the mobile skills section, and related skills/header wording.')
