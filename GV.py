class GV:
   """ Collection of constants [SI units]
       and useful quantities """
   def __init__(self):
      import numpy as np
      self.G = 6.6742e-11
      self.pi = np.pi
      self.fp3G = 4.*self.pi*self.G/3.
      self.sXd = 86400. 
      self.sXy = self.sXd*365
      self.sXMy= self.sXy*1e6
      self.C2K = 273.15
      self.SSa = 4.5e3 # [My] Solar system age
      self.Rgc = 8.3144621 # [J/K/mol] Gas constant
      self.d2r = np.pi/180.
      self.r2d = 180./np.pi

