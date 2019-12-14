def pat(s):
    for i in range(1,s+1):
        for j in range(1,s+1):
            if i==1 or j==1 or i==s or j==s:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    return