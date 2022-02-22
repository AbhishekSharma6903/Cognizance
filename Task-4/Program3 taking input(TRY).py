L1=[["ROLL NUMBER","NAME","MARKS"]]
cond='Y'
m=1
while (cond.lower()=='y'):
    print("Enter 1 to ADD INFORMATION\nEnter 2 to SHOW DATABASE\n")                    #CHOICE
    choice=int(input("Please Enter Your Choice:"))
    if choice==1:
        L1.append([int(input("Please Enter The Roll No.:")),input("Please Enter The Student Name:"),int(input("Please Enter The Marks:"))])
    elif choice==2:
        element = int(input("Enter The Roll No:"))
        for i in range(len(L1)):
            if element == L1[i][0]:
                for n in range(len(L1[i])):
                    print(L1[0][n], "\t \t", end="")
                print("\n")
                for n in range(len(L1[i])):
                    print(L1[i][n], "\t\t\t", end="")
                print("\n")
            else:
                m=1
        if m==0:
            print("No Data Found")
    else:
        print("Enter A Valid Option\n")
    cond=input("Do You Want To Continue ? (Y/N):\n")
input()   
