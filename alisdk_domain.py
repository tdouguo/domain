#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkdomain.request.v20180129.CheckDomainRequest import CheckDomainRequest
import json
import time


# strs = [chr(i) for i in range(ord("A"),ord("Z")+1)] + [str(i) for i in range(10)]

client = AcsClient('AccessKey ID', 'AccessKey Secret', 'cn-beijing')

file_name= "domain.txt"

def check(domain):
    try:
        request = CheckDomainRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain)

        response = client.do_action_with_exception(request)
        res = str(response, encoding='utf-8')
        res_json = json.loads(res)

        # python2:  print(response)
        # 1：可注册。 3：预登记。4：可删除预订。0：不可注册。 -1：异常。 -2：暂停注册。 -3：黑名单。
        if res_json['Avail'] ==1:
            print(domain, res)
            with open(file_name, 'a') as f:
                f.write(domain+"\r\n")
    except Exception as e:
        # print (domain,e)
        time.sleep(0.1)
        check(domain)


# for i1 in strs:
#     for i2 in strs:
#         for i3 in strs:
#             domain = i1+i2+i3+".cn"
#             check(domain)

strs = [chr(i) for i in range(ord("A"),ord("Z")+1)]

for i1 in strs:
    for i2 in strs:
        check( i1+i2+ "123.com");


print ("完成。")