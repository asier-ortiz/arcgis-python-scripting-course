import arcpy
strAprx = r'C:\Users\linkedin\Desktop\Exercise Files\GISData\MotoristAssistance\MotoristAssistance.aprx'
strOutFile = r'C:\Users\linkedin\Desktop\Exercise Files\GISData\BrokenLinks.txt'

aprx = arcpy.mp.ArcGISProject(strAprx)
mapObj = aprx.listMaps("New Orleans")[0]

outFile = open(strOutFile, 'w')

outFile.write("Broken Layers Report\n")
print ("Broken Layers Report Header written to file")

outFile.write(mapObj.name)

lstBroken = mapObj.listBrokenDataSources()
for eachLyr in lstBroken:
    outFile.write(eachLyr.name + '-' + eachLyr.dataSource)
    print (eachLyr.name + '-'+eachLyr.dataSource,"written to the file")

outFile.close()



