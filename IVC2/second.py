''' EvenList function'''
def Evenlist(s):
    p = []
    for i in range(len(s)):
        if int(s[i])%2==0:
            p.append(int(s[i]))
    return p
