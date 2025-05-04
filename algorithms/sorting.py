# (1). bubble sort 
# 1st method
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list
#2nd method using while loop
arr = [1,5,2,3,5,7,10]
flag = True
while flag:
    flag = False
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            flag = True
# (2). selection sort
 def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

#(3). insertion sort
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list

# (4). merge sort
def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)



original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)

# (5). quick sort
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list
    

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)

 
 


my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)

# quick sort (simple implementation)
def quick_sort(arr):
    # Base case: arrays with fewer than 2 elements are already sorted
    if len(arr) < 2:
        return arr
    
    # Choose the pivot (we use the first element here)
    pivot = arr[0]
    
    # Divide the array into two parts: less than pivot and greater than pivot
    less = [i for i in arr[1:] if i <= pivot]  # Elements less than or equal to pivot
    greater = [i for i in arr[1:] if i > pivot]  # Elements greater than pivot
    
    # Recursively sort the partitions and combine them with the pivot
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage
my_list = [4, 6, 1, 7, 3, 2, 5]
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)

# quick sort (linked list version)
def quickSort(head):
    if not head or not head.next:
        return head
        
    def concat(left,pivot,right):
        pivot.next = right
        if left:
            left_head = left
            while left.next:
                left = left.next
            left.next = pivot
            return left_head
        return pivot
        
    pivot = head
    left , right = Node(-1),Node(-1)
    leftTail,rightTail = left,right
    curr = pivot.next
    while curr:
        if curr.data < pivot.data:
            leftTail.next = curr
            leftTail = curr
        else:
            rightTail.next = curr
            rightTail = curr
        curr = curr.next
        
    leftTail.next = None
    rightTail.next = None
    
    sorted_left = quickSort(left.next)
    sorted_right = quickSort(right.next)
    
    return concat(sorted_left,pivot,sorted_right)
           
