def MergeSort(array):
    if len(array) > 1:
        midpoint = len(array)/2

        LeftHalf = array[:midpoint]
        RightHalf = array[midpoint:]

        MergeSort(LeftHalf)
        MergeSort(RightHalf)

        merge(LeftHalf, RightHalf, array)
    else:
        return array


def merge(left, right, listInt):
    leftpointer = 0
    rightpointer = 0
    listpointer = 0

    while leftpointer < len(left) and rightpointer < len(right):
        if left[leftpointer] > right[rightpointer]:
            listInt[listpointer] = left[leftpointer]
            leftpointer = leftpointer + 1
        else:
            listInt[listpointer] = right[rightpointer]
            rightpointer = rightpointer + 1

        listpointer = listpointer + 1

    while leftpointer < len(left):
        listInt[listpointer] = left[leftpointer]
        leftpointer = leftpointer + 1
        listpointer = listpointer + 1

    while rightpointer < len(right):
        listInt[listpointer] = right[rightpointer]
        rightpointer += 1
        listpointer += 1


print ("This is n ")
n = [43, 56, -333, 898, 6789, 8798, 100, 01]
MergeSort(n)
print (n)
