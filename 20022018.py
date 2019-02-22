nterms=10
number=1
sum=0
# Excercise 1: Multiples of 3 and 5 below 10
nterms=int(input("Please Enter numeric number----->"))
print("Multiples of 3 and 5 below", nterms, ":")
while number<nterms:
    if number%3==0 or number%5==0:
        sum=sum+number
    number+=1

print(sum)

n1=1
n2=2
count=0
# Excercise 2: Even Fibonacci numbers
print("Fibonacci sequence upto", nterms, ":")
while count < nterms:
    print(n1, end=',')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

# Excercise 3: Largest prime factor


print("Largest prime factor", nterms, ":")

def max_factor(num):
    factor=2
    factors=[]
    while factor*factor <= num:
        while num % factor ==0:
            num //=factor
            factors.append(factor)
        factor +=1
    if (num!=1):
        factors.append(num)
    return max(factors)

print("max prime factor is ", max_factor(600851475143))


# Excercise 4: Largest palindrome product
def check_palindrome(number):
    ornum=number
    renum=0
    n=ornum
    while n !=0:
        reminder=n%10
        renum=renum*10+reminder
        n=n//10

    if ornum==renum:
        #print("{:d} is a palindrome".format(int(ornum)))
        return True


def findLargestPalindrome():
    palindrome = -1

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):

            # if product is palindrome and is greater than last recorded palindrome
            if check_palindrome(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome

print("Largest palindrome product of Three number is ", findLargestPalindrome())

# Excercise 5: Smallest multiple
def lcm(x,y):
    if (x>y):
        gretar=x
    else:
        gretar=y

    while(True):
        if ((gretar%x==0) and (gretar%y==0)):
            lcm=gretar
            break
        gretar=gretar+1

    return lcm

n = 1
for i in range(1, 20):
     n = lcm(n, i)
print("smallest multiple", n)

# Excercise 6: Sum square difference
def suare_diff(x,y):
    sum=0
    sumnumber=0
    diff=0
    for i in range(x,y+1):
        sum=sum+i*i
        sumnumber=sumnumber+ i
        diff=sumnumber**2 - sum
    return diff

print("Sum square difference of 10 natural numbers", suare_diff(1,100))
