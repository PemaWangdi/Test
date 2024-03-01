a=str(input('what is your name?'))
print('hello',a)
b=str(input('are you student?'))
c=int(input('how old are you?'))
if c>=12 or 18<=c<=25:
    print('you will get discount, congratulation')
elif c>=13 and b=='yes':
     print('you will get discount, congratulation')
else:
    print('sorry you will not get discount')