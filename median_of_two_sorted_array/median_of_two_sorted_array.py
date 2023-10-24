# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# [1,3] + [2,4,5] = [1,2,3,4,7] > median = 3
# [1,3] + [2,4] = [1, 2, 3, 4] > median = (2+3) / 2 = 2.5
# empty?

class MedianOfTwoSortedArray:

    def mergeSorted(self, array, array_to_merge):
        len_first = len(array)
        len_second = len(array_to_merge)

        if len_first < 1:
            if len_second < 1:
                print("Both arrays are empty")
                return 1
            else:
                return array_to_merge
        elif len_second < 1:
            return array
        else:
            array.extend(array_to_merge)
            array.sort()
            return array

    def medianOfTheArray(self, array):
        length = len(array)
        if length % 2 == 1:
            return array[int(round(length/2, 0)) - 1]
        else:
            return (array[int(length/2) - 1] + array[int(length/2)]) / 2


if __name__ == "__main__":
    array_one = [2, 3, 7, 9, 11]
    array_two = [1, 4, 8, 7, 6]
    median = MedianOfTwoSortedArray()
    mergedArray = median.mergeSorted(array_one, array_two)
    median_value = median.medianOfTheArray(mergedArray)
    print(median_value)
