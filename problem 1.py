// The Problem
'''Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.'''
// for the matter of readability and cleaness, I haven't write all the problem here...you can find it on the official site of hackerrank.com

//here the code goes

  def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400==0:
                return not leap
            else:
                return leap
        else:
            return not leap  
    else:
        return leap
year = int(input())
print(is_leap(year))

