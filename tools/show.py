import json,sys
u=json.load(open('src/uniq.json'))
a,n=int(sys.argv[1]),int(sys.argv[2])
for i in range(a,min(a+n,len(u))):
    print(f"{i}\t{u[i][1]}".replace('\n','\\n'))
