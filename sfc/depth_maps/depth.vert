uniform mat4 transform;
uniform mat3 normalMatrix;
uniform vec3 lightNormal;
 
attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
 
uniform vec3 cameraPosition;
uniform float far;
 
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying float dist;
 
void main() {
    vertNormal = normal;
    dist = distance(cameraPosition, position.xyz)/far;
    gl_Position = transform * position;
}