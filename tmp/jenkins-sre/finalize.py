import json,sys
from pathlib import Path
from dataclasses import asdict,replace
sys.path.insert(0,str(Path('plugins/resume-creator-plugin/scripts').resolve()))
from plugin_core import BundledJsonResumeStore,BundledHtmlResumeRenderer
out=Path('output/pdf/jenkins-sre');p=next(out.glob('*.profile.json'))
d=json.loads(p.read_text());source=json.loads(Path('tmp/jenkins-sre/plugin/assets/people/rajendra-prasad-n.json').read_text())
d['full_name']='Rajendra P N';d['summary_html']=source['summary_html']
role_skills=[['Jenkins','Groovy','Python/Bash/PowerShell','Prometheus/Grafana','On-Call','Azure/AWS'],['Jenkins','Groovy','Bash/PowerShell','Azure Monitor','CloudWatch','Production Support'],['Jenkins','Groovy','Python/PowerShell','AKS/EKS','Observability','On-Call'],['CloudBees Jenkins','Python/FastAPI','JFrog','Prometheus/Grafana','On-Call','Azure/AWS'],['Jenkins','Java/Maven','Bash/PowerShell','ELK','CloudWatch','Production Support'],['Jenkins','Git','Python/Bash/PowerShell','CloudWatch','Linux','On-Call']]
for j,s in zip(d['experience'],role_skills):j['skills_used']=s
p.write_text(json.dumps(d,indent=2)+'\n')
store=BundledJsonResumeStore(out,Path('plugins/resume-creator-plugin/assets/static'))
profile=store.load_person(p.name[:-5])
html=p.with_name(p.name.replace('.profile.json','.html'))
html.write_text(BundledHtmlResumeRenderer(Path('tmp/jenkins-sre/plugin/assets/templates/base_resume.html')).render(profile))
