"""Read the current playthrough's Lily affinity from a PC save.

Usage: python read_stellar_lily.py PATH_TO_StellarBladeSave00.sav

Only reads the save. AchievementTable.uasset in the game's stock IoStore
archive sets Ach_RealEnding_Result's required progress to 105. The counter 2
therefore computes to 1.90476%, verified as 1.9% in the game's HUD.
"""
from pathlib import Path
import re
import struct
import sys

ACHIEVEMENT_STRUCT = b'\x0e\x00\x00\x00SBAchievement\x00\x0f\x00\x00\x00StructProperty\x00'
COUNTER_ALIAS = b'Ach_RealEnding_Result\x00'
UINT32_TAG = b'ProgressValue\x00\x0f\x00\x00\x00UInt32Property\x00'
MAX_PROGRESS = 105


def read_counter(path: Path) -> int:
    data = path.read_bytes()
    if not data.startswith(b'EVAS'):
        raise ValueError('Unsupported Stellar Blade PC save (missing EVAS header)')
    tag = data.find(ACHIEVEMENT_STRUCT)
    if tag < 0:
        raise ValueError('Current-playthrough SBAchievement section not found')
    size_at = tag + len(ACHIEVEMENT_STRUCT)
    size = struct.unpack_from('<Q', data, size_at)[0]
    if size > len(data) or size < 40:
        raise ValueError('Invalid achievement section size')
    section = data[tag: min(len(data), size_at + size + 80)]
    matches = list(re.finditer(re.escape(COUNTER_ALIAS), section))
    if not matches:
        return 0
    if len(matches) != 1:
        raise ValueError('Ambiguous Lily counter in current playthrough')
    tail = section[matches[0].end():matches[0].end() + 100]
    progress = tail.find(UINT32_TAG)
    if progress < 0:
        raise ValueError('Lily counter lacks ProgressValue')
    size_at = progress + len(UINT32_TAG)
    if struct.unpack_from('<Q', tail, size_at)[0] != 4:
        raise ValueError('Unexpected Lily counter value type')
    return struct.unpack_from('<I', tail, size_at + 9)[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python read_stellar_lily.py <StellarBladeSave00.sav>')
    path = Path(sys.argv[1])
    score = read_counter(path)
    percent = min(100.0, score / MAX_PROGRESS * 100)
    print(f'{path.name}: Lily affinity = {percent:.1f}% (current playthrough: {score}/{MAX_PROGRESS})')
