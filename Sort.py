# 3 sorting implementations from labs
class Sort:
    @staticmethod
    def bubble_sort(arr):
        arr_size = len(arr)
        for i in range(arr_size):
            for j in range(i, arr_size):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    @staticmethod
    def partition(arr, low, high):
        """Return a pivot element for Quicksort."""
        key = arr[high]
        pivot = low
        for i in range(low, high):
            if arr[i] <= key:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                pivot += 1

        arr[pivot], arr[high] = arr[high], arr[pivot]
        return pivot

    @staticmethod
    def quicksort(arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        if high < low:
            return
        else:
            pivot = Sort.partition(arr, low, high)
            Sort.quicksort(arr, low, pivot - 1)
            Sort.quicksort(arr, pivot + 1, high)

    @staticmethod
    def quick_sort_simple(arr):
        if len(arr) > 1:
            less = []
            equal = []
            greater = []
            pivot = arr[0]

            for x in arr:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                else:
                    greater.append(x)

            return Sort.quick_sort_simple(less) + equal + Sort.quick_sort_simple(greater)

        else:
            return arr

    @staticmethod
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        if left:
            result.extend(left[left_idx:])
        if right:
            result.extend(right[right_idx:])
        return result

    @staticmethod
    def mergesort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = Sort.mergesort(left)
        right = Sort.mergesort(right)
        return list(Sort.merge(left, right))
