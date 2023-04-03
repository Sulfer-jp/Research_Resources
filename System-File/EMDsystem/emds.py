import numpy as np
import rpy2.robjects as robjects
import numpy.linalg
import pandas as pd

def KLDiv(mu1, S1, mu2, S2):
    #正規分布間のカルバック・ライブラー情報量
    # 逆行列を計算
    try:
        invS1 = np.linalg.pinv(S1)
    except numpy.linalg.linalg.LinAlgError:
        raise;
    try:
        invS2 = np.linalg.pinv(S2)
    except numpy.linalg.linalg.LinAlgError:
        raise;

    # KL Divergenceを計算
    t1 = np.sum(np.diag(np.dot(invS2, S1)))
    t2 = (mu2 - mu1).transpose()
    t3 = mu2 - mu1
    return t1 + np.dot(np.dot(t2, invS2), t3)

def symKLDiv(mu1, S1, mu2, S2):
    #対称性のあるカルバック・ライブラー情報量
    return 0.5 * (KLDiv(mu1, S1, mu2, S2) + KLDiv(mu2, S2, mu1, S1))

# Rで輸送問題を解くライブラリ
# Rのデフォルトパッケージではないのでインストールが必要
# Rでinstall.packages("lpSolve")
robjects.r['library']('lpSolve')
transport = robjects.r['lp.transport']

def calcEMD(sigFile1, sigFile2):
    # シグネチャをロード
    sig1 = sigFile1
    sig2 = sigFile2

    # 距離行列を計算
    numFeatures = 16                 # クラスタの数
    dist = np.zeros(numFeatures * numFeatures)  # 距離行列（フラット形式）

    for i in range(numFeatures):
        mu1 = sig1[i,1:21].reshape(20,1)
        S1 = sig1[i, 21:421].reshape(20, 20)
        for j in range(numFeatures):
            mu2 = sig2[j, 1:21].reshape(20, 1)
            S2 = sig2[j, 21:421].reshape(20, 20)
            # 特徴量iと特徴量j間のKLダイバージェンスを計算
            dist[i * numFeatures + j] = symKLDiv(mu1, S1, mu2, S2)

    # シグネチャの重み（0列目）を取得
    w1 = sig1[:,0]
    w2 = sig2[:,0]

    # 重みと距離行列からEMDを計算
    # transport()の引数を用意
    costs = robjects.r['matrix'](robjects.FloatVector(dist),
                                 nrow=len(w1), ncol=len(w2),
                                 byrow=True)
    row_signs = ["<"] * len(w1)
    row_rhs = robjects.FloatVector(w1)
    col_signs = [">"] * len(w2)
    col_rhs = robjects.FloatVector(w2)

    t = transport(costs, "min", row_signs, row_rhs, col_signs, col_rhs)
    flow = t.rx2('solution')

    dist = dist.reshape(len(w1), len(w2))
    flow = np.array(flow)
    work = np.sum(flow * dist)
    emd = work / np.sum(flow)
    return emd

sigFile1 = np.load('sigfile1.npy')
sigFile2 = np.load('sigfile2.npy')

sigFile1_pd = pd.DataFrame(sigFile1)
sigFile1_npd = sigFile1_pd.fillna(0)
sigFile2_pd = pd.DataFrame(sigFile2)
sigFile2_npd = sigFile2_pd.fillna(0)

sigFile1 = sigFile1_npd.to_numpy()
sifFile2 = sigFile2_npd.to_numpy()

Result = calcEMD(sigFile1,sigFile2)

print(Result)