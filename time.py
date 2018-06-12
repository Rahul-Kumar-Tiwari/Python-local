import time
local=time.localtime(time.time())
print(local)
formattedtime=time.asctime(time.localtime(time.time()))
print(formattedtime)