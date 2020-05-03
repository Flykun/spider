import requests


headers = {
    'Cookie': '_zap=e1db96db-cc9d-4871-810c-f90ebf5b0723; d_c0="AFAaZIrZMRGPTv7mk1cZm-ZLY7zL3zA3UK8=|1588183137"; '
              '_ga=GA1.2.1371584754.1588183138; _xsrf=u4kdQ3x5EHMOoz6ROq41IMQfE5EKKDTy; _gid=GA1.2.1674570313.1588398038; capsion_ticket="2|1:0|10:1588398052|14:capsion_ticket|44:NzIzNWU1ODJlNGU2NDk5OGI4YmNhZWQ0YmQzNDhkYWM=|1b61243b06289f50128b51c6919d8601dcf5bc928444471f8ff6312c807cba4c"; z_c0="2|1:0|10:1588398062|4:z_c0|92:Mi4xbWxJM0NnQUFBQUFBVUJwa2l0a3hFU1lBQUFCZ0FsVk43bFdhWHdEazloQWtlN0VWVDZEZXcwVGpzS2ZMdkRQcGF3|6074c10f399a2be837c7ab664493cea8d898874dfc4db3417b338acc8a243bc8"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1588183138,1588263450,1588398038,1588402711; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588402711; _gat_gtag_UA_149949619_1=1; SESSIONID=y76iu5LW8xOWt0O6hM1OEPju6XFhEgYV7XU8tHsk5vD; KLBRSID=975d56862ba86eb589d21e89c8d1e74e|1588402714|1588402711; JOID=V1wUAE-GoFOTw7ZOcIAQjsPvr3tl_pJn_beCByW_2RnGsIcAQ5i9-8vDskl1VienKSVn3KEFn5E5mfAdS-YCVIk=; osd=V14QB06GoleUwrZMdIcRjsHrqHpl_JZg_LeAAyK-2RvCt4YAQZy6-svBtk50ViWjLiRn3qUCnpE7nfccS-QGU4g=',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',

}
r = requests.get('http://www.zhihu.com', headers=headers)

print(r.text, sep='\n')