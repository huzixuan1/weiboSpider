import csv
from pyecharts import options as opts
from pyecharts.charts import Bar
from collections import Counter

def visualize_top_ip_addresses(csv_filename, top_n=20):
    comment_ips = []

    # 从CSV文件中读取评论IP数据
    with open(csv_filename, mode="r", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            comment_ips.append(row[3])

    # 统计IP地址出现的次数
    ip_counter = Counter(comment_ips)

    # 获取前20个出现频率最高的IP地址及其出现次数
    top_ip_addresses = ip_counter.most_common(top_n)

    # 提取横坐标和纵坐标数据
    x_data = [ip[0] for ip in top_ip_addresses]
    y_data = [ip[1] for ip in top_ip_addresses]

    # 创建柱状图
    bar = (
        Bar(init_opts=opts.InitOpts(renderer='svg'))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="IP地址出现次数", y_axis=y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论中前20个IP地址出现次数"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )

    # 保存为HTML文件
    bar.render("showTopComments.html")

# 传入你的CSV文件名
visualize_top_ip_addresses("weiboData.csv")
