# ***************************************************************************
# *   Copyright (c) 2021 David Carter <dcarter@davidcarter.ca>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************
"""Class for drawing fins"""

__title__ = "FreeCAD Fins"
__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"
    
import FreeCAD
import Part
import math

from App.Constants import FIN_CROSS_SQUARE, FIN_CROSS_ROUND, FIN_CROSS_AIRFOIL, FIN_CROSS_WEDGE, \
    FIN_CROSS_DIAMOND, FIN_CROSS_TAPER_LETE

from App.FinShapeHandler import FinShapeHandler

CROSS_SECTIONS = 100  # Number of cross sections for the ellipse

class FinSketchShapeHandler(FinShapeHandler):

    def __init__(self, obj):
        super().__init__(obj)

    def getFace(self):
        profile = self._obj.Profile
        print("Profile %s" % profile)
        print("Fully constrained %s" % str(profile.FullyConstrained))
        shape = profile.Shape
        print("Shape %s" % profile.Shape)
        if shape is None:
            print("shape is empty")
            return None
        else:
            return Part.Wire(shape)
            # auto shape = getProfileShape();
            # if(shape.isNull())
            #     err = "Linked shape object is empty";
            # else {
            #     auto faces = shape.getSubTopoShapes(TopAbs_FACE);
            #     if(faces.empty()) {
            #         if(!shape.hasSubShape(TopAbs_WIRE))
            #             shape = shape.makEWires();
            #         if(shape.hasSubShape(TopAbs_WIRE))
            #             shape = shape.makEFace(0,"Part::FaceMakerCheese");
            #         else
            #             err = "Cannot make face from profile";
            #     } else if (faces.size() == 1)
            #         shape = faces.front();
            #     else
            #         shape = TopoShape().makECompound(faces);
            # }

    def _makeProfiles(self):
        halfThickness = float(self._obj.RootThickness) / 2.0

        face1 = self.getFace()
        face1.translate(FreeCAD.Vector(0, -halfThickness, 0))

        face2 = self.getFace()
        face2.translate(FreeCAD.Vector(0,  halfThickness, 0))

        profiles = [face1, face2]
        return profiles
