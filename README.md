# 🎈 弹幕推送客户端 (适用于 OK影视/Fongmi影视/TVbox)

这是一个基于原生 JavaScript 编写的轻量级单页面 Web 客户端。本项目配合开源的弹幕 API 服务器（如 `huangxd-/danmu_api`）使用，旨在为局域网内的“OK影视”播放器提供一键式的弹幕搜索、解析与推送服务。
<p align="center"><img src="https://cdn.jsdelivr.net/gh/Meroser/TVbox_danmu@main/img/picture (1).png"></p>

<p align="center"><img src="https://cdn.jsdelivr.net/gh/Meroser/TVbox_danmu@main/img/picture (2).png"></p>

<p align="center"><img src="https://cdn.jsdelivr.net/gh/Meroser/TVbox_danmu@main/img/picture (3).png"></p>

<p align="center"><img src="https://cdn.jsdelivr.net/gh/Meroser/TVbox_danmu@main/img/picture (4).png"></p>


## ℹ️ 更新内容
1. **支持从电视机获取当前播放节目，搜索弹幕更便捷**
2. **支持搜索历史记录**
3. **页面展示优化**

## ✨ 核心特性

* 🚀 **极简部署，开箱即用**：纯 HTML + CSS + JS 打造的单文件应用。无需 Node.js 环境，无需 `npm install`，没有任何外部框架依赖，双击 `html` 文件即可直接在浏览器运行。
* 🔍 **智能搜索与数据净化**：支持番剧/影视关键字搜索。内置强大的正则过滤逻辑，自动剔除接口返回的冗余平台后缀（如 `【电视剧】from tencent`）和剧集前缀（如 `【qq】`），还你最清爽的阅读体验。
* 🏷️ **多源聚合与精美分组**：当一部剧集存在多个播放源时，系统会自动按照配置的优先级（如腾讯、爱奇艺、优酷等）进行分类聚合，并配以精美的专属平台 Logo。
* 📺 **一键直推电视端**：直接调用 OK影视 的本地 HTTP 接口，在手机或电脑上点击对应的集数，即可瞬间将弹幕文件（XML）推送到电视屏幕上。
* ⚙️ **人性化配置面板**：内置可视化的接口设置弹窗，支持一键“测试连通性”，避免填错地址。配置数据自动缓存在本地（LocalStorage），下次打开无需重复输入。
* 📱 **全平台响应式设计**：精心打磨的现代化 UI 界面，完美适配电脑宽屏、平板和手机竖屏。

## 🛠️ 准备工作

在使用本客户端之前，您需要准备好以下两项基础服务：

1.  **弹幕 API 服务**：部署好弹幕 API 后端程序（如 `huangxd-/danmu_api`），获取其访问地址和 Token（例如：`http://192.168.1.10:9321/87654321`）。
2.  **OK影视客户端**：确保您的电视/机顶盒上已安装并运行“OK影视”，并获取其局域网控制地址（例如：`http://192.168.1.20:9978`）。

## 📖 使用指南

1.  **下载/克隆项目**：将本项目中的 `.html` 文件（如 `push_danmu.html`）以及 `danmu_logo` 文件夹下载到本地或上传到您的静态 Web 服务器（如群晖 Web Station、Nginx 等）。
2.  **打开网页**：在浏览器中打开该 HTML 文件。
3.  **配置接口**：
    * 首次打开会自动弹出**设置窗口**（或点击右上角“⚙️ 设置”）。
    * 在“弹幕API完整地址”中填入您的 API 地址（含 Token）。
    * 在“OK影视完整地址”中填入电视端的 IP 和端口。
    * 点击“测试”按钮确保网络畅通，然后点击**保存配置**。
4.  **搜索与推送**：
    * 在搜索框输入影视名称（如：生万物）并回车。
    * 在搜索结果中点击想看的影视剧卡片。
    * 在剧集列表中，找到对应平台的集数，点击按钮即可完成推送！

## 🎨 进阶自定义 (修改排序与 Logo)

如果您想调整搜索结果的显示顺序，或者替换平台的 Logo 图片，只需用文本编辑器打开 `html` 文件，找到 `<script>` 标签开头的 `SOURCE_CONFIG` 变量进行修改即可：

```javascript
const SOURCE_CONFIG = {
    // 1. 平台数据映射定义 (修改名称或图片路径)
    "source_data": {
        "tencent": { "name": "腾讯视频", "logo": "./danmu_logo/tencent.png" },
        "iqiyi": { "name": "爱奇艺", "logo": "./danmu_logo/iqiyi.png" },
        // ... 添加或修改你的平台
        "default": { "name": "其他", "logo": "./danmu_logo/default.png" }
    },
    // 2. 搜索结果与剧集的分组排序优先级 (越靠前优先级越高)
    "order": ["tencent", "youku", "iqiyi", "imgo", "bilibili", "renren", "360", "vod"]
};
```

## ⚠️ 免责声明

本项目仅供个人学习、技术研究与局域网内交流使用。请勿将本项目用于任何商业用途或非法用途。使用者因使用本项目所产生的任何问题或法律责任由使用者自行承担。
