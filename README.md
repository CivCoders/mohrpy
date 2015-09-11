#mohrpy

Script for plotting Mohr's circle for a system of stess. Written in python using matplotlib package.

Add the following in matplotlib.patches.Circle

     def set_center(self, xy):
          """
          Set the center of the circle
          """
          self.center = xy
     def get_center(self):
         'return the radius of circle'
         return self.xy

