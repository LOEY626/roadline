# Project North — Loey's Digital Routebook

一个适合作品集展示的交互式数字路书网站。

**路线：** 重庆北碚区兼善中学附近 → 四川段 → 甘肃段 → 兰州市七里河区
**时间：** 14天（11天徒步 + 3天公共交通接驳）
**总徒步距离：** 约350km
**每日徒步：** 25–40km

---

## 项目定位

这不是普通旅游攻略，而是一个适合作品集展示的数字路书。

- **设计风格：** 酸性超现实 (Acid Surreal) — 暗黑氖光 + 毛玻璃 + 粒子交互
- **颜色主题：** 虚空黑 #0a0a0f · 氖光品红 #ff2d78 · 电青 #00f0ff · 紫罗兰 #8b5cf6 · 冰白 #e8e8f0
- **技术栈：** 纯 HTML + CSS + JavaScript + Leaflet.js + Chart.js + Canvas 粒子网络
- **部署：** 适合 GitHub Pages / Netlify 一键部署

---

## 项目文件

| 文件 | 说明 |
|------|------|
| `index.html` | 主页面结构，包含所有章节 |
| `style.css` | 完整样式，响应式布局 |
| `script.js` | 所有数据 + 地图 + 图表 + 交互逻辑 |
| `README.md` | 本文件 |

---

## 如何本地运行

### 方式一：直接打开（推荐）

用浏览器打开 `index.html` 即可运行。无需安装任何东西。

**注意：** 由于 Leaflet.js 和 Chart.js 使用 CDN 加载，需要网络连接。

### 方式二：本地服务器

如果希望使用本地服务器（某些浏览器对 file:// 协议有限制）：

```bash
# Python 3
python -m http.server 8000

# 或者使用 Node.js
npx serve .
```

然后在浏览器中打开 `http://localhost:8000`。

---

## 如何部署到 GitHub Pages

1. 在 GitHub 上创建一个新仓库
2. 将所有文件推送到仓库
3. 进入仓库的 **Settings → Pages**
4. 在 **Source** 中选择 `main` 分支，根目录 `/`
5. 点击 **Save**
6. 等待几分钟，你的网站将在 `https://<你的用户名>.github.io/<仓库名>/` 上线

---

## 如何部署到 Netlify

1. 在 Netlify 网站点击 **Add new site → Deploy manually**
2. 将项目文件夹（包含 index.html、style.css、script.js）拖拽到上传区域
3. 等待部署完成
4. Netlify 会自动分配一个子域名，你也可以绑定自定义域名

---

## 如何替换路线数据（零基础版）

1. 用任何文本编辑器打开 `script.js`
2. 找到开头的 `const routeData` 数组（大约第20行左右）
3. 按照以下结构修改每一天的数据：

```javascript
{
  day: 1,
  type: 'walking',           // 'walking' 或 'transit'
  from: '起点名称',
  to: '终点名称',
  province: '省份',
  dist: 28,                  // 徒步距离 (km)，交通日写 0
  ascent: 320,               // 预计爬升 (m)
  hours: 6.5,                // 预计步行时间
  startCoord: [29.81, 106.43],  // 起点坐标 [纬度, 经度]
  endCoord: [30.02, 106.38],    // 终点坐标 [纬度, 经度]
  accommodation: '住宿建议',
  food: '美食搜索词',
  foodQuery: '美食搜索关键词',
  stayQuery: '住宿搜索关键词',
  risk: '风险提示',
  transitAdvice: '',         // 交通日填交通建议，徒步日留空
  photoTheme: '摄影主题',
  photoTime: '推荐拍摄时间',
  photoSuggestions: ['建议1', '建议2'],
  weather: { temp: '22~30°C', condition: '多云转晴', wind: '微风' }
}
```

### 获取坐标的方法

1. 打开 [高德地图](https://ditu.amap.com/) 或 [百度地图](https://map.baidu.com/)
2. 找到你的起点位置，右键点击
3. 选择"获取坐标"或查看 URL 中的参数
4. 注意：Leaflet 使用 [纬度, 经度] 格式（WGS84坐标系）

### 高德地图（GCJ-02）坐标转换提示

如果你使用高德地图获取的坐标（GCJ-02 坐标系），和 Leaflet 使用的 WGS-84 有细微偏移。对于路线规划示意而言，这个偏移可以忽略。

---

## 如何替换图片

`script.js` 中的 `photoData` 数组控制摄影记录部分。

如果要添加真实图片：

1. 在项目中创建一个 `images/` 文件夹
2. 将图片放入该文件夹
3. 修改 `renderPhotos()` 函数中的 `photo-placeholder`，替换为 `<img src="images/你的图片.jpg" alt="...">`

---

## 重要声明

**本路线为规划示意，不构成安全出行建议。**

实际出行前必须使用高德地图、百度地图、天气平台、住宿平台和当地交通信息逐日核验路线、住宿、隧道、施工、天气、补给与安全条件。

路线、住宿、餐饮、票务信息以对应 App 和平台实时查询为准。

海拔和爬升数据为示意，实际应以 GPS、高德、两步路、Strava 或运动手表数据为准。

---

## 功能清单

- [x] 首页 Hero（大留白、地图纹理）
- [x] 路线总览（统计卡片自动计数动画）
- [x] 交互地图（Leaflet.js + OpenStreetMap）
- [x] 每日行程卡片（含天气、风险、住宿、美食）
- [x] 滚动联动地图高亮
- [x] 数据可视化（Chart.js 四个图表）
- [x] 徒步进度条（滚动联动）
- [x] 摄影记录（带设备标签和占位卡片）
- [x] 装备清单（accordion 折叠 + localStorage 保存勾选）
- [x] 路餐计划
- [x] 安全指南
- [x] 总结页
- [x] 底部固定导航栏（移动端）
- [x] 返回顶部按钮
- [x] 沉浸淡入动画
- [x] GPS 轨迹动画
- [x] 外部跳转按钮（高德地图、12306、携程、大众点评等）
- [x] 移动端适配
- [x] 响应式布局

---

## 技术栈

| 技术 | 用途 |
|------|------|
| HTML5 | 页面结构 |
| CSS3 | 样式、动画、响应式布局 |
| JavaScript (ES6+) | 所有交互逻辑 |
| Leaflet.js | 交互式地图 |
| OpenStreetMap | 地图瓦片 |
| Chart.js | 数据可视化图表 |
| localStorage | 装备清单勾选状态持久化 |

---

## 许可证

本项目为个人作品集用途。路线数据为模拟示意，不构成任何形式的出行建议。

---

*向北走，慢慢走。*
