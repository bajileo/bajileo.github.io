import time
time_object = time.localtime()
doy = time.strftime("%j", time_object)
woy = time.strftime("%U", time_object)
print(f"Day of Year is : {doy} \nWeek of Year is : {woy}")
