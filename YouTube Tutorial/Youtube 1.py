import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use ('ggplot')

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,12,31)

df = web.DataReader ("XQM", "yahoo", "start", "end")
