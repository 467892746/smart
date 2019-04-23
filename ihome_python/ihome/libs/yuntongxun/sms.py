#coding=utf-8


from CCPRestSDK import REST


#主帐号
accountSid= '8a216da869dca619016a0b1eaeb9148e'

#主帐号Token
accountToken= 'da98c88fac58446989288634a01ef152'
#应用Id
appId='8a216da869dca619016a0b1eaf131495'

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

#请求端口 
serverPort='8883'

#REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id

class CCP(object):
    '''发送短信的辅助类'''
    # 用来保存对象的类属性
    instance = None
    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象,如果没有,创建一个对象,并且保存
        # 如果有,则将保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls.instance = obj
        return cls.instance
    def sendTemplateSMS(self,to,datas,tempId):
        result = self.rest.sendTemplateSMS(to,datas,tempId)
        # for k,v in result.iteritems():
        #
        #     if k=='templateSMS' :
        #             for k,s in v.iteritems():
        #                 print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)
        status_code = result.get('statusCode')
        if status_code == '000000':
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1

   
#sendTemplateSMS(手机号码,内容数据,模板Id)

if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.sendTemplateSMS('15197815013', ['1234', '5'], 1)
    print(ret)