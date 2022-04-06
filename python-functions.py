# 1. sum_to(n)
# define function 
  # def sum_to(n)
    # return sum of the integers from 1 to n
# Examples:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55


# find the sum of integers from 1 to n using RANGE
# n = 9
# print(range(1, n))
# for num in range(1, n):
#   print(num)

def sum_to(n):
  total = 0
  for n in range(1, n + 1):
    total = total + n
  print(total)

sum_to(9)

# 2. largest
# def largest(list)
  #  list arg represents a list of numbers
  # read through the list
    # compare the numbers to each other to find the largest one
    # set largestNum variable to 0
      #  if the following number is larger than largestNum, largestNum is reassigned to that number
def largest(list):
  largestNum = 0
  for num in list:
    if num > largestNum:
      largestNum = num
  print(largestNum)
largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])

# 3. 
# def occurrences(str1, str2)
  # COUNT the number of time str2 appears in str1
  # Initialize count to start at 0
  # use a loop to iterate through each char in string
    # if char is equal to str2 
    # count = count + 1

def occurrences(str1, str2):
  # count = 0
  # for char in str1:
  #   if char == str2:
  #     count = count + 1
    
  # print(f'{str2} appears {count} times in {str1}')
  newString = str1.replace(str2, "")
  print(len(str1) - len(newString)) 

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')

# 4. product(args)
# def product(*args)
  # multiply each argument to each other
    # use for loop to access each argument 
    # initialize a product variable to 1  
      # 1 * # = #     
  # print the product

def product(*args):
  product = 1
  for arg in args:
    product = product * arg
  print(product)

product(-1, 4)
product(2, 5, 5)
product(4, 0.5, 5)










