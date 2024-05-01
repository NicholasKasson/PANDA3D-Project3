from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath, Vec3
from direct.task import Task
#---------------------------------------------------------------------MODEL CREATION SCRIPT INIT---------------------------------------------------------------------
def addAdditionalModel(self,ModelFile,scale,CoordX,CoordY,CoordZ,TextureFile,Yaw,Pitch,Rotation):
        new_obj = self.loader.loadModel(ModelFile) 
        new_obj.setScale(scale)
        new_obj.setColorScale(1.0,1.0,1.0,1.0)
        new_obj.reparentTo(self.render)
        new_obj.setPos(CoordX,CoordY,CoordZ)
        new_obj_tex = self.loader.loadTexture(TextureFile)
        new_obj.setTexture(new_obj_tex)
        new_obj.setHpr(Yaw,Pitch,Rotation)
#---------------------------------------------------------------------PLANET INIT---------------------------------------------------------------------
class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.modelNode = self.model
#---------------------------------------------------------------------UNIVERSE INIT---------------------------------------------------------------------
class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
#---------------------------------------------------------------------DRONE INIT---------------------------------------------------------------------
class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
#---------------------------------------------------------------------SPACESTATION INIT---------------------------------------------------------------------
class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)        
#---------------------------------------------------------------------SHIP INIT---------------------------------------------------------------------
class Ship(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)                
#---------------------------------------------------------------------PLAYER INIT---------------------------------------------------------------------
class Player(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.taskMgr = taskMgr
        self.render = NodePath()

#---------------------------------------------------------------------MOVEMENT INIT---------------------------------------------------------------------        
    def SetKeyBindings(self):
        self.accept('space', self.UpwardsThrust, [1])
        self.accept('space-up', self.UpwardsThrust, [0])
        self.accept('shift', self.DownwardsThrust, [1])
        self.accept('shift-up', self.DownwardsThrust, [0])
        self.accept('w', self.ForwardsThrust, [1])
        self.accept('w-up', self.ForwardsThrust, [0])
        self.accept('s', self.BackwardsThrust, [1])
        self.accept('s-up', self.BackwardsThrust, [0])
        self.accept('a', self.StrafeLeft, [1])
        self.accept('a-up', self.StrafeLeft, [0])
        self.accept('d', self.StrafeRight, [1])
        self.accept('d-up', self.StrafeRight, [0])
        self.accept('q', self.LeftTurn, [1])
        self.accept('q-up', self.LeftTurn, [0])
        self.accept('e', self.RightTurn, [1])
        self.accept('e-up', self.RightTurn, [0])
        self.accept('z', self.LeftRotate, [1])
        self.accept('z-up', self.LeftRotate, [0])
        self.accept('x', self.RightRotate, [1])
        self.accept('x-up', self.RightRotate, [0])
        self.accept('c', self.ForwardsRoll, [1])
        self.accept('c-up', self.ForwardsRoll, [0])
        self.accept('v', self.BackwardsRoll, [1])
        self.accept('v-up', self.BackwardsRoll, [0])
        
#DIRECTIONAL MOVEMENT        
    def UpwardsThrust(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyUpwardsThrust, 'upwards thrust')
        else: 
            self.taskMgr.remove('upwards thrust')
    def ApplyUpwardsThrust(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.up())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)
        return Task.cont   
    def DownwardsThrust(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyDownwardsThrust, 'downwards thrust')
        else: 
            self.taskMgr.remove('downwards thrust')
    def ApplyDownwardsThrust(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.down())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)
        return Task.cont
    #Forwards works!
    def ForwardsThrust(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyForwardsThrust, 'forwards thrust')
        else: 
            self.taskMgr.remove('forwards thrust')
    def ApplyForwardsThrust(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.forward())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)
        return Task.cont
    def StrafeLeft(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyStrafeLeft, 'strafe left')
        else: 
            self.taskMgr.remove('strafe left')
    def ApplyStrafeLeft(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.left())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)
        return Task.cont 
    def StrafeRight(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyStrafeRight, 'strafe right')
        else: 
            self.taskMgr.remove('strafe right')
    def ApplyStrafeRight(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.right())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)      
        return Task.cont
    def BackwardsThrust(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyBackwardsThrust, 'backwards thrust')
        else: 
            self.taskMgr.remove('backwards thrust')
    def ApplyBackwardsThrust(self, task):
        rate = 4
        trajectory = self.render.getRelativeVector(self.model, Vec3.back())
        trajectory.normalize()
        self.model.setFluidPos(self.model.getPos() + trajectory * rate)
        return Task.cont    

    #ROTATIONAL
    def LeftTurn(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyLeftTurn, 'left-turn')
        else: 
            self.taskMgr.remove('left-turn')
    def ApplyLeftTurn(self, task):
        rate = 1.5
        self.model.setH(self.model.getH() + rate)
        return Task.cont
    def RightTurn(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else: 
            self.taskMgr.remove('right-turn')
    def ApplyRightTurn(self, task):
        rate = 1.5
        self.model.setH(self.model.getH() - rate)
        return Task.cont
    def LeftRotate(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyLeftRotate, 'left-rotate')
        else: 
            self.taskMgr.remove('left-rotate')
    def ApplyLeftRotate(self, task):
        rate = 1.5
        self.model.setR(self.model.getR() + rate)
        return Task.cont
    def RightRotate(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyRightRotate, 'right-rotate')
        else: 
            self.taskMgr.remove('right-rotate')
    def ApplyRightRotate(self, task):
        rate = 1.5
        self.model.setR(self.model.getR() - rate)
        return Task.cont
    def ForwardsRoll(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyForwardsRoll, 'forwards-roll')
        else: 
            self.taskMgr.remove('forwards-roll')
    def ApplyForwardsRoll(self, task):
        rate = 1.5
        self.model.setP(self.model.getP() + rate)
        return Task.cont
    def BackwardsRoll(self, keyDown):
        if keyDown: 
            self.taskMgr.add(self.ApplyBackwardsRoll, 'backwards-roll')
        else: 
            self.taskMgr.remove('backwards-roll')
    def ApplyBackwardsRoll(self, task):
        rate = 1.5
        self.model.setP(self.model.getP() - rate)
        return Task.cont

    # def DirectionalInput(self, keyDown):
    #     if keyDown: return
    #     else: return
    # def ApplyDownwardsThrust(self, task):
    #     return Task.cont
    # class MovementControls():        
    #     def negX(self,keyDown):
    #         if keyDown:
    #             taskMgr.add(self.mvNegX, 'moveNegX')
    #         else:
    #             taskMgr.remove('moveNegX')
    #             self.acceptOnce('arrow_left', self.negX, [1])
    #             self.acceptOnce('arrow_left-up',self.negX,[0])
    #     def mvNegX(self, task):
    #         self.player.setX(self.player,-1)                  
    #         return task.cont
    #     def negY(self,keyDown):
    #         if keyDown:
    #             taskMgr.add(self.mvNegY, 'moveNegY')
    #         else:
    #             taskMgr.remove('moveNegY')
    #             self.acceptOnce('arrow_down', self.negY, [1])
    #             self.acceptOnce('arrow_down-up',self.negY,[0])
    #     def mvNegY(self, task):
    #         self.player.setY(self.player,-1)                  
    #         return task.cont
    #     def plusX(self,keyDown):
    #         if keyDown:
    #             taskMgr.add(self.mvPlusX, 'movePlusX')
    #         else:
    #             taskMgr.remove('movePlusX')
    #             self.acceptOnce('arrow_right', self.plusX, [1])
    #             self.acceptOnce('arrow_right-up',self.plusX,[0])
    #     def mvPlusX(self, task):
    #         self.player.setX(self.player,1)                  
    #         return task.cont
    #     def plusY(self,keyDown):
    #         if keyDown:
    #             taskMgr.add(self.mvPlusY, 'movePlusY')
    #         else:
    #             taskMgr.remove('movePlusY')
    #             self.acceptOnce('arrow_up', self.plusY, [1])
    #             self.acceptOnce('arrow_up-up',self.plusY,[0])      
    #     def mvPlusY(self, task):
    #         self.player.setY(self.player,1) 
    #         return task.cont
            