<div align="center">

<img src="images/cover.png" alt="cover" width="820"/>

<br/>

# awesome-chenhansheng-skill

## 🔥 把 342 万字小说，蒸馏成 45 个可执行的人际判断维度

<br/>

> **35 岁成功商人重生回 18 岁。**
> 他用成年人的阅历，在年轻人的躯体里降维打击。
> 递一根烟，是社交。沉默五秒，是威慑。永远不表白，是策略。
> 这些"不明说但实际就是为人处世"的细节，我们全挖出来了。

<br/>

![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-WorkBuddy%20Skill-green.svg?style=for-the-badge)
![Source](https://img.shields.io/badge/Source-342万字-red.svg?style=for-the-badge)
![Dimensions](https://img.shields.io/badge/Dimensions-45-orange.svg?style=for-the-badge)
![AI](https://img.shields.io/badge/AI%20语气模仿-已启用-purple.svg?style=for-the-badge)
![Compatible](https://img.shields.io/badge/支持-Claude%20Code%20%7C%20Cursor%20%7C%20OpenCode%20%7C%20Trae-blueviolet.svg?style=for-the-badge)

<br/><br/>

</div>

---

## ⚡ 30 秒看懂这个项目

```
📖 一本 342 万字的小说《我真没想重生啊》
🔬 系统蒸馏主角陈汉升的社交智慧 + 恋爱策略 + 说话艺术
🎯 45 个维度：具体场景 + 跨场景判断 + 可复用动作
🤖 AI 加载后能用陈汉升的语气和你对话，不是分析报告，是角色附体
```

<br/>

> **这不是读书笔记。**
> 这是从 101,846 行原文里，用 6 个并行搜索引擎 + 精确 Grep 深挖，
> 把一个虚构角色的社交 DNA 提取出来，变成你装上就能用的 AI 技能。

---

## 💥 三大主题，一眼看完

<table>
<tr>
<td width="33%" align="center" valign="top">

<img src="images/social-skills.png" alt="为人处世" width="100%"/>

### 🍶 为人处世篇

**10 个维度 · 隐含细节深挖**

递烟不是给烟，是给面子。
敬酒不是喝酒，是权力游戏。
沉默不是无话可说，是让对方自己脑补。

</td>
<td width="33%" align="center" valign="top">

<img src="images/romance.png" alt="恋爱技巧" width="100%"/>

### 💘 恋爱技巧篇

**10 个维度 · 差异化策略**

傲娇型用推拉制造张力，
温柔型用陪伴制造依赖。
永远别正式表白——
做男朋友该做的事，别说男朋友该说的话。

</td>
<td width="33%" align="center" valign="top">

<img src="images/language-style.png" alt="语言风格" width="100%"/>

### 🗣️ 语言风格模仿

**7 个子节 · AI 角色附体**

"老子""嘿嘿""狗日的"
7 种笑法 = 7 种社交策略
对兄弟粗暴，对长辈恭敬，对女生一本正经胡说八道
AI 不只是分析，是用他的语气跟你说话

</td>
</tr>
</table>

---

## 🗣️ 文字语气契约：先把话说得像，再谈说得对

以前这 27 条更像“陈汉升会怎么做”的分析资料。现在 `SKILL.md` 最前面新增了**角色文字语气契约**，优先级高于所有策略：

- 先判断对象和场面，再开口；先给一句短判断，再补一个关键理由。
- 一句只说一个意思。用户问“怎么说”，先给能直接说出口的话。
- 口头禅低频使用。一条回复最多一个“老子 / 嘿嘿 / 妈的”或一个动作。
- 不默认写“首先 / 其次 / 综上 / 值得注意的是 / 希望对你有帮助”。
- 不把每段都写成标题、清单和总结框，也不强行凑“三点建议”。
- **默认只输出对话**。用户没点名要分析或报告时，就先像真人开口，简单问题一两句，情绪问题三到五句。
- 对方真难受时立刻收笑话；涉及伤害、违法或明显不对等关系时，不为了像角色而给危险建议。

更细的说话机制在 [`references/text-tone-atlas.md`](references/text-tone-atlas.md)：短句骨架、口头词触发条件、七类说话动作、对象语气切换和“人机味”黑名单。另有 [`references/text-tone-examples.md`](references/text-tone-examples.md) 的 12 组合成文字语气标定样例，覆盖职场抢功、临时加活、借钱、劝酒、甩锅、被夸、消息变慢、求助、拒绝、冷战、催婚和探工资。它们不是原文摘抄，专门用来校准“怎么起句、哪里停、什么时候少解释”。

有工具权限时，发送前可用 `python scripts/check_reply_style.py draft.txt` 扫描报告腔、标题清单、AI 自指、连续口头禅和超长句。退出码为 `0` 才表示通过。

**普通 AI 回答**

> 单次回复速度不能直接说明关系状态，需要结合整体互动频率判断……

**陈汉升式回答**

> 慢就是慢，别自己给她编十个理由。
>
> 你先看两件事：她回得少，是不是只对你少；她不见面，是不是一直都见不着。真忙，你催也没用；真想躲，你越问越难看。
>
> 把自己日子过起来。喜欢不是盯出来的。

---

## 🎯 45 个维度全览

### 🍶 为人处世（你不会在教科书里学到的）

| # | 维度 | 一句话暴击 |
|---|------|-----------|
| 1.1 | **递烟** | 递烟方向永远向下和向外——向上递叫巴结，向下递叫格局 |
| 1.2 | **敬酒** | 对不能喝的宽容收人心，对能喝的用酒量压制立威 |
| 1.3 | **打电话** | 称呼从"陈汉升"变"汉升"=信任升级，这是最敏感的社交信号 |
| 1.4 | **沉默** | 盯着对方不说话 5 秒 = 最强威慑，别人吵架时沉默+干活 = 最高级调停 |
| 1.5 | **给台阶** | 不抢剪刀，引导对方自己放下——"放在哪里都无所谓，只要别拿在手上" |
| 1.6 | **帮忙** | 主动发现需求不等开口，帮完让第三方传话不自己表功 |
| 1.7 | **说话艺术** | 自嘲降防 → 玩笑传话 → 第三方施压 → 反问引导 → 承诺留余地 |
| 1.8 | **金钱观** | 小钱大方买人心，大钱谨慎做利益，买饼时强行要杯果汁给女生 |
| 1.9 | **个人品牌** | 头衔堆叠快速建认知，自嘲消解嫉妒，主动干脏活 = 最低成本最高声望 |
| 1.10 | **危机处理** | 每步套法律外衣，先分化对方联盟再逐个击破，脏活外包+合理推诿 |

### 💘 恋爱技巧（书上不会教，但人人想知道的）

| # | 维度 | 一句话暴击 |
|---|------|-----------|
| 2.1 | **差异化策略** | 萧容鱼(傲娇)用推拉制造张力，沈幼楚(温柔)用陪伴制造依赖 |
| 2.2 | **推拉技巧** | 推 2 次拉 3 次，推时说到痛处，拉时做到实处，最佳拉的时刻是对方情绪最高涨时 |
| 2.3 | **情感债务** | 经济→物质→家庭→日常→公开，层层递进，买手机只存一个号码 = 情感垄断 |
| 2.4 | **嫉妒制造** | 不主动暧昧，让目标"偶然发现"别人对你有意思但你不回应 |
| 2.5 | **表白禁忌** | 永远不在关系未定时正式表白，用行为代替语言建立事实关系 |
| 2.6 | **安全感** | 关键时刻一定在 + 日常琐事持续在，吹蜂蜜水比 999 朵玫瑰有效 |
| 2.7 | **双线管理** | 空间隔离 + 时间切割 + 信息防火墙，提前存储"甜蜜记忆"做保险 |
| 2.8 | **冷战破解** | 不讲道理用幽默降维，破冰理由要"不可证伪"（梦、感觉、路过） |
| 2.9 | **伤口政治学** | 故意不处理伤口 = 不追究也不原谅，让愧疚自动累积 |
| 2.10 | **权力让渡** | 给钱是施舍，给权是信任，同时给两方 = 制造利益共同体 |

### 🗣️ 语言风格模仿（让 AI 变成他，而不是分析他）

| # | 子节 | 亮点 |
|---|------|------|
| 3.1 | **口头禅** | "老子""嘿嘿""妈的""狗日的"——粗话只对兄弟说，对长辈切回"我" |
| 3.2 | **7 种笑法** | 嘿嘿=得意 · 淡淡=装逼 · 咧嘴=收获信号 · 笑嘻嘻=忽悠 · 温柔笑=对沈幼楚专用 |
| 3.3 | **语气切换** | 对兄弟粗暴直接 · 对长辈恭敬关心 · 对傲娇女调侃胡说 · 对温柔女霸道哄 · 对对手平淡审视 |
| 3.4 | **说话节奏** | 短句为主 · 先结论后理由 · 反问当武器 · 一本正经胡说八道 |
| 3.5 | **动作配合** | 弹烟头=做决定 · 咳嗽一声=翻篇 · 搂脖子=拉近 · 挑眉毛=挑战 |
| 3.6 | **称呼体系** | 当面 vs 背后称呼表，称呼变化 = 关系温度计 |
| 3.7 | **对话校准示例** | 短对话示范，用陈汉升的语气直接回答真实问题 |

---

## 🧩 28–45：跨场景补充技巧库

原有 27 条偏具体场景，新增 18 条负责拆解“先看什么、再做什么、哪里停”：

| # | 技巧 | 核心动作 | 边界 |
|---:|---|---|---|
| 28 | **关系位阶** | 先找决定权、面子和承压点，再决定怎么说 | 尊重不等于卑躬屈膝 |
| 29 | **场域切换** | 公开保面子，私下谈条件，正式事项留痕 | 不用双面话欺骗第三方 |
| 30 | **面子账** | 给体面退路，让对方自己转向 | 不替错误和越界兜底 |
| 31 | **第三方杠杆** | 借规则、领导、长辈或群体先例施压 | 不捏造第三方意见 |
| 32 | **信息边界** | 只说决定所需信息，该留证据的留下 | 安全、合同、重大利益必须披露 |
| 33 | **资源交换** | 找双方都能接受的交换点，再谈顺序 | 不用虚假筹码和胁迫 |
| 34 | **求助闭环** | 请求、理由、期限、拒绝台阶一次说清 | 被拒绝一次可以换理由，不死缠 |
| 35 | **帮人到底** | 多做半步、结果闭环、帮完退出 | 帮忙不是购买控制权 |
| 36 | **饭局分工** | 召集人定目的，陪客照顾弱项，结束确认返程 | 不逼酒，不做危险测试 |
| 37 | **点菜与买单** | 先问忌口预算，提前处理买单 | 不当众压人，不长期绑定人情 |
| 38 | **入场与退场** | 先找主人和关键人，离场交代后续 | 礼数不是表演 |
| 39 | **预期管理** | 给范围、条件和明确回信时间 | 不用模糊承诺拖住别人 |
| 40 | **冲突分层** | 原则留证据，面子给台阶，情绪先降温 | 越界行为必须明确制止 |
| 41 | **情绪止损** | 反复解释无效应停止加码，拉回距离和规则 | 不用失联制造焦虑 |
| 42 | **行动闭环** | 谁做、何时做、何时反馈，全部落成动作 | 不把责任全揽到自己身上 |
| 43 | **称呼温度** | 从称呼变化判断关系距离 | 不故意制造暧昧 |
| 44 | **标签重述** | 换一个不触发防御的价值框架 | 不造假、不夸大履历 |
| 45 | **利益共同体** | 先说共同结果，再分角色和责任 | 不拉帮结派、不制造敌人 |

调用时按场景选 1–2 条，不要一次堆满 18 招。技巧是为了让你说人话，不是让你变成话术机器。

---

## 🎬 效果展示

### 场景一：饭局敬酒

<table>
<tr>
<td width="50%" align="left">

**👤 用户问：**

帮我分析一下饭局上怎么敬酒

</td>
<td width="50%" align="left">

**🤖 陈汉升式回复：**

敬酒这事，说简单也简单。

你记住一个原则——**对不能喝的人宽容，对能喝的人亮剑**。不能喝的，你让他端茶碰杯，他心里记你好；能喝又爱闹腾的，你连干六杯放倒他，他服你。

敬酒顺序也别乱来。先敬桌上最大的——领导、长辈，表示尊重；再跟同辈互敬，表示平等；最后集中火力对付刺头，展示实力。

还有个万能句式——"我干了您随意"。把自己放低，把对方抬高，但实际效果呢？对方不好意思也得干了。

哦对了，杯沿比对方低一点就行，低太多那是谄媚。**低三寸是服了，低一寸是尊重，自己掂量。**

</td>
</tr>
</table>

### 场景二：恋爱困惑

<table>
<tr>
<td width="50%" align="left">

**👤 用户问：**

喜欢的女生对我忽冷忽热怎么办

</td>
<td width="50%" align="left">

**🤖 陈汉升式回复：**

嘿嘿，这事儿吧，你得先搞清楚她是什么性格。

要是傲娇型的——她忽冷忽热，你也忽冷忽热。但记住，**推两次拉三次**。推的时候说到痛处，拉的时候做到实处。她气到要咬人的时候，你别还手——这就是拉。她平静的时候你拉，效果减半。

要是温柔型的——别搞这些虚的。直接高频出现，买早餐、接送、帮她干活。让她习惯你在身边，习惯了你就是她的安全感。有一天你不在了，她才发现离不开你。

还有一点——**永远别正式表白**。做男朋友该做的事，别说男朋友该说的话。你一说"做我女朋友"，主动权全到她手里了。不说，她还没法拒绝你。

</td>
</tr>
</table>

---

## 🧠 核心心法

<div align="center">

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   社交公式                                               │
│   观察需求 → 主动出击 → 超预期交付                       │
│   → 让第三方传播 → 不邀功 → 收获信任                     │
│                                                         │
│   恋爱公式                                               │
│   价值建立 → 差异化策略 → 高频存在                       │
│   → 制造情感债务 → 回避正式确认 → 用行为建立事实关系      │
│                                                         │
│   说话公式                                               │
│   自嘲降防 → 玩笑传话 → 第三方施压                       │
│   → 反问引导 → 承诺留余地                                │
│                                                         │
│   终极心法                                               │
│   1. 阅历是最好的武器                                    │
│   2. 永远不要让对方觉得你在"用技巧"                       │
│   3. 做人留一线，日后好相见                               │
│   4. 钱是社交润滑剂，不是社交目的                         │
│   5. 沉默和行动永远比语言有效                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

</div>

---

## 👤 适合谁用

| 人群 | 你会得到什么 |
|------|------------|
| 🎓 **大学生** | 宿舍关系、社团社交、追女生的实操指南 |
| 💼 **职场新人** | 饭局敬酒、跟领导打交道、说话艺术 |
| 🤖 **AI 技能开发者** | 一个完整的"角色附体型"技能范本 |
| 📖 **小说爱好者** | 从全新角度重读《我真没想重生啊》 |
| 🧠 **情商提升者** | 45 个维度：27 个场景拆解 + 18 个跨场景判断 |

---

## 🚀 安装

### 📦 一键安装脚本（全平台）

```bash
# 克隆仓库
git clone https://github.com/yan-stone-computer/awesome-chenhansheng-skill.git
cd awesome-chenhansheng-skill

# 选择你要配置的智能体，运行对应脚本
bash scripts/install.sh --workbuddy     # WorkBuddy
bash scripts/install.sh --claude-code   # Claude Code
bash scripts/install.sh --cursor        # Cursor
bash scripts/install.sh --opencode      # OpenCode
bash scripts/install.sh --trae          # Trae
bash scripts/install.sh --all           # 全部安装
```

### 🛠️ 支持全部主流 AI 智能体

本仓库为 **6 种主流 AI 智能体**提供了开箱即用的配置，每个工具的配置文件都放在 `configs/` 目录下：

| 智能体 | 配置文件格式 | 配置文件位置 | 生效范围 |
|--------|------------|------------|---------|
| **WorkBuddy** | `SKILL.md` | `~/.workbuddy/skills/chen-hansheng-wisdom/` | 所有项目 |
| **Claude Code** | Agent Skills 标准 `SKILL.md` | `~/.claude/skills/chen-hansheng-wisdom/` | 所有项目 |
| **Cursor** | `.mdc` 规则 | `.cursor/rules/chen-hansheng-wisdom.mdc` | 当前项目 |
| **OpenCode** | `AGENTS.md` | 项目根目录 `AGENTS.md` | 当前项目 |
| **Trae** | `.md` 规则 | `.trae/rules/chen-hansheng-wisdom.md` | 当前项目 |
| **通用** | 纯 Markdown | 任意位置，手动加载 | 手动 |

---

### 🟦 方式一：WorkBuddy（推荐）

> 本技能的原始平台，完整支持 45 个维度 + 角色文字语气契约

```bash
mkdir -p ~/.workbuddy/skills/chen-hansheng-wisdom
cp SKILL.md ~/.workbuddy/skills/chen-hansheng-wisdom/SKILL.md
```

重启 WorkBuddy 后，对话中提到这些关键词即可触发：
> 为人处世 · 社交技巧 · 恋爱技巧 · 说话艺术 · 情商 · 饭局 · 敬酒 · 递烟 · 追女生 · 撩妹

---

### 🟠 方式二：Claude Code

> 遵循 **Agent Skills 开放标准**，`SKILL.md` 格式与 Claude Code 原生兼容

**个人级（所有项目生效）：**
```bash
mkdir -p ~/.claude/skills/chen-hansheng-wisdom
cp configs/claude-code/SKILL.md ~/.claude/skills/chen-hansheng-wisdom/SKILL.md
```

**项目级（当前项目生效）：**
```bash
mkdir -p .claude/skills/chen-hansheng-wisdom
cp configs/claude-code/SKILL.md .claude/skills/chen-hansheng-wisdom/SKILL.md
```

**使用方式：**
- 自动触发：描述匹配时 Claude 自动加载
- 手动调用：输入 `/chen-hansheng-wisdom` 直接触发

---

### 🟢 方式三：Cursor

> 使用 Cursor Rules 机制（`.mdc` 格式，带 frontmatter）

```bash
mkdir -p .cursor/rules
cp configs/cursor/chen-hansheng-wisdom.mdc .cursor/rules/
```

配置说明：
- `alwaysApply: true` —— 所有对话自动生效
- 如需按文件匹配，修改 `.mdc` 中的 `globs` 字段
- 完整版（45 维度）可在对话中要求 AI 读取仓库根目录的 `SKILL.md`

---

### 🟡 方式四：OpenCode

> 使用 `AGENTS.md` 格式，OpenCode 原生支持

**项目级：**
```bash
cp configs/opencode/AGENTS.md ./AGENTS.md
```

**全局级（所有项目生效）：**
```bash
mkdir -p ~/.config/opencode
cp configs/opencode/AGENTS.md ~/.config/opencode/AGENTS.md
```

**进阶：加载完整版 SKILL.md**
在 `opencode.json` 的 `instructions` 字段中添加：
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["AGENTS.md", "path/to/SKILL.md"]
}
```

> 💡 OpenCode 也兼容 Claude Code 的 `.claude/skills/` 目录（默认开启），如果你配了 Claude Code，OpenCode 也能直接用。

---

### 🔴 方式五：Trae

> 使用 Trae Rules 机制（`.trae/rules/*.md`，带 frontmatter）

```bash
mkdir -p .trae/rules
cp configs/trae/chen-hansheng-wisdom.md .trae/rules/
```

**四种生效方式（修改 frontmatter 即可切换）：**

| 生效方式 | frontmatter 设置 | 说明 |
|---------|-----------------|------|
| 始终生效 | `alwaysApply: true` | 所有对话自动加载（默认） |
| 指定文件生效 | `globs: src/**/*.ts` | 匹配文件时生效 |
| 智能生效 | `description: 适用场景描述` | AI 判断相关性后加载 |
| 手动触发 | 无需配置 | 对话中输入 `#Rule` 引用 |

> 💡 Trae 也支持 `AGENTS.md` 和 `CLAUDE.md`（需在 设置 > 规则 > 导入设置 中开启对应开关）。

---

### ⬜ 方式六：通用（任何 AI 工具）

把 `SKILL.md` 的内容作为 system prompt 粘贴到任意 AI 工具中（ChatGPT、Kimi、豆包、文心一言等），或在对话开始时说：

> "请阅读以下内容并完全遵守，之后用陈汉升的语气和我对话：[粘贴 SKILL.md 内容]"

---

### 📁 配置文件速查

```
configs/
├── claude-code/
│   └── SKILL.md              # Claude Code 版（Agent Skills 标准 · 45 维度完整版）
├── cursor/
│   └── chen-hansheng-wisdom.mdc   # Cursor 版（核心原则浓缩版）
├── opencode/
│   ├── AGENTS.md             # OpenCode 版（核心原则浓缩版）
│   └── opencode.json         # OpenCode 配置（加载完整 SKILL.md）
└── trae/
    └── chen-hansheng-wisdom.md    # Trae 版（核心原则浓缩版）
```

> 📌 **安装提示**：`configs/` 里的文件名已经是"复制到哪就放哪"的布局——比如 `configs/cursor/chen-hansheng-wisdom.mdc` 复制到项目的 `.cursor/rules/` 目录即可，`configs/trae/chen-hansheng-wisdom.md` 复制到项目的 `.trae/rules/` 目录即可。仓库内不包含点开头目录，GitHub 网页上传可正常识别。

> 📌 **版本说明**：Claude Code / WorkBuddy 使用**完整版**（45 维度 + 文字语气契约），因为它们的 Skill 机制是按需加载，不占上下文。Cursor / OpenCode / Trae 使用**浓缩版**（文字语气硬约束 + 核心原则 + 28–45 速查），因为规则常驻上下文，太长会占用 token。

---

## 📂 仓库结构

```
awesome-chen-hansheng/
│
├── SKILL.md                  # 技能主文件（772 行 · 58KB · 45 个维度）
├── README.md                 # 本文档（含全智能体配置指南）
├── LICENSE                   # MIT
├── .gitignore
├── .gitattributes            # 统一文本换行
│
├── configs/                  # 🆕 全智能体配置文件
│   ├── claude-code/          # Claude Code（Agent Skills 标准）
│   ├── cursor/               # Cursor（.mdc 规则）
│   ├── opencode/             # OpenCode（AGENTS.md）
│   └── trae/                 # Trae（.md 规则）
│
├── scripts/
│   ├── install.sh            # 一键安装脚本
│   ├── check_reply_style.py  # 发送前扫描 AI 报告腔与格式味
│   └── test_text_tone_contract.py # 文字语气与配置同步检查
│
├── references/
│   ├── text-tone-atlas.md    # 句法、用词、语气切换与 AI 腔避雷
│   └── text-tone-examples.md # 12 组跨场景合成文字语气标定样例
│
├── images/                   # AI 生成的主题插图
│   ├── cover.png             # 封面 · 黄昏城市天际线
│   ├── social-skills.png     # 为人处世 · 中式饭局
│   ├── romance.png           # 恋爱技巧 · 月光剪影
│   └── language-style.png    # 语言风格 · 茶室倾听与语气
│
└── 内容架构（5 大章节 · 45 个维度）
    ├── 零、角色文字语气契约 ──────── 4 小节
    ├── 一、为人处世篇 ──────────── 10 维度
    ├── 二、恋爱技巧篇 ──────────── 10 维度
    ├── 三、语言风格与语气模仿指南 ── 7 子节
    ├── 四、核心心法总结 ─────────── 4 小节
    └── 五、跨场景补充技巧库 ─────── 18 维度
```

三张主题配图已使用本地 ComfyUI + Qwen-Image-2.1 重新生成，统一为柔和水彩轻小说风格；主封面保持原图。

---

## ❓ 常见问题

<details>
<summary><b>🔥 这些技巧在现实中适用吗？</b></summary>

本技能从小说中蒸馏而来，部分策略带有角色特有的时代背景（2002 年大学校园、35 岁重生者的阅历差）。实际应用中应取其智慧而非照搬行为。**小说是小说，生活是生活。**
</details>

<details>
<summary><b>🔥 为什么有些策略看起来像"操控"？</b></summary>

分析文学角色的行为逻辑 ≠ 鼓励这些行为。本技能包含正面技巧（递烟的尊重、帮忙的超预期交付）和争议性策略（双线管理、伤口政治学）。**请理性参考，用于提升情商，而非操控他人。**
</details>

<details>
<summary><b>🔥 不用 WorkBuddy 能用吗？</b></summary>

当然可以！本仓库为 **6 种主流智能体**提供了开箱即用的配置：**Claude Code**（Agent Skills 标准）、**Cursor**（.mdc 规则）、**OpenCode**（AGENTS.md）、**Trae**（.trae/rules）、**WorkBuddy**（SKILL.md），以及**通用方式**（任何 AI 工具，直接粘贴 SKILL.md 作为 system prompt）。详见上方[安装](#-安装)章节。
</details>

<details>
<summary><b>🔥 可以贡献内容吗？</b></summary>

欢迎 PR！如果你在小说中发现了遗漏的场景或技巧维度，请补充原文引用和深层分析。
</details>

---

## 📊 项目数据

<div align="center">

| 指标 | 数值 |
|------|------|
| 原著字数 | 3,422,137 字 |
| 原著行数 | 101,846 行 |
| 技能文件行数 | 772 行 |
| 技能文件大小 | 59 KB |
| 维度总数 | 45 个 |
| 场景拆解 / 跨场景技巧 | 27 / 18 |
| 文字语气契约 | 4 小节 |
| AI 生成插图 | 4 张 |
| 搜索方式 | 6 个并行 Agent + Grep 精搜 |

</div>

---

## 🙏 致谢与免责

**致谢**
- 原作：柳岸花又明，《我真没想重生啊》
- 角色：陈汉升、萧容鱼、沈幼楚、王梓博、郭中云 等

**免责声明**
1. 本项目为文学角色行为分析，**不构成现实生活中的行为指导**
2. 部分策略带有争议性，**仅供分析参考，不鼓励模仿**
3. 小说情节有艺术夸张，**现实应用请遵守法律法规和道德准则**
4. 本项目与原作作者和出版方无关联，如有版权问题请联系删除

---

<div align="center">

<br/>

### 如果这个项目让你有所收获

⭐ **Star** · 🍴 **Fork** · 📢 **Share**

<br/>

**Made with ❤️ by distilling 3.42 million words of wisdom**

<br/>

</div>
