class PLC:
   """ Planetary parameters in SI units  """     
   #def __init__(self,body,version='Tosi2013',debug=0):
   def __init__(self,body='Mercury',version='up2date',debug=2):
      import numpy as np
      import sys
      from GV import GV
      gc = GV()
      # PLANET-DEPENDENT PARAMETERS
      if body=='Mercury':#&&=
         if version=='up2date':#&&=
            # Linear [m]
            self.Rpl   = 2.439e6 # Planetary radius [Perry et al 2015]
            self.Rcore = 2.02e6 # Core radius [Hauck et al 2013]
            self.Cr    = 35.e3  # Crustal thickness [Padovan et al 2015]
            # Mass [kg]
            self.Mass = 3.3e23  # [Smith et al. 2012] 
            # Densities [kg/m3] from Hauck et al. (2013)
            self.dOS = 3380. # OS: Outer Shell
            self.dCo = 6980. # Co: Core
            # Temperatures [K]
            self.TS  = 440.   # Surface 
            self.Tcmb = 1900. # CMB 
            # Maximum melting pressure (above which, ie deeper, melt
            # will not raise).
            self.MaxMeltP = 100.e9 # GPa (i.e., melt buoyant in the entire mantle)
            # Orbital data
            self.ecc  = 0.2056  # eccentricity [1]
            self.a    = 57.91e9 # semimajor axis [m] (Mercury fact sheet)
            self.Msun = 1.9885e30 # mass of the Sun [kg] (Sun fact sheet) 
            # Derive orbital period
            self.n    = ((gc.G*self.Msun)/self.a**3.)**(1./2.) #[1/s]
            # Factor for the Calculation of the total tidal dissipation
            self.Edotf= 21./2. # This corresponds to a SOR 1:1.Segatz et al. (1988)
                               # It might be different for Mercury.
            self.Rtidal=2.2e6  # Top of the tidal dissipating region#=&&
         elif version=='Tosi2013':#&&=
            # Linear [m]
            self.Rpl   = 2.440e6 # Table 2 
            self.Rcore = 2.040e6 # Table 2
            self.Cr    = 35.e3  # Crustal thickness [Padovan et al 2015]
            # Mass [kg]
            self.Mass = 3.3e23  # [Smith et al. 2012] 
            # Densities [kg/m3] from Hauck et al. (2013)
            self.dOS = 3500. # Table 2
            self.dCo = 7200. # Table 2
            # Temperatures [K]
            self.TS  = 440.   # Table 2
            self.Tcmb = 1890. # Table 2
            # Maximum melting pressure (above which, ie deeper, melt
            # will not raise).
            self.MaxMeltP = 100.e9 # Pa (i.e., melt buoyant in the entire mantle)
            # Orbital data
            self.ecc  = 0.2056  # eccentricity [1]
            self.a    = 57.91e9 # semimajor axis [m] (Mercury fact sheet)
            self.Msun = 1.9885e30 # mass of the Sun [kg] (Sun fact sheet) 
            # Derive orbital period
            self.n    = ((gc.G*self.Msun)/self.a**3.)**(1./2.) #[1/s]
            # Factor for the Calculation of the total tidal dissipation
            self.Edotf= 21./2. # This corresponds to a SOR 1:1.Segatz et al. (1988)
                               # It might be different for Mercury.
            self.Rtidal=2.2e6  # Top of the tidal dissipating region#=&&
         if(self.Rtidal<=self.Rcore):
            print ("Rtidal cannot be <= Rcore")
            sys.exit()#=&&
      elif body=='Moon':#&&=
         # Linear [m]
         self.Rpl   = 1.74e6  # Planetary radius [GAIA spreadsheet]
         self.Rcore = 3.9e5   # Core radius [GAIA spreadsheet]
         #self.Cr    = 38.5e3  # Crustal thickness [Wieczorek et al 2014]
         self.Cr    = 40.e3  # Crustal thickness [Laneuville et al 2013]
         # Mass [kg]
         self.Mass = 7.346e22 # [Smith et al. 2012] 
         # Densities [kg/m3] from Hauck et al. (2013)
         self.dOS = 3300. # OS: Outer Shell [Moon Fact sheet]
         self.dCo = 7000. # Co: Core
         # Temperatures [K]
         self.TS  = 250.   # Surface 
         self.Tcmb = 1900. # CMB 
         # Maximum melting pressure (above which, ie deeper, melt
         # will not raise).
         self.MaxMeltP = 100.e9 # Pa (i.e., melt buoyant in the entire mantle)
         # Orbital data (for an orbit around the Earth)
         self.ecc    = 0.0549    # eccentricity [Moon fact sheet]
         self.a      = 3.844e8   # semimajor axis [m] (Moon fact sheet)
         self.MEarth = 5.97e24 # mass of the Sun [kg] (Moon fact sheet) 
         # Derive orbital period
         self.n    = ((gc.G*self.MEarth)/self.a**3.)**(1./2.) #[1/s]
         # Factor for the Calculation of the total tidal dissipation
         self.Edotf= 21./2.  # This corresponds to a SOR 1:1.Segatz et al. (1988)
                             # It might be different for Mercury.
         self.Rtidal=1.065e6 # Top of the tidal dissipating region
         if(self.Rtidal<=self.Rcore):
            print ("Rtidal cannot be <= Rcore")
            sys.exit()
         # Internal heating#=&&
      elif body=='Mars':#&&=
         # Sources: MaFS [Mars Fact Sheet], R11 [Rivoldini et al, 2011]
         #          N04 [Neumann et al., 2004] WZ04 [Wieczorek & Zuber, 2004]
         #          P15 [Plesa et al., 2015]
         # Linear [m]
         self.Rpl   = 3.3895e6 # Planetary radius [R11==MaFS]
         self.Rcore = 1.794e6  # [R11] [1.7e6 in MaFS]
         self.Cr    = 50.e3  # Crustal thickness [WZ04, sigma 12 km]
         self.NCr   = 32.e3  # Northern hemisphere modal Cr thickness [N04]
         self.SCr   = 58.e3  # Southern hemisphere modal Cr thickness [N04]
         # Mass [kg]
         self.Mass = 6.41855e23 # [R11] [MaFS=6.4171e23] 
         # Densities [kg/m3] 
         self.dOS = 3500. # OS: Outer Shell [P15] 
         self.dCo = 6433. # Obtained from Rcore, rhomean, and self.dOS with TwoLModel.py
         # Temperatures [K]
         #self.TS  = 210.   # Surface [Equilibrium temperature with albed=0.25 from SolarConstant.py]
         self.TS  = 230.   # Global mean surface temperature from Yang class, UTEXAS (in Papers)
         self.Tcmb = 2225. # CMB [TS+DeltaT across the mantle from Plesa et al., 2015] 
         # Maximum melting pressure (above which, ie deeper, melt
         # will not raise).
         self.MaxMeltP = 7.e9 # Pa 
         # Orbital data 
         self.ecc    = 0.0935    # eccentricity [MaFS]
         self.a      = 2.2792e8   # semimajor axis [m] (MaFS)
         self.Msun   = 1.9885e30 # mass of the Sun [kg] (Sun fact sheet) 
         # Derive orbital period
         self.n    = ((gc.G*self.Msun)/self.a**3.)**(1./2.) #[1/s] #=&&
         # Factor for the Calculation of the total tidal dissipation
         self.Edotf= 21./2. # This corresponds to a SOR 1:1.Segatz et al. (1988)
                            # It might be different for Mars.
         self.Rtidal=2.2e6  # Top of the tidal dissipating region#=&&
      else:
         print ("Planet unknown or its")
         print ("data are not available")
         sys.exit()

         
      # PLANET-INDEPENDENT PARAMETERS
      if version=='up2date':
         self.Cp  = 1200.  # [J/kg/K] Ina's spreadsheet
         self.Ka  = 1.e-6  # [m2/s] Thermal diffusivity
         # Rheological parameters (Tref,Dref,and etaref should be consistent)
         #self.etaref = 1.e19 # Pa s
         #self.etaref = 5.e19 # Pa s
         self.etaref = 1.e20 # Pa s
         #self.etaref = 5.e20 # Pa s
         #self.etaref = 1.e21 # Pa s
         self.TrefKa = 1600    # K 
         self.PrefPa = 3e9     # Pa
         self.alfa   = 3.e-5 # 1/K (This is the value adopted by Roberts & Barnouin)
         # mantle's k is obtained from Ka,dOS, and Cp. Regolith/crust might have lower
         # conductivity, so and independent value can be set here.
         self.kc  = 3.3 # [W/m/K] thermal conductivity regolith/crust
      elif version=='Tosi2013':
         self.Cp  = 1200.  # Table 2
         self.Ka  = 9.523809523809523e-7  # Reverse engineered to obain km=4
         #self.Ka  = 7.142857142857143e-07 # Reverse engineered to obain km=3
         # Rheological parameters (Tref,Dref,and etaref should be consistent)
         #self.etaref = 4.46e21 # Pa s # Tosi's (2013) refernce value for 2D simulations
         self.etaref = 1e21 # 
         self.TrefKa = 1600    # K 
         self.PrefPa = 3e9     # Pa
         self.alfa   = 2.e-5 # 1/K
         # mantle's k is obtained from Ka,dOS, and Cp. Crust might have lower
         # conductivity, so and independent value can be set here.
         self.kc  = 3.3 # [W/m/K] thermal conductivity crust
      elif version=='Mars':
         self.Cp  = 1200. # P15, Table 3 
         self.Ka  = 1e-6  # P15, Table 3
         # Rheological parameters (Tref,Dref,and etaref should be consistent)
         #self.etaref = 4.46e21 # Pa s # Tosi's (2013) refernce value for 2D simulations
         self.etaref = 1e21   # P15, who uses between 1e20 e 1e23 
         self.TrefKa = 1600   # K 
         self.PrefPa = 3e9    # Pa
         self.alfa   = 2.5e-5 # 1/K [P15, which also considers 4.26]
         # mantle's k is obtained from Ka,dOS, and Cp. Crust might have lower
         # conductivity, so and independent value can be set here.
         self.kc  = 2. # or 3 [P15] [W/m/K] thermal conductivity crust

      # DERIVED QUANTITIES
      self.D = self.Rpl-self.Rcore # [m] Mantle thickness
      self.DeltaT = self.Tcmb-self.TS # [K] T scaling
      self.T0  = self.TS/self.DeltaT
      self.km  = self.Ka*self.dOS*self.Cp # [W/m/K] thermal conductivity mantle  
      self.g0 = (gc.G*self.Mass)/(self.Rpl**2.) #[m/s2] grav. acc.
      # Additional Scaling Factors
      self.Pscale  = self.dOS*self.g0*self.D  # [Pa] pressure scale
      self.Cpscale = (self.g0*self.D)/(self.DeltaT) # [J/kg/K] specific heat scale
      self.vscaleman  = self.Ka/self.D   # [m/s] velocity scale mantle (~1e-12 m/s)
      print "Vscale mant: m/s",self.vscaleman
      print "Vscale mant: cm/y",self.vscaleman*1e2*gc.sXy
      #self.vscale  = np.sqrt(self.Cp*self.DeltaT)   # [m/s] velocity scale (~ km/s)
      self.vscaleimp  = np.sqrt(self.g0*self.D)   # [m/s] velocity scale impacts (~ km/s)
      self.sEscale = self.Cp*self.DeltaT # [J/kg] specific energy scale
      self.tscale  = self.D*self.D/self.Ka
      # Rayleigh number
      self.Ra = (self.dOS*self.g0*self.alfa*self.DeltaT*self.D**3.)/(self.Ka*self.etaref)
      # Dissipation number (eg, eq.16 of King et al.,2010, JGI)
      self.Di = (self.alfa*self.g0*self.D)/self.Cp
      # Internal heating Rayleigh number factor, which corresponds to RaH/Hr in
      # equation (6.10.26) of Schubert et al. (2001). This works, if needed, for
      # any form internal energy source.
      #self.RaH_Hm3 = (self.alfa*self.dOS**3.*self.g0*self.Cp*self.D**5.)/(self.etaref*self.km*2.)
      self.RaH_Hkg = (self.alfa*self.dOS**2.*self.g0*self.D**5.)/(self.etaref*self.km*self.Ka)
      self.RaH_Hm3 = (self.alfa*self.dOS*self.g0*self.D**5.)/(self.etaref*self.km*self.Ka)
      # For use in the Boussinesq module, you need the factor to convert the energy produced
      # into a non dimensional quantity (the var_q used in the Boussinesq)
      # Non-dimensional factor for internal heating expressed in W/kg.
      self.qScaleWkg = (self.D**2.*self.dOS)/(self.km*self.DeltaT)
      # Non-dimensional factor for internal heating expressed in W/m3.
      self.qScaleWm3 = (self.D**2.)/(self.km*self.DeltaT)
      # Refernce depth and temperature
      self.Tref = (self.TrefKa - self.TS)/self.DeltaT
      self.Pref = self.PrefPa/self.Pscale
#      print "\******* LINEAR SCALING FACTORS ******"
#      print "D = %e"%(self.D)," m"
#      print "t = %e"%(self.tscale)," s"
      print "\n => => => => USING VERSION  %s <= <= <= <="%version
      print " => => => => USING VERSION  %s <= <= <= <="%version
      print " => => => => USING VERSION  %s <= <= <= <=\n"%version
      self.AgeOfSS = (4.5e9*365.*24*60*60)/self.tscale
      print "; t = %e"%(self.tscale/gc.sXMy)," My"
      print "\n;--------- global ini entries -------"
      print "Ra   = %e"%(self.Ra)
      print "Tref = %5.4f"%(self.Tref)
      print "Dref = %5.4f"%(self.Pref)
      print "T0   = %5.4f"%(self.T0)
      print "MaxTime = %5.4f"%(self.AgeOfSS)," ; Age of Solar System"
      print "Di   = %e"%(self.Di)
      print ";-------------------------------------\n"
      if debug>0:
         print "Body,version = ",body,", ",version
         print "D      = ",self.D      
         print "DeltaT = ",self.DeltaT 
         print "TS     = ",self.TS
         print "T0     = ",self.T0     
         print "km     = ",self.km     
         print "g0     = ",self.g0     
         print "Tref   = ",self.Tref     
         print "Pref   = ",self.Pref     
         print "dOS    = ",self.dOS   
         print "dCo    = ",self.dCo   
         print "Cp     = ",self.Cp   
         print "etaref = ",self.etaref
         print "\n"
         #print "   = ",self.     

