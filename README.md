# 海外独角兽微信封面 Skill

把一张选好的图片，加上关键词或公司 Logo，生成一套可继续编辑的海外独角兽微信封面：

- 公众号横图：900 × 383（2.35:1）
- 方形小图：900 × 900（1:1）
- 横图与方图组合预览：1307 × 383
- 三种图片对应的 2× 高清版本
- 可编辑的 Figma 图层与直接访问链接

这个 Skill 固定品牌与交付标准，但不固定构图模板。它会先识别素材中的主体、留白、方向、文字、材质与光影，再决定采用裁剪、延展画布、移动主体或拆分重组。

## 固定规则与自适应决策

| 固定规则 | 每张素材单独判断 |
| --- | --- |
| 三种输出尺寸及 2× 高清版 | 主体如何裁剪、分离和重组 |
| 海外独角兽白色 Logo | 横图与方图是否使用不同构图 |
| 关键词或公司 Logo 居中 | 主体的大小、位置与层次 |
| 中央内容统一视觉尺度 | 背景延展、留白和局部明暗 |
| 默认黑/白文字，可指定强调色 | 是否需要对角、左右或非对称构图 |
| 保留原图风格与所有敏感细节 | 如何消除蒙版接缝并保持高级感 |

## 安装

把本仓库中以下目录作为 Codex Skill 安装：

```text
skills/haiwai-wechat-cover
```

也可以直接把该目录的 GitHub 链接发给 Codex，并说：

```text
请安装这个 GitHub 链接里的 haiwai-wechat-cover Skill。
安装后，用它处理我接下来上传的图片。
```

安装完成后，在下一轮对话中调用：

```text
使用 haiwai-wechat-cover。
素材：见附件。
中心关键词：Agent Identity。
除非我另外指定，文字颜色根据背景自动选择。
请输出横图、方图、组合图、2× 高清版和 Figma 链接。
```

更完整的输入格式见 [examples/request.example.yaml](examples/request.example.yaml)。

## 运行要求

- Codex 或兼容的 Skill 运行环境
- Python 3 和 Pillow
- 已连接并具备编辑权限的 Figma MCP
- 一个可写入的 Figma Design 文件

每位使用者都需要提供自己的可编辑 Figma Design 链接。公开版不包含任何私人或固定工作区地址。

## 仓库结构

```text
.
├── README.md
├── BRAND-ASSET-NOTICE.md
├── docs/
│   ├── one-shot-guide.md
│   └── website-integration.md
├── examples/
│   └── request.example.yaml
└── skills/
    └── haiwai-wechat-cover/
        ├── SKILL.md
        ├── agents/
        ├── assets/
        ├── references/
        └── scripts/
```

## 网站接入

Skill 适合先验证视觉规则；生产网站不应依赖手工复制 Figma 操作。建议把它拆为：

1. 素材分析与版式规划；
2. 确定性的高清渲染服务；
3. 可选的 Figma 编辑副本；
4. 文件存储与下载。

具体接口与迁移方案见 [docs/website-integration.md](docs/website-integration.md)。

## 品牌资产

代码、规则与品牌 Logo 的授权范围可能不同。发布或二次分发前请阅读 [BRAND-ASSET-NOTICE.md](BRAND-ASSET-NOTICE.md)。
