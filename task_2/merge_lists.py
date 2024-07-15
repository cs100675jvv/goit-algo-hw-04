import heapq

def merge_k_lists(lists):
    # Мін-купа для підтримки найменшого елементу на верхівці
    min_heap = []
    
    # Додаємо перші елементи всіх списків до мін-купи
    for i, lst in enumerate(lists):
        if lst:  # Перевірка, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list = []
    
    # Виконуємо злиття
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо в поточному списку є ще елементи, додаємо наступний до мін-купи
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
