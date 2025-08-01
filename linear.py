#Linear time  complexity
import time
def linear_time(n):
# Take three inputs from the user
 print (f"\nO(n) for n={n}")
 for n in [n]:
    start = time.time()

    total = 0
    for i in range(n):
        total += i  # simple operation

    end = time.time()

    print(f"Time taken for n = {n} is {end - start:.6f} seconds")
    
    
linear_time(10000)
linear_time(20000)
linear_time(40000)