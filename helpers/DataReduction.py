import math
import pandas as pd
import numpy as np

def FindPeaksAndValleys (data, data_column, time_column, quantity):
    convSize = math.floor(len(data.index) / quantity)
    if(convSize == 0):
        convSize = 1
    time = []
    temp = []
    for i in range(0, quantity):
        dsp = i * convSize
        tmp = data[dsp : dsp + convSize].copy()
        indx = np.where(tmp[data_column] == max(tmp[data_column]))[0]
        indxR = indx[math.floor(indx[0].size / 2)]
        dIndx = tmp.index[indxR]
        time.append(tmp[time_column][dIndx])
        temp.append(tmp[data_column][dIndx])
    pAv = pd.DataFrame({data_column : temp, time_column : time })
    return pAv