<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes" encoding="iso-8859-1"/>
<xsl:template match="sPara">
    <html><body>
        <xsl:apply-templates/>
    </body></html>
</xsl:template>
<xsl:template match="titre/nmrAlinea">
    <i style="display:none;"> <xsl:apply-templates/> </i>
</xsl:template>
<xsl:template match="titre/numero">
    <b> <xsl:apply-templates/> : </b>
</xsl:template>
<xsl:template match="titre/texte/txt">
    <b> <xsl:apply-templates/> </b>
</xsl:template>
<xsl:template match="alinea/nmrAlinea">
    <b> <xsl:apply-templates/> : </b>
</xsl:template>
<xsl:template match="alinea/texte">
    <xsl:apply-templates/>
</xsl:template>
<xsl:template match="illustration/numero">
    <b> <xsl:apply-templates/> : </b>
</xsl:template>
</xsl:stylesheet>
