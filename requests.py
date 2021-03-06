#!python
# -*- coding: utf-8
'''
    将按顺序从上往下对配置项进行并发测试
'''

requests = [
    {
        'url': 'https://{your_domain}/api/checkout/order/4814c489-4513-4ed7-9e6c-7cb98ae9e09f?step=contact_information',
        # 可选，默认 GET
        'method': 'GET',
        # 可选，
        'headers': [
            {
                'STORE-ID': 1156
            }
        ],
        # 可选，
        'body': None,
        # 可选，并发请求数
        'connections': 20,
        # 可选，请求持续时长
        'duration': '10s',
    },
    {
        'url': 'https://www.baidu.com',
        'connections': 100
    },
    {
        'url': 'https://{your_domain}/api/cart/a171913f-49c1-4e5c-bdf3-fed6311f2e08',
        'method': 'POST',
        'headers': [
            {
                'Content-Length': 106,
                'Content-Type': 'application/json',
                'Cookie': 'awesomecookie=9alc4bfrfimvmnepn0vss77shh; _identity_cart=6af33595-1174-44ee-acab-be62700899e0; client_id=1552913406905376; _identity_popups=%C3%8F%A81%EC%A2%7E%13%DF+%9E1%2B%7F%C3%F7a71b01f98439ad8375d4145d6cf99c075319a44b7338b8c4593457effbb71ba2%DE%D9%89%3D%86Xb%A34%237%0Fe%B7c%A2%2AS%9DpsO%94%241%96%D9n%25g%ED%E0m+%99%A8F%87%FF%0E%0B%8Bxql%AD%EEUT%A3D%5EUf%21W%C8ta%09E%60%96%15; admin_id=1552916272009276; Hm_lvt_059e6bb1e7807ca60743d87d83ce2b34=1552916272,1552936256; _fbp=fb.1.1552987566385.1352581131; _ga=GA1.2.1552987566475396; CSRF-TOKEN=4%2FTWJ6apw1hXitglKpyyLejr1dFx6zx0JNz8vs37Eldm8jmi86EHr34scUzIf00kkeurHQa9jnKeBsBGCaSbDA%3D%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221171%22%2C%22%24device_id%22%3A%2216990da1c29421-0b4cd603bb68a7-36667905-2073600-16990da1c2aba8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216990da1c29421-0b4cd603bb68a7-36667905-2073600-16990da1c2aba8%22%7D; awesomev2=MTU1MzIzMDk2NnxGQVplRkVINGZKbW12RDMyQXA4RlZHclVjenBPX3Z0Z2tCa2EzbFZBa3otV2FUd05QNDkzT092c3RKVUpSMjRxUzhuVGNYTU16ZjA9fD2Bb9smE10BLHZrBVdiVKQfwMkhlEKOXPM3KrjpTX0g; Hm_lpvt_059e6bb1e7807ca60743d87d83ce2b34=1553230967; store_locale=zh-TW; session_id=1553246877960204',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }
        ],
        'body': {'ware_id': 61, 'package_num': 2, 'coll_fee': 100, 'recv_address': {'address': 'u5742u7530u8857u9053u53d1u8fbeu8def6u53f7u4e91u91ccu667au80fdu56ed',
                                                                                    'city': {'adcode': '440300', 'center': {'lat': 22.547, 'lng': 114.085947},
                                                                                             'create_time': '2019-06-19 11:13:45', 'name': 'u6df1u5733u5e02',
                                                                                             'provincecode': '440000', 'rank': 23, 'update_time': '2019-06-19 11:13:45'},
                                                                                    'city_adcode': '440300', 'create_time': '2019-06-20 11:34:40',
                                                                                    'district': {'adcode': '440307', 'center': {'lat': 22.721511, 'lng': 114.251372},
                                                                                                 'citycode': '440300', 'create_time': '2019-06-19 11:13:45',
                                                                                                 'name': 'u9f99u5c97u533a', 'provincecode': '440000', 'rank': 204,
                                                                                                 'update_time': '2019-06-19 11:13:45'}, 'district_adcode': '440307',
                                                                                    'geo': {'lat': 22.629942, 'lng': 114.069548}, 'id': 55, 'is_deleted': 0, 'merchant_id': 31,
                                                                                    'name': 'wp', 'phone': '13900000000',
                                                                                    'province': {'adcode': '440000', 'center': {'lat': 23.125178, 'lng': 113.280637},
                                                                                                 'countrycode': '100000', 'create_time': '2019-06-19 11:13:58',
                                                                                                 'name': 'u5e7fu4e1cu7701', 'rank': 2, 'update_time': '2019-06-19 11:13:58'},
                                                                                    'province_adcode': '440000',
                                                                                    'street': {'adcode': '002852', 'center': {'lat': 22.6659, 'lng': 114.054}, 'citycode': '440300',
                                                                                               'create_time': '2019-06-19 11:13:45', 'districtcode': '440307',
                                                                                               'name': 'u5742u7530u8857u9053', 'provincecode': '440000', 'rank': 2852,
                                                                                               'update_time': '2019-06-19 11:13:45'}, 'street_adcode': '002852',
                                                                                    'title': 'u4e91u91ccu65d7u8230', 'update_time': '2019-06-20 16:04:49'},
                 'vehicle_mode': 'minivan', 'is_urgent': 1}
    }
]
