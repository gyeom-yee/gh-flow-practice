# i -> print("Hello") -> esc -> :wq +enter

for i in range(1, 17):
    if i%(3*5)==0:
        print('fizzbuzz')
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print('buzz')
    else:
        print(i)
