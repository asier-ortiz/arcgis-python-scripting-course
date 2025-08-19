import arcpy
from sys import argv

Tank_Layer = sys.argv[1]
Retention_Ponds_Layer = sys.argv[2]
Buffer_Distance = sys.argv[3]
Danger_Areas_Output_FeatureClass = sys.argv[4]

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Process: Buffer (Buffer) (analysis)
Output_Feature_Class = "C:\\Users\\linkedin\\Desktop\\Exercise Files\\GISData\\PythonPracticeProject\\PythonPracticeProject.gdb\\Tanks_Buffer"
arcpy.analysis.Buffer(in_features=Tank_Layer, out_feature_class=Output_Feature_Class, buffer_distance_or_field=Buffer_Distance, line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")

# Process: Buffer (2) (Buffer) (analysis)
Output_Feature_Class_2_ = "C:\\Users\\linkedin\\Desktop\\Exercise Files\\GISData\\PythonPracticeProject\\PythonPracticeProject.gdb\\RetentionPonds_Buffer"
arcpy.analysis.Buffer(in_features=Retention_Ponds_Layer, out_feature_class=Output_Feature_Class_2_, buffer_distance_or_field=Buffer_Distance, line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")

# Process: Intersect (Intersect) (analysis)
arcpy.analysis.Intersect(in_features=[[Output_Feature_Class, ""], [Output_Feature_Class_2_, ""]], out_feature_class=Danger_Areas_Output_FeatureClass, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")



