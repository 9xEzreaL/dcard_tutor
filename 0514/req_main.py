# import requests
# import os
import random
from curl_cffi import requests




def fetch_dcard_data():
    session = requests.Session()
    # session.proxies = random_proxy()

    # url = "https://www.dcard.tw/service/api/v2/globalPaging/page?enrich=true&forumLogo=true&pinnedPosts=widget&country=HK&platform=web&listKey=athena-HK-2&immersiveVideoListKey=v_local_HK&pageKey=e2722799-fb69-4e73-a3d9-06f773c5c5ff&offset=30"
    url = "https://www.dcard.tw/service/api/v2/globalPaging/page?enrich=true&forumLogo=true&pinnedPosts=widget&country=TW&platform=web&listKey=popular_TW_decay_cap&immersiveVideoListKey=v_popular_TW&pageKey=1173136d-6d85-473b-a9a7-53024db1444d&offset=0"
    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.dcard.tw/f',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        # 'Cookie': '__cf_bm=IXxLjuDhxaNHuX5Z50AGRECAbTE1dXUX4PCFNt7AGQY-1746687456-1.0.1.1-Ai7Y7YSCFrhfNC88StmaQ8TLg1KtCmkuJwSc7jmHN6Me20IC15bVcYtwgxQ1Ewrt0lmaULfnWzHba6NPDmwE7JnMPyDMMMSSBkN4NtAdbJo; _cfuvid=I9nRIhADS3gSFf74tgKeKV43vx7bT4652Qr2dqaYLzM-1746687456195-0.0.1.1-604800000; __cf_dm=YWRtaW46MDox.521.crc.cf4dca1e; NID=57806570; dcsrd=rSGgAVaOaQzGPdjg7bJjCtmr; cf_clearance=swgPcg6YfNFBUanvMJqkXz5GUnCelF9995EPMH5aT8M-1746687457-1.2.1.1-FQ6Rf3Wk7HKB6CQJephAOpwVZq.36Gayr0BsQ1Nb2DgpkGyxW6UO2ifPhTWKcJeSPwIgb_gR.FwzT0.uS8_1KCaONPpZZtT4dqt6SDWjfDqJyB_vel7NEzhC939Y5LcTQPT.caE2ovXDhYBAwyhMOhCG38HnOVxp1QZGhWk0djAWB4xN3ChmWwCoM2ka8yt56yMistleZeuhnS2_4_8cTECbYcFk7lxwkVtO7guOehAuoA4h_3nYQ7reog9TzIaswSJ50VgmfMBN2tPD4Gai3ng4PhBDQ7df_DGwSU248vZfeVDD62f2lDkk.RVwweDWGgo7.2VTtKgUWm38GDOMvxdLQUEVKuKcFQFVXcdQsMY'
    }
    proxies = None
    print(proxies)
    response = session.request(
        "GET", url, headers=headers, data=payload, proxies=proxies)

    print(response.text)


if __name__ == "__main__":
    fetch_dcard_data()
