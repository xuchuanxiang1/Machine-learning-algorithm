# -*- coding: UTF-8 -*-
import pickle


"""
函数说明:存储决策树
Parameters:
    inputTree - 已经生成的决策树
    filename - 决策树的存储文件名
"""
def storeTree(inputTree,filename):
    with open(filename,'wb') as fw:
        pickle.dump(inputTree,fw)


"""
函数说明:读取决策树
Parameters:
    filename - 决策树的存储文件名
Returns:
    pickle.load(fr) - 决策树字典
"""
def grabTree(filename):
    with open(filename,'rb') as fr:
        return pickle.load(fr)

if __name__ == '__main__':
    myTree = {'有自己的房子': {0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
    storeTree(myTree, 'classifierStorage.txt')
    myTree01 = grabTree('classifierStorage.txt')
    print(myTree01)