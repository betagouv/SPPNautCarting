<?xml version="1.0" encoding="UTF-8"?>
<!-- ============================================================================================= -->
<!--
	© Copyright 2015 ... (Draft - Copyright statement tbd)
	Prepared under NOAA contract
	
	License
  Certain parts of the text of this document refer to or are based on the standards of the International
  Organization for Standardization (ISO). The ISO standards can be obtained from any ISO member and from the
  Web site of the ISO Central Secretariat at www.iso.org.
    
  Permission to copy and distribute this document is hereby granted provided that this notice is retained
  on all copies, and that IHO & NOAA are credited when the material is redistributed or used in part or
	whole in derivative works.
	
  Certain parts of this work are derived from or were originally prepared as works for the UK Location Programme
  (UKLP) and GEMINI project and are (C) Crown copyright (UK). These parts are included under and subject to the
  terms of the Open Government license.

	Disclaimer	(Draft)
	This work is provided without warranty, expressed or implied, that it is complete or accurate or that it
	is fit for any particular purpose.  All such warranties are expressly disclaimed and excluded.
	
	Document history
	Version 1.0	2015-08-18	Raphael Malyankar (Jeppesen) for NOAA / IIC Technologies / IHO
            1.1 2015-09-16  Raphael Malyankar (Jeppesen) corrected element datasetDiscoveryMetadata to S100_DatasetDiscoveryMetadata
	-->
<!-- ============================================================================================= -->
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron">
  <sch:ns prefix="fn" uri="http://www.w3.org/2005/xpath-functions"/>
  <sch:ns prefix="gco" uri="http://www.isotc211.org/2005/gco"/>
  <sch:ns prefix="gmd" uri="http://www.isotc211.org/2005/gmd"/>
  <sch:ns prefix="gmx" uri="http://www.isotc211.org/2005/gmx"/>
  <sch:ns prefix="gml" uri="http://www.opengis.net/gml/3.2"/>
  <!--<sch:ns uri="http://www.isotc211.org/2005/gmi" prefix="gmi"/>-->
  <sch:ns uri="http://www.iho.int/s100/xc" prefix="S100XC"/>

  <!-- to do: adapt abstract test suite general test for by-value or by-reference or gco:nilReason (A.2.1) (not implemented - leave to tools?) -->
  <!-- require  EX_geographicBoundingBox or EX_GeographicDescription in dataset discovery when hierarchy level is dataset or absent (default=dataset) -->
    
  <sch:title>IHO S-100 Schematron validation rules for S-100 Exchange Catalogues</sch:title>

  <sch:pattern fpi="S100_2.0.0_4a-D.2.6_R16-17">
    <sch:title>Comparative validity of maximum and minimum display scales</sch:title>
    <sch:rule context="/S100XC:S100_ExchangeCatalogue/S100XC:S100_DatasetDiscoveryMetadata/S100XC:maximumDisplayScale">
      <sch:assert test="number() > 0">
        maximumDisplayScale must be a positive number.
      </sch:assert>
    </sch:rule>
    <sch:rule context="/S100XC:S100_ExchangeCatalogue/S100XC:S100_DatasetDiscoveryMetadata/S100XC:minimumDisplayScale">
      <sch:assert test="number() > 0">
        minimumDisplayScale must be a positive number.
      </sch:assert>
          <sch:assert test="not(../S100XC:maximumDisplayScale) or (number(../S100XC:maximumDisplayScale) &lt; number())">
        maximumDisplayScale must be less than minimumDisplayScale
      </sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Rules to test validity of bounding box coordinates (if any). Assumes lat/lon in decimal degrees, ranges +/-90.0 and +/-180.0. -->
  <sch:pattern is-a="S100_ValidBBoxPattern" fpi="S100_XC_ValidBBox">
    <sch:title>Validity of bounding box corners</sch:title>
      <sch:param name="bbox" value="//S100XC:boundingBox | //*[@gco:isoType = 'gmd:EX_GeographicBoundingBox']"/>
  </sch:pattern>

  <sch:pattern id="S100_ValidBBoxPattern" abstract="true" fpi="S100_BBox_LLDD_MinMax">
    <sch:title>Check the values of the bounding box min/max. Assumes values are latitude and longitude in decimal degrees in +/-90 or +/-180 range respectively.</sch:title>
    <sch:rule context="$bbox">
      <sch:assert test="gmd:westBoundLongitude and (string-length(gmd:westBoundLongitude) > 0) and (gmd:westBoundLongitude >= -180.0) and (gmd:westBoundLongitude &lt;= 180.0)" flag="badWB">
          westBoundLongitude must be present and in the range [-180.0, 180.0].
      </sch:assert>
      <sch:assert test="gmd:eastBoundLongitude and (string-length(gmd:eastBoundLongitude) > 0) and (gmd:eastBoundLongitude >= -180.0) and (gmd:eastBoundLongitude &lt;= 180.0)" flag="badEB">
          eastBoundLongitude must be present and in the range [-180.0, 180.0].
      </sch:assert>
      <sch:assert test="gmd:southBoundLatitude and (string-length(gmd:southBoundLatitude) > 0) and (gmd:southBoundLatitude >= -90.0) and (gmd:southBoundLatitude &lt;= 90.0)" flag="badSB">
          southBoundLatitude must be present and in the range [-90.0, 90.0].
      </sch:assert>
      <sch:assert test="gmd:northBoundLatitude and (string-length(gmd:northBoundLatitude) > 0) and (gmd:northBoundLatitude >= -90.0) and (gmd:northBoundLatitude &lt;= 90.0)" flag="badNB">
          northBoundLatitude must be present and in the range [-90.0, 90.0].
      </sch:assert>
      <sch:assert test="not(badEB or badWB) and (gmd:westBoundLongitude &lt; gmd:eastBoundLongitude)">
        westBoundLongitude (<sch:value-of select="gmd:westBoundLongitude"/>) must be less than eastBoundLongitude (<sch:value-of select="gmd:eastBoundLongitude"/>)
      </sch:assert>
        <sch:assert test="not(badNB or badSB) and (gmd:southBoundLatitude &lt; gmd:northBoundLatitude)">
        northBoundLatitude (<sch:value-of select="gmd:northBoundLatitude"/>) must be greater than southBoundLatitude (<sch:value-of select="gmd:southBoundLatitude"/>)
      </sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Test for availability or nilling of reference to ISO 19115 metadata file -->
  <sch:pattern fpi="S100_XC_ISO19115Filename">
    <sch:rule context="//S100XC:S100_DatasetDiscoveryMetadata/S100XC:S100_19115DatasetMetadata">
      <sch:assert test="@gco:nilReason or gmx:FileName[string-length(normalize-space(@src)) > 0]">
        Reference to ISO 19115 metadata file must be nilled or have the gmx:FileName@src attribute populated.
      </sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Tests that mandatory elements with string types are non-empty / non-blank.    -->
  <!-- Test for identifier sub-element of exchange catalogue. -->
  <sch:pattern fpi="S100_XC_cString_generic_exchangecatalog">
    <sch:title>Rule to check for presence of mandatory elements of type string</sch:title>
    <sch:rule context="/S100XC:S100_ExchangeCatalogue/S100XC:identifier/S100XC:identifier 
      | /S100XC:S100_ExchangeCatalogue/S100XC:identifier/S100XC:editionNumber
      | /S100XC:S100_ExchangeCatalogue/S100XC:exchangeCatalogueName
      | /S100XC:S100_ExchangeCatalogue/S100XC:exchangeCatalogueDescription|/S100XC:S100_ExchangeCatalogue/S100XC:metadataLanguage">
      <sch:assert test="string-length(normalize-space())"><sch:name/> must contain a string value that is not all whitespace</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Test for sub-elements of dataset discovery -->
  <sch:pattern fpi="S100_XC_cString_generic_DSDMD">
    <sch:title>Rule to check for presence of mandatory elements of type string in S100_DatasetDiscoveryMetadata</sch:title>
    <sch:p>Note: filePath CAN be empty, but not blank</sch:p>
    <sch:rule context="/S100XC:S100_ExchangeCatalogue/S100XC:datasetDiscoveryMetadata">
      <sch:assert test="string-length(normalize-space(S100XC:fileName)) > 0">S100_DatasetDiscoveryMetadata.filename must not be empty or blank</sch:assert>
      <sch:assert test="(string-length(S100XC:filePath) = 0) or (string-length(normalize-space(S100XC:filePath)) > 0)">S100_DatasetDiscoveryMetadata.filePath must not be blank (but may be empty)</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:description)) > 0">S100_DatasetDiscoveryMetadata.description must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:purpose)) > 0">S100_DatasetDiscoveryMetadata.purpose must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:specificUsage)) > 0">S100_DatasetDiscoveryMetadata.specificUsage must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:editionNumber)) > 0">S100_DatasetDiscoveryMetadata.editionNumber must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:horizontalDatumReference)) > 0">S100_DatasetDiscoveryMetadata.horizontalDatumReference must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:verticalDatum)) > 0">S100_DatasetDiscoveryMetadata.verticalDatum must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:soundingDatum)) > 0">S100_DatasetDiscoveryMetadata.soundingDatum must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:dataType)) > 0">S100_DatasetDiscoveryMetadata.dataType must not be empty or blank</sch:assert>
      <sch:assert test="string-length(normalize-space(S100XC:dataTypeVersion)) > 0">S100_DatasetDiscoveryMetadata.dataTypeVersion must not be empty or blank</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Test for sub-elements of product specification sub-element of dataset discovery -->
  <sch:pattern fpi="S100_XC_cString_generic_productSpecification">
    <sch:title>Rule to check for presence of mandatory elements of type string</sch:title>
    <sch:rule context="//S100XC:datasetDiscoveryMetadata/S100XC:productSpecification/S100XC:name 
      | //S100XC:datasetDiscoveryMetadata/S100XC:productSpecification/S100XC:version">
      <sch:assert test="string-length(normalize-space())"><sch:name/> must contain a string value that is not all whitespace</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- rule to check that role is either nilled or not empty -->
  <sch:pattern fpi="S100_XC_DSMD_role_Nillable">
    <sch:rule context="/S100XC:S100_ExchangeCatalogue/S100XC:datasetDiscoveryMetadata//gmd:role">
    <sch:assert test="(count(*) > 0) or (@gco:nilReason = 'inapplicable' or
      @gco:nilReason = 'missing' or 
      @gco:nilReason = 'template' or
      @gco:nilReason = 'unknown' or
      @gco:nilReason = 'withheld' or
      starts-with(@gco:nilReason, 'other:'))" flag="isNilled">
      The <sch:name/> element shall have a value or a valid Nil Reason.
    </sch:assert>
      <sch:assert test="isNilled or (gmd:CI_RoleCode and (string-length(gmd:CI_RoleCode/@codeListValue) > 0))">
          The codeListValue attribute does not have a value.
    </sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- Rule to allow productspecification to be omitted in S100_SupportFileDiscoveryMetadata only if dataType is Text -->
<!--  <sch:pattern fpi="S100_XC_productSpecification">
    <sch:rule context="//S100XC:supportFileDiscoveryMetadata">
      <sch:assert test="not(S100XC:dataType != 'Text') or S100XC:productSpecification">
        Support file discovery metadata element must contain a productSpecification element if the dataType is other than Text
      </sch:assert>
    </sch:rule>
  </sch:pattern>-->

  <!-- ========================================================================================== -->
  <!-- The following patterns are extracts from the Schematron Schema for the UK GEMINI Standard  -->
  <!-- Version 2.1 and are incuded subject to the terms applicable to that schema, reproduced     -->
  <!-- below.                                                                                     -->
  <!-- ========================================================================================== -->
  
  <!-- 
     James Rapaport                                
     SeaZone Solutions Limited                                                  
     2010-07-13
     
     This Schematron schema has been developed for the UK Location Programme (UKLP) by
     SeaZone Solutions Limited (SeaZone), with funding from Defra and CLG.
     
     It is designed to validate the constraints introduced in the GEMINI2.1 draft standard.
     Constraints have been taken from:
     
     UK GEMINI Standard, Version 2.1, August 2010.
     
     The schema has been developed for XSLT Version 1.0 and tested with the ISO 19757-3 Schematron
     XML Stylesheets issued on 2009-03-18 at http://www.schematron.com/tmp/iso-schematron-xslt1.zip 
     
     The schema tests constraints on ISO / TS 19139 encoded metadata. The rules expressed in this 
     schema apply in addition to validation by the ISO / TS 19139 XML schemas.
     
     The schema is designed to test ISO 19139 encoded metadata incorporating ISO 19136 (GML Version
     3.2.1) elements where necessary. Note that GML elements must be mapped to the Version 3.2.1 
     GML namespace - http://www.opengis.net/gml/3.2
     
     (C) Crown copyright, 2011
     
     You may use and re-use the information in this publication (not including logos) free of charge
     in any format or medium, under the terms of the Open Government Licence.
   
   
     Document History:
     
     2010-10-14 - Version 1.0
     Baselined version for beta release.  No technical changes against v0.11.
     
     2011-01-18 - Version 1.1
     - Metadata Point of Contact (Metadata Item 35) - test now ensures that at least one 
     metadata contact has a role of pointOfContact.
     - Temporal element (Metadata Item 7) - test changed so that it is nolonger the case 
     that only one gmd:temporalElement can be encoded for any gmd:extent element.
     
     2011-04-19 - Version 1.2a
     Changes to allow round trip interoperability with INSPIRE metadata.
     - Temporal extent (Metadata Item 7) - remove rule constraining temporal extent to 
     one only.
     - Geographic bounding box (Metadata Item 11, 12, 13, 14) - allow one or more geographic bounding box
     - Spatial reference system (Metadata Item 17) - remove rule constraining spatial reference
     system to only one.
     - Frequency of update (Metadata Item 24) - remove rule constraining frequency of update to single
     - Unique resource identifier (Metadata Item 36) - amend rule to allow 1 or more Unique resource identifier
     - Equivalent scale (Metadata Item 43) - remove rule constraining Equivalent scale to zero or 1
     
     2011-04-20 - Version 1.2b
     - Unique resource identifier (Metadata item 36) - change sense of failure message to 'one or more'
     - Spatial resolution (Metadata item 18) - remove rule that tests for units of measure
     
     2011-04-21 - Version 1.2c
     - Temporal extent (Metadata item 7) - temporal extent can be implemented as a gml:TimePeriod or 
     gml:TimeInstant. If gml:TimePeriod is used, the child elements are allowed to be gml:begin or gml:beginPosition, and
     gml:end or gml:endPosition.
     
     2011-05-09 - Version 1.2
     - Vertical extent (Metadata item 16) - remove rule restricting number of vertical extent elements
     to 0 or 1.
	 
	2012-12-20 - Version 1.3a
	 - Metadata language - ensure that metadata contains one metadata language element. Gemini2-mi33 edited and rule added.
	2013-02-01 - Version 1.3
	 - as above, but tested by data.gov.uk & EDINA, so accepted for publication
-->
  
  <!-- ========================================================================================== -->
  <!-- Abstract Patterns                                                                          -->
  <!-- ========================================================================================== -->
  
  <!-- Test that an element has a value or has a valid nilReason value -->
  <!-- Provisionally extended to account for child elements - RMM -->
  <sch:pattern abstract="true" id="TypeNillablePattern_S100Ext">
    <sch:rule context="$context">
      <sch:assert test="(string-length(.) &gt; 0) or (count(*) > 0) or
        (@gco:nilReason = 'inapplicable' or
        @gco:nilReason = 'missing' or 
        @gco:nilReason = 'template' or
        @gco:nilReason = 'unknown' or
        @gco:nilReason = 'withheld' or
        starts-with(@gco:nilReason, 'other:'))">
        The <sch:name/> element shall have a value, element content, or a valid Nil Reason.
      </sch:assert>
    </sch:rule>
  </sch:pattern>
  
  <!-- Test that an element has a value - the value is not nillable -->
  <sch:pattern abstract="true" id="TypeNotNillablePattern">
    <sch:rule context="$context">
      <sch:assert test="string-length(.) &gt; 0 and count(./@gco:nilReason) = 0">
        The <sch:name/> element is not nillable and shall have a value.
      </sch:assert>
    </sch:rule>
  </sch:pattern>
  
  <!-- Test ISO code lists -->
  <sch:pattern abstract="true" id="IsoCodeListPattern">
    <sch:rule context="$context">
      <sch:assert test="string-length(@codeListValue) &gt; 0">
        The codeListValue attribute does not have a value.
      </sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- End of patterns included from GEMINI 2.1 Schematron Schema -->


</sch:schema>