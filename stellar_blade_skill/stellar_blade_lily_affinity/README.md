# 剑星：读取百合好感度

这个 Codex skill 从《剑星》PC 版存档中读取**当前周目**的百合好感度。它会避开存档里继承自旧周目的历史计数，并根据当前计数计算百分比。

**绝对不允许修改游戏存档。** 本 skill 及其脚本只读取 `.sav` 文件，不会写入、替换、移动、重命名或删除存档。

## 安装到 Codex

在 Codex 中输入以下内容，让内置的 `$skill-installer` 从本仓库安装：

```text
$skill-installer 请从 https://github.com/anmuxixixi/Game_SKILLS/tree/main/stellar_blade_skill/stellar_blade_lily_affinity 安装这个 skill。
```

安装后，skill 名称是 `$stellar-blade-lily-affinity`。如果它没有立即出现在技能列表中，请重启 Codex。安装方法参考 [OpenAI 的技能文档](https://developers.openai.com/zh-Hans/docs/build-skills)。

## 使用

在 Codex 中发送：

```text
使用 $stellar-blade-lily-affinity 读取我当前周目的百合好感度。存档位于 C:\Users\<用户名>\AppData\Local\SB\Saved\SaveGames\<Steam-ID>\StellarBladeSave00.sav。绝对不要修改存档。
```

把 `<用户名>` 和 `<Steam-ID>` 换成你自己的目录名。如果不确定路径，可以先让 Codex 在 `%LOCALAPPDATA%\SB\Saved\SaveGames\` 下查找。`StellarBladeSave00_1.sav` 等带后缀的文件可能是旧存档或备份；应明确指定想读取的文件。

也可以安装 Python 3 后，直接运行随 skill 附带的只读脚本。在 Windows 命令提示符中，从本目录执行：

```bat
python scripts\read_stellar_lily.py "%LOCALAPPDATA%\SB\Saved\SaveGames\<Steam-ID>\StellarBladeSave00.sav"
```

### 输出示例

```text
StellarBladeSave00.sav: Lily affinity = 3.8% (current playthrough: 4/105)
```

示例表示当前周目计数为 4，满进度计数为 105，换算并保留一位小数后是 3.8%。该换算曾与游戏中显示的 1.9%（2/105）和 3.8%（4/105）核对。若脚本报错或读数与游戏显示不符，应停止使用该结果进行判断，并提供存档版本及游戏中的百分比以便重新校验；仍不得修改游戏存档。
