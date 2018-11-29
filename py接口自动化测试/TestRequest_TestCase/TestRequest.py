import json
import requests
from log import logger
# 添加一个数组，用来装测试结果
hlist = []
#公共的头文件设置
header = {
'content-type': "application/json;charset=UTF-8"
}
#Post
def testPostRequest(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,response_testhope):
    hr=requests.post(hurl,data=hdata,headers=headers)
    hresult=json.loads(hr.text)# 获取并处理返回的json数据
    hstatus=hresult["status"]
    if hstatus==htesthope and response_testhope in str(hresult):
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"POST",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"通过"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.info(htestcasename)
        logger.info("通过")
        logger.info(" 实际结果：" + str(hresult))
    else:
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"POST",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"失败"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.error(htestcasename)
        logger.error("失败")
        logger.error(" 实际结果：" + str(hresult))
    # print(hlist)

#GET
def testGetRequest(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,response_testhope):
    hr=requests.get(hurl,params=hdata,headers=header)
    hresult=json.loads(hr.text)# 获取并处理返回的json数据
    hstatus=str(hresult["status"])#不同场景需修改为code或status
    if hstatus==htesthope and response_testhope in str(hresult):
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"GET",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"通过"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.info(htestcasename)
        logger.info("通过")
        logger.info(" 实际结果：" + str(hresult))
    else:
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"GET",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"失败"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.error(htestcasename)
        logger.error("失败")
        logger.error(" 实际结果：" + str(hresult))
    # print(hlist)

#Delete  返回状态码3种：200-OK 202-accept 204-No Content
def testDelRequest(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,response_testhope):
    hr=requests.delete(hurl,params=hdata,headers=header)
    hresult=json.loads(hr.text)# 获取并处理返回的json数据
    hstatus=hresult["status"]
    if hstatus==htesthope and response_testhope in str(hresult):
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"DELETE",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"通过"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.info(htestcasename)
        logger.info("通过")
        logger.info(" 实际结果：" + str(hresult))
    else:
        data={
            "t_id":htestcaseid,
            "t_name":htestcasename,
            "t_method":"DELETE",
            "t_url":hurl,
            "t_param":"测试数据："+str(hdata),
            "t_hope":"status:" + htesthope + " 期望结果：" + response_testhope,
            "t_actual":"status:" + hstatus + " 实际结果：" + str(hresult),
            "t_result":"失败"
            }
        hlist.append(data) # 把测试结果添加到数组里面
        logger.error(htestcasename)
        logger.error("失败")
        logger.error(" 实际结果：" + str(hresult))
    # print(hlist)