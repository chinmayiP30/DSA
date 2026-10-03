
def pal(s,l,r):
    if l>=r:
        return True 
    if s[l]!=s[r]:
        return False
    return pal(s,l+1,r-1)
s='ababac'
if pal(s,0,len(s)-1):
    print("pal")
else:
    print("not pal")