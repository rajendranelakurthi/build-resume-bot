import json,re
from pathlib import Path
from html import unescape
from docx import Document
from docx.shared import Pt,Mm,RGBColor
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
root=Path('tailored_resume/rajendra-prasad-n');stem='Rajendra-AWS-DevOps-SRE-Terraform'
for p in [Path('plugins/resume-creator-plugin/assets/variants/rajendra-aws-terraform-observability.json'),root/(stem+'.profile.json')]:
 d=json.loads(p.read_text());d['certifications']=[c for c in d['certifications'] if 'mulesoft' not in c.lower()];p.write_text(json.dumps(d,indent=2)+'\n')
d=json.loads((root/(stem+'.profile.json')).read_text());doc=Document();sec=doc.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297);sec.top_margin=sec.bottom_margin=Mm(12);sec.left_margin=sec.right_margin=Mm(14)
n=doc.styles['Normal'];n.font.name='Arial';n.font.size=Pt(9);n.paragraph_format.space_after=Pt(3)
for sn in ['Heading 1','Heading 2']:
 s=doc.styles[sn];s.font.name='Arial';s.font.size=Pt(11);s.font.bold=True;s.font.color.rgb=RGBColor(35,47,62);s.paragraph_format.space_before=Pt(9);s.paragraph_format.space_after=Pt(5)
def put(p,t,b=False,size=None,col=None):
 r=p.add_run(t);r.bold=b
 if size:r.font.size=Pt(size)
 if col:r.font.color.rgb=RGBColor.from_string(col)
 return r
def plain(s):return unescape(re.sub('<[^>]+>','',s))
def table(rows,cols):
 t=doc.add_table(rows=rows,cols=cols);t.autofit=False
 for row in t.rows:
  for c in row.cells:
   c.width=Mm(182/cols);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   pr=c._tc.get_or_add_tcPr();m=OxmlElement('w:tcMar')
   for side in ['top','left','bottom','right']:
    e=OxmlElement('w:'+side);e.set(qn('w:w'),'90');e.set(qn('w:type'),'dxa');m.append(e)
   pr.append(m)
 return t
t=table(1,2)
for c in t.rows[0].cells:
 e=OxmlElement('w:shd');e.set(qn('w:fill'),'232F3E');c._tc.get_or_add_tcPr().append(e)
p=t.cell(0,0).paragraphs[0];p.style='Title';put(p,d['full_name'].upper(),True,19,'FFFFFF');p=t.cell(0,0).add_paragraph();put(p,d['headline'],True,10,'FFB347')
p=t.cell(0,1).paragraphs[0];p.alignment=2
for i,line in enumerate(d['contact_lines_html']):
 if i:p=t.cell(0,1).add_paragraph();p.alignment=2
 p.paragraph_format.space_after=Pt(1);put(p,plain(line),size=8,col='FFFFFF')
p=doc.add_paragraph(plain(d['summary_html']));p.paragraph_format.space_before=Pt(8)
doc.add_heading('Certifications',1);t=table(1,4)
for c,s in zip(t.rows[0].cells,d['certifications']):
 p=c.paragraphs[0];p.alignment=1;put(p,s,True,8)
 e=OxmlElement('w:shd');e.set(qn('w:fill'),'F1F4F8');c._tc.get_or_add_tcPr().append(e)
doc.add_heading(d['achievements_title'],1)
def bullet(s):
 p=doc.add_paragraph(style='List Bullet');p.paragraph_format.left_indent=Mm(4);p.paragraph_format.first_line_indent=Mm(-3);p.paragraph_format.space_after=Pt(2);p.paragraph_format.keep_together=True;put(p,s)
for a in d['achievements']:bullet(a['tag']+': '+a['text'])
doc.add_heading('Core Technologies',1);t=table(4,2)
for i,s in enumerate(d['skill_sections']):
 c=t.cell(i//2,i%2);p=c.paragraphs[0];put(p,s['title'],True,9);p=c.add_paragraph();p.paragraph_format.space_after=Pt(2);put(p,s['content'],size=8.5)
doc.add_heading('Professional Experience',1)
for j in d['experience']:
 p=doc.add_paragraph();p.paragraph_format.space_before=Pt(7);p.paragraph_format.keep_with_next=True;p.paragraph_format.tab_stops.add_tab_stop(Mm(182),WD_TAB_ALIGNMENT.RIGHT)
 put(p,j['title']+' | '+j['company'],True,10);put(p,'\t'+j['date_range'],size=8)
 for key in ['client','project']:
  if j.get(key):
   p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;put(p,key.title()+': ',True,8);put(p,j[key],size=8)
 p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;put(p,'Skills Used: ',True,8);put(p,', '.join(s for s in j['skills_used'] if 'keyvault' not in re.sub(r'\W','',s.lower())),size=8)
 for b in j['impact']:bullet(b)
doc.add_heading('Education',1)
for e in d['education']:
 p=doc.add_paragraph();p.paragraph_format.keep_with_next=True;put(p,e['degree'],True);doc.add_paragraph(e['school'])
for s in doc.styles:
 for e in list(s.element.iter(qn('w:pBdr'))):e.getparent().remove(e)
doc.core_properties.title='Rajendra AWS DevOps SRE Resume';doc.core_properties.author=d['full_name'];doc.save(root/(stem+'.docx'))
assert 'mulesoft' not in '\n'.join(p.text for p in doc.paragraphs).lower()
print(root/(stem+'.docx'))
