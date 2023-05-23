import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def build_polygon(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    y = np.arange(1, n + 1) / n
    plt.plot(sorted_data, y, marker='o')
    plt.xlabel('Значення')
    plt.ylabel('Імовірність')
    plt.title('Полігон частот')
    plt.show()


def build_histogram(data):
    plt.hist(data, bins='auto')
    plt.xlabel('Інтервали')
    plt.ylabel('Частота')
    plt.title('Гістограма частот')
    plt.show()


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def calculate_mode(data):
    count = Counter(data)
    modes = count.most_common()
    max_count = modes[0][1]
    mode_values = [x[0] for x in modes if x[1] == max_count]
    return mode_values


def calculate_variance(data):
    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)


def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    return variance ** 0.5


def build_boxplot(data):
    plt.boxplot(data)
    plt.xlabel('Дані')
    plt.ylabel('Значення')
    plt.title('Діаграма розмаху')
    plt.show()


def build_pareto(data):
    sorted_data = sorted(data, reverse=True)
    cum_sum = np.cumsum(sorted_data)
    percent = cum_sum / sum(data) * 100
    plt.plot(range(1, len(sorted_data) + 1), percent, marker='o')
    plt.xlabel('Ранг')
    plt.ylabel('Відсоток накопиченого сумарного внеску')
    plt.title('Діаграма Парето')
    plt.show()


def build_pie_chart(data):
    count = Counter(data)
    labels, values = zip(*count.items())
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Кругова діаграма')
    plt.show()


def main():
    data = [69, 70, 68, 70, 70, 67, 70, 70, 68, 69, 70, 71, 70, 69, 67, 69, 69, 67, 67, 67, 67, 72, 74, 72, 69, 71, 70,
            71, 73, 66, 68, 69, 69, 72, 70, 72, 68, 71, 69, 70, 71, 69, 69, 69, 65, 68, 73, 69, 69, 67, 65, 67, 68, 66,
            67, 72, 69, 69, 68, 68, 68, 71, 67, 65, 65, 70, 68, 72, 69, 71, 67, 72, 70, 71, 68, 69, 70, 71, 71, 66, 68,
            66, 68, 72, 71, 70, 71, 65, 68, 69, 67, 70, 71, 67, 69, 73, 66, 71, 63, 69, 68, 68, 70, 73]

    build_polygon(data)
    build_histogram(data)

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std_dev = calculate_standard_deviation(data)

    print(f'Вибіркове середнє: {mean}')
    print(f'Медіана: {median}')
    print(f'Мода: {mode}')
    print(f'Вибіркова дисперсія: {variance}')
    print(f'Середньоквадратичне відхилення: {std_dev}')

    build_boxplot(data)
    build_pareto(data)
    build_pie_chart(data)


if __name__ == '__main__':
    main()
