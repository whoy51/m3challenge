import m3

# US data
us_data = [369, 423, 416, 750, 928]
us_rateOfChange = []
us_average = m3.average_roc(m3.roc(us_data), len(us_rateOfChange) - 1)
us_prediction = m3.predict(us_data, us_average)

# UK data
uk_data = us_data
uk_rateOfChange = []
uk_average = m3.average_roc(m3.roc(uk_data), len(uk_rateOfChange) - 1)
uk_prediction = m3.predict(uk_data, uk_average)
