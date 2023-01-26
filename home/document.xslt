<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes" encoding="iso-8859-1"/>
<xsl:template match="sPara">
    <html><body>
        <xsl:apply-templates/>
    </body></html>
</xsl:template>
<xsl:template match="sPara/titre/nmrAlinea">
    <h5> <xsl:apply-templates/> </h5>
</xsl:template>
<xsl:template match="sPara/titre/texte/txt">
    <h4 align="center"> <xsl:apply-templates/> </h4>
</xsl:template>
<xsl:template match="sPara/alinea/nmrAlinea">
    <h6> <xsl:apply-templates/> </h6>
</xsl:template>
<xsl:template match="sPara/alinea/texte">
    <p> <xsl:apply-templates/> </p>
</xsl:template>

</xsl:stylesheet>
