import requests
import unittest

# http统一处理
# 使用libs封装requests的传参方式，尽可能的省略传参方法
class BaseHttp(object):
    host = 'http://localhost'
    def post_data(self,url,data,icon=1,*args,**kwargs):
        '''
        :param url:
        :param data:
        :param icon: 1代表正常请求，2代表文件上传
        :return:
        '''
        url = '{}{}'.format(self.host,url)
        if icon == 1:
            result = requests.post(url=url,data=data,*args,**kwargs)
        elif icon ==  2 :
            result = requests.post(url=url,files=data,*args,**kwargs)
        return result


    def get_data(self,url,params,*args,**kwargs):
        '''
        :param url:
        :param params:
        :return:
        '''
        result = requests.get(url=url,params=params,*args,**kwargs)
        return result

    # def get_request(method='post', data='', url='', *args, **kwargs):
    #     '''
    #     封装request方法
    #     :param method: 请求方式
    #     :param data:
    #     :param url:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     '''
    #     try:
    #         if os.path.isfile(data):
    #             res = requests.request(method=method, files=data, url=url, *args, **kwargs)
    #     except TypeError as e:
    #         res = requests.request(method=method, data=data, url=url, *args, **kwargs)
    #     except BaseException as e:
    #         print(e)
    #
    #     return res


class VerifyClass(unittest.TestCase):

    # 校验状态码
    def verifyCode(self,result,v_code):
        '''
        :param result: 响应体
        :param v_code: 校验的状态码
        :return:
        '''
        self.assertEqual(result.status_code,v_code)

    # 校验某个json字段
    def verifyJson(self,result,key,value):
        '''
        :param result: 响应体
        :param key: 响应体需要校验的字段
        :param value: 校验的正确值
        :return:
        '''
        result = result.json()
        # 转换为字典后，通过Key字段获取我想要的value
        v = result.get(key)
        # 使用value来进行校验
        self.assertEqual(v, value)

    # 校验某个Html字段
    def verifyHtml(self, result,value):
        result = result.text
        self.assertAlmostEqual(result,value)
