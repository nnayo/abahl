"""
the purpose of this script is to generate E186 wing profile.

this is based on "Examples for a feature class and its view provider."
from Werner Mayer <wmayer[at]users.sourceforge.net>

This program is free software; you can redistribute it and/or modify  
it under the terms of the GNU General Public License (GPL)            
as published by the Free Software Foundation; either version 2 of     
the License, or (at your option) any later version.                   
for detail see the LICENCE text file.                                 

FreeCAD is distributed in the hope that it will be useful,            
but WITHOUT ANY WARRANTY; without even the implied warranty of        
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
GNU Library General Public License for more details.                  

You should have received a copy of the GNU Library General Public     
License along with FreeCAD; if not, write to the Free Software        
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  
USA                                                                   
"""

__author__ = 'Yann GOUY <yann_gouy@yahoo.fr>'

import FreeCAD, Part
from FreeCAD import Base
from pivy import coin

import math

class E186Profile:
    # Airfoil name : E186  (10,27%)
    profile = [
        [100.00000, 0.00000],
        [99.66700,  -0.06100],
        [98.72500,  -0.25500],
        [97.27500,  -0.55500],
        [95.35700,  -0.88100],
        [92.95200,  -1.19000],
        [90.06200,  -1.49300],
        [86.72300,  -1.79300],
        [82.97200,  -2.08800],
        [78.85400,  -2.37200],
        [74.41400,  -2.64300],
        [69.70200,  -2.89600],
        [64.77300,  -3.12700],
        [59.68100,  -3.33200],
        [54.48300,  -3.50700],
        [49.23900,  -3.64900],
        [44.00700,  -3.75400],
        [38.84700,  -3.81900],
        [33.81500,  -3.83900],
        [28.96800,  -3.81200],
        [24.36000,  -3.73200],
        [20.04000,  -3.59700],
        [16.05400,  -3.40400],
        [12.44400,  -3.14900],
        [9.24400,   -2.83300],
        [6.48400,   -2.45500],
        [4.18700,   -2.01800],
        [2.37000,   -1.53000],
        [1.04600,   -1.00200],
        [0.22500,   -0.46800],
        [0.00000,   0.07000],
        [0.36700,   0.69400],
        [1.19600,   1.41100],
        [2.47500,   2.15900],
        [4.19100,   2.90400],
        [6.33000,   3.62000],
        [8.87400,   4.28900],
        [11.80000,  4.89500],
        [15.07900,  5.42400],
        [18.67800,  5.86100],
        [22.55800,  6.19200],
        [26.67700,  6.39600],
        [31.00700,  6.44500],
        [35.52900,  6.32700],
        [40.22400,  6.04200],
        [45.07300,  5.60000],
        [50.05200,  5.02200],
        [55.13800,  4.34600],
        [60.28300,  3.63100],
        [65.41200,  2.92200],
        [70.44700,  2.24900],
        [75.31400,  1.63700],
        [79.93600,  1.10400],
        [84.23900,  0.66300],
        [88.15400,  0.32200],
        [91.61200,  0.08500],
        [94.55200,  -0.05000],
        [96.90700,  -0.09100],
        [98.61900,  -0.06600],
        [99.65400,  -0.02100],
        [100.00000, 0.00000],
    ]

    profile_up = [
        [0.00000,   0.07000],
        [0.36700,   0.69400],
        [1.19600,   1.41100],
        [2.47500,   2.15900],
        [4.19100,   2.90400],
        [6.33000,   3.62000],
        [8.87400,   4.28900],
        [11.80000,  4.89500],
        [15.07900,  5.42400],
        [18.67800,  5.86100],
        [22.55800,  6.19200],
        [26.67700,  6.39600],
        [31.00700,  6.44500],
        [35.52900,  6.32700],
        [40.22400,  6.04200],
        [45.07300,  5.60000],
        [50.05200,  5.02200],
        [55.13800,  4.34600],
        [60.28300,  3.63100],
        [65.41200,  2.92200],
        [70.44700,  2.24900],
        [75.31400,  1.63700],
        [79.93600,  1.10400],
        [84.23900,  0.66300],
        [88.15400,  0.32200],
        [91.61200,  0.08500],
#        [94.55200,  -0.05000],
#        [96.90700,  -0.09100],
#        [98.61900,  -0.06600],
#        [99.65400,  -0.02100],
#        [100.00000, 0.00000],
    ]


    def __init__(self, obj):
        obj.Proxy = self

        """ Add some custom properties to our box feature """
        obj.addProperty('App::PropertyLength','side0_cord','e186','side #0 cord').side0_cord = 500.0
        obj.addProperty('App::PropertyVector','side0_position','e186','side #0 position').side0_position = FreeCAD.Vector(0.0, 0.0, 0.0)
        obj.addProperty('App::PropertyFloat','side0_ratio','e186', 'side #0 thickness ratio from nominal').side0_ratio = 5.0
        obj.addProperty('App::PropertyLength','side1_cord','e186','side #1 cord').side1_cord = 500.0
        obj.addProperty('App::PropertyVector','side1_position','e186','side #1 position').side1_position = FreeCAD.Vector(-707.0, 707.0, 0.0)
        obj.addProperty('App::PropertyFloat','side1_ratio','e186', 'side #1 thickness ratio from nominal').side1_ratio = 5.0
        obj.addProperty('App::PropertyBool','up_only','e186', 'upper part only').up_only = True
        obj.addProperty('App::PropertyFloat','up_side0_ratio','e186', 'up side #0 thickness ratio from nominal').up_side0_ratio = 15.0
        obj.addProperty('App::PropertyFloat','up_side1_ratio','e186', 'up side #1 thickness ratio from nominal').up_side1_ratio = 15.0

    def onChanged(self, fp, prop):
        """ Print the name of the property that has changed """
        FreeCAD.Console.PrintMessage('Change property: ' + str(prop) + '\n')
        #FreeCAD.Console.PrintMessage('fp = %r\n' % fp)
        #FreeCAD.Console.PrintMessage('dir(fp) = %r\n' % dir(fp))
        if prop in ('cord0', 'vector0', 'ratio0', 'cord1', 'vector1', 'ratio1', 'up_only', 'up_side0_ratio', 'up_side1_ratio'):
            self.execute(fp)

    def execute(self, fp):
        """ Print a short message when doing a recomputation, this method is mandatory """
        #FreeCAD.Console.PrintMessage('\nrecompute profile\n')

        # compute dimensions
        if fp.up_only:
            profile = E186Profile.profile_up
            reverse = list(profile)
            reverse.reverse()

            x_ratio = float(fp.side0_cord) / 100.
            z_ratio = fp.side0_ratio
            pos = fp.side0_position

            vectors0 = []
            for (x, z) in profile:
                vectors0.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))

            z_ratio = fp.up_side0_ratio
            for (x, z) in reverse:
                vectors0.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))
            vectors0.append(vectors0[0])    # close the wire
            #FreeCAD.Console.PrintMessage('vectors0 = %r\n' % vectors0)

            x_ratio = float(fp.side1_cord) / 100.
            z_ratio = fp.side1_ratio
            pos = fp.side1_position

            vectors1 = []
            for (x, z) in profile:
                vectors1.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))

            z_ratio = fp.up_side1_ratio
            for (x, z) in reverse:
                vectors1.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))
            vectors1.append(vectors1[0])    # close the wire

        else:
            profile = E186Profile.profile

            x_ratio = float(fp.side0_cord) / 100.
            z_ratio = fp.side0_ratio
            pos = fp.side0_position

            vectors0 = []
            for (x, z) in profile:
                vectors0.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))
                FreeCAD.Console.PrintMessage('x, z = %f, %f\n' % (x, z))

            x_ratio = float(fp.side1_cord) / 100.
            z_ratio = fp.side1_ratio
            pos = fp.side1_position

            vectors1 = []
            for (x, z) in profile:
                vectors1.append(FreeCAD.Vector(-x * x_ratio + pos.x, 0 + pos.y, z * z_ratio + pos.z))

        face0 = Part.Face(Part.makePolygon(vectors0))
        face1 = Part.Face(Part.makePolygon(vectors1))
        wire0 = face0.Wires[0]
        wire1 = face1.Wires[0]
        surf = Part.makeRuledSurface(wire0, wire1)

        shell = Part.Shell(surf.Faces)
        FreeCAD.Console.PrintMessage('face0 = %r\n' % face0)
        shell.add(face0)
        shell.add(face1)

        shell = Part.Shell(shell.Faces)
        solid = Part.Solid(shell)
        fp.Shape = solid


class ViewProviderE186Profile:
    def __init__(self, obj):
        """ Set this object to the proxy object of the actual view provider """
        obj.Proxy = self

    def attach(self, obj):
        """ Setup the scene sub-graph of the view provider, this method is mandatory """
        return

    def updateData(self, fp, prop):
        """ If a property of the handled feature has changed we have the chance to handle this here """
        return

    def getDisplayModes(self,obj):
        """ Return a list of display modes. """
        modes=[]
        return modes

    def getDefaultDisplayMode(self):
        """ Return the name of the default display mode. It must be defined in getDisplayModes. """
        return 'Shaded'

    def setDisplayMode(self, mode):
        """ Map the display mode defined in attach with those defined in getDisplayModes.
            Since they have the same names nothing needs to be done. This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """ Print the name of the property that has changed """
        FreeCAD.Console.PrintMessage('Change property: ' + str(prop) + '\n')

    def getIcon(self):
        """ Return the icon in XMP format which will appear in the tree view. This method is optional
            and if not defined a default icon is shown.
        """
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
                '16 16 6 1',
                ' 	c None',
                '.	c #141010',
                '+	c #615BD2',
                '@	c #C39D55',
                '#	c #000000',
                '$	c #57C355',
                '        ........',
                '   ......++..+..',
                '   .@@@@.++..++.',
                '   .@@@@.++..++.',
                '   .@@  .++++++.',
                '  ..@@  .++..++.',
                '###@@@@ .++..++.',
                '##$.@@$#.++++++.',
                '#$#$.$$$........',
                '#$$#######      ',
                '#$$#$$$$$#      ',
                '#$$#$$$$$#      ',
                '#$$#$$$$$#      ',
                ' #$#$$$$$#      ',
                '  ##$$$$$#      ',
                '   #######      '};
        """

    def __getstate__(self):
        """ When saving the document this object gets stored using Python's cPickle module.
            Since we have some un-pickable here -- the Coin stuff -- we must define this method
            to return a tuple of all pickable objects or None.
        """
        return None

    def __setstate__(self, state):
        """ When restoring the pickled object from document we have the chance to set some
            internals here. Since no data were pickled nothing needs to be done here.
        """
        return None


# create ramjet in current document
a = FreeCAD.ActiveDocument.addObject('Part::FeaturePython', 'e186')
E186Profile(a)
ViewProviderE186Profile(a.ViewObject)

