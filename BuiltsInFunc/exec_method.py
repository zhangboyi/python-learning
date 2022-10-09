
# -*- coding: utf-8 -*-
# @Time:2022/7/17 17:51
# @Author:boyizhang

run_code = """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/17 17:46
# @Author:boyizhang
class FooParent(object):
  def __init__(self):
    self.parent = "I\'m the parent."
    print('Parent')

  def bar(self, message):
    print("%s from Parent" % message)

class FooParent2(object):
  def __init__(self):
    self.parent = "I'm the parent."
    print('Parent2')

  def bar(self, message):
    print("%s from Parent2" % message)

class FooChild(FooParent2,FooParent):

  def __init__(self):
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    super(FooChild, self).__init__()
    print('Child')

  def bar(self, message):
    super(FooChild, self).bar(message)
    print('Child bar fuction')
    print(self.parent)


if __name__ == '__main__':
  fooChild = FooChild()
  fooChild.bar('HelloWorld')
"""
# execfile('super_method.py')
exec(run_code)