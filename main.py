arr = [ 0 , 1 , 2 , 3 , 4]

arr[0] = int(input('insert first number '))
arr[1] = int(input('insert second number '))
arr[2] = int(input('insert third number '))
arr[3] = int(input('insert fourth number '))
arr[4] = int(input('insert fifth number '))

print('for getting the max value , please enter (max)\nfor getting the min value , please enter (min) ')

sss = input('enter your word')
while sss.isalpha() == True :
    if sss == 'max':
        print('the max value is',max(arr))
        break
    elif sss == 'min' :
        print('the min value is',min(arr))
        break
    else :
        print('sorry , you should write either max or min below please')
        sss =input('enter max or min')






