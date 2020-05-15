# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Spotlight",
    "author" : "henry",
    "description" : "Create target light",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "Bijoul soyé indoulgent, siouplé",
    "category" : "Generic",
    "wiki_url": "https://www.google.com"
}

from . import operators, panels, properties
import bpy

def register():
    operators.register()
    panels.register()
    properties.register()     

def unregister():
    operators.unregister()
    panels.unregister()
    properties.unregister() 