import numpy as np
import pandas as pd
import librosa
from sklearn.cluster import KMeans

filename='./sample/Samp2.wav'
y,sr=librosa.load(filename)
mfcc=librosa.feature.mfcc(y=y,sr=sr,n_mfcc=20)

mfcc_array_orig = np.array(mfcc)

mfcc_array_T = mfcc_array_orig.transpose()
mfcc_array = mfcc_array_T


pred = KMeans(n_clusters=16).fit_predict(mfcc_array)
kmeans_array = np.array(pred)


df = pd.DataFrame(mfcc_array)
df2 = pd.DataFrame(kmeans_array)
df.columns = range(0,20)
df['clu_num'] = df2

Fin_List = []
Fin_df = pd.DataFrame(Fin_List)

average = df.groupby('clu_num').mean()
average_np =np.array(average)

len_list = []
for i in range(16):
    group = df.groupby('clu_num').get_group(i)
    num = len(group)
    len_list.append(num)

Tlen_list = np.array(len_list)
Tr_len_list = Tlen_list.T
DF_len_list = pd.DataFrame(Tr_len_list)

Fin_df['weight'] = DF_len_list

for i in range(20):
    Fin_df[str(i)] = average_np[:,i]

print(Fin_df)

Cov_list = []

for i in range(16):
    get_group = df.groupby('clu_num').get_group(i)
    drop_num = get_group.drop('clu_num',axis=1)
    np_group = drop_num.to_numpy()
    Tnp_group = np_group.T
    Cov_group0 = np.cov(Tnp_group)
    Cov_group = np.ravel(Cov_group0)
    Cov_list.append(Cov_group)

Cov_np = np.array(Cov_list)
Cov_rnp = Cov_np.reshape(16,400)

for i in range(400):
    Fin_df['cov' + str(i)] = Cov_rnp[:,i]

SigFile = np.array(Fin_df)
np.save('./sample/sigfile2.npy',SigFile)