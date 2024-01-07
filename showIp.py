
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

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
    Map(opts.InitOpts(width='1200px', height='600px',renderer='svg'))
    .add("comments", city_counts_list, "china", is_map_symbol_show=False,name_map=name_map)
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}"),
        tooltip_opts=opts.TooltipOpts(formatter="{a}: {c}")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("mapComments.html")
)