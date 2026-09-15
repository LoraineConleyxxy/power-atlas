# 诸界力量图鉴 · _自用力量体系

密教、COC、DND 与战锤 40K 的交互展示页。

**访问：https://loraineconleyxxy.github.io/power-atlas/**

**v1.18 战锤审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.18.html#warhammer-level-6**

**DND 审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.18.html#dnd-level-55**

**COC 人类审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.18.html#coc-level-21**

**COC 眷族审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.18.html#coc-level-34**

**COC 神祇审查入口：https://loraineconleyxxy.github.io/power-atlas/review-v1.18.html#coc-level-93**

v1.18 重建战锤目录：10个种族／存在分类、44条道路、134个原职级或具体身份。采用“种族 → 道路 → 职级／身份”点选，每项含明确战斗力短句、职责与五项能力参考。阿斯塔特采用侦察兵、战斗兄弟、老兵、军士、副连长、连长、战团长；其他道路使用自身的职级或专业身份。配套快速回复v1.6。

v1.17 已核对全部320项身份、59件器物和6项兼容旧身份：正文首行统一明确显示【战斗力】，网页完整保留首行，发布时核对全部条目。

v1.15 将 DND 每个职业阶段整理为五项代表技能，明确仅作能力参考；高阶换出部分基础技能，增强具体攻防、穿透、追索、移动与持续承压表现。每个身份继续明确显示【战斗力】短句。

v1.11 新增93条 COC 非人身份：18种眷族的54个层次、5个特殊个体、20位神祇本体与14个有名化身。连同34个人类身份，COC共127项。网页可按人类、眷族、神祇筛选，再查看具体种类、神名与完整发送正文。配套快速回复v1.4。

DND 按九大种族 → 十二职业 → 七档等级点选，共 756 种身份组合。初阶爆墙、进阶爆楼、高阶爆街、大师爆城、传奇爆国、史诗爆星、神话恒星；同档采用统一攻防定义。种族与职业保留简短提示，十二职业每档展示五项参考技能，随阶段换入成熟手段，高阶描述按当前量级增强。演绎承接 DND 知识与人物设定，页面可选择种族并查看完整发送正文。

COC 人类收录学者、侦探、神话巫师、时空术士、死灵术士、幻梦术士六条路线，共34个身份。四条施术路线大师阶爆星、深层阶恒星。COC 身份详情可查看当前单项关键词发送给 AI 的完整正文，目录标出人类、眷族与神祇。

密教的十三相共52个等级身份，另有21位已有司辰，连同33项器物均有逐项正文。v1.9 补充了十三相的 39 种通晓者、长生者、具名者与另外 12 相司辰，刃之司辰保留已有完整正文。各等级展开感知、技艺、交锋、庇护、全力场景与日常关系。页面显示内容版本和更新时间，返回页面时会检查新版；密教详情中的“查看发送给 AI 的正文”按当前单项关键词列出相应正文。

- 按体系、职业、等级、道具类别与量级浏览，支持文字搜索。
- 查看等级或道具的完整说明及相关原作资料。
- 逐项复制关键词，或组合一项身份、多个道具和量级后一起复制。
- 下载最新的单一合并世界书和快速回复。
- 页面无第三方脚本、无追踪、无在线依赖；下载 `index.html` 后可离线使用。

四体系的全部身份采用量级短句，通用尺度、攻防与配套规则集中到常驻总表。DND 删除重复的独立战斗力段落，其他体系的具体施力与战斗场景继续保留。

## 更新展示内容

仅需 Python 标准库。将最新版成品文件作为输入：

```sh
python3 build.py --worldbook path/to/_自用力量体系.json --quickreply path/to/_自用力量体系_快速回复_v1.6.json
```

提交生成的 `index.html` 和 `downloads/` 中的最新版文件。GitHub Pages 从 `main` 分支根目录发布，无前端构建依赖。

构建同时生成 `release.json` 与一个版本专属的 `review-v*.html`，将它们一并提交，以便刷新和版本审查。目录仅保留最新审查页。

世界书导入 SillyTavern 的世界书界面；快速回复导入快速回复扩展。启用 ST-Prompt-Template 处理世界书中的模板。页面复制的关键词须发送到聊天中生效。

量级沿用当前世界书的默认配置。剧情中的实际条件、消耗、角色选择和另行指定的量级仍适用。

## 内容与授权

这是非官方的个人整理项目，各作品名称和设定归原权利人。作品资料沿用世界书内标明的原作、规则与资料出处。DND 内容按下列授权提供；中文内容进行了翻译、节选与演绎适配。

This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.

其余内容未附统一开放许可。

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.
