# Dcard cloudflare can't using session get/post
# Use Drission instead
"""
https://www.drissionpage.cn/

"""

import time
import random
from DrissionPage.common import Settings
from DrissionPage import Chromium
Settings.set_language('zh_cn')

from page.all_forum import _ALL_FORUMS

def get_article_and_href(tab):
    # 先抓所有文的block
    articles = tab.eles(
        '@class=d_a5_22 d_eg_6y7mag d_s7_2o d_2l_f d_9w_25 d_mk_f7aqx6 d_mh_140cd6v d_mg_140cd6v w1n8s3eg')
    # print(articles)

    for article in articles:
        time_href_element = article.ele('@class=d_2nx2hs_8stvzk')
        # Get href and article post time.
        href = time_href_element.attr('href')
        post_time = time_href_element.ele('tag:time').attr('title')
        # article title
        article_title = article.ele(
            '@class=d_75_3c d_d8_2s d_cn_1t d_gk_qslrf5 d_lc_1u d_a5_3e d_tx_2c d_gf_3r d_7v_1gltyc2 d_hk_26 p1ukfoib')
        print(href)
        print(post_time)
        print(article_title.text)
        tab.actions.scroll(on_ele=article_title)
        # time.sleep(5)
        # Just in case of network issue or been block by website
        time.sleep(random.uniform(0.5, 2))


target = "感情"

tab = Chromium().latest_tab
tab.get(f'https://www.dcard.tw{_ALL_FORUMS[target]}')
# # tab.set.load_mode.normal()
time.sleep(5)
get_article_and_href(tab)








