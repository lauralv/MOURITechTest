# Function to move all zeros present in the list to the end
def reorder(A):

    # k stores index of next available position
    k = 0

    # do for each element
    for i in A:
        if i:
            A[k] = i
            k = k + 1

    # move all 0's to the end of the list (remaining indices)
    for i in range(k, len(A)):
        A[i] = 0


A1 = [6, 0, 8, 2, 3, 0, 4, 0, 1]
reorder(A1)
print(A1)
    
A2 = [0, 0, 8, 2, 3, 0, 1, 0, 0]
reorder(A2)
print(A2)