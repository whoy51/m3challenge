# Finds the rate of change between each data point in _data array and returns
# an array of the calculated rates
def roc(_data: list) -> list:
    rates: list = []
    for i in range(len(_data)):
        if not len(_data) - 1 <= i:
            rates.append(_data[i + 1] / _data[i])
    return rates


# Calculates the average rate of change for a list of rates _data and returns it
def avg_roc(_data: list) -> float:
    average = 0.0
    for value in _data:
        average += value
    average /= len(_data) - 1
    return average


def predict(_data: list, _average: float, _start: int, _years: int) -> list:
    data = [_data[_start] *1000]

    for i in range(_years):
        data.append((data[0] * (_average ** i + 1 + _start))*1000)
    return data


# change populations to be percentages based of population of country
def scale(_data: list, _population: int) -> list:
    data = []
    for i in range(len(_data)):
        data.append(((_data[i] * 1000) / _population) * 100)
    return data
