import maya.cmds as cmds
import math




#############
####先选面，再选旋转轴####
####Firstly,choose the faces you want to turn,then plus the edge you want it as povit####
corner=45 ###change the degrees here###
#############



povit=cmds.ls( selection=True, tail=1 )

cmds.sets(povit,n='Edge_povit')

cmds.select(povit,d=True)
cmds.sets(n='faces')

cmds.select('Edge_povit')


cmds.ConvertSelectionToVertices()

vertex=cmds.ls(sl=1,tail=2)

v1=cmds.pointPosition( vertex[0] )
v2=cmds.pointPosition( vertex[1] )

x=v2[0]-v1[0]
y=v2[1]-v1[1]
z=v2[2]-v1[2]

r=math.sqrt(x**2+y**2+z**2)

if x!=0:
    if x>0:
        pom=1
    else:
        pom=2
    
    rx=0
    ry=math.degrees( math.atan(z/x) )*-1
    rz=math.degrees( math.acos(y/r) )*((-1)**pom)
else:
    if z>0:
        pom=2
    else:
        pom=1
    rx=math.degrees( math.acos(y/r) )*((-1)**pom)
    ry=0
    rz=0
    
cmds.polyCylinder(h=3,r=0.1,n='temp')
cmds.rotate(0,0,0)
cmds.rotate(0,0,rz,r=1,ws=1,fo=1)
cmds.rotate(0,ry,0,r=1,ws=1,fo=1)
cmds.rotate(rx,0,0,r=1,ws=1,fo=1)

mP=cmds.xform( 'temp', q=True, ws=True, ro=True )
mPx=mP[0]
mPy=mP[1]
mPz=mP[2]
cmds.select(cl=1)
cmds.delete('temp')


cmds.select('faces')


cmds.manipPivot(p=v1,o=(mPx,mPy,mPz))

#############
cmds.rotate(0,corner,0,p=v1)

Len=1/(math.cos(math.radians(corner)))
#print(Len)
cmds.scale(Len,1,Len, p=v1)
#############
cmds.delete('faces','Edge_povit')
cmds.manipPivot(r=1)

