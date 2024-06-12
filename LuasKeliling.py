print("program menghitung Luas dan Keliling lingkaran")
r = float(input('masukan nilai jari jari :'))

phi = 3.14
diameter = 2*r

luas = phi*r*r
keliling = phi*diameter
print('luasnya =',str("%.2f"% luas))
print('kelilingnya =',str("%.2f"% keliling))

