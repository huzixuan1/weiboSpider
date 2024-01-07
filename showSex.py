# import pandas as pd
# from pyecharts import options as opts
# from pyecharts.charts import Pie

# # 读取CSV文件
# df = pd.read_csv('./weiboData.csv')

# # 统计性别分布
# gender_distribution = df['性别'].value_counts()

# # 创建饼图
# pie_chart = (
#     Pie()
#     .add(
#         "",
#         [list(z) for z in zip(gender_distribution.index, gender_distribution.values)],
#         radius=["40%", "75%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="性别分布饼图"),
#         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )

# # 保存为HTML文件或直接显示
# pie_chart.render("gender_distribution_pie_chart.html")
# # 或者直接显示
# # pie_chart.render_notebook()


import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 读取CSV数据
df = pd.read_csv('./weiboData.csv')

# 统计性别分布
data = df['性别']
sex_counts = data.value_counts().reset_index()
sex_list = [list(sex_count) for sex_count in zip(sex_counts['index'], sex_counts['性别'])]

c = (
    Pie(init_opts=opts.InitOpts(renderer='svg'))
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
    .render("showSex.html")
)

