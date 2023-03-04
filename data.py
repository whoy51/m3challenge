import m3

# US data
us_data = [369, 423, 416, 750, 928]
us_rateOfChange = []
print(m3.roc(us_data))
us_average = m3.avg_roc(m3.roc(us_data))
print(us_average)
us_prediction = m3.predict(us_data, us_average)

# UK data
uk_data = us_data
uk_rateOfChange = []
uk_average = m3.avg_roc(m3.roc(uk_data))
uk_prediction = m3.predict(uk_data, uk_average)
