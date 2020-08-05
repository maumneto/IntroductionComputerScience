# import functions from time module
from time import asctime, localtime
# time receive localtime struct
time = localtime()
# prints time with asc format
print(asctime(time))