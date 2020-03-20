#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif
 
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying float dist;
 
void main() {
    gl_FragColor = vec4(vec3(1/clamp(dist, 0, 1000)), 1.0);
}