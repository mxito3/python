import requests.models

class client():
    def get(self,url):
        header = {}
        header['Content-Type'] = 'applicaton/json'
        return requests.get(url,headers=header)
    def post(self,url,data):
        header = {}
        header['Content-Type'] = 'application/x-www-form-urlencoded'
        try:
            return requests.post(url,headers=header,data=data)
        except Exception as e:
            print(e)
        
        
if __name__ == "__main__": 
    test_client = client()
    url = 'http://wwww.baidu.com'
    result = test_client.get(url)
    # print(result.status_code)

    # print(result.headers['Content-Type'])
    json = result.json
    # print(json)
    # print(result.text)
    #'_content', 'status_code', 'headers', 'url', 'history','encoding', 'reason', 'cookies', 'elapsed', 'request'
    # print(result)

    data ={}
    usdt_url = "https://api.omniexplorer.info/v1/transaction/address"
    data = "addr=1EXoDusjGwvnjZUyKkxZ4UHEf77z6A5S4P&page=0"
    tx=test_client.post(usdt_url,data=data).text
    print(tx)
