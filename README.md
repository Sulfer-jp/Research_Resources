# Research_Resources
These scripts are based on a blog [類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413).  
It was modified to work in the following environment.  
However, the environments in which GenSigFile.py and emds.py were confirmed to work correctly are different.  
It's because librosa and rpy2 were not installed correctly under the same environment in my environment.   
  
GenSigFile.py : Anaconda23.1.0, Python3.9.16  
emds.py : Python3.9.8  
  
The required libraries are the following.  
  
GenSigFile.py : librosa, numpy, pandas, scikit-learn  
emds.py : numpy, pandas, rpy2  
  
### Contents
#### System-File>sample>GenSigFile.py  
This script creates a signature file(please check said blog if you don't know what is "signature file")  
Put the wav file in the sample folder and write its filename in filename=''. 
You can rename the signature file by using the last code np.save().   
  
#### System-File>EMDsystem>emds.py  
This script loads two signature files and outputs an EMD.
Put the two signature files created by GenSigFile.py into the EMDsystem folder and rewrite the script part corresponding to the file names. 
  
  
  
  
  
# Research_Resources
このスクリプトは [類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413)というブログを参考にして作られています.  
以下の環境で動作するように修正しました.  
なお，librosaとrpy2が同じ環境下でインストールできなかったことから，GenSigFile.pyとemds.pyの動作確認が行われた環境が異なります．
  
GenSigFile.py : Anaconda23.1.0, Python3.9.16  
emds.py : Python3.9.8  
  
必要なライブラリは以下の通りです.    
  
GenSigFile.py : librosa, numpy, pandas, scikit-learn  
emds.py : numpy, pandas, rpy2  
  
### 内容
#### System-File>sample>GenSigFile.py  
このスクリプトでは，シグネチャファイルを作成します．（シグネチャファイルについては前述のブログを参照してください．)  
wavファイルをsampleフォルダに入れ，filename=''にそのwavファイル名を入力してください．  
末尾のnp.save()からシグネチャファイルのファイル名を変更できます．  
  
#### System-File>EMDsystem>emds.py  
このスクリプトは2つのシグネチャファイルをロードして，EMDを出力します．  
GenSigFile.pyで作成した2つのシグネチャファイルをEMDsystemフォルダに入れ，対応するスクリプトの箇所を書き換えてください．
