import pandas as pd
import numpy as np

series = pd.read_csv("titanic.csv") 

#First Question

seriesname = series.name
if seriesname = "Mrs":
	x = txt.replace("Mrs", "Ms")
	print(x)
	pass


#Second Question

import pandas as pd
import numpy as np

series = pd.read_csv("titanic.csv") 

df = pd.DataFrame(series , index=labels)
print("Middle name of passengers:")
print(df.iloc[4])




#Third Question

first_name = series.first
second_name = series.last

first_char = first_name[0]
second_char =  second_name[0]

print('Initials : ', first_char + '.',second_char)