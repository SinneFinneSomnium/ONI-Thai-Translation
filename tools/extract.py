import polib,json,sys,re
p=polib.pofile(sys.argv[1])
order=['STRINGS.UI.FRONTEND','STRINGS.ELEMENTS','STRINGS.BUILDINGS.PREFABS','STRINGS.UI.TOOLS','STRINGS.UI.OVERLAYS','STRINGS.UI','STRINGS.DUPLICANTS','STRINGS.ITEMS','STRINGS.CREATURES','STRINGS.EQUIPMENT','STRINGS.RESEARCH','STRINGS.BUILDING','STRINGS.MISC','STRINGS.INPUT_BINDINGS','STRINGS.']
def rank(ctx):
    for i,o in enumerate(order):
        if ctx.startswith(o): return i
    return len(order)
import os
uniq=[tuple(x) for x in json.load(open(sys.argv[2]))] if os.path.exists(sys.argv[2]) else []
seen={m:i for i,(c,m) in enumerate(uniq)}
old=len(uniq)
for e in sorted(p,key=lambda e:(rank(e.msgctxt or ''))):
    if not e.msgid.strip() or e.msgid in seen: continue
    if not re.search(r'[A-Za-z]{2}',re.sub(r'<[^>]*>|\{[^}]*\}','',e.msgid)): continue
    seen[e.msgid]=len(uniq); uniq.append((e.msgctxt,e.msgid))
json.dump(uniq,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False)
print('total',len(uniq),'new',len(uniq)-old)
