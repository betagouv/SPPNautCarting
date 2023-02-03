<?xml version="1.0" encoding="UTF-8"?>

<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" doctype-public="XSLT-compat" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />
    <xsl:template match="/">
        <xsl:for-each select="sPara">
            <h4> Titre : <xsl:value-of select="titre/texte/txt" /></h4>
            <xsl:value-of select="nmrAlinea" />
            <xsl:for-each select="alinea">
                <h5> Num Alinea : <xsl:value-of select="nmrAlinea" /></h5>
                <div> Texte Alinea : <xsl:value-of select="texte" /></div>
            </xsl:for-each>
        </xsl:for-each>
    </xsl:template>
</xsl:transform>
