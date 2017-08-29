class GV:
   """ Collection of constants [SI units]
       and useful quantities """
   def __init__(self):
      import numpy as np
      self.G = 6.6742e-11 # Gravitational constant [m3/kg/s2] (Mohr et al., 2016).
      self.pi = np.pi     # [1]
      self.fp3G = 4.*self.pi*self.G/3.
      self.sXd = 86400.  # Seconds per day
      self.sXy = self.sXd*365 # Seconds per year
      self.sXMy= self.sXy*1e6 # Seconds per million years
      self.C2K = 273.15 # Celsius to Kelvin conversion
      self.SSa = 4.55e3 # Solar system age [My] (Bouvier and Wadhwa, 2010).
      self.Rgc = 8.3144621 # [J/K/mol] Gas constant
      self.d2r = np.pi/180.
      self.r2d = 180./np.pi

