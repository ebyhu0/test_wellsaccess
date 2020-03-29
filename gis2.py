import sys
import os

# edit these paths to match your setup
arcver = "10.7"
# Anaconda home folders
conda32 = r"C:\Users\ebyhu0\AppData\Local\Continuum\anaconda3_32bit"
conda64 = r"C:\Users\ebyhu0\AppData\Local\Continuum\anaconda3"
# here are the conda environments you've set up use with ArcGIS
# arc1022 is the environment setup for ArcGIS
conda_env32 = "{}/envs/{}".format(conda32, "arc1070")
conda_env64 = "{}/envs/{}".format(conda64, "arc1070")

# do not edit below this line

# ArcGIS Python home folders
# i.e. C:\Python27\ArcGIS10.2
arcver = arcver[:4]
arcpy32 = r"C:\Python27\ArcGIS10.7{}".format(arcver)
arcpy64 = r"C:\Python27\ArcGIS10.7{}".format(arcver)

print ('done')

try:
        if sys.version.find("64 bit") < 0:
            conda_path = os.path.normpath(conda_env32)
            arcpy_path = os.path.normpath(arcpy32)
            arcpy_pthfile = os.path.normpath(
                arcpy_path + "/lib/site-packages/desktop{}.pth".format(arcver))
            print ('done1')    
        else:
            conda_path = os.path.normpath(conda_env64)
            arcpy_path = os.path.normpath(arcpy64)
            arcpy_pthfile = os.path.normpath(
                arcpy_path + "/lib/site-packages/DTBGGP64.pth")
            print ('done2')
        for p in [conda_path, arcpy_path, arcpy_pthfile]:
            if not os.path.exists(p):
                raise Exception("{} not found".format(p))
        
        ## print(sys.prefix)
        ## print(conda_path)

        # If running ArcGIS's Python, add conda modules to path
        if (sys.executable.lower().find("desktop" + arcver) != -1
            or sys.prefix.lower().find("arcgis10") != -1):
            sys.path.append(os.path.dirname(arcpy_path))
            conda_site = os.path.join(conda_path, "lib", "site-packages")
            if not os.path.isdir(conda_site):
                raise Exception()
            sys.path.append(conda_site)
            print("usercustomize.py: added conda paths to arc")
            print ('done3')
        # if running Anaconda add arcpy to path
        elif sys.prefix.lower() == conda_path.lower():
            with open(arcpy_pthfile, "r") as f:
                sys.path +=  [p.strip() for p in f.readlines()]
            print("usercustomize.py: added arcpy paths to conda")
            print ('done4')
except Exception as msg:
    print(msg)
    pass


print ('Done5')