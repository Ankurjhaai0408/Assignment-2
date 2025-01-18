import time
import random
import tracemalloc


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def test_sorting_algorithm(algorithm, data):
    tracemalloc.start()  
    start_time = time.time()  
    sorted_data = algorithm(data)  
    end_time = time.time()  
    current, peak = tracemalloc.get_traced_memory()  
    tracemalloc.stop()  
    
    return {
        "execution_time": end_time - start_time,
        "memory_used": peak,
        "sorted_data": sorted_data[:10],  
    }


sizes = [1000, 5000, 10000]
results = {}

for size in sizes:
    
    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))
    random_data = random.sample(range(size), size)

    print(f"\nTesting with dataset size: {size}")

    
    print("\nQuick Sort:")
    results["quick_sorted"] = test_sorting_algorithm(quick_sort, sorted_data)
    results["quick_reverse_sorted"] = test_sorting_algorithm(quick_sort, reverse_sorted_data)
    results["quick_random"] = test_sorting_algorithm(quick_sort, random_data)

    
    print("\nMerge Sort:")
    results["merge_sorted"] = test_sorting_algorithm(merge_sort, sorted_data)
    results["merge_reverse_sorted"] = test_sorting_algorithm(merge_sort, reverse_sorted_data)
    results["merge_random"] = test_sorting_algorithm(merge_sort, random_data)

    
    for key, value in results.items():
        print(f"{key}: Execution Time: {value['execution_time']:.4f}s, Memory Used: {value['memory_used']} bytes")
