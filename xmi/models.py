# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Abstractrxn(models.Model):
    categoryofauthority = models.CharField(
        db_column="Categoryofauthority", max_length=-1, blank=True, null=True
    )
    graphic = models.CharField(
        db_column="Graphic", max_length=-1, blank=True, null=True
    )
    rxncode = models.CharField(
        db_column="Rxncode", max_length=-1, blank=True, null=True
    )
    textcontent = models.CharField(
        db_column="Textcontent", max_length=-1, blank=True, null=True
    )
    abstractrxnid = models.OneToOneField(
        "Informationtype",
        models.DO_NOTHING,
        db_column="AbstractrxnID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Abstractrxn"


class Actionoractivity(models.Model):
    anchoring = models.CharField(
        db_column="Anchoring", max_length=-1, blank=True, null=True
    )
    berthing = models.CharField(
        db_column="Berthing", max_length=-1, blank=True, null=True
    )
    dischargingoverboard = models.CharField(
        db_column="DischargingOverboard", max_length=-1, blank=True, null=True
    )
    diving = models.CharField(
        db_column="Diving", max_length=-1, blank=True, null=True
    )
    enteringport = models.CharField(
        db_column="EnteringPort", max_length=-1, blank=True, null=True
    )
    fishing = models.CharField(
        db_column="Fishing", max_length=-1, blank=True, null=True
    )
    landing = models.CharField(
        db_column="Landing", max_length=-1, blank=True, null=True
    )
    leavingport = models.CharField(
        db_column="LeavingPort", max_length=-1, blank=True, null=True
    )
    navigatingwithapilot = models.CharField(
        db_column="NavigatingWithAPilot", max_length=-1, blank=True, null=True
    )
    overtaking = models.CharField(
        db_column="Overtaking", max_length=-1, blank=True, null=True
    )
    passing = models.CharField(
        db_column="Passing", max_length=-1, blank=True, null=True
    )
    reporting = models.CharField(
        db_column="Reporting", max_length=-1, blank=True, null=True
    )
    slipping = models.CharField(
        db_column="Slipping", max_length=-1, blank=True, null=True
    )
    transiting = models.CharField(
        db_column="Transiting", max_length=-1, blank=True, null=True
    )
    weighinganchor = models.CharField(
        db_column="WeighingAnchor", max_length=-1, blank=True, null=True
    )
    workingcargo = models.CharField(
        db_column="WorkingCargo", max_length=-1, blank=True, null=True
    )
    actionoractivityid = models.CharField(
        db_column="ActionoractivityID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Actionoractivity"


class Additionalinformation(models.Model):
    providesinformation = models.ForeignKey(
        "Nauticalinformation",
        models.DO_NOTHING,
        db_column="providesInformation",
        blank=True,
        null=True,
    )
    informationprovidedfor = models.ForeignKey(
        "Informationtype",
        models.DO_NOTHING,
        db_column="informationProvidedFor",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "AdditionalInformation"


class Applicability(models.Model):
    categoryofcargo = models.CharField(
        db_column="Categoryofcargo", max_length=-1, blank=True, null=True
    )
    categoryofdangerousorhazardouscargo = models.CharField(
        db_column="Categoryofdangerousorhazardouscargo",
        max_length=-1,
        blank=True,
        null=True,
    )
    categoryofvessel = models.CharField(
        db_column="Categoryofvessel", max_length=-1, blank=True, null=True
    )
    categoryofvesselregistry = models.CharField(
        db_column="Categoryofvesselregistry", max_length=-1, blank=True, null=True
    )
    inballast = models.CharField(
        db_column="Inballast", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    logicalconnectives = models.CharField(
        db_column="Logicalconnectives", max_length=-1, blank=True, null=True
    )
    thicknessoficecapability = models.CharField(
        db_column="Thicknessoficecapability", max_length=-1, blank=True, null=True
    )
    vesselperformance = models.CharField(
        db_column="Vesselperformance", max_length=-1, blank=True, null=True
    )
    vesselsmeasurements = models.CharField(
        db_column="Vesselsmeasurements", max_length=-1, blank=True, null=True
    )
    applicabilityid = models.OneToOneField(
        "Informationtype",
        models.DO_NOTHING,
        db_column="ApplicabilityID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Applicability"


class Associatedrxn(models.Model):
    therxn = models.ForeignKey(
        Abstractrxn, models.DO_NOTHING, db_column="theRxN", blank=True, null=True
    )
    appliesinlocation = models.ForeignKey(
        "Featuretype",
        models.DO_NOTHING,
        db_column="appliesInLocation",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "AssociatedRxN"


class Authority(models.Model):
    categoryofauthority = models.CharField(
        db_column="Categoryofauthority", max_length=-1, blank=True, null=True
    )
    textcontent = models.CharField(
        db_column="Textcontent", max_length=-1, blank=True, null=True
    )
    authorityid = models.OneToOneField(
        "Informationtype", models.DO_NOTHING, db_column="AuthorityID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Authority"


class Authoritycontact(models.Model):
    thecontactdetails = models.ForeignKey(
        "Contactdetails",
        models.DO_NOTHING,
        db_column="theContactDetails",
        blank=True,
        null=True,
    )
    theauthority = models.ForeignKey(
        Authority, models.DO_NOTHING, db_column="theAuthority", blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "AuthorityContact"


class Authorityhours(models.Model):
    theservicehours = models.ForeignKey(
        "Servicehours",
        models.DO_NOTHING,
        db_column="theServiceHours",
        blank=True,
        null=True,
    )
    theauthority_srvhrs = models.ForeignKey(
        Authority,
        models.DO_NOTHING,
        db_column="theAuthority_srvHrs",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "AuthorityHours"


class Bearinginformation(models.Model):
    cardinaldirection = models.CharField(
        db_column="Cardinaldirection", max_length=-1, blank=True, null=True
    )
    distance = models.CharField(
        db_column="Distance", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    orientation = models.CharField(
        db_column="Orientation", max_length=-1, blank=True, null=True
    )
    sectorbearing = models.CharField(
        db_column="Sectorbearing", max_length=-1, blank=True, null=True
    )
    bearinginformationid = models.CharField(
        db_column="BearinginformationID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Bearinginformation"


class Categoryofrxn(models.Model):
    agriculture = models.CharField(
        db_column="Agriculture", max_length=-1, blank=True, null=True
    )
    cargooperation = models.CharField(
        db_column="CargoOperation", max_length=-1, blank=True, null=True
    )
    communication = models.CharField(
        db_column="Communication", max_length=-1, blank=True, null=True
    )
    customs = models.CharField(
        db_column="Customs", max_length=-1, blank=True, null=True
    )
    environmentalprotection = models.CharField(
        db_column="EnvironmentalProtection", max_length=-1, blank=True, null=True
    )
    finance = models.CharField(
        db_column="Finance", max_length=-1, blank=True, null=True
    )
    health = models.CharField(
        db_column="Health", max_length=-1, blank=True, null=True
    )
    naturalresourcesorexploitation = models.CharField(
        db_column="NaturalResourcesOrExploitation", max_length=-1, blank=True, null=True
    )
    navigation = models.CharField(
        db_column="Navigation", max_length=-1, blank=True, null=True
    )
    port = models.CharField(
        db_column="Port", max_length=-1, blank=True, null=True
    )
    refuge = models.CharField(
        db_column="Refuge", max_length=-1, blank=True, null=True
    )
    security = models.CharField(
        db_column="Security", max_length=-1, blank=True, null=True
    )
    wildlifeprotection = models.CharField(
        db_column="WildlifeProtection", max_length=-1, blank=True, null=True
    )
    categoryofrxnid = models.CharField(
        db_column="CategoryofrxnID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Categoryofrxn"


class Categoryofschedule(models.Model):
    closure = models.CharField(
        db_column="Closure", max_length=-1, blank=True, null=True
    )
    normaloperation = models.CharField(
        db_column="NormalOperation", max_length=-1, blank=True, null=True
    )
    unmannedoperation = models.CharField(
        db_column="UnmannedOperation", max_length=-1, blank=True, null=True
    )
    categoryofscheduleid = models.CharField(
        db_column="CategoryofscheduleID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Categoryofschedule"


class Categoryofvessel(models.Model):
    bulkcarrier = models.CharField(
        db_column="BulkCarrier", max_length=-1, blank=True, null=True
    )
    containercarrier = models.CharField(
        db_column="ContainerCarrier", max_length=-1, blank=True, null=True
    )
    fishingvessel = models.CharField(
        db_column="FishingVessel", max_length=-1, blank=True, null=True
    )
    generalcargovessel = models.CharField(
        db_column="GeneralCargoVessel", max_length=-1, blank=True, null=True
    )
    jackupexplorationorprojectinstallation = models.CharField(
        db_column="JackupExplorationOrProjectInstallation",
        max_length=-1,
        blank=True,
        null=True,
    )
    lightrecreational = models.CharField(
        db_column="LightRecreational", max_length=-1, blank=True, null=True
    )
    livestockcarrier = models.CharField(
        db_column="LivestockCarrier", max_length=-1, blank=True, null=True
    )
    passengervessel = models.CharField(
        db_column="PassengerVessel", max_length=-1, blank=True, null=True
    )
    refrigeratedcargovessel = models.CharField(
        db_column="RefrigeratedCargoVessel", max_length=-1, blank=True, null=True
    )
    roll_onroll_off = models.CharField(
        db_column="Roll-onRoll-off", max_length=-1, blank=True, null=True
    )   Field renamed to remove unsuitable characters.
    semi_submersibleoffshoreinstallation = models.CharField(
        db_column="Semi-submersibleOffshoreInstallation",
        max_length=-1,
        blank=True,
        null=True,
    )   Field renamed to remove unsuitable characters.
    service = models.CharField(
        db_column="Service", max_length=-1, blank=True, null=True
    )
    sportfishing = models.CharField(
        db_column="SportFishing", max_length=-1, blank=True, null=True
    )
    tanker = models.CharField(
        db_column="Tanker", max_length=-1, blank=True, null=True
    )
    towedorpushedcompositeunit = models.CharField(
        db_column="TowedOrPushedCompositeUnit", max_length=-1, blank=True, null=True
    )
    tugandtow = models.CharField(
        db_column="TugAndTow", max_length=-1, blank=True, null=True
    )
    warship = models.CharField(
        db_column="Warship", max_length=-1, blank=True, null=True
    )
    categoryofvesselid = models.CharField(
        db_column="CategoryofvesselID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Categoryofvessel"


class Cautionarea(models.Model):
    condition = models.CharField(
        db_column="Condition", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    cautionareaid = models.OneToOneField(
        "Featuretype", models.DO_NOTHING, db_column="CautionareaID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Cautionarea"


class Concentrationofshippinghazardarea(models.Model):
    categoryofconcentrationofshippinghazardarea = models.CharField(
        db_column="Categoryofconcentrationofshippinghazardarea",
        max_length=-1,
        blank=True,
        null=True,
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    concentrationofshippinghazardareaid = models.OneToOneField(
        "Featuretype",
        models.DO_NOTHING,
        db_column="ConcentrationofshippinghazardareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Concentrationofshippinghazardarea"


class Contactaddress(models.Model):
    administrativedivision = models.CharField(
        db_column="Administrativedivision", max_length=-1, blank=True, null=True
    )
    cityname = models.CharField(
        db_column="Cityname", max_length=-1, blank=True, null=True
    )
    countryname = models.CharField(
        db_column="Countryname", max_length=-1, blank=True, null=True
    )
    deliverypoint = models.CharField(
        db_column="Deliverypoint", max_length=-1, blank=True, null=True
    )
    postalcode = models.CharField(
        db_column="Postalcode", max_length=-1, blank=True, null=True
    )
    contactaddressid = models.CharField(
        db_column="ContactaddressID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Contactaddress"


class Contactdetails(models.Model):
    callname = models.CharField(
        db_column="Callname", max_length=-1, blank=True, null=True
    )
    callsign = models.CharField(
        db_column="Callsign", max_length=-1, blank=True, null=True
    )
    categoryofcommpref = models.CharField(
        db_column="Categoryofcommpref", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    contactaddress = models.CharField(
        db_column="Contactaddress", max_length=-1, blank=True, null=True
    )
    contactinstructions = models.CharField(
        db_column="Contactinstructions", max_length=-1, blank=True, null=True
    )
    frequencypair = models.CharField(
        db_column="Frequencypair", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    language = models.CharField(
        db_column="Language", max_length=-1, blank=True, null=True
    )
    mmsicode = models.CharField(
        db_column="Mmsicode", max_length=-1, blank=True, null=True
    )
    onlineresource = models.CharField(
        db_column="Onlineresource", max_length=-1, blank=True, null=True
    )
    radiocommunications = models.CharField(
        db_column="Radiocommunications", max_length=-1, blank=True, null=True
    )
    telecommunications = models.CharField(
        db_column="Telecommunications", max_length=-1, blank=True, null=True
    )
    contactdetailsid = models.OneToOneField(
        "Informationtype",
        models.DO_NOTHING,
        db_column="ContactdetailsID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Contactdetails"


class Exceptionalworkday(models.Model):
    partialworkingday = models.ForeignKey(
        "Nonstandardworkingday",
        models.DO_NOTHING,
        db_column="partialWorkingDay",
        blank=True,
        null=True,
    )
    theservicehours_nsdy = models.ForeignKey(
        "Servicehours",
        models.DO_NOTHING,
        db_column="theServiceHours_nsdy",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "ExceptionalWorkday"


class Featurename(models.Model):
    displayname = models.CharField(
        db_column="Displayname", max_length=-1, blank=True, null=True
    )
    language = models.CharField(
        db_column="Language", max_length=-1, blank=True, null=True
    )
    name = models.CharField(
        db_column="Name", max_length=-1, blank=True, null=True
    )
    featurenameid = models.CharField(
        db_column="FeaturenameID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Featurename"


class Featuretype(models.Model):
    featurename = models.CharField(
        db_column="Featurename", max_length=-1, blank=True, null=True
    )
    fixeddaterange = models.CharField(
        db_column="Fixeddaterange", max_length=-1, blank=True, null=True
    )
    periodicdaterange = models.CharField(
        db_column="Periodicdaterange", max_length=-1, blank=True, null=True
    )
    sourceindication = models.CharField(
        db_column="Sourceindication", max_length=-1, blank=True, null=True
    )
    textcontent = models.CharField(
        db_column="Textcontent", max_length=-1, blank=True, null=True
    )
    featuretypeid = models.CharField(
        db_column="FeaturetypeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Featuretype"


class Fixeddaterange(models.Model):
    dateend = models.CharField(
        db_column="Dateend", max_length=-1, blank=True, null=True
    )
    datestart = models.CharField(
        db_column="Datestart", max_length=-1, blank=True, null=True
    )
    fixeddaterangeid = models.CharField(
        db_column="FixeddaterangeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Fixeddaterange"


class Frequencypair(models.Model):
    contactinstructions = models.CharField(
        db_column="Contactinstructions", max_length=-1, blank=True, null=True
    )
    frequencyshorestationreceives = models.CharField(
        db_column="Frequencyshorestationreceives", max_length=-1, blank=True, null=True
    )
    frequencyshorestationtransmits = models.CharField(
        db_column="Frequencyshorestationtransmits", max_length=-1, blank=True, null=True
    )
    frequencypairid = models.CharField(
        db_column="FrequencypairID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Frequencypair"


class Graphic(models.Model):
    bearinginformation = models.CharField(
        db_column="Bearinginformation", max_length=-1, blank=True, null=True
    )
    pictorialrepresentation = models.CharField(
        db_column="Pictorialrepresentation", max_length=-1, blank=True, null=True
    )
    picturecaption = models.CharField(
        db_column="Picturecaption", max_length=-1, blank=True, null=True
    )
    pictureinformation = models.CharField(
        db_column="Pictureinformation", max_length=-1, blank=True, null=True
    )
    sourcedate = models.CharField(
        db_column="Sourcedate", max_length=-1, blank=True, null=True
    )
    graphicid = models.CharField(
        db_column="GraphicID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Graphic"


class Inclusiontype(models.Model):
    membership = models.CharField(
        db_column="Membership", max_length=-1, blank=True, null=True
    )
    inclusiontypeid = models.CharField(
        db_column="InclusiontypeID", primary_key=True, max_length=-1
    )
    abstractrxnid = models.ForeignKey(
        Abstractrxn, models.DO_NOTHING, db_column="AbstractrxnID", blank=True, null=True
    )
    applicabilityid = models.ForeignKey(
        Applicability,
        models.DO_NOTHING,
        db_column="ApplicabilityID",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Inclusiontype"


class Information(models.Model):
    filelocator = models.CharField(
        db_column="Filelocator", max_length=-1, blank=True, null=True
    )
    filereference = models.CharField(
        db_column="Filereference", max_length=-1, blank=True, null=True
    )
    headline = models.CharField(
        db_column="Headline", max_length=-1, blank=True, null=True
    )
    language = models.CharField(
        db_column="Language", max_length=-1, blank=True, null=True
    )
    text = models.CharField(
        db_column="Text", max_length=-1, blank=True, null=True
    )
    informationid = models.CharField(
        db_column="InformationID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Information"


class Informationtype(models.Model):
    featurename = models.CharField(
        db_column="Featurename", max_length=-1, blank=True, null=True
    )
    fixeddaterange = models.CharField(
        db_column="Fixeddaterange", max_length=-1, blank=True, null=True
    )
    periodicdaterange = models.CharField(
        db_column="Periodicdaterange", max_length=-1, blank=True, null=True
    )
    sourceindication = models.CharField(
        db_column="Sourceindication", max_length=-1, blank=True, null=True
    )
    informationtypeid = models.CharField(
        db_column="InformationtypeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Informationtype"


class Ispscodesecuritylevel(models.Model):
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    ispslevel = models.CharField(
        db_column="Ispslevel", max_length=-1, blank=True, null=True
    )
    ispscodesecuritylevelid = models.OneToOneField(
        "Organisationcontactarea",
        models.DO_NOTHING,
        db_column="IspscodesecuritylevelID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Ispscodesecuritylevel"


class Localportservicearea(models.Model):
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    requirementsformaintenanceoflisteningwatch = models.CharField(
        db_column="Requirementsformaintenanceoflisteningwatch",
        max_length=-1,
        blank=True,
        null=True,
    )
    serviceaccessprocedure = models.CharField(
        db_column="Serviceaccessprocedure", max_length=-1, blank=True, null=True
    )
    localportserviceareaid = models.OneToOneField(
        "Reportableservicearea",
        models.DO_NOTHING,
        db_column="LocalportserviceareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Localportservicearea"


class Militarypracticearea(models.Model):
    categoryofmilitarypracticearea = models.CharField(
        db_column="Categoryofmilitarypracticearea", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    nationality = models.CharField(
        db_column="Nationality", max_length=-1, blank=True, null=True
    )
    restriction = models.CharField(
        db_column="Restriction", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    militarypracticeareaid = models.OneToOneField(
        "Supervisedarea",
        models.DO_NOTHING,
        db_column="MilitarypracticeareaID",
        primary_key=True,
    )
    theservicehours = models.ForeignKey(
        "Servicehours",
        models.DO_NOTHING,
        db_column="theServiceHours",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Militarypracticearea"


class Nauticalinformation(models.Model):
    nauticalinformationid = models.OneToOneField(
        Abstractrxn,
        models.DO_NOTHING,
        db_column="NauticalinformationID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Nauticalinformation"


class Nonstandardworkingday(models.Model):
    datefixed = models.CharField(
        db_column="Datefixed", max_length=-1, blank=True, null=True
    )
    datevariable = models.CharField(
        db_column="Datevariable", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    nonstandardworkingdayid = models.OneToOneField(
        Informationtype,
        models.DO_NOTHING,
        db_column="NonstandardworkingdayID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Nonstandardworkingday"


class Noticetime(models.Model):
    noticetimehours = models.CharField(
        db_column="Noticetimehours", max_length=-1, blank=True, null=True
    )
    noticetimetext = models.CharField(
        db_column="Noticetimetext", max_length=-1, blank=True, null=True
    )
    operation = models.CharField(
        db_column="Operation", max_length=-1, blank=True, null=True
    )
    noticetimeid = models.CharField(
        db_column="NoticetimeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Noticetime"


class Onlinefunction(models.Model):
    browsegraphic = models.CharField(
        db_column="Browsegraphic", max_length=-1, blank=True, null=True
    )
    browsing = models.CharField(
        db_column="Browsing", max_length=-1, blank=True, null=True
    )
    completemetadata = models.CharField(
        db_column="Completemetadata", max_length=-1, blank=True, null=True
    )
    download = models.CharField(
        db_column="Download", max_length=-1, blank=True, null=True
    )
    emailservice = models.CharField(
        db_column="Emailservice", max_length=-1, blank=True, null=True
    )
    fileaccess = models.CharField(
        db_column="Fileaccess", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    offlineaccess = models.CharField(
        db_column="Offlineaccess", max_length=-1, blank=True, null=True
    )
    order = models.CharField(
        db_column="Order", max_length=-1, blank=True, null=True
    )
    search = models.CharField(
        db_column="Search", max_length=-1, blank=True, null=True
    )
    upload = models.CharField(
        db_column="Upload", max_length=-1, blank=True, null=True
    )
    onlinefunctionid = models.CharField(
        db_column="OnlinefunctionID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Onlinefunction"


class Onlineresource(models.Model):
    applicationprofile = models.CharField(
        db_column="Applicationprofile", max_length=-1, blank=True, null=True
    )
    linkage = models.CharField(
        db_column="Linkage", max_length=-1, blank=True, null=True
    )
    nameofresource = models.CharField(
        db_column="Nameofresource", max_length=-1, blank=True, null=True
    )
    onlinefunction = models.CharField(
        db_column="Onlinefunction", max_length=-1, blank=True, null=True
    )
    onlineresourcedescription = models.CharField(
        db_column="Onlineresourcedescription", max_length=-1, blank=True, null=True
    )
    protocol = models.CharField(
        db_column="Protocol", max_length=-1, blank=True, null=True
    )
    protocolrequest = models.CharField(
        db_column="Protocolrequest", max_length=-1, blank=True, null=True
    )
    onlineresourceid = models.CharField(
        db_column="OnlineresourceID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Onlineresource"


class Organisationcontactarea(models.Model):
    organisationcontactareaid = models.OneToOneField(
        Featuretype,
        models.DO_NOTHING,
        db_column="OrganisationcontactareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Organisationcontactarea"


class Orientation(models.Model):
    orientationuncertainty = models.CharField(
        db_column="Orientationuncertainty", max_length=-1, blank=True, null=True
    )
    orientationvalue = models.CharField(
        db_column="Orientationvalue", max_length=-1, blank=True, null=True
    )
    orientationid = models.CharField(
        db_column="OrientationID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Orientation"


class Periodicdaterange(models.Model):
    dateend = models.CharField(
        db_column="Dateend", max_length=-1, blank=True, null=True
    )
    datestart = models.CharField(
        db_column="Datestart", max_length=-1, blank=True, null=True
    )
    periodicdaterangeid = models.CharField(
        db_column="PeriodicdaterangeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Periodicdaterange"


class Permissiontype(models.Model):
    categoryofrelationship = models.CharField(
        db_column="Categoryofrelationship", max_length=-1, blank=True, null=True
    )
    permissiontypeid = models.CharField(
        db_column="PermissiontypeID", primary_key=True, max_length=-1
    )
    featuretypeid = models.ForeignKey(
        Featuretype, models.DO_NOTHING, db_column="FeaturetypeID", blank=True, null=True
    )
    applicabilityid = models.ForeignKey(
        Applicability,
        models.DO_NOTHING,
        db_column="ApplicabilityID",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Permissiontype"


class Pilotagedistrict(models.Model):
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    pilotagedistrictid = models.OneToOneField(
        Featuretype, models.DO_NOTHING, db_column="PilotagedistrictID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Pilotagedistrict"


class Pilotboardingplace(models.Model):
    callsign = models.CharField(
        db_column="Callsign", max_length=-1, blank=True, null=True
    )
    categoryofpilotboardingplace = models.CharField(
        db_column="Categoryofpilotboardingplace", max_length=-1, blank=True, null=True
    )
    categoryofpreference = models.CharField(
        db_column="Categoryofpreference", max_length=-1, blank=True, null=True
    )
    categoryofvessel = models.CharField(
        db_column="Categoryofvessel", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    destination = models.CharField(
        db_column="Destination", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    pilotmovement = models.CharField(
        db_column="Pilotmovement", max_length=-1, blank=True, null=True
    )
    pilotvessel = models.CharField(
        db_column="Pilotvessel", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    pilotboardingplaceid = models.OneToOneField(
        Organisationcontactarea,
        models.DO_NOTHING,
        db_column="PilotboardingplaceID",
        primary_key=True,
    )
    componentof = models.ForeignKey(
        Pilotagedistrict,
        models.DO_NOTHING,
        db_column="componentOf",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Pilotboardingplace"


class Pilotservice(models.Model):
    categoryofpilot = models.CharField(
        db_column="Categoryofpilot", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    noticetime = models.CharField(
        db_column="Noticetime", max_length=-1, blank=True, null=True
    )
    pilotqualification = models.CharField(
        db_column="Pilotqualification", max_length=-1, blank=True, null=True
    )
    pilotrequest = models.CharField(
        db_column="Pilotrequest", max_length=-1, blank=True, null=True
    )
    remotepilot = models.CharField(
        db_column="Remotepilot", max_length=-1, blank=True, null=True
    )
    pilotserviceid = models.OneToOneField(
        "Reportableservicearea",
        models.DO_NOTHING,
        db_column="PilotserviceID",
        primary_key=True,
    )
    servicearea = models.ForeignKey(
        Pilotagedistrict,
        models.DO_NOTHING,
        db_column="serviceArea",
        blank=True,
        null=True,
    )
    theservicehours = models.ForeignKey(
        "Servicehours",
        models.DO_NOTHING,
        db_column="theServiceHours",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Pilotservice"


class Piracyriskarea(models.Model):
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    restriction = models.CharField(
        db_column="Restriction", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    piracyriskareaid = models.OneToOneField(
        "Reportableservicearea",
        models.DO_NOTHING,
        db_column="PiracyriskareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Piracyriskarea"


class Placeofrefuge(models.Model):
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    placeofrefugeid = models.OneToOneField(
        "Reportableservicearea",
        models.DO_NOTHING,
        db_column="PlaceofrefugeID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Placeofrefuge"


class Radarrange(models.Model):
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    radarrangeid = models.OneToOneField(
        Featuretype, models.DO_NOTHING, db_column="RadarrangeID", primary_key=True
    )
    componentof = models.ForeignKey(
        Localportservicearea,
        models.DO_NOTHING,
        db_column="componentOf",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Radarrange"


class Radiocallinginpoint(models.Model):
    callsign = models.CharField(
        db_column="Callsign", max_length=-1, blank=True, null=True
    )
    categoryofcargo = models.CharField(
        db_column="Categoryofcargo", max_length=-1, blank=True, null=True
    )
    categoryofvessel = models.CharField(
        db_column="Categoryofvessel", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    orientationvalue = models.CharField(
        db_column="Orientationvalue", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    trafficflow = models.CharField(
        db_column="Trafficflow", max_length=-1, blank=True, null=True
    )
    radiocallinginpointid = models.OneToOneField(
        Featuretype,
        models.DO_NOTHING,
        db_column="RadiocallinginpointID",
        primary_key=True,
    )
    componentof = models.ForeignKey(
        Localportservicearea,
        models.DO_NOTHING,
        db_column="componentOf",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Radiocallinginpoint"


class Radiocommunications(models.Model):
    categoryofcommpref = models.CharField(
        db_column="Categoryofcommpref", max_length=-1, blank=True, null=True
    )
    categoryofmaritimebroadcast = models.CharField(
        db_column="Categoryofmaritimebroadcast", max_length=-1, blank=True, null=True
    )
    categoryofradiomethods = models.CharField(
        db_column="Categoryofradiomethods", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    contactinstructions = models.CharField(
        db_column="Contactinstructions", max_length=-1, blank=True, null=True
    )
    frequencypair = models.CharField(
        db_column="Frequencypair", max_length=-1, blank=True, null=True
    )
    signalfrequency = models.CharField(
        db_column="Signalfrequency", max_length=-1, blank=True, null=True
    )
    timeintervalsbydayofweek = models.CharField(
        db_column="Timeintervalsbydayofweek", max_length=-1, blank=True, null=True
    )
    radiocommunicationsid = models.CharField(
        db_column="RadiocommunicationsID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Radiocommunications"


class Recommendations(models.Model):
    recommendationsid = models.OneToOneField(
        Abstractrxn, models.DO_NOTHING, db_column="RecommendationsID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Recommendations"


class Regulations(models.Model):
    regulationsid = models.OneToOneField(
        Abstractrxn, models.DO_NOTHING, db_column="RegulationsID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Regulations"


class Relatedorganisation(models.Model):
    theinformation = models.ForeignKey(
        Abstractrxn,
        models.DO_NOTHING,
        db_column="theInformation",
        blank=True,
        null=True,
    )
    theorganisation = models.ForeignKey(
        Authority, models.DO_NOTHING, db_column="theOrganisation", blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "RelatedOrganisation"


class Reportreqmt(models.Model):
    mustbefiledby = models.ForeignKey(
        Applicability,
        models.DO_NOTHING,
        db_column="mustBeFiledBy",
        blank=True,
        null=True,
    )
    theshipreport = models.ForeignKey(
        "Shipreport",
        models.DO_NOTHING,
        db_column="theShipReport",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "ReportReqmt"


class Reportableservicearea(models.Model):
    reportableserviceareaid = models.OneToOneField(
        "Supervisedarea",
        models.DO_NOTHING,
        db_column="ReportableserviceareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Reportableservicearea"


class Reptauthority(models.Model):
    theshipreport = models.ForeignKey(
        "Shipreport",
        models.DO_NOTHING,
        db_column="theShipReport",
        blank=True,
        null=True,
    )
    reportto = models.ForeignKey(
        Authority, models.DO_NOTHING, db_column="reportTo", blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "ReptAuthority"


class Restrictedareanavigational(models.Model):
    categoryofrestrictedarea = models.CharField(
        db_column="Categoryofrestrictedarea", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    restriction = models.CharField(
        db_column="Restriction", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    restrictedareanavigationalid = models.OneToOneField(
        "Supervisedarea",
        models.DO_NOTHING,
        db_column="RestrictedareanavigationalID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Restrictedareanavigational"


class Restrictedarearegulatory(models.Model):
    categoryofrestrictedarea = models.CharField(
        db_column="Categoryofrestrictedarea", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    restriction = models.CharField(
        db_column="Restriction", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    restrictedarearegulatoryid = models.OneToOneField(
        "Supervisedarea",
        models.DO_NOTHING,
        db_column="RestrictedarearegulatoryID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Restrictedarearegulatory"


class Restrictions(models.Model):
    restrictionsid = models.OneToOneField(
        Abstractrxn, models.DO_NOTHING, db_column="RestrictionsID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Restrictions"


class Routeingmeasure(models.Model):
    categoryofnavigationline = models.CharField(
        db_column="Categoryofnavigationline", max_length=-1, blank=True, null=True
    )
    categoryofrouteingmeasure = models.CharField(
        db_column="Categoryofrouteingmeasure", max_length=-1, blank=True, null=True
    )
    categoryoftrafficseparationscheme = models.CharField(
        db_column="Categoryoftrafficseparationscheme",
        max_length=-1,
        blank=True,
        null=True,
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    routeingmeasureid = models.OneToOneField(
        Featuretype, models.DO_NOTHING, db_column="RouteingmeasureID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Routeingmeasure"


class Rxncode(models.Model):
    actionoractivity = models.CharField(
        db_column="Actionoractivity", max_length=-1, blank=True, null=True
    )
    categoryofrxn = models.CharField(
        db_column="Categoryofrxn", max_length=-1, blank=True, null=True
    )
    headline = models.CharField(
        db_column="Headline", max_length=-1, blank=True, null=True
    )
    rxncodeid = models.CharField(
        db_column="RxncodeID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Rxncode"


class Schedulebydayofweek(models.Model):
    categoryofschedule = models.CharField(
        db_column="Categoryofschedule", max_length=-1, blank=True, null=True
    )
    timeintervalsbydayofweek = models.CharField(
        db_column="Timeintervalsbydayofweek", max_length=-1, blank=True, null=True
    )
    schedulebydayofweekid = models.CharField(
        db_column="SchedulebydayofweekID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Schedulebydayofweek"


class Serviceprovisionarea(models.Model):
    servicearea = models.ForeignKey(
        Pilotboardingplace,
        models.DO_NOTHING,
        db_column="serviceArea",
        blank=True,
        null=True,
    )
    serviceprovider = models.ForeignKey(
        Pilotservice,
        models.DO_NOTHING,
        db_column="serviceProvider",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "ServiceProvisionArea"


class Servicehours(models.Model):
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    schedulebydayofweek = models.CharField(
        db_column="Schedulebydayofweek", max_length=-1, blank=True, null=True
    )
    servicehoursid = models.OneToOneField(
        Informationtype, models.DO_NOTHING, db_column="ServicehoursID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Servicehours"


class Shipreport(models.Model):
    categoryofshipreport = models.CharField(
        db_column="Categoryofshipreport", max_length=-1, blank=True, null=True
    )
    imoformatforreporting = models.CharField(
        db_column="Imoformatforreporting", max_length=-1, blank=True, null=True
    )
    noticetime = models.CharField(
        db_column="Noticetime", max_length=-1, blank=True, null=True
    )
    textcontent = models.CharField(
        db_column="Textcontent", max_length=-1, blank=True, null=True
    )
    shipreportid = models.OneToOneField(
        Informationtype, models.DO_NOTHING, db_column="ShipreportID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Shipreport"


class Shipreportingservicearea(models.Model):
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    requirementsformaintenanceoflisteningwatch = models.CharField(
        db_column="Requirementsformaintenanceoflisteningwatch",
        max_length=-1,
        blank=True,
        null=True,
    )
    serviceaccessprocedure = models.CharField(
        db_column="Serviceaccessprocedure", max_length=-1, blank=True, null=True
    )
    shipreportingserviceareaid = models.OneToOneField(
        Reportableservicearea,
        models.DO_NOTHING,
        db_column="ShipreportingserviceareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Shipreportingservicearea"


class Signalstationtraffic(models.Model):
    categoryofsignalstationtraffic = models.CharField(
        db_column="Categoryofsignalstationtraffic", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    signalstationtrafficid = models.OneToOneField(
        Organisationcontactarea,
        models.DO_NOTHING,
        db_column="SignalstationtrafficID",
        primary_key=True,
    )
    componentof = models.ForeignKey(
        Localportservicearea,
        models.DO_NOTHING,
        db_column="componentOf",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Signalstationtraffic"


class Signalstationwarning(models.Model):
    categoryofsignalstationwarning = models.CharField(
        db_column="Categoryofsignalstationwarning", max_length=-1, blank=True, null=True
    )
    communicationchannel = models.CharField(
        db_column="Communicationchannel", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    signalstationwarningid = models.OneToOneField(
        Featuretype,
        models.DO_NOTHING,
        db_column="SignalstationwarningID",
        primary_key=True,
    )
    componentof = models.ForeignKey(
        Localportservicearea,
        models.DO_NOTHING,
        db_column="componentOf",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Signalstationwarning"


class Sourceindication(models.Model):
    categoryofauthority = models.CharField(
        db_column="Categoryofauthority", max_length=-1, blank=True, null=True
    )
    countryname = models.CharField(
        db_column="Countryname", max_length=-1, blank=True, null=True
    )
    featurename = models.CharField(
        db_column="Featurename", max_length=-1, blank=True, null=True
    )
    reporteddate = models.CharField(
        db_column="Reporteddate", max_length=-1, blank=True, null=True
    )
    source = models.CharField(
        db_column="Source", max_length=-1, blank=True, null=True
    )
    sourcetype = models.CharField(
        db_column="Sourcetype", max_length=-1, blank=True, null=True
    )
    sourceindicationid = models.CharField(
        db_column="SourceindicationID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Sourceindication"


class Srvcontact(models.Model):
    thecontactdetails = models.ForeignKey(
        Contactdetails,
        models.DO_NOTHING,
        db_column="theContactDetails",
        blank=True,
        null=True,
    )
    serviceplace = models.ForeignKey(
        Organisationcontactarea,
        models.DO_NOTHING,
        db_column="servicePlace",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "SrvContact"


class Supervisedarea(models.Model):
    supervisedareaid = models.OneToOneField(
        Organisationcontactarea,
        models.DO_NOTHING,
        db_column="SupervisedareaID",
        primary_key=True,
    )
    controlauthority = models.ForeignKey(
        Authority,
        models.DO_NOTHING,
        db_column="controlAuthority",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "Supervisedarea"


class Telecommunications(models.Model):
    categoryofcommpref = models.CharField(
        db_column="Categoryofcommpref", max_length=-1, blank=True, null=True
    )
    contactinstructions = models.CharField(
        db_column="Contactinstructions", max_length=-1, blank=True, null=True
    )
    schedulebydayofweek = models.CharField(
        db_column="Schedulebydayofweek", max_length=-1, blank=True, null=True
    )
    telcomcarrier = models.CharField(
        db_column="Telcomcarrier", max_length=-1, blank=True, null=True
    )
    telecommunicationidentifier = models.CharField(
        db_column="Telecommunicationidentifier", max_length=-1, blank=True, null=True
    )
    telecommunicationservice = models.CharField(
        db_column="Telecommunicationservice", max_length=-1, blank=True, null=True
    )
    telecommunicationsid = models.CharField(
        db_column="TelecommunicationsID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Telecommunications"


class Telecommunicationservice(models.Model):
    data = models.CharField(
        db_column="Data", max_length=-1, blank=True, null=True
    )
    email = models.CharField(
        db_column="Email", max_length=-1, blank=True, null=True
    )
    facsimile = models.CharField(
        db_column="Facsimile", max_length=-1, blank=True, null=True
    )
    sms = models.CharField(
        db_column="Sms", max_length=-1, blank=True, null=True
    )
    streameddata = models.CharField(
        db_column="Streameddata", max_length=-1, blank=True, null=True
    )
    telegraph = models.CharField(
        db_column="Telegraph", max_length=-1, blank=True, null=True
    )
    telex = models.CharField(
        db_column="Telex", max_length=-1, blank=True, null=True
    )
    voice = models.CharField(
        db_column="Voice", max_length=-1, blank=True, null=True
    )
    telecommunicationserviceid = models.CharField(
        db_column="TelecommunicationserviceID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Telecommunicationservice"


class Textcontent(models.Model):
    categoryoftext = models.CharField(
        db_column="Categoryoftext", max_length=-1, blank=True, null=True
    )
    information = models.CharField(
        db_column="Information", max_length=-1, blank=True, null=True
    )
    onlineresource = models.CharField(
        db_column="Onlineresource", max_length=-1, blank=True, null=True
    )
    sourceindication = models.CharField(
        db_column="Sourceindication", max_length=-1, blank=True, null=True
    )
    textcontentid = models.CharField(
        db_column="TextcontentID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Textcontent"


class Timeintervalsbydayofweek(models.Model):
    dayofweek = models.CharField(
        db_column="Dayofweek", max_length=-1, blank=True, null=True
    )
    dayofweekisrange = models.CharField(
        db_column="Dayofweekisrange", max_length=-1, blank=True, null=True
    )
    timeofdayend = models.CharField(
        db_column="Timeofdayend", max_length=-1, blank=True, null=True
    )
    timeofdaystart = models.CharField(
        db_column="Timeofdaystart", max_length=-1, blank=True, null=True
    )
    timeintervalsbydayofweekid = models.CharField(
        db_column="TimeintervalsbydayofweekID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Timeintervalsbydayofweek"


class Trafficservrept(models.Model):
    reptfortrafficserv = models.ForeignKey(
        Shipreport,
        models.DO_NOTHING,
        db_column="reptForTrafficServ",
        blank=True,
        null=True,
    )
    reptforlocation = models.ForeignKey(
        Reportableservicearea,
        models.DO_NOTHING,
        db_column="reptForLocation",
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "TrafficServRept"


class Underkeelallowance(models.Model):
    operation = models.CharField(
        db_column="Operation", max_length=-1, blank=True, null=True
    )
    underkeelallowancefixed = models.CharField(
        db_column="Underkeelallowancefixed", max_length=-1, blank=True, null=True
    )
    underkeelallowancevariablebeambased = models.CharField(
        db_column="Underkeelallowancevariablebeambased",
        max_length=-1,
        blank=True,
        null=True,
    )
    underkeelallowancevariabledraughtbased = models.CharField(
        db_column="Underkeelallowancevariabledraughtbased",
        max_length=-1,
        blank=True,
        null=True,
    )
    underkeelallowanceid = models.CharField(
        db_column="UnderkeelallowanceID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Underkeelallowance"


class Underkeelclearanceallowancearea(models.Model):
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    underkeelallowance = models.CharField(
        db_column="Underkeelallowance", max_length=-1, blank=True, null=True
    )
    waterleveltrend = models.CharField(
        db_column="Waterleveltrend", max_length=-1, blank=True, null=True
    )
    underkeelclearanceallowanceareaid = models.OneToOneField(
        Featuretype,
        models.DO_NOTHING,
        db_column="UnderkeelclearanceallowanceareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Underkeelclearanceallowancearea"


class Underkeelclearancemanagementarea(models.Model):
    dynamicresource = models.CharField(
        db_column="Dynamicresource", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    underkeelclearancemanagementareaid = models.OneToOneField(
        Reportableservicearea,
        models.DO_NOTHING,
        db_column="UnderkeelclearancemanagementareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Underkeelclearancemanagementarea"


class Vesselsmeasurements(models.Model):
    comparisonoperator = models.CharField(
        db_column="Comparisonoperator", max_length=-1, blank=True, null=True
    )
    vesselscharacteristics = models.CharField(
        db_column="Vesselscharacteristics", max_length=-1, blank=True, null=True
    )
    vesselscharacteristicsunit = models.CharField(
        db_column="Vesselscharacteristicsunit", max_length=-1, blank=True, null=True
    )
    vesselscharacteristicsvalue = models.CharField(
        db_column="Vesselscharacteristicsvalue", max_length=-1, blank=True, null=True
    )
    vesselsmeasurementsid = models.CharField(
        db_column="VesselsmeasurementsID", primary_key=True, max_length=-1
    )

    class Meta:
        managed = True
        db_table = "Vesselsmeasurements"


class Vesseltrafficservicearea(models.Model):
    categoryofvesseltrafficservice = models.CharField(
        db_column="Categoryofvesseltrafficservice", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    requirementsformaintenanceoflisteningwatch = models.CharField(
        db_column="Requirementsformaintenanceoflisteningwatch",
        max_length=-1,
        blank=True,
        null=True,
    )
    serviceaccessprocedure = models.CharField(
        db_column="Serviceaccessprocedure", max_length=-1, blank=True, null=True
    )
    vesseltrafficserviceareaid = models.OneToOneField(
        Reportableservicearea,
        models.DO_NOTHING,
        db_column="VesseltrafficserviceareaID",
        primary_key=True,
    )

    class Meta:
        managed = True
        db_table = "Vesseltrafficservicearea"


class Waterwayarea(models.Model):
    dynamicresource = models.CharField(
        db_column="Dynamicresource", max_length=-1, blank=True, null=True
    )
    geometry = models.CharField(
        db_column="Geometry", max_length=-1, blank=True, null=True
    )
    siltationrate = models.CharField(
        db_column="Siltationrate", max_length=-1, blank=True, null=True
    )
    status = models.CharField(
        db_column="Status", max_length=-1, blank=True, null=True
    )
    waterwayareaid = models.OneToOneField(
        Supervisedarea, models.DO_NOTHING, db_column="WaterwayareaID", primary_key=True
    )

    class Meta:
        managed = True
        db_table = "Waterwayarea"
