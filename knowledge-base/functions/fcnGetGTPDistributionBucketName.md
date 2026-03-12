# fcnGetGTPDistributionBucketName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetGTPDistributionBucketName`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
groundTimePayBucketName is a string initially null.if( thePayTrip <> nulland  thePayTrip <> unknownand theDutyPeriod <> nulland theDutyPeriod <> unknownand thePayLeg <> nulland thePayLeg <> unknown) then {isDutyPeriodUnderReserve is a boolean initially (fcnGetRapAssociationListAsString(theDutyPeriod)<> "none").tripAssignmentPosition is a string initially thePayTrip.assignmentCrewPosition.isFirstLegInDP is a boolean initially fcnIsFirstLegInDP(theDutyPeriod, thePayLeg).previousPayLeg is some PayLeg initially fcnGetPrevLegOfDP(theDutyPeriod, thePayLeg).prevLegCrewLegPosition is a string initially fcnGetLegCrewPosition(previousPayLeg).if(tripAssignmentPosition = "FAA" and not isDutyPeriodUnderReserve) then {groundTimePayBucketName = "GTPABUCKET".}if(groundTimePayBucketName = null) then {if(tripAssignmentPosition = "FAA") then {if(isFirstLegInDP) then {groundTimePayBucketName = "GTPABUCKET".} else {if(prevLegCrewLegPosition = null) then {groundTimePayBucketName = "GTPABUCKET".} else {if(prevLegCrewLegPosition = "FAA") then {groundTimePayBucketName = "GTPABUCKET".} else {groundTimePayBucketName = "GTPBUCKET".}}}} else {if(isFirstLegInDP) then {groundTimePayBucketName = "GTPBUCKET".} else {if(prevLegCrewLegPosition = null) then {groundTimePayBucketName = "GTPBUCKET".} else {if(prevLegCrewLegPosition = "FAA") then {groundTimePayBucketName = "GTPABUCKET".} else {groundTimePayBucketName = "GTPBUCKET".}}}}}}return groundTimePayBucketName.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetLegCrewPosition](fcnGetLegCrewPosition.md)
- [fcnGetPrevLegOfDP](fcnGetPrevLegOfDP.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)
- [fcnIsFirstLegInDP](fcnIsFirstLegInDP.md)

