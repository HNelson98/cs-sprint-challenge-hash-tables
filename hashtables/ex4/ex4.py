def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = list()
    length = len(a)

    for i in range(length):
        for j in range (i + 1, length):
            if(abs(a[i]) == abs(a[j])):
                result.append(abs(a[i]))

    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
