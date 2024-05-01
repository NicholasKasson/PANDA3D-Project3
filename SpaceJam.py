import sys, math
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
# from direct.task import Task
# from direct.gui.DirectGui import *
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
fullCycle = 60


class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept('escape', self.quit)
        #W is Forwards, S is backwards
        #A is Strafe Left, D is Strafe Right
        #Space is Upwards, Ctrl is Backwards
        #Q Rolls Left, E Rolls Right, despite being labelled as "turns" on the lecture slides
        #Z & X Rotate Left and Right Respectively
        #C and V Roll the Camera Forwards and Backwards respectively
#---------------------------------------------------------------------Planet Placement Phase--------------------------------------------------------------------
        print("Phase 1: Planet Placement")
        self.Universe = spaceJamClasses.Universe(self.loader,"./Assets/Universe/Universe.x",self.render,'Universe',"./Assets/Universe/starfield-in-blue.jpg",(0,0,0),10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet1',"./Assets/Planets/pluto.jpg",(2832,-512,0),230)
        self.Planet2 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet2',"./Assets/Planets/jupiter.jpg",(797,492,0),110)      
        self.Planet3 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet3',"./Assets/Planets/moonLike.jpg",(-2290,-672,0),110)
        self.Planet4 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet4',"./Assets/Planets/orangePlanet.jpg",(-1864,-2672,0),210)    
        self.Planet5 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet5',"./Assets/Planets/redPlanet.jpg",(-800,800,0),80) 
        self.Planet6 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet6',"./Assets/Planets/yellowPlanet.png",(390,-820,0),65)
        self.Planet7 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet7',"./Assets/Planets/bluePlanet.jpg",(1200,-1850,0),80)
        self.Planet8 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet8',"./Assets/Planets/velvetPlanet.png",(1890,-2200,0),58)
        self.Planet9 = spaceJamClasses.Planet(self.loader,"./Assets/Planets/protoPlanet.x",self.render,'Planet9',"./Assets/Planets/healthyPlanet.png",(-1270,-100,0),115)
        self.Station1 = spaceJamClasses.SpaceStation(self.loader,"./Assets/station/spaceStation.x",self.render,'Station1',"./Assets/station/SpaceStation1_Dif2.png",(-3064,-3472,0),5)
        self.Station2 = spaceJamClasses.SpaceStation(self.loader,"./Assets/station/spaceStation.x",self.render,'Station2',"./Assets/station/SpaceStation1_Dif2.png",(610,472,40),6)
        self.Ship1 = spaceJamClasses.Ship(self.loader,"./Assets/blorg/theBorg.x",self.render,'Ship1',"./Assets/blorg/small_space_ship_2_color.jpg",(558,557,29),1)
        self.Ship2 = spaceJamClasses.Ship(self.loader,"./Assets/blorg/theBorg.x",self.render,'Ship2',"./Assets/blorg/small_space_ship_2_color.jpg",(631,532,2),1)
        self.Ship3 = spaceJamClasses.Ship(self.loader,"./Assets/blorg/theBorg.x",self.render,'Ship3',"./Assets/blorg/small_space_ship_2_color.jpg",(700,312,36),1)
        self.Ship4 = spaceJamClasses.Ship(self.loader,"./Assets/blorg/theBorg.x",self.render,'Ship4',"./Assets/blorg/small_space_ship_2_color.jpg",(692,42,8),1)
        self.Ship5 = spaceJamClasses.Ship(self.loader,"./Assets/blorg/theBorg.x",self.render,'Ship5',"./Assets/blorg/small_space_ship_2_color.jpg",(0,70,8),1)
        self.Hero = spaceJamClasses.Player(self.loader,"./Assets/blorg/theBorg.x",self.render,'Hero',"./Assets/blorg/small_space_ship_2_color.jpg",(0,0,0),1, (0, 90, 0))
        print("Phase 1: Done")
#---------------------------------------------------------------------Controller & Camera Modification--------------------------------------------------------------------
        print("Phase 2: Keybind Init")
        self.Hero.SetKeyBindings()
        # self.SetCamera()
        print("Phase 2: Done")
#---------------------------------------------------------------------Drone Placement Phase--------------------------------------------------------------------- 
        print("Phase 3: Drone Placement")
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawBaseballSeams(self.Planet2, nickName, j, 60)
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCircleXYDefense(self.Planet3, nickName, j)
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCircleXZDefense(self.Planet4, nickName, j)
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCircleYZDefense(self.Planet5, nickName, j)
        print("Phase 3: Done")
#---------------------------------------------------------------------Drone Placement Rules--------------------------------------------------------------------
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 280 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    def DrawCircleXYDefense(self, centralObject, droneName, step):
        unitVec = defensePaths.XYPath(step)
        unitVec.normalize()
        position = unitVec * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    def DrawCircleXZDefense(self, centralObject, droneName, step):
        unitVec = defensePaths.XZPath(step)
        unitVec.normalize()
        position = unitVec * 350 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    def DrawCircleYZDefense(self, centralObject, droneName, step):
        unitVec = defensePaths.YZPath(step)
        unitVec.normalize()
        position = unitVec * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    # def SetCamera(self):
    #     self.disableMouse()
    #     print("Mouse Control Disabled")
    #     self.camera.reparentTo(self.Hero.model)
    #     print("Camera Attached to Player")
    #     self.camera.setFluidPos(0,1,0)
    #     print("Following")
    def quit(self):
        sys.exit()
app = SpaceJam()
app.run()
