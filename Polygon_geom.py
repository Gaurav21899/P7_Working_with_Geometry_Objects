import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_Ayodhya_Rameshwaram"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_charkop = 72.82190281349168
y_charkop = 19.213723099498782

x_Ayodhya = 82.21315797881975
y_Ayodhya = 26.801878733546854

x_Rameshwaram = 79.32067227711936
y_Rameshwaram = 9.288824973942063


# Point Object
pnt_Mumbai_obj = arcpy.Point(x_charkop, y_charkop)
pnt_Ayodhya_obj = arcpy.Point(x_Ayodhya, y_Ayodhya)
pnt_Rameshwaram_obj = arcpy.Point(x_Rameshwaram, y_Rameshwaram)

# spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

polygon_array = arcpy.Array()

polygon_array.add(pnt_Mumbai_obj)
polygon_array.add(pnt_Ayodhya_obj)
polygon_array.add(pnt_Rameshwaram_obj)

polygon_geom = arcpy.Polygon(polygon_array, spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, output_fc_path)

print("Process Completed")