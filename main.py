t=str(input())
f=t[8]
h=t[0:2]
if f=='P' and h!="12":
    ans=12+int(h)
    hr=str(ans)
    res=t.replace(h,hr)
elif f=='A' and t[0:2]=='12':
    hr="00"
    res=t.replace(h,hr)
print(res)