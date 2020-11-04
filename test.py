def convsec(getter):
    sec,min,hour=0,0,0
    if getter < 61:
        sec=getter
        if sec==60:
            min=1
            sec=0
    else:
        sec=getter%60
        temp=getter-sec
        tempmin=temp/60
        tempmin=int(tempmin)
        if tempmin < 61:
            min+=tempmin
            if tempmin==60:
                hour=1
                min=0
        else:
            min+=tempmin%60
            temp=tempmin/60
            hour+=int(temp)
    return hour,min,sec
inp = int(input(""))
print(convsec(inp))
