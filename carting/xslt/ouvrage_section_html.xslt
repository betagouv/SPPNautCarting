<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

    <xsl:template match="
        titre/nmrAlinea
    ">
    </xsl:template>

    <xsl:template match="
        alinea/nmrAlinea
    ">
        <span class="fr-text--xs fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="titre/numero">
        <span class="sppnaut-bold fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="
        titre/texte/txt|
        alinea/texte|
        illustration|
        tableau
    ">
        <xsl:apply-templates />
    </xsl:template>

    <xsl:template match="
        illustration/numero|
        illustration/txt|
        tableau/numero|
        tableau/txt
    ">
        <span class="fr-pr-1w">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="
        principal|
        reference
    ">
        <a
            id="{@bpn_id}"
            href="#{@bpn_id}"
            class="sppnaut-scroll-mt-8w"
        >
            <xsl:apply-templates />
        </a>
    </xsl:template>

</xsl:stylesheet>
