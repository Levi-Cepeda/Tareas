producto1= "pay de limon" #str
producto2= "arroz con leche" #str
producto3= "pan dulce" #str
producto4= "cafe" #str
producto5= "gelanita" #str
producto6= "jugo" #str
producto7= "galletas" #str
producto8= "gansito" #str
producto9= "frappe" #str
producto10= "chicles" #str
costo1= 20
costo2= 20
costo3= 10
costo4= 25
costo5= 5
costo6= 11
costo7= 15
costo8= 18
costo9= 50
costo10= 2
iva1= 1
total1=costo1 + (costo1*iva1)
total2=costo2 + (costo2*iva1)
total3=costo3 + (costo3*iva1)
total4=costo4 + (costo4*iva1)
total5=costo5 + (costo5*iva1)
total6=costo6 + (costo6*iva1)
total7=costo7 + (costo7*iva1)
total8=costo8 + (costo8*iva1)
total9=costo9 + (costo9*iva1)
total10=costo10 + (costo10*iva1)
print("{:^20} {:^20} {:^20}".format("Producto","Costo nomarl", "Costo total"))
print("{:<25} {:<25} {:<25,.2f}".format(producto1,costo1,total1))
print("{:<25} {:<25} {:<25,.2f}".format(producto2,costo2,total2))
print("{:<25} {:<25} {:<25,.2f}".format(producto3,costo2,total3))
print("{:<25} {:<25} {:<25,.2f}".format(producto4,costo4,total4))
print("{:<25} {:<25} {:<25,.2f}".format(producto5,costo5,total5))
print("{:<25} {:<25} {:<25,.2f}".format(producto6,costo6,total6))
print("{:<25} {:<25} {:<25,.2f}".format(producto7,costo7,total7))
print("{:<25} {:<25} {:<25,.2f}".format(producto8,costo8,total8))
print("{:<25} {:<25} {:<25,.2f}".format(producto9,costo9,total9))
print("{:<25} {:<25} {:<25,.2f}".format(producto10,costo10,total10))
