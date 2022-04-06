import password
import time

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','E','F','H','I','J','K','L','M','N','R','S','T','U','V','W','X','Y','Z']
special = ['!','@','#','$','%','&','*']

generate_password = input('Do you want to create a password?(y/n) ')
if generate_password == 'y':
  print('Your password is:',password.random_password(upper,lower,special))
  time.sleep(1)
  multiple_passwords = input('Want create more passwords?(y/n) ')
  if multiple_passwords == 'y':
    for i in range(5):
      time.sleep(2)
      print('Your password is:',password.random_password(upper,lower,special))
  elif multiple_passwords == 'n' or multiple_passwords != 'y':
    print('Thank you for using this software')