
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

# 读取CSV数据
df = pd.read_csv('./weiboData.csv')

# 处理粉丝数（以“万”为单位的情况）
df['粉丝数'] = df['粉丝数'].apply(lambda x: float(x.replace('万', '')) * 10000 if '万' in str(x) else float(x))

# 选择粉丝数前20的用户
top20_users = df.nlargest(20, '粉丝数')


c = (
    Bar(init_opts=opts.InitOpts(renderer='svg'))
    .add_xaxis(list(top20_users['评论用户名']))
    .add_yaxis("粉丝数", list(top20_users['粉丝数']))
    .add_yaxis("关注数", list(top20_users['关注人数']))
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="评论用户粉丝前20情况"))
    .render("fans.html")
)

