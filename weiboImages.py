
import requests
import re
import os

def getImage(weiboId):
    url = "https://m.weibo.cn/detail/"+str(weiboId)
    response = requests.get(url)

    # 使用正则表达式匹配包含 pic_ids 的部分
    pattern = re.compile(r'"pic_ids":\s*\[([^\]]*)\]')

    # 在响应文本中搜索匹配的内容
    match = pattern.search(response.text)

    if match:
        # 获取匹配的内容
        pic_ids_str = match.group(1)

        # 使用逗号分隔的值拆分为列表
        pic_ids_list = pic_ids_str.split(',')

        # 去除每个元素两侧的空格和引号
        pic_ids_list = [re.sub(r'\s|"', '', pic_id) for pic_id in pic_ids_list]

        # 创建保存图片的目录
        if not os.path.exists("Image"+str(weiboId)):
            os.makedirs("Image"+str(weiboId))

        for data in pic_ids_list:
            # 构建图片的URL
            img_url = f"https://wx3.sinaimg.cn/large/{data}.jpg"

            # 发送请求获取图片数据
            response = requests.get(img_url)

            # 构建保存路径
            save_path = os.path.join("Image"+str(weiboId), f"{data}.jpg")

            # 保存图片
            with open(save_path, 'wb') as f:
                f.write(response.content)

            print(f"图片 {data}.jpg 已保存")

    else:
        print("未找到包含图片ID的内容")

if __name__ == "__main__":
    # getImage(weiboId)
    # for example 
    getImage(4978087118766712)
