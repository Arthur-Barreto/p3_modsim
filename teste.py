from math import*

v0 = 3.49035865684291 # em m/s²
teta = 56.65929265099678 # teta inicial em graus
# convertendo o angulo em radianos
teta = radians(teta)

# agora as componentes das velocidades
v0x = v0*cos(teta)
print(v0x)
v0y = v0*sin(teta)
print(v0y)
