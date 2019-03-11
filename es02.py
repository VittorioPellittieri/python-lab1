stringa=input("Immetti una stringa: ")
i = 0
var=""
if(len(stringa)>2):
    for car in stringa:
        print(car)
        if(i==0 or i==1 or i==(len(stringa)-2) or i==(len(stringa)-1)):
            var=var+car
            print("entrato")
        i=i+1


print(var)