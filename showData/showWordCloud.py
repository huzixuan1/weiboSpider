
import csv
from pyecharts import options as opts
from pyecharts.charts import WordCloud

def generate_wordcloud_from_csv(csv_filename):
    user_descriptions = []

    # 从CSV文件中读取用户简介数据
    with open(csv_filename, mode="r", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            user_descriptions.append(row[7])

    # 将所有用户简介拼接成一个字符串
    text = ' '.join(user_descriptions)

    # 创建词云
    wordcloud = (
        WordCloud(init_opts=opts.InitOpts(renderer='svg'))
        .add(series_name="评论用户简介", data_pair=[(word, 1) for word in text.split()], word_size_range=[10, 50])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论用户简介词云"),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .set_series_opts(
            textstyle_opts=opts.TextStyleOpts(font_size=30),  # 设置字体大小
        )
    )

    # 保存为HTML文件
    wordcloud.render("ShowWordcloud.html")

# 传入你的CSV文件名
generate_wordcloud_from_csv("weiboData.csv")


