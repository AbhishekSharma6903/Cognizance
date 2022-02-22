n=int(input("Enter the number of rows for pattern ="))
for i in range(1,n+1):                         #i starts from 1 to n+1 
    print(" "*(n-i)+"* "*i)                    #for example we can take n=5 , the range would be 1 to 6 (loop will be printed 5 times)
                                        #for loop 1 -> space will be printed (5-1) 4 times and '* ' only 1 time >>         *
                                        #for loop 2 -> space will be printed (5-2) 3 times and '* ' only 2 time >>        * *
                                        #for loop 3 -> space will be printed (5-3) 2 times and '* ' only 3 time >>       * * *  
                                        #for loop 4 -> space will be printed (5-4) 1 times and '* ' only 4 time >>      * * * *
                                        #for loop 5 -> space will be printed (5-5) 0 times and '* ' only 5 time >>     * * * * *
input()