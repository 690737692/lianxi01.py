#def cc(s):
#   for i in s:
#        if i==i.lower():
##            lst = i.upper()
#        else:
#            i = i.lower()
#    print(lst)
#    return "".join(lst)


#cc("KaJaPf")

def c(s):
    lst = [i.upper() if i == i.lower() else i.lower() for i in s]
    return ''.join(lst)
s = "AaBbCc"
ss = c(s)
print(ss)