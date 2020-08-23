import requests
import pandas as pd
import json
import numpy as np

# load test data
path = "-path-"
company_list = pd.read_excel(path, sheet_name = "-sheet_name-")
encode = "utf-8"
token = '-token-'
reqInterNme = "-URL-"
test_data_list = list(company_list["公司名称"])
user_id = "ACMR"
print("用户ID:", user_id)
print("公司列表路径：", path)
print("编码：", encode)
print("令牌：", token)
print("接口：", reqInterNme)

#设置请求URL
result_list = []
for i in test_data_list:   
    paramStr = f'name={i}'
    url = reqInterNme + "?Y_TOKEN=" + token + "&" + paramStr + "&" + "off_on=off_on" + "&" + "CONSUMER_USER_ID=" + user_id + "&" + "Y_TOKEN=" + token + paramStr ;
    response = requests.get(url)
    
    #结果返回处理
    print(response.status_code)
    resultJson = json.dumps(str(response.content, encoding = encode))
    # convert unicode to chinese
    resultJson = resultJson.encode(encode).decode("unicode-escape")
    result_list.append(resultJson)
    print(i, " load") 
print("所有数据已经读入result_list!")

df = pd.DataFrame()
for i in range(len(result_list)):
              df =  df.append(pd.DataFrame(pd.Series(json.loads(result_list[i][1:-1])["result"]["result"])).T)

df.set_index("name", inplace = True)
df.to_excel("C://Users/Thinkpad/Desktop/经营-企业基本信息v1.xlsx", sheet_name="经营-企业基本信息v1", index=True, encoding="utf-8")
