from libs.Tools import BaseHttp

class LoginBaseClass(BaseHttp):
    # 定义一个公共的请求头信息
    # 这真的是个类变量
    leibianliang = {
        'PHPSESSID':''
    }
    # 登录接口
    def login(self,email='test006',
              user_pwd='Q3VDZ01Yek5aYnRIaGRLVXVXS254RHVURHJPdm5Tc0ZVSUdkaG9zbFhuVWRFUVpFdHclMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
              ajax='1'):
        login_url = '/index.php?ctl=user&act=dologin'
        login_data = {
            'email': email,
            'user_pwd': user_pwd,
            'ajax': ajax,
        }
        result = self.post_data(url=login_url, data=login_data)
        pid = result.cookies['PHPSESSID']
        # 登录成功后把pid字段放入公共请求头信息中
        self.leibianliang['PHPSESSID'] = pid
        return result

if __name__ == '__main__':
    run = LoginBaseClass()
    run.login()
