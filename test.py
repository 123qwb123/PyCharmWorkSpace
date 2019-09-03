from pip._vendor.distlib.compat import raw_input

x=int(raw_input("请输入一个人数:\n"))
a=x/10000
b=x%10000//1000
c=x%1000//100
d=x%100/10
e=x%10
print(a,b,c,d,e)
