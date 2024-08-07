import matplotlib.pyplot as plt  # 导入matplotlib.pyplot模块，用于绘图
import matplotlib as mpl  # 导入matplotlib模块，用于设置全局参数

from shapely.geometry import Point  # 导入shapely.geometry模块中的Point类，用于创建点几何对象
# 导入shapely.geometry模块中的Polygon类，用于创建多边形几何对象
from shapely.geometry import Polygon
from geopandas import GeoDataFrame  # 导入geopandas模块中的GeoDataFrame类，用于创建地理数据框
import pandas as pd  # 导入pandas模块，用于处理数据
import numpy as np  # 导入numpy模块，用于处理数组
import geopandas as gpd  # 导入geopandas模块，用于处理地理数据
import contextily as cx  # 导入contextily模块，用于添加背景地图
import rasterio  # 加载rasterio模块，用于读写栅格数据

import osmnx as ox  # 加载osmnx模块，用于读写网格数据
import networkx as nx  # 加载networkx模块，用于处理网络数据

shanghai = gpd.read_file('/home/mw/input/stda3723/上海市.shp')
shanghai = shanghai.to_crs(epsg=3857)  # 将geodataframe对象转换为Web墨卡托投影（EPSG:3857）
shanghai.head()