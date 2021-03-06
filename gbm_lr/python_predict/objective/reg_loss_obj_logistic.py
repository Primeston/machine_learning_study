#!/usr/bin/env python
# coding=utf-8

'''
    > File Name: reg_loss_obj_logistic.py
    > Author: ZS
    > Mail: dragon_201209@126.com
    > Created Time: 2016年11月12日 星期六 21时46分48秒
'''

#import types
from util.common import Common

class RegLossObjLogistic(Common):
    
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
            return self._common_tool.sigmoid_list(pred)
        return self._common_tool.sigmoid(pred)

