from pathlib import Path
from html import escape
import json
src=Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-ai-azure-devops-aggressive')
p=json.loads(src.with_suffix('.profile.json').read_text())
h=src.with_suffix('.html').read_text()
bullets=[
'Built Harness CI/CD pipelines for C#/.NET and Java applications, integrating source control, automated builds and tests, container image publication to ACR, and deployments to AKS.',
'Created reusable Harness pipeline, stage, and step templates with runtime inputs and environment-specific configuration to standardize application onboarding and release promotion.',
'Deployed and maintained Harness delegates on Kubernetes; configured Git, Azure, container registry, and cluster connectors and resolved authentication, connectivity, and task execution failures.',
'Configured Harness services, environments, and infrastructure definitions for Kubernetes application delivery using versioned manifests, Helm charts, and controlled artifact selection.',
'Implemented rolling and canary deployment workflows with approval gates, health checks, failure strategies, and rollback steps to support controlled production releases.',
'Applied Harness RBAC and secret references to protect deployment credentials, reviewed execution logs and audit trails, and automated support tasks with Python and Bash.'
]
anchor=p['experience'][0]['impact'][5]
old='<li>'+escape(anchor)+'</li>'
assert h.count(old)==1
h=h.replace(old,old+'\n'+'\n'.join('<li>'+escape(b)+'</li>' for b in bullets))
p['experience'][0]['impact'][6:6]=bullets
oldskills=', '.join(p['experience'][0]['skills_used'])
p['experience'][0]['skills_used'].insert(3,'Harness CI/CD')
h=h.replace(escape(oldskills),escape(', '.join(p['experience'][0]['skills_used'])))
oldcore=p['skill_sections'][1]['content']
p['skill_sections'][1]['content']='Harness CI/CD, '+oldcore
h=h.replace(escape(oldcore),escape(p['skill_sections'][1]['content']))
# Keep the supplied design and restore horizontal date alignment for print.
h=h.replace('</style>','@media print{.job-header{flex-direction:row;} .job-meta{white-space:nowrap;}}\n</style>')
out=Path('output/pdf/rajendra-pn-ai-azure-devops-harness')
out.with_suffix('.html').write_text(h)
out.with_suffix('.profile.json').write_text(json.dumps(p,indent=2))
assert all(escape(b) in h for j in p['experience'] for b in j['impact'])
print('Added 6 Harness responsibilities; retained all original experience bullets.')
