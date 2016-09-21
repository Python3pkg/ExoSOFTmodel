#@Author: Kyle Mede, kylemede@astron.s.u-tokyo.ac.jp

dirs_dict = {
# full path to input astrometry data file. [string]
'DIdataFile': '/mnt/HOME/MEGA/Dropbox/EclipseWorkspaceDB/ExoSOFT/examples/DIdata.dat',                
# full path to input radial velocity data file. [string]
'RVdataFile': '/mnt/HOME/MEGA/Dropbox/EclipseWorkspaceDB/ExoSOFT/examples/RVdata.dat',        
}

params_dict = {
#####################################
# Special Settings for the models ###
#####################################
# Operate in low eccenctricity mode? [bool]
# Then step through in sqrt(e)sin(omega) and sqrt(e)cos(omega) instead of e & omega directly
'lowEcc'   : (True,"low eccentricty stepping?"),
# Step through parameter space in Time of Center Transit (Inferior Conjunction)?  [bool]
'TcStep' : (False,"Step in Tc not T?"),
# take the time of center transit (inferior conjunction) into account? [bool]
'TcEqualT' : (True,"Fix Tc=T?"),
# force adding a value in degrees to argument of periapsis used in RV orbit fit [double]
'omegaPrv' : (0.0,"Custom fixed val added to RV omega in model"),
##################################################
## Special settings DI model:
# force adding a value in degrees to argument of periapsis used in DI orbit fit [double]
'omegaPdi' : (0.0,"Custom fixed val added to DI omega in model"),
}

data_dict = {
# Is the data in the DIdata.dat in PA,SA format? else, it is in E,N (x,y) format [bool]
'pasa'     : (False,"Is astrometry data in PA,SA format?"),
}

ranges_dict={
###################################################
# Ranges for acceptable random number inputs ######
###################################################
## For Omega, e, T, inc and omega, None indicates to use default ranges.
## For Omega and omega, values can vary outside ranges, but are shifted by 
## +/-360 befire being stored.
# Minimum/Maximum allowed value for the mass of the primary body [double][Msun]
# NOTE: For DI only cases, use mass1 values as total mass and set mass2 values to zero.
#       This will be done during start up otherwise.
'm1_min' : 0.2,
'm1_max' : 2.55,
# Minimum/Maximum allowed value for the mass of the secondary body [double][Msun]
# Note: 1Mj ~ 0.00095 Msun
'm2_min' : 0.0001,
'm2_max' : 0.005,
# Minimum/Maximum allowed value for the Parallax [double][mas]
'para_min' : 1.0,
'para_max' : 100.0,
# Minimum/Maximum allowed value for the Longitude of the Ascending Node [double][deg] OR None
# Default: [0,360] if 'dataMode' is '3D', else [0,180].
'long_an_min' : None,
'long_an_max' : None,
# Minimum/Maximum allowed value for the Eccentricity [double] OR None
# Default: [0,0.98]
'ecc_min' : None,
'ecc_max' : None,
# Minimum/Maximum value for the Time of Last Periapsis (or Time of Center Transit) [JD] OR None
# Default: [earliestsEpoch-period,earliestEpoch]
't_min' : 2449000,
't_max' : 2453500,
# Minimum/Maximum allowed value for the Period [double][yrs]
'p_min' : 1.0,
'p_max' : 50.0,
# Minimum/Maximum allowed value for the Inclination [double][deg] OR None
# Default: [0,180].  [0,90] is another popular choice.
'inc_min' : 1,
'inc_min' : 90,
# Minimum/Maximum allowed value for the Argument of Perigee [double][deg] OR None
# Default: [0,360]
'arg_peri_min' : -50,
'arg_peri_max' : 90,
# Minimum/Maximum values of Radial Velocity Offsets.  
# Must be one per set of RV data in same order as data comes in RVdata.dat, or the a single value to be used by all [comma separated list of doubles]
'offset_mins' :[-3],
'offset_maxs' :[3],
}

priors_dict={
############################
#    System Information    #
# ONLY FOR GAUSSIAN PRIORS #
############################
#best estimate of primary's mass, and error [double][Msun]
'm1_est' : 0.0,
'm1_err' : 0.0,
#best estimate of secondary's mass, and error [double][Msun]
'm2_est' : 0.0,
'm2_err' : 0.0,
#best estimate of parallax, and error [double][mas]
'para_est'  : 50,
'para_err'  : 2.5,
##################################
# Push prior functions into dict #
##################################
# For ALL: False indicates a flat prior. True indicates to use defaults.
'ecc_prior'    :(True,'Use prior for eccentricity?'),
'p_prior'    :(True,'Use prior for period?'),
# For the inclination prior, use strings or booleans to inducate the specific 
# function to use.  Either sin(i), cos(i) or flat.  True indicates sin(i).
'inc_prior'  :('cos',"inclination prior ['cos','sin',True or False]"),
# For m1 and m2: use strings to indicate specific prior function.
# For m1: ['PDMF', 'IMF', True or False], default is 'PDMF'.
'm1_prior':(True,"m1 prior "),
# for m2: ['PDMF', 'IMF', 'CMF', True or False], default is 'CMF'
'm2_prior':(True,"m2 prior ['PDMF', 'IMF', 'CMF', True or False]"),
'para_prior' :(True,'Use prior for parallax?'),
}

######################
# Merge All dicts#
######################
settings = {}
for key in dirs_dict:
    settings[key]=dirs_dict[key]
for key in params_dict:
    settings[key]=params_dict[key]
for key in data_dict:
    settings[key]=data_dict[key]
for key in ranges_dict:
    settings[key]=ranges_dict[key]
for key in priors_dict:
    settings[key]=priors_dict[key]
