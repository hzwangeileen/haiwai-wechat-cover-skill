# 网站接入方案

## 目标

把 Skill 中已经验证的视觉规则迁移到排版工具网站，减少人工重复操作，同时保留 Figma 作为可选的编辑出口。

## 推荐架构

```text
用户上传素材
    ↓
素材分析与风险检测
    ↓
版式规划器输出结构化 Layout JSON
    ↓
确定性渲染服务生成 2× 主文件
    ↓
下采样生成标准版
    ↓
文件下载 + 可选 Figma 副本
```

### 素材分析

输出以下信息：

- 主体及其边界；
- 必须完整保留的文字、Logo、图表和产品；
- 可分离元素；
- 推荐留白区域；
- 主色、背景边缘色和中心对比度；
- 原始分辨率是否足够。

### Layout JSON

渲染器只接受经过约束的结构化数据，避免直接执行模型生成的任意代码。

```json
{
  "canvas": {"width": 1800, "height": 766},
  "background": {"type": "solid", "color": "#F2F2F2"},
  "subjects": [
    {
      "assetId": "work-badge",
      "x": 56,
      "y": 4,
      "width": 522,
      "height": 760,
      "fit": "contain"
    }
  ],
  "centerContent": {
    "mode": "keyword",
    "text": "Agent Identity",
    "fontFamily": "Alegreya",
    "fontStyle": "ExtraBold",
    "color": "#111111",
    "maxWidth": 576,
    "maxHeight": 138
  },
  "brandLogo": {
    "assetId": "haiwai-unicorn-white",
    "width": 162,
    "position": "top-right"
  }
}
```

所有坐标以 2× 主文件为准。标准文件由同一主文件高质量下采样生成，避免两套版式产生偏差。

## 建议接口

```text
POST /api/covers
Content-Type: multipart/form-data

source_image
center_mode=keyword|company_logo
keyword
company_logo
highlights
figma_file_url
```

返回：

```json
{
  "status": "completed",
  "files": {
    "landscape": "...",
    "square": "...",
    "combined": "...",
    "landscape2x": "...",
    "square2x": "...",
    "combined2x": "..."
  },
  "figma": {
    "workspace": "...",
    "landscapeFrame": "...",
    "squareFrame": "...",
    "combinedFrame": "..."
  },
  "font": {
    "requested": "Albertus Nova",
    "used": "Alegreya ExtraBold",
    "fallback": true
  }
}
```

## 渲染建议

- 服务端使用支持高质量重采样和透明图层的图形库；
- 字体、Logo 和输出尺寸放入版本化品牌配置；
- 上传素材与生成文件使用有时效的私有地址；
- 对人脸、产品、Logo、图表和截图禁用生成式重绘；
- 保存 Layout JSON，使同一结果可以重新渲染和审计；
- 先渲染 2× 主文件，再下采样到标准尺寸；
- Figma 作为可选编辑出口，不能成为生产下载链路的单点依赖。

## 从 Skill 迁移到网站

1. 先把 `references/design-principles.md` 转成版式规划器约束；
2. 把 `references/layout-spec.md` 转成服务端校验规则；
3. 把 `scripts/prepare_image.py` 的裁剪、透明边界和多边形蒙版能力迁移到渲染服务；
4. 增加 Layout JSON 的 schema 校验；
5. 用一组不同风格素材建立回归测试；
6. 最后再接入排版工具的登录、存储和 Figma 授权。
