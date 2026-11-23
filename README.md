# Excel×PowerPoint（30秒モーショングラフィックス）

サロン向けAI勉強会 第3回＋第4回（再開催）の趣旨「使い慣れた道具が、言葉で動くようになった」を表した30秒の映像。映像も音も、すべてコードで1フレームずつ書いたもの。

- 公開ページ: https://sanny114.github.io/excel-powerpoint-opening/
- `opening.mp4` — 本編（1920×1080 / 60fps / 音声つき）
- `live.html` — Canvas版。ブラウザでリアルタイムに描画（同じフォルダに `audio.wav` を置くと音つき）
- `src/sfx_opening.py` — サウンドトラックをnumpyで合成

書き出し: `live.html` を120fpsの連番PNGにし、`ffmpeg -framerate 120 -i frames/f%05d.png -i audio.wav -vf "tmix=frames=2,fps=60,format=yuv420p" -c:v libx264 -crf 20 -c:a aac opening.mp4`

フォント（`fonts/`）: Noto Sans JP（SIL Open Font License）。制作: Claude Code。
