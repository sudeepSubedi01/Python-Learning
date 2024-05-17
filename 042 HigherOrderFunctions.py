def loud(text):
  return text.upper()

def quiet(text):
  return text.lower()

def hello(func):  	  #higher order function
  text = func('Hello World')
  print(text)

hello(quiet)
hello(loud)
#---------------------------------------------------------
def divisor(x):
  def dividend(y):
    return y/x
  return dividend

divide = divisor(2)   #function to a variable
print(divide(10))