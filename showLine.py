
import csv
from pyecharts import options as opts
from pyecharts.charts import Line
from collections import Counter
from datetime import datetime

def count_comments_by_date(csv_filename):
    comment_dates = []

    # 从CSV文件中读取评论发布时间数据
    with open(csv_filename, mode="r", encoding="utf-8-sig") as csvfile:
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
    line = (
        Line(init_opts=opts.InitOpts(renderer='svg'))
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

    line.render("showCommentsTime.html")

count_comments_by_date('./weiboData.csv')
