class planets_data( object ):
    """
       Database of basic planetary data. After calling:
       from planets_data import *
       the data are stored in objects named after each planet and retrieved with the dot operator. 

       Available data (so far) are:
       name: name of the planet
       radius: mean planetary radius in m
       core: radius of the outer core in m (inferred)
       mass: planetary mass in kg
       gravity: surface gravity acceleration in m/s^2
       density: mean density in kg/m^3
       moif: moment of inertia factor I/MR^2
    """

    def __init__(self, data):
        self.name    = data['name']
        self.radius  = data['radius']
        self.core    = data['core']
        self.mass    = data['mass']
        self.gravity = data['gravity']
        self.density = data['density']
        self.moif    = data['moif']

        
mercury  = planets_data( {
           'name'   : "Mercury",
           'radius' : 2.4397e6,
           'core'   : 2.020e6,
           'mass'   : 3.3019e23,
           'gravity': 3.7,
           'density': 5427.,
           'moif'   : 0.336,
})

venus  = planets_data( {
           'name'   : "Venus",
           'radius' : 6.0518e6,    
           'core'   : 3.089e6,
           'mass'   : 4.8685e24,
           'gravity': 8.87,
           'density': 5234.9, 
           'moif'   : 0.33,
})

earth  = planets_data( {
           'name'   : "Earth",
           'radius' : 6.378e6,       
           'core'   : 3.48e6,
           'mass'   : 5.972e24,  
           'gravity': 9.807,
           'density': 5515.0, 
           'moif'   : 0.33,
})

moon   = planets_data( {
           'name'   : "Moon",
           'radius' : 1.7347e6,        
           'core'   : 4e5,        
           'mass'   : 7.347e22,     
           'gravity': 1.622,
           'density': 3344.7, 
           'moif'   : 0.3931,
})

mars   = planets_data( {
           'name'   : "Mars",
           'radius' : 3.3895e6, 
           'core'   : 1.7e6,        
           'mass'   : 6.4185e23,  
           'gravity': 3.711,
           'density': 3934.9, 
           'moif'   : 0.3654,
})
