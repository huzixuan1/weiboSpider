from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Page
import pandas as pd
from pyecharts.charts import Map

from pyecharts.charts import Line
from collections import Counter
from datetime import datetime
import csv
from pyecharts.charts import Pie
from pyecharts.charts import WordCloud
from pyecharts.commons.utils import JsCode

from pyecharts.components import Table


def index():
    table = Table()
    table.add(headers=["微博评论可视化"], rows=[], attributes={
        "align": "center",
        "border": False,
        "padding": "50px",
        "style":"background:{};width:500px;height:30px;color:red;font-size:20px;"
    })

    return table


def showFans() -> Bar:
    df = pd.read_csv('./weiboData.csv')

    # 处理粉丝数（以“万”为单位的情况）
    df['粉丝数'] = df['粉丝数'].apply(lambda x: float(x.replace('万', '')) * 10000 if '万' in str(x) else float(x))

    # 选择粉丝数前20的用户
    top20_users = df.nlargest(20, '粉丝数')

    c = (
        Bar(init_opts=opts.InitOpts(renderer='svg',theme="dark"))
        .add_xaxis(list(top20_users['评论用户名']))
        .add_yaxis("粉丝数", list(top20_users['粉丝数']))
        .add_yaxis("关注数", list(top20_users['关注人数']))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="评论用户粉丝前20情况"))
    )

    return c  # 返回图表对象而不是调用 render 函数


def showIp() -> Bar:
    # 读取CSV数据
    df = pd.read_csv('./weiboData.csv')

    # 统计评论IP出现次数
    data = df['评论ip'].str.replace('来自', '').str.strip()
    ip_counts = data.value_counts().reset_index()

    # 格式化城市统计次数的列表
    city_counts_list = [list(city_count) for city_count in zip(ip_counts['index'], ip_counts['评论ip'])]

    name_map = {
        '江苏省': '江苏',
        '浙江省': '浙江',
        '北京市': '北京',
        '上海市': '上海',
        '江西省': '江西',
        '湖南省': '湖南',
        '安徽省': '安徽',
        '福建省': '福建',
        '山东省': '山东',
        '河北省': '河北',
        '天津市': '天津',
        '湖北省': '湖北',
        '河南省': '河南',
        '广东省': '广东',
        '广西壮族自治区': '广西',
        '四川省': '四川',
        '重庆市': '重庆',
        '贵州省': '贵州',
        '云南省': '云南',
        '西藏自治区': '西藏',
        '陕西省': '陕西',
        '甘肃省': '甘肃',
        '青海省': '青海',
        '宁夏回族自治区': '宁夏',
        '新疆维吾尔自治区': '新疆',
        '内蒙古自治区': '内蒙古',
        '黑龙江省': '黑龙江',
        '吉林省': '吉林',
        '辽宁省': '辽宁',
        '台湾省': '中国台湾',
        '香港特别行政区': '香港',
        '澳门特别行政区': '澳门',
        '海南省': '海南',
        '山西省': '山西',
    }


    #绘制地图
    c = (
        Map(opts.InitOpts(renderer='svg',theme="dark"))
        .add("comments", city_counts_list, "china", is_map_symbol_show=False,name_map=name_map)
        .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}"),
            tooltip_opts=opts.TooltipOpts(formatter="{a}: {c}")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(),
            visualmap_opts=opts.VisualMapOpts(),
        )
        # .render("mapComments.html")
    )
    return c


def showCommentsTime() -> Line:
    comment_dates = []

    # 从CSV文件中读取评论发布时间数据
    with open("./weiboData.csv", mode="r", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            comment_date = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
            comment_dates.append(comment_date)

    # 排序日期
    sorted_comment_dates = sorted(comment_dates)

    # 统计每个日期的评论数量
    comment_count_by_date = dict(Counter(sorted_comment_dates))

    # 获取横坐标和纵坐标数据
    x_data = list(comment_count_by_date.keys())
    y_data = [comment_count_by_date[date] for date in x_data]

    # 绘制图表
    c = (
        Line(init_opts=opts.InitOpts(renderer='svg',theme="dark"))
        .add_xaxis(x_data)
        .add_yaxis("评论数量", y_data, is_smooth=True)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论数量统计"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )

    return c


def showSex() -> Bar:
    # 读取CSV数据
    df = pd.read_csv('./weiboData.csv')

    # 统计性别分布
    data = df['性别']
    sex_counts = data.value_counts().reset_index()
    sex_list = [list(sex_count) for sex_count in zip(sex_counts['index'], sex_counts['性别'])]

    c = (
        Pie(init_opts=opts.InitOpts(renderer='svg',theme="dark"))
        .add(
            "",
            sex_list,
            center=["35%", "50%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论性别分布"),
            legend_opts=opts.LegendOpts(pos_left="15%"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return c

def showTopComments() -> Line:
    comment_ips = []

    # 从CSV文件中读取评论IP数据
    with open("weiboData.csv", mode="r", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            comment_ips.append(row[3])

    # 统计IP地址出现的次数
    ip_counter = Counter(comment_ips)

    # 获取前20个出现频率最高的IP地址及其出现次数
    top_ip_addresses = ip_counter.most_common(20)

    # 提取横坐标和纵坐标数据
    x_data = [ip[0] for ip in top_ip_addresses]
    y_data = [ip[1] for ip in top_ip_addresses]

    # 创建柱状图
    c = (
        Bar(init_opts=opts.InitOpts(renderer='svg',theme="dark"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="IP地址出现次数", y_axis=y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论中前20个IP地址出现次数"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )

    return c


def showWordcloud() -> Line:
    user_descriptions = []

    # 从CSV文件中读取用户简介数据
    with open("weiboData.csv", mode="r", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            user_descriptions.append(row[7])

    # 将所有用户简介拼接成一个字符串
    text = ' '.join(user_descriptions)

    # 创建词云
    wordcloud = (
        WordCloud(init_opts=opts.InitOpts(renderer='svg',theme="dark"))
        .add(series_name="评论用户简介", data_pair=[(word, 1) for word in text.split()], word_size_range=[10, 50])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论用户简介词云"),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .set_series_opts(
            textstyle_opts=opts.TextStyleOpts(font_size=30),  # 设置字体大小
        )
    )

    return wordcloud

def pageLayout():
    # 创建拖拽布局的页面
    page = Page(layout=Page.DraggablePageLayout)

    # 添加自定义图表函数
    page.add(
        index(),
        showFans(),
        showIp(),
        showCommentsTime(),
        showSex(),
        showTopComments(),
        showWordcloud()
    )


    # 渲染页面
    page.render("demo.html")

    # page.save_resize_html(
    #     source="custom_dashboard.html", 
    #     cfg_file="chart_config.json", 
    #     dest="final_dashboard.html")

if __name__ == "__main__":
    pageLayout()


