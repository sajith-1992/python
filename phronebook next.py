import csv 


with open ("phone.csv","a") as file:
    name = input ("name:")
    number = input ("number:")
    writer = csv.writer(file) #its a function passing into the  file 

    writer.writerow([name,number])
     