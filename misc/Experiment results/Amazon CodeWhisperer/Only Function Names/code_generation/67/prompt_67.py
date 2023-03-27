
def fruit_distribution(s,n):
    s.sort()
    i=0
    j=n-1
    while i<j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    return s