# Research_Resources
This scripts are based on a blog [類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413).  
It was modified to work in the following environment.  
However, the environments in which GenSigFile.py and emds.py were confirmed to work correctly are different.  
It's because librosa and rpy2 were not installed correctly under the same environment in my environment.   
GenSigFile.py : Anaconda23.1.0, Python3.9.16  
emds.py : Python3.9.8  
  
The required libraries are the following.  
  
GenSigFile.py : librosa, numpy, pandas, scikit-learn  
emds.py : numpy, pandas, rpy2  
  
### Contents
System-File>sample>GenSigFile.py  
This scripts create a signature file(please check said blog if you don't know what is "signature file")
sampleフォルダ内にwavファイルを入れ，そのファイル名をfilename=''に入力してください.  
末尾のコードnp.save()内の名前を変更して，シグネチャファイルの名前を変更できます．  
  
System-File>EMDsystem>emds.py  
2つのシグネチャファイルをロードし，EMDを出力するスクリプトです．
GenSigFile.pyで作成したシグネチャファイルを2つEMDsystemフォルダ内へ入れ，ファイル名に対応するスクリプト部を書き換えてください．  
