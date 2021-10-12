#phải lọc dữ liệu trước khi xuất file
#ví dụ:
# a 4			a 4
# a 5			a 5
# b 1			a 1
# b 6			b 1
# c 4			b 6
# d 4			c 4
# a 1 thành >>	d 4

import pandas as pd

df = pd.read_csv("test.csv")

lst = []
i = 0

while i < len(df['image']):
	f = open("test/"+df['image'][i]+".txt","w")
	lst.append("%s %s %s %s\n" % (str(df['xmin'][i]),str(df['ymin'][i]),
		str(df['xmax'][i]),str(df['ymax'][i])))
	try:
		while (df['image'][i+1]==df['image'][i]):
			lst.append("%s %s %s %s\n" % (str(df['xmin'][i+1]),str(df['ymin'][i+1]),
				str(df['xmax'][i+1]),str(df['ymax'][i+1])))
			i += 1
	except: pass
	print(lst)
	f.writelines(lst)
	f.close()
	lst.clear()
	i+=1
