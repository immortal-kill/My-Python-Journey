# H
num_a=int(input("Enter a number: "))
num_b=int(input("Enter a number: "))
#比较大小
'''if num_a>=num_b:
    print(num_a,"大于等于",num_b)
if num_a<num_b:
    print(num_a,"小于",num_b)'''

print("使用条件表达式进入比较")
print((str(num_a)+'大于等于'+str(num_b)) if num_a>=num_b else (str(num_a)+'小于'+str(num_b)))
#如果中间if为Ture则往左执行，若为False则往右执行