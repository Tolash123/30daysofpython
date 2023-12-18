# Number guessing
import random

attempt = 1
print('Totally Random One-Million-to-One')
number = random.randint(1,1000000)
while True:
  guess = int(input('What is your guess:'))
  if guess == number:
    print('You are a genius')
    break
  elif guess > number:
    print('Too high')
    attempt = attempt + 1
  elif guess < number:
    print('Too low')
    attempt = attempt + 1
    continue
  else:
    print('Finally')
    exit()

print('It took you', attempt, 'guesses to get the number correct.')
print('You are a genius!')