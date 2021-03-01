def palindrome(num):
    if num==rev(num):
        print(num)
    else:
        palindrome(num+1)
def rev(n):
    r=0
    while n>0:
        r*=10
        r+=n%10
        n//=10
    return r
num=int(input("Enter any number -> "))
num=num+1
palindrome(num)   
