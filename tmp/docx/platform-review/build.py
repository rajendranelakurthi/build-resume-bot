import json,re
from pathlib import Path
from html import unescape
from docx import Document
from docx.shared import Pt,Mm,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
root=Path('tailored_resume/rajendra-prasad-n')
stem='rajendra-prasad-n-platform-engineer-aggressive-devops-platform-engineer-azure-infrastructure-and-healthcare-technology'
d=json.loads((root/(stem+'.profile.json')).read_text())
doc=Document();sec=doc.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297)
sec.top_margin=sec.bottom_margin=Mm(10);sec.left_margin=sec.right_margin=Mm(12)
style=doc.styles['Normal'];style.font.name='Arial';style.font.size=Pt(9)
style.paragraph_format.space_after=Pt(2);style.paragraph_format.line_spacing=1.0
for name in ['Heading 1','Heading 2']:
 s=doc.styles[name];s.font.name='Arial';s.font.color.rgb=RGBColor.from_string('174A8B');s.font.size=Pt(11);s.font.bold=True;s.paragraph_format.space_before=Pt(8);s.paragraph_format.space_after=Pt(4)
def shade(cell,color):
 e=OxmlElement('w:shd');e.set(qn('w:fill'),color);cell._tc.get_or_add_tcPr().append(e)
def text(p,s,bold=False,size=None,color=None):
 r=p.add_run(s);r.bold=bold
 if size:r.font.size=Pt(size)
 if color:r.font.color.rgb=RGBColor.from_string(color)
 return r
def plain(s):return unescape(re.sub('<[^>]+>','',s))
def bullet(s):
 p=doc.add_paragraph(style='List Bullet');p.paragraph_format.space_after=Pt(1);p.paragraph_format.line_spacing=1.0;text(p,s)
header=doc.add_table(rows=1,cols=2);header.columns[0].width=Mm(118);header.columns[1].width=Mm(68)
for c in header.rows[0].cells:shade(c,'174A8B')
p=header.cell(0,0).paragraphs[0];p.style='Title';text(p,d['full_name'].upper(),True,21,'FFFFFF')
p=header.cell(0,0).add_paragraph();text(p,d['headline'],True,9,'FFD400')
p=header.cell(0,1).paragraphs[0];p.alignment=2
for i,s in enumerate(d['contact_lines_html']):
 if i:p=header.cell(0,1).add_paragraph();p.alignment=2
 text(p,plain(s),False,8,'FFFFFF')
p=doc.add_paragraph();p.paragraph_format.space_before=Pt(7);text(p,plain(d['summary_html']))
doc.add_heading('Certifications',1)
certs=[s for s in d['certifications'] if 'mulesoft' not in s.lower()]
t=doc.add_table(rows=1,cols=len(certs))
for c,s in zip(t.rows[0].cells,certs):
 shade(c,'F1F5FB');p=c.paragraphs[0];p.alignment=1;text(p,s,True,8,'174A8B')
doc.add_heading(d['achievements_title'],1)
for a in d['achievements']:bullet(a['tag']+': '+a['text'])
doc.add_heading('Core Technologies',1)
skills=d['skill_sections'];t=doc.add_table(rows=(len(skills)+1)//2,cols=2)
for i,s in enumerate(skills):
 c=t.cell(i//2,i%2);shade(c,'F1F5FB');p=c.paragraphs[0];text(p,s['title'],True,8.5,'174A8B');p=c.add_paragraph();text(p,s['content'],False,8)
doc.add_heading('Professional Experience',1)
for j in d['experience']:
 p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;p.paragraph_format.space_before=Pt(6)
 text(p,j['title']+' | '+j['company'],True,10,'174A8B');text(p,'    '+j['date_range'],False,8)
 if j.get('client'):
  p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;text(p,'Client: ',True,8);text(p,j['client'],False,8)
 p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;text(p,'Skills Used: ',True,8);text(p,', '.join(s for s in j['skills_used'] if 'keyvault' not in re.sub(r'\W','',s.lower())),False,8)
 for b in j['impact']:bullet(b if isinstance(b,str) else b['tag']+': '+b['text'])
doc.add_heading('Education',1)
for e in d['education']:
 p=doc.add_paragraph();text(p,e['degree'],True);p=doc.add_paragraph(e['school'])
doc.core_properties.title='Rajendra P N Platform Engineer Resume';doc.core_properties.author=d['full_name']
doc.save(root/(stem+'.docx'))
print(root/(stem+'.docx'))
