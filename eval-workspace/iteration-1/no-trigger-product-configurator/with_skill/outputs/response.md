I built the Stridewell configurator as one HTML file: `stridewell-configurator.html`. Open it in any browser. It needs no build step. Three.js r128 loads from cdnjs.

**What it does**
- **Rotating 3D shoe:** I named the model "Lane 01". It slowly spins when the page opens. Drag to rotate, scroll or pinch to zoom, and use the arrow keys when the view is focused. The Side, Top and Sole buttons move the camera to set angles, and Spin turns the slow rotation back on.
- **Sole colours (6):** Chalk white, Natural gum (+$8), Pitch black, Ultramarine (+$6), Chalk on gum two-tone (+$12) and Clear ice (+$16). Clear ice shows as a glossy see-through sole.
- **Lace colours (6):** White, Black, Moss, Signal orange (+$4), Ultramarine (+$4) and 3M reflective (+$9). Reflective laces show with a metallic finish.
- **Live price:** It starts at $128. The total counts up to the new price when you change an option, and a breakdown underneath shows each add-on. Size (UK 6 to 12) is included and doesn't change the price.
- **Add to bag:** It shows a confirmation with the full build and price. It isn't connected to a real cart yet.

**Design:** I used a cool chalk-grey "studio floor" with ink-green text, the Archivo typeface in a wide setting, and one ultramarine accent. Ultramarine is also the colour of the stripe on the shoe's side. The layout puts the shoe on the left and the options on the right. On phones it stacks, and the price bar stays pinned to the bottom. It supports dark mode, keyboard focus and reduced motion.

**Before you ship, keep in mind**
- The shoe is built in code from simple shapes. It's a clean stand-in, not your real product. When you have a GLB/glTF model of the actual sneaker, I can swap it in and recolour its sole and lace parts the same way.
- All prices, colour names and the "Lane 01" name are placeholders I made up. They're kept together in the `SOLES`, `LACES` and `BASE` lists at the top of the script, so they're easy to change.

I checked it in headless Chrome at desktop and phone sizes. The price math was right, there were no console errors and the page doesn't scroll sideways. Screenshots are saved next to the file: `preview-desktop.png` and `preview-mobile.png`.
