'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):

    # The length of the input array
    length = len(arr)

    # The answer array to be returned
    answer = [0]*length

    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):

        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with arr[i - 1] would give the product of all
        # elements to the left of index 'i'
        answer[i] = arr[i - 1] * answer[i - 1]

    # Right contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the Right would be 1
    Right = 1
    for i in reversed(range(length)):

        # For the index 'i', Right would contain the
        # product of all elements to the right. We update Right accordingly
        answer[i] = answer[i] * Right
        Right *= arr[i]

    return answer


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # expected = [13547520, 10536960, 94832640, 11854080, 15805440,
    #             13547520, 11854080, 11854080, 13547520, 9483264]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
product_of_all_other_numbers(arr)
print(
    f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
