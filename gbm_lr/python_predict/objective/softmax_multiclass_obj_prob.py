#!/usr/bin/env python
# coding=utf-8

'''
    > File Name: softmax_multiclass_obj_prob.py
    > Author: ZS
    > Mail: dragon_201209@126.com
    > Created Time: 2016年11月12日 星期六 22时04分53秒
'''

#import types
from util.common import Common

class SoftmaxMulticlassObjProb(Common):
    
    _common_tool = Common()

    def __init__(self):
        '''
        __init__
        '''
        self._common_tool = Common()
        return

    def __del__(self):
        '''
        __del__
        '''
        return 

    def pred_transform(self, pred):
        '''
        pred_transform
        '''
        if (isinstance(pred, list)):
        #if (types.ListType == type(pred)):
            return self._common_tool.softmax(pred)
        return False

