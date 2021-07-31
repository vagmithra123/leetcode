class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mylist = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0 :
                mylist.append("FizzBuzz")
            elif(num % 3 == 0):
                mylist.append("Fizz")
            elif(num % 5 == 0):
                mylist.append("Buzz")
            else: 
                mylist.append(str(num))
                
        return mylist
        