什么是模块？
    把很多函数分组，分别放到不同的文件里。这样，每个文件包含的代码就相对较少。 

模块的好处？
    避免函数名，变量名的冲突。
    a.py
      def sayhi():
          hahasa
    b.py
      import a
      def sayhi():
          xxxx
     a模块的sayhi（）和 b 模块的 sayhi（）不冲突
 

模块的分类：
    标准模块（内置模块，标准库） 近300个
    第三方模块 18万个左右。 pip install
    自定义模块，自己写的。   
    
    
模块的导入&调用
    import os 
    import sys
    或者 import os, sys 
    
    from os improt rename, path, replace  #打开os模块, 调用rename, path, replace
    rename()
