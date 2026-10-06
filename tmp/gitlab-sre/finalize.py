import json,sys
from pathlib import Path
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer
p=next(Path('output/pdf/gitlab-sre').glob('*.profile.json'));d=json.loads(p.read_text())
d['summary_html']=json.loads(Path('tmp/gitlab-sre/plugin/assets/people/rajendra-prasad-n.json').read_text())['summary_html']
p.write_text(json.dumps(d,indent=2)+'\n')
profile=BundledJsonResumeStore(p.parent,Path('plugins/resume-creator-plugin/assets/static')).load_person(p.name[:-5])
p.with_name(p.name.replace('.profile.json','.html')).write_text(BundledHtmlResumeRenderer(Path('tmp/gitlab-sre/plugin/assets/templates/base_resume.html')).render(profile))
