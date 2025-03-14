def fib(n):
    fib_series =[0,1]
    while len(fib_series)<n:
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series
    
num_terms=10
print(f"fib series {num_terms}:")
print("fibbonacci{num_terms}:")