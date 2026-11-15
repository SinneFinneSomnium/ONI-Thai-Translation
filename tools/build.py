import json,glob,re,polib,sys,os
from pythainlp.tokenize import word_tokenize
ZW='\u200b'
u=json.load(open('src/uniq.json'))
GL=json.load(open('tools/gloss.json',encoding='utf-8'))
VIS=re.compile(r'<[^>]*>|\{[^}]*\}')
def vislen(s): return len(VIS.sub('',s))
def gloss(src,text):
    # Thai meaning in ( ) after a transliterated term: once per string, long texts only
    if vislen(src)<40: return text
    for term,th in GL.items():
        if th in text: continue
        pos=None; depth=0
        for m in re.finditer(r'<[^>]*>|\{[^}]*\}|[^<{]+',text):
            seg=m.group(0)
            if seg[0]=='<':
                if seg.startswith('</'): depth=max(0,depth-1)
                elif not seg.endswith('/>'): depth+=1
                continue
            if seg[0]=='{': continue
            k=seg.find(term)
            if k<0: continue
            if depth==0:
                pos=m.start()+k+len(term)
            else:
                c=text.find('</',m.end()); pos=text.find('>',c)+1 if c>=0 else len(text)
            break
        if pos is not None and not text[pos:].startswith(' ('):
            tail=' ' if re.match(r'[\u0e00-\u0e7f<]',text[pos:pos+1]) else ''
            text=text[:pos]+' ('+th+')'+tail+text[pos:]
    return text
tr={}
for f in sorted(glob.glob('tr/*.tsv')):
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if '\t' not in ln: continue
        i,t=ln.split('\t',1); tr[u[int(i)][1]]=gloss(u[int(i)][1],t.replace('\\n','\n'))
THAI=re.compile(r'[\u0e00-\u0e7f]+')
def zw(text):
    # insert zero-width spaces between Thai words, only outside tags/placeholders
    parts=re.split(r'(<[^>]*>|\{[^}]*\})',text)
    out=[]
    for p in parts:
        if p.startswith('<') or p.startswith('{'): out.append(p); continue
        out.append(THAI.sub(lambda m: ZW.join(word_tokenize(m.group(0),engine='newmm',keep_whitespace=True)),p))
    return ''.join(out)
pot=polib.pofile('src/strings_template.pot')
po=polib.POFile(wrapwidth=0)
po.metadata={'Project-Id-Version':'ONI Thai Translation','Language':'th','Font':'NotoSansThai-Regular','MIME-Version':'1.0','Content-Type':'text/plain; charset=UTF-8','Content-Transfer-Encoding':'8bit'}
n=0
for e in pot:
    t=tr.get(e.msgid)
    if t is None: continue
    po.append(polib.POEntry(msgctxt=e.msgctxt,msgid=e.msgid,msgstr=zw(t),comment=e.comment)); n+=1
os.makedirs('mod/ThaiTranslation',exist_ok=True)
po.save('mod/ThaiTranslation/strings.po')
print('entries',n,'of',len(pot))
