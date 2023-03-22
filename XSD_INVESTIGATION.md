
## Using xmlschema to validate S-123 GML files

install xmlschema


>>> sources = [open('/Users/nicolasoudard/Downloads/S-123 App_D-1 GMLFormat 1.0.0/S123/1.0/20170831/S123.xsd'), open('/Users/nicolasoudard/Downloads/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/s100gmlbase.xsd'), open('/Users/nicolasoudard/Downloads/S-123 App_D-1GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/s100gmlbaseExt.xsd'), open('/Users/nicolasoudard/Downloads/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfile.xsd'), open('/Users/nicolasoudard/Downloads/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfileExt.xsd'), open('/Users/nicolasoudard/Downloads/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfileLevels.xsd')]
>>> schema = xmlschema.XMLSchema(sources)
>>> schema.is_valid('/Users/nicolasoudard/Downloads/S-123 SampleData 1.0.0/MRS_ROOT/JSNPI123EX_A0001/JSNPI123EX_A0001.GML')
>>> schema.validate('/Users/nicolasoudard/Downloads/S-123 SampleData 1.0.0/MRS_ROOT/JSNPI123EX_A0001/JSNPI123EX_A0001.GML')

