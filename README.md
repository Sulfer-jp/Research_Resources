# Research_Resources
スクリプト作成にあたって，[類似楽曲検索システムを作ろう](https://aidiary.hatenablog.com/entry/20121014/1350211413)というブログを参考にしました.  
EMDを出力までのスクリプトを以下の環境で動かせるよう改変しています．librosa，rpy2のインストールがうまくいかなかったため，GenSigFile.pyとEMDs.pyの正常な実行を確認した環境が異なります．  
  
GenSigFile.py : Anaconda23.1.0, Python3.9.16  
EMDs.py : Python3.9.8  
  
必要なライブラリは以下の通りです.  
  
GenSigFile.py : librosa, numpy, pandas, scikit-learn  
EMDs.py : numpy, pandas, rpy2  
  
## 内容
System-File>sample>GenSigFile.py  

シグネチャファイルを出力するスクリプト．  
wavファイルでの正常な出力を確認している．
