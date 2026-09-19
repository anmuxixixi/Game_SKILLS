---
name: stellar-blade-lily-affinity
description: Read and verify Lily's current-playthrough affinity percentage from a Stellar Blade PC .sav file. Use when the user asks for 百合好感度, Lily affinity, or validation against the in-game percentage.
---

# Read Lily affinity from a Stellar Blade PC save

## Absolute rule: never modify game saves

Treat every game save as read-only. Never write to, edit, replace, rename, move, delete, truncate, or repair any `.sav` file or anything in the game's save directory. Do not use a tool or script that can change a save, even for calibration or troubleshooting. Only read the save bytes and report the result. If further calibration is needed, ask the user to provide the in-game percentage and save snapshots; do not create or alter them yourself.

Use [scripts/read_stellar_lily.py](scripts/read_stellar_lily.py) with Python 3 and the user's `StellarBladeSave00.sav` path. It reads the file without changing it. If the save path is unknown, look under `%LOCALAPPDATA%\SB\Saved\SaveGames\<Steam-ID>\` and identify the intended save from the user's description and file timestamps. Do not assume a suffixed backup such as `StellarBladeSave00_1.sav` is the current playthrough.

The script reads `Ach_RealEnding_Result` inside the current `SBAchievement` section, rather than the inherited `AchievementSaveData` record. The game's `AchievementTable.uasset` sets this counter's required progress to 105. Report `min(100, counter / 105 × 100)` rounded to one decimal place. This was checked against in-game readings of 1.9% at 2/105 and 3.8% at 4/105; a prior 107/105 save displayed 100% after capping.

Run, for example:

```text
python scripts/read_stellar_lily.py "C:\Users\Administrator\AppData\Local\SB\Saved\SaveGames\<Steam-ID>\StellarBladeSave00.sav"
```

Give the current-playthrough counter and calculated percentage. If the format check fails, the counter is ambiguous, or the result conflicts with a known in-game value, do not claim a verified percentage. Inspect the save format and ask the user for a before/after save pair with a known in-game percentage change before adapting the parser or formula.
