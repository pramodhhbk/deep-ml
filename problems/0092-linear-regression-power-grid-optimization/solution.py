import math
import numpy as np
PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	X = np.arange(1,11,1)
	#print(X)
	
	for i in range(1,11):
		fi = 10 * np.sin((2*PI*i)/10)
		consumption_data[i-1] = consumption_data[i-1] - fi
	
	y = np.array(consumption_data)
	X = np.column_stack([np.ones(len(X)), X])

	theta = np.linalg.inv(X.T@ X) @ (X.T @ y)
	# theta (b,w)

	base_15 = theta[0] + theta[1] * 15

	fi_15 = 10 * np.sin((2*PI*15)/10)

	power_15 = base_15 + fi_15

	return int(np.round((math.ceil(power_15) * 1.05)))