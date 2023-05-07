import csv 


file = open ("phone.csv","a")
name = input ("name:")
number = input ("number:")
writer = csv.writer(file) #its a function passing into the  file 

writer.writerow([name,number])
file.close()    