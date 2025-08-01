import time

def exponential_time(n):

    print(f"\nO(2^n) for n = {n}")
    def helper(k):
        if k == 0:
            return 
        
        helper(k-1)
        helper(k-1)
    start = time.time()

    helper(n)  # This takes exponential time

    end = time.time()
    print(f"Time taken for n = {n} is {end - start:.6f} seconds")

# Keep n small due to rapid growth of O(2^n)
exponential_time(20)
exponential_time(25)
exponential_time(30)
