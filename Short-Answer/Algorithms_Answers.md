#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

                                Runtime Analysis
a)  a = 0                       
    while (a < n * n * n):      O(n^3)    
      a = a + n * n             O(n)
                       Answer   O(n^3)    



b)  sum = 0                      
    for i in range(n):          O(n)       
      j = 1                     
      while j < n:              O(n)
        j *= 2                  O(1)
        sum += 1                0(1)
                       Answer   0(2)

c)  def bunnyEars(bunnies):
      if bunnies == 0:                  O(n)
        return 0
      return 2 + bunnyEars(bunnies-1)   O(2+n+n)
                       Answer           O(n^2)
      

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken 
if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than 
floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs 
is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity 
of your solution.


building = number of story building
eggs = infinite
if egg_dropped =< f === breaks egg
else egg doesn't break
recursion


def maxFloor(building):
    for floor in building:
        find the middle floor
        drop egg
        if breaks go down by half num of floors
        else go up by half num of floors
        repeat until egg breaks on one floor and floor directly below it does not
        return that floor
        
        
Fast runtime = O(nLogn)
Overall time complexity of Merge sort is O(nLogn). It is more efficient as it is in worst case also the 
runtime is O(nlogn) The space complexity of Merge sort is O(n). This means that this algorithm takes a 
lot of space and may slower down operations for the last data sets