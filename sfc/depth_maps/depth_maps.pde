PShader depth;
PGraphics pg;

void setup()
{
  size(600,600,P3D);
  depth = loadShader("depth.frag", "depth.vert");
  pg = createGraphics(600,600,P3D);
  depth.set("far", 385.0);
  
  float fov = PI/32;
  float cameraZ = (height/2.0) / tan(fov/2.0);
  pg.perspective(fov, float(width)/float(height), 
    cameraZ/10.0, cameraZ*10.0);
}

void mouseClicked() {
  save("spheres.png");
}

void draw()
{
 pg.hint(ENABLE_DEPTH_TEST);
 pg.shader(depth);
 pg.beginDraw();
 pg.noStroke();
 pg.background(0);
 for (int r = 0; r < 4; r++) {
   for (int c = 0; c < 4; c++ ) {
     float x = c*width/5 + 120;
     float y = r*height/5 + 120;
     pg.push();
     pg.translate(x, y, 80);
     pg.sphere(60);
     pg.pop();
   }
 }
 pg.endDraw();
 image(pg,0,0);
}
