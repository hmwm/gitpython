temperature_dic = {"1101": 36.0, "1102": 37.0, "1103": 38.6, "1104": 36.2}
for staff_id, temperature in temperature_dic.items():
    if temperature >= 38.0:
        print(staff_id,temperature)
        print("GG了")