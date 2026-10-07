from pathlib import Path
import json,re
from docx import Document
src=Document('/Users/rajendra/Documents/1Resume/APPLIED/rajendra-pn-platform-engineer.docx')
k=json.loads(Path('tmp/docx/kubernetes-conversion/profile.json').read_text())
d=dict(k);d['headline']='Lead DevOps Engineer'
d['summary_html']='Lead DevOps Engineer with 10+ years of IT infrastructure, Kubernetes platform engineering, CI/CD automation, and production operations experience. Designs and administers Azure infrastructure and end-to-end AKS platforms using Terraform, Azure DevOps, Jenkins, Helm, and Argo CD GitOps. Builds developer self-service integrations with Python/FastAPI, manages Linux/Unix systems and build agents, and delivers GPU workloads and Milvus/Qdrant services. Combines Kubernetes security, observability, upgrade planning, resource optimization, SonarQube quality controls, and JFrog artifact management with senior incident troubleshooting. Brings GCP/GKE knowledge and HIPAA/SOC2 control awareness; hands-on cloud delivery focuses on Azure.'
d['certifications']=[c.text for c in src.tables[1].rows[0].cells]
d['achievements_title']='Kubernetes & Platform Engineering Highlights'
d['achievements']=[{'tag':'End-to-End Kubernetes Platforms','text':'Connects AKS architecture, security, workload onboarding, observability, scaling, upgrades, and recovery readiness into maintainable platform services.'},{'tag':'Developer Enablement','text':'Standardizes reusable Terraform, CI/CD, GitOps, artifacts, build agents, and Python/FastAPI self-service workflows for repeatable application delivery.'},{'tag':'AI Workload & Production Operations','text':'Deploys GPU capacity and persistent vector database services while troubleshooting platform incidents and improving resource utilization and operational readiness.'}]
d['skill_sections']=[]
for row in src.tables[2].rows:
 for c in row.cells:
  lines=c.text.split('\n');d['skill_sections'].append({'title':lines[0],'content':' '.join(lines[1:])})
# Consolidate complementary Kubernetes lifecycle skills into the platform categories.
for s in d['skill_sections']:
 if s['title']=='Containers & Production Operations':s['content']='Kubernetes, AKS, Docker, Azure CNI, ingress/DNS, namespaces, RBAC, workload identity, NetworkPolicies, TLS/certificates, HPA, cluster autoscaler, requests/limits; AKS upgrades, API compatibility, cordon/drain, PodDisruptionBudgets, surge capacity; OpenShift projects/routes'
 if s['title']=='Vector Database Platform Operations':s['title']='AI & Vector Database Platforms';s['content']='GPU node pools, NVIDIA device plugin, GPU requests, taints/tolerations, node affinity, Milvus, Qdrant, Helm, StatefulSets, persistent storage, sizing, health checks, backup/restore'
d['experience']=[];job=None;active=False
for p in src.paragraphs:
 s=p.text
 if s=='Professional Experience':active=True;continue
 if s=='Education':break
 if not active or not s:continue
 m=re.match(r'(.*?) \| (.*?)\s+(\d{2}/\d{4} - (?:Present|\d{2}/\d{4}))$',s)
 if m:job={'title':m[1],'company':m[2],'date_range':m[3],'skills_used':[],'impact':[]};d['experience'].append(job)
 elif s.startswith('Client:'):job['client']=s[7:].strip()
 elif s.startswith('Skills Used:'):job['skills_used']=[t.strip() for t in s[12:].split(',') if 'keyvault' not in re.sub(r'\W','',t.lower())]
 else:job['impact'].append(s)
a=d['experience'][0];a['title']='Lead DevOps Engineer'
# Replace overlapping points with the fuller Kubernetes versions, preserving unique platform work.
for pi,ki in [(0,0),(5,6),(7,3),(11,4)]:a['impact'][pi]=k['experience'][0]['impact'][ki]
for ki in [1,7,8,9,10]:a['impact'].append(k['experience'][0]['impact'][ki])
a['skills_used']+=['FastAPI','GPU Nodes','Docker','Bicep','Prometheus','Grafana']
a['impact'].insert(13,k['experience'][0]['impact'][2])
a['impact'].pop(8) # retain the more specific Jenkins/SonarQube/JFrog quality-gate point
# Carry Kubernetes specifics into historical projects without duplicating common delivery work.
b=d['experience'][2];b['impact'][9]=k['experience'][2]['impact'][3];b['impact'][8]=k['experience'][2]['impact'][0];b['impact'][3]=k['experience'][2]['impact'][1];b['skills_used']+=['GPU Nodes','Python']
b=d['experience'][1];b['impact'][9]=k['experience'][1]['impact'][3];b['skills_used']+=['Helm']
b=d['experience'][3];b['skills_used']+=['AKS','Prometheus','Grafana','Helm']
b=d['experience'][5];b['impact'][1]=k['experience'][5]['impact'][1];b['skills_used']+=['PowerShell','ARM templates']
for j in d['experience']:j['skills_used']=list(dict.fromkeys(j['skills_used']))
Path('output/docx/rajendra-pn-devops-kubernetes-platform.profile.json').write_text(json.dumps(d,indent=2))
s=Path('tmp/docx/platform-review/build.py').read_text();start=s.index('root=Path(');end=s.index('doc=Document()');s=s[:start]+"root=Path('output/docx')\nstem='rajendra-pn-devops-kubernetes-platform'\nd=json.loads((root/(stem+'.profile.json')).read_text())\n"+s[end:]
s=s.replace("doc.core_properties.title='Rajendra P N Platform Engineer Resume'","doc.core_properties.title='Rajendra P N DevOps Kubernetes and Platform Engineer Resume'")
s=s.replace("doc.save(root/(stem+'.docx'))","\nfor style in doc.styles:\n for e in list(style.element.iter(qn('w:pBdr'))):e.getparent().remove(e)\ndoc.save(root/(stem+'.docx'))")
exec(compile(s,'builder','exec'))
print('Project bullets:',[len(j['impact']) for j in d['experience']])
