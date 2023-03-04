# Finds the rate of change between each data point in _data array and returns
# an array of the calculated rates
def roc(_data: list) -> list:
    rates: list = []
    for i in range(len(_data)):
        if not len(_data) - 1 <= i:
            rates.append(_data[i + 1] / _data[i])
    return rates

# Calculates the average rate of change for a list of rates _data and returns it
def avg_roc(_data: list, _len: int) -> float:
    average = 0.0
    for value in _data:
        average += value
    average /= _len
    return average


def predict(_data: list, _average: float):
    # print("we do something")
    data = [_data[0]]

    for i in range(10):
        data.append(data[0] * (_average ** i))
    return data
