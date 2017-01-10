import random

random_list = random.sample(xrange(0,10001),5)

def insert(arr):
    print "running insert program\n"
    print "random list is: \n",random_list,"\n"

    for i in range(1,len(arr)):

        print "outer for loop is running. i is now: ",i,"\n --------------"

        for j in range(i,0,-1):
            print "inner for loop is running. j is now: ",j,"\n"

            if arr[j] < arr[j-1]:

                arr[j-1],arr[j] = arr[j],arr[j-1]
                print arr

insert(random_list)
