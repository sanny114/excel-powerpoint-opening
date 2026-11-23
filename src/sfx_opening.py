# 効果音。時刻は 絵コンテ.md と opening.html（HITS / CLICK / BAR_T など）と同じ。
#   python sfx_opening.py <出力.wav>
import sys
sys.path.insert(0, "scripts")  # sfx.py（効果音キット）を置いたフォルダ
from sfx import *

out = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"
dry, wet = init(30.0)

# 0–2 冒頭：線で描かれる2つの道具
for i, t in enumerate([0.0, .5, 1.0, 1.5]):
    put(dry, t, tick(1800 + i * 150, .35)); put(dry, t, kick(.45))
put(wet, 1.0, pad(CHORDS['Am'], 1.0, .22))
put(dry, 1.75, whoosh(.45, 500, 1600, .3, pan0=0, pan1=-.4))
put(dry, 2.0, kick(1.0)); put(dry, 2.0, sub(.5, .8))

# 2–5 手作業：1つずつ選ぶ → =AVERAGE( と打ちかけて止まる
for t in [2.5, 3.0, 3.5, 4.0]:
    put(dry, t, snap(.7), pan=-.3); put(dry, t, kick(.35))
for t in [2.25, 2.75, 3.25, 3.75]:
    put(dry, t, hat(.15))
for k in range(9):
    put(dry, 4.1 + k * .072, key(.55), pan=.2)

# 5–6 入力欄のある枠が開く。画面が青に
put(dry, 4.5, riser(.5, 200, 900, .4))
put(dry, 5.0, whoosh(.5, 600, 2000, .4, pan0=.9, pan1=.4))
put(dry, 5.5, kick(.9)); put(wet, 5.5, stab(CHORDS['C'], .6, .45)); put(wet, 5.5, pluck(523.3, .5, .6))

# 6–9 一文を打つ（16分音符）
for k in range(20):
    put(dry, 6.0 + k * .125, key(.5), pan=.35 + (k % 3) * .08)
for b in range(12, 18):
    t = b * .5
    put(dry, t, kick(.4) if b % 2 == 0 else hat(.2))
put(wet, 6.0, pad(CHORDS['F'], 1.4, .22)); put(wet, 7.5, pad(CHORDS['G'], 1.4, .22))

# 9–10 送る
put(dry, 8.75, blip(500, 1200, .3, .2))
put(dry, 9.0, snap(.6)); put(dry, 9.3, whoosh(.7, 700, 2600, .6, pan0=.6, pan1=-.4, shape='up'))
put(dry, 10.0, kick(1.2)); put(dry, 10.0, sub(.6, 1.0)); put(wet, 10.0, crash(.3, 1.5)); put(wet, 10.0, stab(CHORDS['C'], .6, .5))

# 10–14 ひとりでに埋まる → 棒が1本ずつ伸びる
for k in range(6):
    put(dry, 10.0 + k * .125, tick(2000 + k * 180, .3), pan=-.2); put(wet, 10.0 + k * .125, pluck(523.3 * 2 ** (k / 12), .3, .3))
put(dry, 11.0, whoosh(.35, 600, 1500, .25, pan0=-.2, pan1=0)); put(dry, 11.0, kick(.5))
for i, f in enumerate([392.0, 440.0, 523.3, 659.3]):
    t = 11.5 + i * .5
    put(dry, t, kick(.7)); put(dry, t, snap(.5)); put(wet, t, pluck(f, .6, .6)); put(dry, t + .25, hat(.2))
put(wet, 13.0, stab(CHORDS['C'], .6, .45)); put(wet, 13.0, pad(CHORDS['C'], 1.4, .25))

# 14–16 グラフが運ばれて、スライドへ
put(dry, 14.0, blip(600, 1100, .3, .18)); put(dry, 14.0, kick(.5))
put(dry, 14.6, whoosh(.65, 900, 3200, .7, pan0=-.8, pan1=.9))
put(dry, 15.2, kick(1.1)); put(dry, 15.2, clap(.7)); put(wet, 15.2, stab(CHORDS['F'], .5, .45))

# 16–18 一文を打つ
for k in range(17):
    put(dry, 16.0 + k * .1, key(.5), pan=.35 + (k % 3) * .08)
put(dry, 16.0, kick(.4)); put(dry, 16.5, hat(.2)); put(dry, 17.0, kick(.4)); put(dry, 17.5, hat(.2))
put(dry, 17.7, whoosh(.3, 600, 2200, .45, pan0=.6, pan1=-.3, shape='up'))

# 18–21 新しい1枚が増え、グラフが収まる
put(dry, 18.0, kick(1.1)); put(dry, 18.0, snap(.6)); put(wet, 18.0, stab(CHORDS['G'], .5, .45))
put(dry, 18.5, whoosh(.5, 700, 1800, .3, pan0=-.5, pan1=.1))
put(dry, 19.0, kick(1.0)); put(dry, 19.0, clap(.5)); put(wet, 19.0, stab(CHORDS['C'], .7, .5))
for i, f in enumerate([523.3, 587.3, 659.3]):
    put(wet, 19.0 + i * .25, pluck(f, .5, .5)); put(dry, 19.0 + i * .25, tick(2200, .3))
put(wet, 19.5, pad(CHORDS['C'], 1.4, .25))
put(dry, 20.0, kick(.4)); put(dry, 20.5, hat(.2))

# 21–25 引く → 線が通る → 大きな文字
put(dry, 21.0, whoosh(1.0, 2600, 500, .45, pan0=.6, pan1=-.3))
put(dry, 21.5, riser(.5, 250, 1000, .35))
put(dry, 22.0, kick(1.1)); put(wet, 22.0, crash(.3, 1.8))
put(wet, 22.0, pad(CHORDS['F'], 2.0, .32)); put(wet, 24.0, pad(CHORDS['G'], 1.0, .3))
for i, f in enumerate([523.3, 587.3, 659.3, 784.0, 880.0, 1046.5]):
    put(wet, 22.25 + i * .25, pluck(f, .4, .45), pan=-.6 + i * .24)
for t, a in [(22.5, .8), (23.0, .9), (23.5, 1.0), (24.0, 1.0)]:
    put(dry, t, kick(a)); put(dry, t, snap(.5))
put(wet, 23.5, stab(CHORDS['C'], .5, .5))
t = 22.0
while t < 25.0:
    put(dry, t + .25, hat(.2)); t += .5

# 25–27 線が点にまとまり、白い円が広がる
put(dry, 25.0, whoosh(1.0, 2200, 600, .35, pan0=-.6, pan1=.5))
put(dry, 26.0, riser(.5, 300, 1200, .45))
put(dry, 26.5, kick(1.2)); put(dry, 26.5, clap(.6)); put(wet, 26.5, crash(.3, 1.6)); put(wet, 26.5, stab(CHORDS['C'], .7, .5))

# 27–30 タイトル
put(wet, 27.0, pad(CHORDS['C'], 2.9, .36)); put(wet, 27.0, pluck(523.3, .5, .7))
put(wet, 27.4, pluck(659.3, .45, .7)); put(wet, 27.6, pluck(784.0, .45, .7))
put(wet, 28.0, pluck(1046.5, .5, .9))
write(out)
