import time
import csv
import random
import requests
from fake_useragent import UserAgent

def get_comments(weiboId):
    cookies = 'Fill in your own cookie values'


    params = {
        'id': weiboId,
        'mid': weiboId,
        'max_id_type': '0',
    }

# If possible, it is recommended to add proxies
    proxie = { 
            'http1': 'http://114.231.45.11:8888',
            'http2': 'http://113.121.38.12:9999',
            'http3': 'http://114.231.42.231:8888',
            'http4': 'http://180.121.129.132:8888',
            'http5': 'http://60.170.204.30:8060',
        } 

    page = 1
    comments_count = 0
    with open("weiboComments.csv",mode="a",newline='',encoding="utf-8-sig") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(['页码','评论id','评论发布时间','评论ip','评论点赞数','评论','评论用户名','评论用户简介','用户Id','关注人数','粉丝数','性别(f=女|m=男)'])


    # 创建一个 UserAgent 对象
    user_agent = UserAgent()
    random.seed()

    while True:
        headers = {
            'cookie': cookies ,
            'referer': 'https://m.weibo.cn/detail',
            
            'user-agent': user_agent.random

            }

        response = requests.get('https://m.weibo.cn/comments/hotflow', 
                                params=params,
                                headers=headers,
                                proxies=proxie)

        json_list = response.json()
        max_id = json_list['data']['max_id']
        try:
            max_id = json_list['data'].get('max_id')  
            if max_id is None:
                print("无法获取更多评论，已退出程序")
                break
        except KeyError as e:
            print("评论已爬取完成，一共爬取了"+str(comments_count)+"条数据")
            break
        results = json_list['data']['data']
        max_id_type = json_list['data']['max_id_type']

        for data in results:
            id = data['id']   # id
            created_at = data['created_at'] # created_time
            source = data['source']     # source
            like_count = data['like_count'] # like_count
            text = data['text']     # text
            screen_name = data['user']['screen_name']  # username
            description = data['user']['description']   # 简介
            userId = data['user']['id']         # userId
            follow_count = data['user']['follow_count'] # 关注的人
            followers_count = data['user']['followers_count'] # 粉丝
            gender = data['user']['gender'] # 性别
            print(page,id,created_at,source,like_count,text,screen_name,description,userId,follow_count,followers_count,gender)
            comments_count +=1
            with open("weiboComments.csv",mode="a",newline='',encoding="utf-8-sig") as f:
                        csv_write = csv.writer(f)
                        csv_write.writerow([page,id,created_at,source,like_count,text,screen_name,description,userId,follow_count,followers_count,gender])

        params['max_id'] = max_id
        params['max_id_type'] = max_id_type
        page += 1

        print(headers['user-agent'])
        # 随机休眠0到5秒
        sleep_time = random.uniform(0, 3)
        print("sleep time:",sleep_time)
        print("爬取评论数量:", comments_count)
        print("======================")
        time.sleep(sleep_time)

if __name__ == "__main__":
    #  get_comments(weiboID)
    # For example, you need to fill in the ID of Weibo here
     get_comments(4983519967183846)
