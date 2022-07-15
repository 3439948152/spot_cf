import pandas as pd
import numpy as np
def cos_sim(x, y):
    '''

    :param x:
    :param y:
    :return: 余弦相似度
    '''
    numerator = x * y.T
    denominator = np.sqrt(np.abs(x * x.T)) * np.sqrt(np.abs(y * y.T))
    return (numerator / denominator)[0, 0]
def similarity(data):
    m = np.shape(data)[0]
    w = np.mat(np.zeros((m, m)))
    for i in range(m):
        for j in range(i, m):
            if j != i:
                w[i, j] = cos_sim(data[i,], data[j,])
                w[j, i] = w[i, j]
            else:
                w[i, j] = 0
    return w

def item_based_recommend(data, w,spot):
    n, m = np.shape(data)  # m特征,n景点
    interaction = data[spot, :].T
    '''   not_inter=[]
    for i in range(n):
        if interaction[i,0]==0:
            not_inter.append(i)
    print(not_inter)'''
    predict = {}
    for x in range(n):
        item = np.copy(interaction)
        for j in range(m):
            if item[j] != 0:
                predict[x] = w[x, j] * item[j]
            else:
                predict[x] = predict[x]+w[x, j] * item[j]
    return sorted(predict.items(), key=lambda d: d[1], reverse=True)

def top_k(predict,k):
    top_recom = []
    len_result = len(predict)
    if k >= len_result:
        top_recom = predict
    else:
        for i in range(k):
            top_recom.append(predict[i])
    return top_recom
#去重
def de_duplication(list):
    dedup_list = []
    for word in list:
        if not word in dedup_list:
            dedup_list.append(word)

    return dedup_list
data = pd.read_csv(r'D:\study\spot-master\travel\data_2.csv',usecols=['sightlevel','distance','com_count'
                                  ,'com_score','heat_score'])
data_1=pd.read_csv(r'D:\study\spot-master\travel\data_2.csv',usecols=['poiid', 'name', 'feature','sightlevel','distance','com_count'
                                  ,'com_score','heat_score'])
data_2 = pd.read_csv(r'D:\study\spot-master\travel\data_2.csv',usecols=['poiid'])
col1 = data.values
col2=data_1.values
col3=data_2.values



def main(poiid: object):

    num = []

    for i in range(len(col2)):
        if poiid == col2[i][0]:
            num=col2[i][2]
            break
    recommd = []
    recom = {}
    data_all = {}
    n = 0
    for i in range(len(col2)):
        if col2[i][2] == num:
            recom[col2[i][0]] = n
            data_all[n] = col3[i]
            n = n + 1
            recommd.append(col1[i])
    data = np.mat(recommd)

    w = similarity(data)

    predict = item_based_recommend(data, w, 0)

    top_recom = top_k(predict, 10)
    poiid_list= {}
    for i in range(len(top_recom)):
        poiid_list[i]=int(data_all[top_recom[i][0]])
    return poiid_list

if __name__ == '__main__':
    df=main(poiid=76340)
    print(df)