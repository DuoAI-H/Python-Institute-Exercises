millam = 1609.344 #En metros
galonL = 3.785411784 #En litros

def l100kmtompg(liters):
    sol = 1/((liters*millam)/(galonL*1000))*100
    return(sol)

def mpgtol100km(miles):
    sol = 1/((miles*millam)/(galonL*1000))*100
    return(sol)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))