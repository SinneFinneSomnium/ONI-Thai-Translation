import json,sys,re,glob
u=json.load(open('src/uniq.json'))
def toks(s):
    return sorted(re.findall(r'\{[^}]*\}|<[^>]*>|%[sd]|\\n',s.replace('\n','\\n')))
tr={}
bad=0
for f in sorted(glob.glob('tr/*.tsv')):
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        i,t=ln.split('\t',1); i=int(i)
        src=u[i][1]
        if toks(src)!=toks(t):
            bad+=1; print(f"{f} {i}: tags differ\n  EN {src}\n  TH {t}")
        tr[i]=t
print(f"translated {len(tr)}/{len(u)} bad={bad}")
