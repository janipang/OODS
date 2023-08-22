def power_cal(nb, power):
	if (power >= 0):
		expo_value = nb * power_cal(nb, power - 1)
		if (power == 0):
			expo_value = 1
	else:
		return (0)
	return (expo_value)

nb, power = map(int, input("Enter Input a b : ").split(" "))
print(power_cal(nb, power))