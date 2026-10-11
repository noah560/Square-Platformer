# Square Platformer

This is a simple platformer game that is 3D and infinite!
You press space to jump and m to mute audio.
This game uses raycasting for the 3D graphics,
and the audio is in a midi-style format.
Terser was used to minify the Javascript code.

## Building
Not much to say here, just minify the javascript in
`index.html` with your preferred minifier (I used
`terser script.js -c --mangle toplevel`), update the
music data in it and put it into a data url.

## Play
```link
data:text/html,<!DOCTYPE html><html><body style="color: %23fff; background-color: %23000;"><h1 id="l">0</h1><canvas id="c" width="400" height="400"></canvas><br/>Space to jump<br/>M to mute<script>let n=[];const f=document.getElementById("c").getContext("2d"),e="n0,71|f12,71|n12,69|f12,69|n0,67|n12,64|f0,67|f12,64|n25,62|n12,64|f0,62|f12,64|n0,64|n12,62|f0,64|f12,62|n0,64|f12,64|n50,71|f12,71|n12,69|n12,67|f0,69|f12,67|n0,67|f12,67|n25,64|f12,64|n0,62|n12,62|f0,62|f12,62|n0,64|n12,62|f0,64|f12,62|n50,71|n12,59|f0,71|f12,59|n0,69|n12,67|f0,69|f12,67|n0,55|n12,64|f0,55|f12,64|n12,62|n0,50|n12,64|f0,62|f0,50|f12,64|n0,64|n0,52|n12,62|f0,64|f0,52|f12,62|n0,64|n0,52|f12,64|f0,52|n50,71|n12,59|f0,71|f12,59|n0,69|n12,67|f0,69|f12,67|n0,67|n12,55|f0,67|f12,55|n12,64|n0,52|n12,62|f0,64|f0,52|f12,62|n0,62|n0,50|n12,64|f0,62|f0,50|f12,64|n0,62|n0,50|f12,62|f0,50|n50,60|n12,59|f0,60|f12,59|n0,62|f12,62|n12,64|n12,55|f0,64|f12,55|n12,67|n0,50|n12,67|f0,67|f0,50|f12,67|n0,64|n12,67|f0,64|n0,50|f12,67|f0,50|n0,52|f12,52|n50,60|f12,60|n0,59|n12,62|f0,59|f12,62|n12,64|n12,55|f0,64|f12,55|n12,52|n0,67|n12,67|f0,52|f0,67|f12,67|n0,64|n12,52|n0,60|f0,64|f12,52|f0,60|n0,50|f12,50|n12,71|n12,69|f0,71|f12,69|n0,67|f12,67",t=e.split("|").map(n=>[n[0],n.slice(1).split(",")[0],n.slice(1).split(",")[1]]);let o=!0;const l=Math,i=new(window.AudioContext||window.webkitAudioContext);async function r(n,f){const e=440*l.pow(2,(n-69)/12),t=i.createOscillator(),o=i.createGain();t.type="square",t.frequency.value=e,t.connect(o),o.connect(i.destination),t.start(),t.stop(i.currentTime+f/1e3)}async function c(n){return new Promise(f=>setTimeout(f,n))}async function s(){for(;;)for(let n of t)await c(10*n[1]),"n"==n[0]&&o&&r(n[2],125)}let a;function d(){a=new Array(500).fill(0);let n=0;for(let f=0;f<50;0){const e=0==f?6:l.floor(2*l.random())+3;for(let t=0;t<e&&t+f<50;t++)a[10*(f+t)+n]=1;f+=e+2,n=l.min(9,l.max(0,n+l.floor(4*l.random())-1))}}s(),d(),document.addEventListener("keydown",f=>{n.push(f.key),"m"==f.key&&(o=!o)}),document.addEventListener("keyup",f=>{n=n.filter(n=>n!==f.key)});let u=1,y=-2,m=0;function w(n){for(let f=1;f<1e3;f++){const e=.03*l.cos(n)*f,t=u+e,o=l.floor(t),i=y+.03*l.sin(n)*f-.5,r=l.floor(i);if(a[10*o+r]&&i>.05)return[400/e,l.abs(l.round(t)-t)<.1];if(o<0||o>49||i<-4.95||i>9.95)break}return[0,!1]}function p(){return a[10*l.floor(u)+l.floor(y)]&&y>.05&&y<9.95}setInterval(()=>{f.fillStyle="%233366ff",f.fillRect(0,0,400,400),u+=.12,m+=.01,y+=m,p()&&(y-=m,m=-.18*~~n.includes(" "),p()&&window.location.reload()),f.fillStyle="%23ffff22";const e=400/(50.25-u);f.fillRect(200-e/2,0,e,400);for(let n=0;n<400;n++){const e=w(l.PI/2*n/400-l.PI/4);f.fillStyle=e[1]?"%23222288":"%23444488",f.fillRect(200-e[0]/2,n,e[0],1)}f.fillStyle="red";for(let n=0;n<50;n++)for(let e=0;e<10;e++)a[10*n+e]&&f.fillRect(4*n,4*e+16,4,4);if(f.fillStyle="black",f.fillRect(4*u-1,4*y-2+16,2,2),y>10&&window.location.reload(),u>50){u=1,y=-2,m=0,d();const n=document.getElementById("l");n.innerHTML=n.innerHTML-0+1}},40);</script></body></html>
```
