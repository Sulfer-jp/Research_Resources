# Research_Resources
スクリプト作成にあたって，[類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413)というブログを参考にしました.  
I referenced the blog [類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413) to create this.
EMDを出力までのスクリプトを以下の環境で動かせるよう改変しています．librosa，rpy2のインストールがうまくいかなかったため，GenSigFile.pyとemds.pyの正常な実行を確認した環境が異なります．  
  
GenSigFile.py : Anaconda23.1.0, Python3.9.16  
emds.py : Python3.9.8  
  
必要なライブラリは以下の通りです.  
  
GenSigFile.py : librosa, numpy, pandas, scikit-learn  
emds.py : numpy, pandas, rpy2  
  
### 内容
System-File>sample>GenSigFile.py  
シグネチャファイルを作成するスクリプトです.  
sampleフォルダ内にwavファイルを入れ，そのファイル名をfilename=''に入力してください.  
末尾のコードnp.save()内の名前を変更して，シグネチャファイルの名前を変更できます．  
  
System-File>EMDsystem>emds.py  
2つのシグネチャファイルをロードし，EMDを出力するスクリプトです．
GenSigFile.pyで作成したシグネチャファイルを2つEMDsystemフォルダ内へ入れ，ファイル名に対応するスクリプト部を書き換えてください．  
