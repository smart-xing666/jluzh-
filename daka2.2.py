import requests
from functools import partial

proxies = {
    "http": 'http://127.0.0.1:8080',
    "https": 'http://127.0.0.1:8080'
}
requests_request = partial(requests.request, proxies=proxies, verify=False, allow_redirects=False)
url="https://www.baidu.com"

headers ={
    'Host': 'work.zcst.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Content-Type': 'text/json',
    'Origin': 'https://work.zcst.edu.cn',
    'Connection': 'close',
    'Referer': 'https://work.zcst.edu.cn/default/work/jlzh/jkxxtb/jkxxcj.jsp?ticket=ST-24330713-ANsD7z4KDr6LPy5L9IMo-authserver.zcst.edu.cn',
    'Cookie': 'JSESSIONID=38ABBCD33F34F72940ABE839030CCCDE'

}

respnse = requests_request('GET',url,headers=headers)
