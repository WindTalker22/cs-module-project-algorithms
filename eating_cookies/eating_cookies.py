'''
Input: an integer
Returns: an integer
'''

# Finished


def eating_cookies(n):
    # Your code here
    print(f"Finding ways to eat {n}")
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3
    eating_cookies(num_cookies)
    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
