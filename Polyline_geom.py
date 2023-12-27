import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_To_Ayodhya"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_charkop = 72.82190281349168
y_charkop = 19.213723099498782

x_Ayodhya = 82.21315797881975
y_Ayodhya = 26.801878733546854

# Point Object
pnt_Mumbai_obj = arcpy.Point(x_charkop, y_charkop)
pnt_Ayodhya_obj = arcpy.Point(x_Ayodhya, y_Ayodhya)

# spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Array Object
polyline_array = arcpy.Array()

polyline_array.add(pnt_Mumbai_obj)
polyline_array.add(pnt_Ayodhya_obj)

polyline_geom = arcpy.Polyline(polyline_array, spatial_ref)

arcpy.CopyFeatures_management(polyline_geom, output_fc_path)

print("process Completed")
