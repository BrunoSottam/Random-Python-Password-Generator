import random

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','E','F','H','I','J','K','L','M','N','R','S','T','U','V','W','X','Y','Z']
special = ['!','@','#','$','%','&','*']

def random_password(lower,upper,special):
  combination = lower + upper + special
  combination2 = random.sample(combination,12)
  final_password = "".join(combination2)
  return final_password



