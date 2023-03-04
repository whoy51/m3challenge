import m3

# US data
us_data = [369, 423, 416, 750, 928]
us_rateOfChange = []
us_average = m3.avg_roc(m3.roc(us_data))
us_prediction = m3.predict(us_data, us_average, 0, 14)
us_scaled = m3.scale(us_prediction, 328200000)


# UK data
uk_data = [2.94, 5.19, 8.37, 12.66, 17.64, 21.48, 25.62, 27.21, 34.17, 40.92, 49.11, 62.22, 83.01, 101.91]
uk_rateOfChange = []
uk_average = m3.avg_roc(m3.roc(uk_data))
uk_prediction = m3.predict(uk_data, uk_average, 12, 15)
uk_scaled = m3.scale(uk_prediction, 67886011)
