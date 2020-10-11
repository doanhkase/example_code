# Viết chương trình tìm dãy Fibonacci:

# Cách 1: fibonacci không dùng đệ quy
f0 = 1
f1 = 1
fn = f1
print(f0)
while fn <1000:
    print(fn)
    f0, f1 = f1, fn
    fn = f0 + f1 # fibonacy
print('Thoát while')

##############################

# Cách 2: fibonacci dùng đệ quy
def fibonacy(n):
    while(n<1000):
        if n == 1:
            return(1)
        elif n == 2:
            return(1)
        else:
            f = fibonacy(n-2) + fibonacy(n -1)
            return f

# for i in range(1,10):
print(fibonacy(10))
