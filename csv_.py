import csv
#trash is a dummy csv that has the contacts we wish to save
with open("trash.csv") as f:
    csr_v = csv.reader(f)
    x = ''
    y = 0
    for row in csr_v:
        #x is the variable that actually concatenates and getst the value for the VCARD
        #modify first to fit your csv --look at vcf's and how they hold data
        x = "BEGIN:VCARD\n"+"VERSION:2.1\n"+"N:;{}".format(row[1])+";;;\n" +
        "FN:{}\n".format(row[1])+"EMAIL;HOME:noelannnane@gmail.com\n"+"END:VCARD\n"
        print(x)
        #this actually creates the vcf with the same name as cs_f.vcf
                            
        with open("cs_f.vcf", "a") as f2:
            f2.write(x)
        y+=1
        #this is to reference the number fo contacts
        #we want it extracted you can delete it to get contacts from the whole csv
        if y==5:
                break
print('csv file successfully created with name ccs_f.vcf')
        
