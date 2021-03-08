相信有不少初学者在学习python的时候，会经常遇到`moduleerror`的错误，现在跟着我一起学习一下相对导入和绝对导入吧。



python在导入包的时候，有相对导入和绝对导入的方式。

- 绝对导入：import p1.m1 或者 from p1 import m1 等。
- 相对导入：from . import m1 或者 from .. import m1 或者 from ..p1 import m1 或者 from .m1 import f1等。 



## 目录结构

代码地址：https://github.com/zhangboyi/python-learning

![image-20210308210105469](https://gitee.com/zbyzgx/uPicWH/raw/master/uPic/image-20210308210105469.png)

<img src="https://gitee.com/zbyzgx/uPicWH/raw/master/uPic/image-20210308211755084.png" alt="image-20210308211755084" style="zoom:50%;" />

## 相对导入

### 格式：

绝对导入：import p1.m1 或者 from p1 import m1 等。

### 注意点

- 若某模块使用了绝对导入，如何运该模块呢？

  - 命令行运行：需要在模块头部导入绝对路径，否则在运行该模块的时候会报错。
  - \_\_name\__  == "\__main__"运行

- 模块头部导入绝对路径是否是必须要添加的？

  - 若是一个web服务，一般情况下都不需要
  - 单独运行脚本的话，肯定是需要的

- 绝对路径怎么写？

  ```python
  #!/usr/bin/env python
  # -*- coding: utf-8 -*-
  # @Time:2021/3/8 8:56 下午
  # @Author:boyizhang
  import sys, os
  # 当前模块的位置：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
  print(__file__)
  # 返回当前模块的绝对路径：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
  print(os.path.abspath(__file__))
  #  当前模块的绝对路径目录：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage
  print(os.path.dirname(os.path.abspath(__file__)))
  # 返回当前模块目录的上层目录，每多一层，即再上一层目录：/Users/boyizhang/PycharmProjects/demo/test_import
  print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  
  # 当前模块的真实地址: (注意与relpath区分)/Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
  print(os.path.realpath(__file__))
  # 当前文件夹的路径: /Users/boyizhang/PycharmProjects/demo/test_import/mypackage
  print(os.path.dirname(os.path.realpath(__file__)))
  path = os.path.dirname(os.path.abspath(__file__))
  # 将目录或路径加入搜索路径
  sys.path.append(path)
  
  
  print(__name__)
  
  
  
  ```

  



## 绝对导入

### 格式：

相对导入：from . import m1 或者 from .. import m1 或者 from ..p1 import m1 或者 from .m1 import f1等。 

### 注意点

相对导入：该模块必须有`包结构`且只能导入它的顶层模块内部的模块（也不能导入和顶层模块同目录的模块）。

- 每多一个点，表示更上一层目录（没有更下一层目录的，同目录的不能导😌）
- 文件夹中必须有__init__.py文件。先执行package中的__init__.py，再执行package下的模块
- 若模块使用了相对导入，如何运行该模块呢？
  - 不能直接运行使用了相对导入的模块。因为一个模块被直接运行，则它就是顶层模块，不存在层次结构，所以找不到相对路径，直接报错`ImportError: attempted relative import with no known parent package`。
  - 命令行运行：可以使用`python -m package.module`

