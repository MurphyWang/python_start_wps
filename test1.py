beforesort={'wps':183,'lyc':166,'zj':160,'wr':168}
beforesortName=['wps', 'lyc', 'zj', 'wr']
beforesortHeight=[183, 166, 160, 168]
aftersort = {}
n = len(beforesort) - 1

while n >= 1:
    i = 1
    while i <= n:
        if beforesortHeight[-i]<beforesortHeight[-i-1]:
            beforesortHeight.insert(-i-1,beforesortHeight[-i])
            beforesortHeight.pop(-i)
        i = i + 1
    aftersort[beforesortName[3-n]]=beforesortHeight[3-n]
    n = n - 1

print(beforesortName)
print(beforesortHeight)
aftersort[beforesortName[3]] = beforesortHeight[3]
print("---------------------")
print(aftersort)
