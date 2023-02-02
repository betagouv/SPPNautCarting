<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes" encoding="iso-8859-1" />

    <xsl:template match="titre/nmrAlinea">
        <div class="carting-titre carting-alinea-numero">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="titre/numero">
        <div class="carting-titre-numero">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="titre/texte/txt">
        <div class="carting-titre-texte">
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="alinea/nmrAlinea">
        <div class="carting-alinea-numero">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="alinea/texte">
        <div class="carting-alinea-texte">
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="illustration">
        <div class="carting-illustration">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="illustration/numero">
        <div class="carting-illustration-numero">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="illustration/txt">
        <div class="carting-illustration-texte">
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tableau">
        <div class="carting-tableau">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="tableau/numero">
        <div class="carting-tableau-numero">
            <xsl:apply-templates />
        </div>
    </xsl:template>
    <xsl:template match="tableau/txt">
        <div class="carting-tableau-texte">
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="principal">
        <a href="#" class="carting-toponyme">
            <xsl:apply-templates />
        </a>
    </xsl:template>

    <xsl:template match="reference">
        <a href="#" class="carting-reference">
            <xsl:apply-templates />
        </a>
    </xsl:template>

</xsl:stylesheet>