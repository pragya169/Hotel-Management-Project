import pymysql
mydb= pymysql.connect(host="localhost",
                             user='root',
                             password='class12',
                             database='hotel')

print("                                  ****WELCOME TO HOTEL STARK AVENUE****                                                 ")


name=str(input("Enter your name:"))

address=input("Enter your address:")

checkindate=input("Enter your check in date:")

checkoutdate=input("Enter your checkout date:")

rno=101

print("Your room no.:",rno)

print("                                          ****ROOM RENT****                                              ")

print ("We have the following rooms for you:-")
print ("1.  SUPER DELUX---->Rs 6000 per Night")
print ("2.  DELUX---->Rs 5000 per Night")
print ("3.  AC---->Rs 3000 per Night")
print ("4.  Only cooler---->Rs 1500 per Night")
x=int(input("Enter Your Choice please:"))
n=int(input("For How Many Nights Did You Stay:"))
if(x==1):
    print ("you have opted room type A")
    r=6000*n
    
elif (x==2):
     print ("you have opted room type B")
     r=5000*n

elif (x==3):
    print ("you have opted room type C")
    r=4000*n

elif (x==4):
    print ("you have opted room type D")
    r=3000*n

else:
    print ("please choose a room")
print ("your room rent is =",r,)


print("                                       ****RESTAURANT MENU****                              ")
print("1.water----->Rs20")
print("2.tea----->Rs10")
print("3.breakfast combo--->Rs90")
print("4.lunch---->Rs110")
print("5.dinner--->Rs150")
print("6.Exit")
while(1):
    c=int(input("Enter your choice:"))
    


    
    if c==1:
        d=int(input("Enter the quantity:"))
        s=20*d
    elif (c==2):
        d=int(input("Enter the quantity:"))
        s=10*d

    elif (c==3):
        d=int(input("Enter the quantity:"))
        s=90*d

    elif (c==4):
        d=int(input("Enter the quantity:"))
        s=110*d

    elif (c==5):
        d=int(input("Enter the quantity:"))
        s=150*d
    elif c==6:
        break
    else:
        print("Invalid option")
print ("Total food Cost=Rs",s)



print ("                                       ****LAUNDRY MENU****                                                                ")
print ("1.Shorts----->Rs3")
print("2.Trousers----->Rs4")
print("3.Shirt--->Rs5")
print("4.Jeans---->Rs6")
print("5.Saree--->Rs8")
print("6.Exit")
t=0
while (1):
    e=int(input("Enter your choice:"))
    if (e==1):
        f=int(input("Enter the quantity:"))
        t=t+3*f

    elif (e==2):
        f=int(input("Enter the quantity:"))
        t=t+4*f

    elif (e==3):
        f=int(input("Enter the quantity:"))
        t=t+5*f

    elif (e==4):
        f=int(input("Enter the quantity:"))
        t=t+6*f

    elif (e==5):
        f=int(input("Enter the quantity:"))
        t=t+8*f
    elif (e==6):
        break
    else:
        print ("Invalid option")
print ("Total Laundary Cost=Rs",t)


print ("                                     ****GAME MENU****                                                                  ")

print ("1.Table tennis----->Rs60")
print("2.Bowling----->Rs80")
print("3.Snooker--->Rs70")
print("4.Video games---->Rs90")
print("5.Pool--->Rs50")
print("6.Exit")


p=0
while (1):
    g=int(input("Enter your choice:"))
    if (g==1):
        h=int(input("No. of hours:"))
        p=p+60*h

    elif (g==2):
        h=int(input("No. of hours:"))
        p=p+80*h

    elif (g==3):
        h=int(input("No. of hours:"))
        p=p+70*h

    elif (g==4):
        h=int(input("No. of hours:"))
        p=p+90*h

    elif (g==5):
        h=int(input("No. of hours:"))
        p=p+50*h
    elif (g==6):
        break;

    else:

        print ("Invalid option")


print ("Total Game Bill=Rs",p,)

 
print ("                                     ******HOTEL BILL******                                                              ")
print ("Customer details:")
print ("Customer name:",name)
print ("Customer address:",address)
print ("Check in date:",checkindate)
print ("Check out date",checkoutdate)
print ("Room no.",rno)
print ("Your Room rent is:",r)
print ("Your Food bill is:",s)
print ("Your laundary bill is:",t)
print ("Your Game bill is:",p)

rt=s+t+p+r

print ("Your grand total bill is:",rt)

rno+=1
print("                                        *****THANK YOU*****                                                                 ")






    




