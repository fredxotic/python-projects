secret_number = 3
number_of_tries = 0
tries_limit = 3
while number_of_tries < tries_limit:
   guess = int(input( 'Guess: '))
   number_of_tries += 1
   if guess == secret_number:
      print('you won!')
      break
else:
   print('sorry you failed')
   
      