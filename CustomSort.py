# A Custom better tuned sorting algorith that takes advantage of the hash table to sort the elements on the go
import time,os

def newRange(array):
    numbers= {a:0 for a in array} #O(n) space
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers: #O(1)
                numbers[left_count]=1
                left_count -= 1
            left_count + 1

            while right_count in numbers:
                numbers[right_count] =1
                right_count += 1
            right_count -=1

            if(right-left) < (right_count - left_count):
                right= right_count
                left= left_count
        return  [left, right]