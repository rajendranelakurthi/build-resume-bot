import json,re
from pathlib import Path
import pdfplumber
pdf=pdfplumber.open('/Users/rajendra/Documents/1Resume/APPLIED/rajendra-pn-kubernetes.pdf');p=pdf.pages[0]
d={'full_name':'Rajendra P N','headline':'LEAD AZURE DEVOPS ENGINEER | AI | K8S','contact_lines_html':['rajendran.scm@gmail.com','+1 (469) 926-4201','Dallas, TX','linkedin.com/in/rajendranelakurthi','rajendranelakurthi.github.io'],'summary_html':p.crop((0,110,p.width,175)).extract_text(),'certifications':['Microsoft Certified: Azure DevOps Engineer Expert','Microsoft Certified: Azure Fundamentals','GitLab Certified Associate','MuleSoft Certified Developer - Level 1'],'achievements_title':'Kubernetes Platform & Reliability Highlights','achievements':[],'skill_sections':[],'experience':[],'education':[{'degree':'B.Tech (2009-2013) in Information Technology','school':'Prakasam Engineering College, Jawaharlal Nehru Technological University, Kakinada'}]}
for a,b,tag in [(300,321,'End-to-End AKS Engineering'),(322,340,'Platform Lifecycle & Reliability'),(341,354,'AI Workload Enablement')]:
 s=p.crop((0,a,p.width,b)).extract_text();d['achievements'].append({'tag':tag,'text':s[len(tag):].strip().replace('\n',' ')})
for a,b in [(385,435),(440,489),(495,534)]:
 for x0,x1 in [(38,298),(301,560)]:
  lines=p.crop((x0,a,x1,b)).extract_text().splitlines();d['skill_sections'].append({'title':lines[0],'content':' '.join(lines[1:])})
job=None;last_y=0
for i,page in enumerate(pdf.pages):
 for l in page.extract_text_lines():
  y=l['top'];s=l['text']
  if i==0 and y<560:continue
  if i==1 and y>=558:break
  if re.search(r'\d{2}/\d{4} - (?:Present|\d{2}/\d{4})$',s):
   m=re.match(r'(.*?) \| (.*?) (\d{2}/\d{4} - (?:Present|\d{2}/\d{4}))$',s);job={'title':m[1],'company':m[2],'date_range':m[3],'impact':[],'skills_used':[]};d['experience'].append(job)
  elif s.startswith('Client:'):job['client']=s[7:].strip()
  elif s.startswith('Skills Used:'):job['skills_used']=[t.strip() for t in s[12:].split(',') if 'keyvault' not in re.sub(r'\W','',t.lower())]
  elif job:
   if not job['impact'] or y-last_y>=10:job['impact'].append(s)
   else:job['impact'][-1]+=' '+s
  last_y=y
print('Bullets', [len(j['impact']) for j in d['experience']]);Path('tmp/docx/kubernetes-conversion/profile.json').write_text(json.dumps(d,indent=2))
s=Path('tmp/docx/platform-review/build.py').read_text();start=s.index("root=Path(");end=s.index('doc=Document()');s=s[:start]+"root=Path('output/docx')\nstem='rajendra-pn-kubernetes'\nd=json.loads(Path('tmp/docx/kubernetes-conversion/profile.json').read_text())\n"+s[end:];s=s.replace("certs=[s for s in d['certifications'] if 'mulesoft' not in s.lower()]","certs=d['certifications']");s=s.replace("doc.core_properties.title='Rajendra P N Platform Engineer Resume'","doc.core_properties.title='Rajendra P N Kubernetes Resume'");s=s.replace("doc.save(root/(stem+'.docx'))","\nfor style in doc.styles:\n for e in list(style.element.iter(qn('w:pBdr'))):e.getparent().remove(e)\ndoc.save(root/(stem+'.docx'))")
exec(compile(s,'builder','exec'))
