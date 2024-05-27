def m2_3(mass):
    res = []
    for i in mass:
        print(i)
        for j in i:
            res.append(j)
    return sorted(res)[-3:]
mass = [[1,2,3],[4,5,6]]
print(m2_3(mass))
            
        
    
