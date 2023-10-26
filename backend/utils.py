
import matplotlib.pyplot as plt


def get_frequencies(times: list) -> dict:
    frequencies = {}
    for time in times:
        if time not in frequencies:
            frequencies[time] = 1
        else:
            frequencies[time] += 1
    return frequencies


def make_frequency_growth_time_histogram(frequency_growth_time: dict) -> None:
    growth_times = list(frequency_growth_time.keys())
    frequencies = list(frequency_growth_time.values())

    plt.bar(growth_times, frequencies)
    plt.xlabel("Growth Time")
    plt.ylabel("Frequency")
    plt.title("Frequency Growth Time Histogram")
    plt.savefig('./static/histogram.png')

