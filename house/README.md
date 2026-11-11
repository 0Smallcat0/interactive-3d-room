# Floor plan → walk-through 3D home · 平面圖變成可以走進去的 3D 房子

**▶ Open it (no download, no install): https://0smallcat0.github.io/interactive-3d-room/house/**

[![Glencoe Residence walkthrough](preview.jpg)](https://0smallcat0.github.io/interactive-3d-room/house/)

A real architectural floor plan is traced to scale and built into a complete single-family home you can walk through in the browser. The plan is Gary Berkovich's single-family residence in Glencoe, Illinois (1994).

把一張真實的建築平面圖照比例描成資料，蓋成一整棟可以在瀏覽器裡走動的獨棟住宅。用的是 Gary Berkovich 1994 年設計、位於伊利諾州 Glencoe 的獨棟住宅平面圖。

**What's inside · 有什麼：**

- **The whole house, to scale.** Thirteen rooms and five terraces sit on a 324 m² footprint, and the furniture is placed by the plan's labels.
  - The traced walls overlap the drawn walls at IoU 0.96.
  - 整棟照比例：13 個空間、5 個露台，佔地 324 m²，家具照平面圖標示擺放；描出的牆和原圖牆線重合度（IoU）0.96。
- **Light baked in Blender Cycles.** Sunlight from a real sky, bounce light, and warm interior lights are baked into a 4096² lightmap, so it looks right on a phone too.
  - 光線用 Blender Cycles 烘焙：真實天空的日光、反射光和室內暖光烘成 4096² 光照圖，手機上也看得到。
- **Photoreal stops.** Every guided-tour stop opens on a full 360° path-traced render of that room, so you can drag to look around a photo-quality view. Walk away or open the dollhouse, and it hands over to the live 3D model.
  - 照片級導覽站：每個導覽站都是該房間的 360° 光線追蹤全景，拖曳就能環顧。走開或切俯瞰時，會換回即時 3D 模型。
- **Walk, dollhouse, guided tour.** Click the floor to walk there along a real path that goes around walls and furniture. Or flip to a cut-away dollhouse, or press *Guided tour*.
  - 走動／俯瞰模型／自動導覽：點地板就沿著繞開牆和家具的路線走過去；也可以切成掀頂的模型俯瞰，或按自動導覽。
- **The original plan is the map.** The minimap is the architect's drawing, with your position, view direction, and current room highlighted.
  - 小地圖就是原平面圖，標出你的位置、視線方向和所在的房間。
- **First-person mode.** On a computer, the mouse turns your head, W A S D walks, Shift runs, with footsteps; you bump into walls and furniture the way you would in the real house.
  - 第一人稱：電腦上滑鼠轉頭、W A S D 走、Shift 跑，有腳步聲；會撞到牆和家具，跟在真的房子裡走一樣。
- **English / 中文** toggle.

Built with three.js and Blender. Every plan goes through the same steps: trace the plan, build and bake the house, render the tour stops, and open it in one shared viewer whose only per-house input is a small settings file.

用 three.js 和 Blender 做。每張平面圖都走同一套流程：描圖、建模烘焙、算導覽站全景，再用同一個導覽程式打開，每棟只差一個小設定檔。

**Credits · 素材來源**

- Floor plan: Gary Berkovich, *Single Family Residence, Glencoe IL* (1994), [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:House_floorpan_by_Gary_Berkovich_(Glencoe,_Illinois).jpg), CC BY-SA 3.0. The traced plan data (`plan.json`) and the recolored map image (`map.png`) are adaptations, shared under CC BY-SA 3.0.
- Furniture models, textures, and the sky (Kloofendal HDRI): [Poly Haven](https://polyhaven.com), CC0.
