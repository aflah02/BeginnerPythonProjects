name_fast = input('Give a Name to Your Fast but Lazy Buddy')
name_slow = input('Give a Name to Your Slow but Steady Buddy')
town = input('Give a Name to Imaginary Town')
activity = input(f'Which activity did {name_fast.title()} start doing thinking he was in the lead?')
print(f'In the old town of {town}, the fast {name_fast.title()} challenged the slow {name_slow.title()} to a race.\n'
      f'Even though {name_fast.title()} was fast he was also very overconfident.\n'
      f'{name_slow.title()} on the other hand practiced a lot and was very persistent.\n'
      f'On the day of the race {name_slow.title()} took a very early lead but then \nbecame relaxed and decided to do some {activity}'
      f'Alas he got tired and fell asleep while {name_slow.title()} \nslowly overtake him by the time he woke up it was too late and \n{name_slow.title()} had defeated him.')
