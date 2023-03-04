# United States

us_data = [369, 423, 416, 750, 928]
uk_data = []


def us_getData():
    us_rateOfChange = []
    # Find rate of change between each data point
    us_average = 0
    for i in range(len(us_data)):
        if not len(us_data) - 1 <= i:
            us_rateOfChange.append(us_data[i + 1] / us_data[i])

    # Find an average of the rate of change

    for x in us_rateOfChange:
        us_average += x

    us_average = us_average / (len(us_data) - 1)

    print("US Average rate of change (in 1000s): " + str(us_average))

    return us_average


# United Kingdom - DATA NEEDED

def uk_getData():
    uk_rateOfChange = []

    uk_average = 0
    for i in range(len(uk_data)):
        if not len(uk_data) - 1 <= i:
            uk_rateOfChange.append(uk_data[i + 1] / uk_data[i])

    for x in uk_rateOfChange:
        uk_average += x

    uk_average = uk_average / (len(uk_data) - 1)

    print("UK Average rate of change (in 1000s): " + str(uk_average))


us_avg = us_getData()
uk_avg = uk_getData()


def us_predict():
    print("we do something")
    data = [us_data[0]]

    for i in range(10):
        data.append(data[0] * (us_getData() ** i))

    return data
