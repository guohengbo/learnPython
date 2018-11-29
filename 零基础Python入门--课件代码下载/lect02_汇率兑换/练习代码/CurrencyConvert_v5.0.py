"""
    功能：汇率兑换
    版本：4.0
    新增:根据输入判断是人民币还是美元，进行相应的转换计算
    4.0 函数优化
    5.0 lambda函数优化
    日期：07/08/2018
"""
USD_VS_RMB = 6.77
def main(): 
    currency_str_value = input("请输入带单位的货币金额：")
    unit = currency_str_value[-3:]
    value = currency_str_value[:-3]
    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB
    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1
        
    if exchange_rate != -1:
        in_money = value
        convert_currency2 = lambda x: x * exchange_rate
        out_money = convert_currency2(in_money)
        print('转换后的金额：', out_money)
    else:
        print('不支持该种货币！')
        
if __name__=='__main__':
    main()