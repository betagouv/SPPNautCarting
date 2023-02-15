<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

    <xsl:template match="titre/nmrAlinea">
        <span class="fr-text--xs fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="titre/numero">
        <span class="sppnaut-bold fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="titre/texte/txt">
        <xsl:apply-templates />
    </xsl:template>

    <xsl:template match="alinea/nmrAlinea">
        <span class="fr-text--xs fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="alinea/texte">
        <xsl:apply-templates />
    </xsl:template>

    <xsl:template match="illustration">
        <xsl:apply-templates />
    </xsl:template>
    <xsl:template match="illustration/numero">
        <span class="fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="illustration/txt">
        <span class="fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="tableau">
        <span>
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="tableau/numero">
        <span class="fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    <xsl:template match="tableau/txt">
        <span class="fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="principal">
        <a href="#">
            <xsl:apply-templates />
        </a>
    </xsl:template>

    <xsl:template match="reference">
        <a href="#">
            <xsl:apply-templates />
        </a>
    </xsl:template>

</xsl:stylesheet>
