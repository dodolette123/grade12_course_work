def sum_to_one(n):
  print("Recursing with input: {}".format(n))
  if n == 1:
    return n
  else:
    return sum_to_one(n-1) + n
# uncomment when you're ready to test
#print(sum_to_one(7))

#Factorial
def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)


#print(factorial(5))

#flatten
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i,list) == True:
      print("list found!")
      flat_list = flatten(i)
      for item in flat_list:
        result.append(item)
    else:
      result.append(i)
  return result

#print(flatten(planets))
#Termplate for flatten
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

#Fibonacci
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n-1) + fibonacci(n-2)


#0 1 1 2 3 5 8 13 21
print(fibonacci(4))