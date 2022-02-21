print(" ROLL NUMBER : NAME OF STUDENT : MARKS ")
Record = [[1,"ABHISHEK",95],[2,"ASWIN",91],[3,"RISHABH",86],[4,"RAVI",80]]
for i in Record :
    print(" ",i[0]," "*(9-len(str(i[0]))),":",
          i[1]," "*(14-len(i[1])),":",
          i[2])
n=int(input("Enter the Roll number (1 to 4) of student whose data is required ="))
print(Record[n-1])
