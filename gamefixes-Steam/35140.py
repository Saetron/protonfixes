""" Game fix Batman Arkham Asylum
    (Currently no contollers)
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Needs windxp, dotnet35, phyzx, d3dx9 """

    #Probably not needed when proton will be merged with newer wine
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dx9_43')
    util.protontricks('physx')
    util._mk_syswow64() #pylint: disable=protected-access

#TODO Controllers fixes
