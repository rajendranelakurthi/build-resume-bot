from pathlib import Path
import re
p=Path('tailored_resume/rajendra-prasad-n/rajendra-prasad-n-azure-devops-aggressive-gitops-administrator-devops-engineer-azure-strong-azure-gitops.html')
s=p.read_text();parts=re.split(r'(<[^>]+>)',s);skip=0;bold=0
terms=['Azure Container Registry','GitHub Actions','Azure DevOps','Azure Monitor','Argo CD','Kubernetes','Containerization','Terraform','GitOps','CI/CD','Docker','AKS','Helm','Security','Monitoring','Infrastructure as Code','IaC']
pat=re.compile(r'(?<![\w])('+'|'.join(re.escape(t) for t in sorted(terms,key=len,reverse=True))+r')(?![\w])',re.I)
for i,t in enumerate(parts):
 if t.startswith('<'):
  if re.match(r'<(style|script|title)\b',t):skip+=1
  if re.match(r'</(style|script|title)',t):skip-=1
  if re.match(r'<strong\b',t):bold+=1
  if t.startswith('</strong'):bold-=1
 elif not skip and not bold:parts[i]=pat.sub(r'<strong>\1</strong>',t)
p.write_text(''.join(parts))
