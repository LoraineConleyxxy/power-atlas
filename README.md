# 诸界力量图鉴 · _自用力量体系

密教、COC、DND 与战锤 40K 的交互展示页。

**访问：https://loraineconleyxxy.github.io/power-atlas/**

**v1.9 审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.9.html#occult-level-16**

密教的 52 个身份与 33 项器物均有逐项正文。v1.9 补充了十三相的 39 种通晓者、长生者、具名者与另外 12 相司辰，刃之司辰保留已有完整正文。各等级展开感知、技艺、交锋、庇护、全力场景与日常关系。页面显示内容版本和更新时间，返回页面时会检查新版；密教详情中的“查看发送给 AI 的正文”按当前单项关键词列出相应正文。

- 按体系、职业、等级、道具类别与量级浏览，支持文字搜索。
- 查看等级或道具的完整说明及相关原作资料。
- 逐项复制关键词，或组合一项身份、多个道具和量级后一起复制。
- 下载最新的单一合并世界书和快速回复。
- 页面无第三方脚本、无追踪、无在线依赖；下载 `index.html` 后可离线使用。

## 更新展示内容

仅需 Python 标准库。将最新版成品文件作为输入：

```sh
python3 build.py --worldbook path/to/_自用力量体系.json --quickreply path/to/_自用力量体系_快速回复_v1.2.json
```

提交生成的 `index.html` 和 `downloads/` 中的最新版文件。GitHub Pages 从 `main` 分支根目录发布，无前端构建依赖。

构建同时生成 `release.json` 与一个版本专属的 `review-v*.html`，将它们一并提交，以便刷新和版本审查。目录仅保留最新审查页。

世界书导入 SillyTavern 的世界书界面；快速回复导入快速回复扩展。启用 ST-Prompt-Template 处理世界书中的模板。页面复制的关键词须发送到聊天中生效。

量级沿用当前世界书的默认配置。剧情中的实际条件、消耗、角色选择和另行指定的量级仍适用。

## 内容与授权

这是非官方的个人整理项目，各作品名称和设定归原权利人。作品资料沿用世界书内标明的原作、规则与资料出处。DND 内容按下列授权提供；中文内容进行了翻译、节选与演绎适配。

This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.

其余内容未附统一开放许可。
