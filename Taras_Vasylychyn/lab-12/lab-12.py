class SortingStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Використовуємо сортування бульбашкою")
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class InsertionSort(SortingStrategy):
    def sort(self, data):
        print("Використовуємо сортування вставкою")
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def perform_sort(self, data):
        return self.strategy.sort(data)

# Використання паттерна Стратегія
data = [5, 1, 3, 7, 2, 8, 4, 6]

bubble_sort_strategy = BubbleSort()
insertion_sort_strategy = InsertionSort()

sorter = Sorter(bubble_sort_strategy)
sorted_data = sorter.perform_sort(data)
print(f"Відсортовані дані: {sorted_data}")

sorter.set_strategy(insertion_sort_strategy)
sorted_data = sorter.perform_sort(data)
print(f"Відсортовані дані: {sorted_data}")
