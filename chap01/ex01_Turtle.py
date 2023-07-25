print("*** Rabbit & Turtle ***")
d,vr,vt,vf = input('Enter Input : ').split()
t = float(vf)/(float(vt)-float(vr))*float(d)
sf = float(vf) * t

print('%.2f' %sf)