print("Print Name N times using Recursion")

def print_name_n_time(name: str, n: int):
    if n == 0:
        return
    print(name, end=" ")
    print_name_n_time(name=name, n=n-1)

print_name_n_time(name="Vishal", n=5)
