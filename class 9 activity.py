def print_next(n, count=10):
    if count == 0:
        return
    print(n)
    print_next(n + 1, count - 1)

# Example usage
start_number = int(input("Enter a starting number: "))
print_next(start_number)