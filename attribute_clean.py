"""
存储request中的不同属性
"""

import re

# 常规request参数，共23个
request_attribute = [
    'ip',
    'method',
    'url',
    'path',
    'host',
    'proto',
    'rawquery',
    'agent',
    '$numberLong',
    'headers',
    'Content-Length',
    'Content-Type',
    'Keep-Alive',
    'User-Agent',
    'Accept',
    'Accept-Encoding',
    'Accept-Language',
    'Connection',
    'Connection-Length',
    'version',
    'resume',
    'ciphersuite',
    'server'
]

# 补充request参数，共9个。这部分参数缺失超过总样本的2/3，因此不予提取这部分参数
request_attribute_2 = [
    'Sec-Fetch-Mode'
    'Sec-Fetch-Site',
    'Sec-Fetch-User',
    'Cookie',
    'Upgrade-Insecure-Requests',
    'Sec-Ch-Ua',
    'Sec-Ch-Ua-Mobile',
    'Sec-Ch-Ua-Platform',
    'Sec-Fetch-Dest'
]

wafinfo_attribute = [
    'rayid',
    '"id',
    'message',
    'data'
]
# 去掉'"', '\[', '\]', '\{', '\}', ':', ','
def string_clean(symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, str1):
    str1 = re.sub(symbol1, '', str1)
    str1 = re.sub(symbol2, '', str1)
    str1 = re.sub(symbol3, '', str1)
    str1 = re.sub(symbol4, '', str1)
    str1 = re.sub(symbol5, '', str1)
    str1 = re.sub(symbol6, '', str1)
    str1 = re.sub(symbol7, '', str1)
    return str1




