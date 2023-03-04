import m3

# US data
us_data = [369, 423, 416, 750, 928]
us_rateOfChange = []
us_average = m3.avg_roc(m3.roc(us_data))
us_prediction = m3.predict(us_data, us_average, 14)

# TODO: Real data
uk_data = [400, 423, 416, 750, 1000]
uk_rateOfChange = []
uk_average = m3.avg_roc(m3.roc(uk_data))
uk_prediction = m3.predict(uk_data, uk_average, 15)
