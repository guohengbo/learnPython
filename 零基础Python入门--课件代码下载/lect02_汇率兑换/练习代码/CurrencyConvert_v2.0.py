"""
    功能：汇率兑换
    版本：2.0
    新增:根据输入判断是人民币还是美元，进行相应的转换计算
    日期：07/08/2018
"""
USD_VS_RMB = 6.77
def usdValue(value):
    rmb_str_value = value
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / USD_VS_RMB
    print('美元(USD)金额是：', usd_value)

def rmbValue(value):
    usd_str_value = value
    usd_value = eval(usd_str_value)
    rmb_value = usd_value * USD_VS_RMB
    print('人民币(CNY)金额是：', rmb_value)

def main(): 
    currency_str_value = input("请输入带单位的货币金额：")
    unit = currency_str_value[-3:]
    value = currency_str_value[:-3]
    if unit == 'CNY':
        usdValue(value)
    elif unit == 'USD':
        rmbValue(value)
    else:
        print('目前版本尚不支持该种货币！')
        
if __name__=='__main__':
    main()