# QuickSort.py
# QuickSort is O(n**2), but usually acts more like 0(n log n)

# Step 1: Pick the final element of the array, name it 'Pivot'
# Create an index at the first element, calling it 'The Wall'
# Everything larger than the pivot stays on the right side of the wall
# Any element smaller than the pivot gets switched with the element directly to the right of the wall.
# The Wall moves one spot to the right to represent the value of the pivot

# When the Current Element reaches the pivot, the Pivot switches with the element directly to the right of the wall.

numbers = [0,1,4,2,3,6,8,5,7,9]

def InvQuickSort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list: # for every element in list...
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return InvQuickSort(less)+equal+InvQuickSort(greater)
    else:
        return list

def main():
    print(InvQuickSort(numbers))

if __name__ == "__main__":
    main()
