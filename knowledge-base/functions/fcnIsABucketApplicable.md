# fcnIsABucketApplicable

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateReserveBucketPosition`

## Propósito
APIC-1381 changes for Reserve - NonA and A bucket distribution.- block added for reserves

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isABucketApplicable is a boolean initially false;// Find out what the Trip position istripAssignmentPosition is a string initially thePayTrip.assignmentCrewPosition.// Find out if the Duty Period is in Reserve or notisDutyPeriodUnderReserve is a boolean initially (fcnGetRapAssociationListAsString(theDutyPeriod)<> "none").// Find out if the Pay Leg is in position A or notlegCrewLegPosition is a string initially fcnGetLegCrewPosition(thePayLeg).if (isDutyPeriodUnderReserve = false) then {if (tripAssignmentPosition <> "FAA") then {if (legCrewLegPosition = "FAA") then {isABucketApplicable = true;}} else {isABucketApplicable = true;}} else {if(legCrewLegPosition = "FAA" or ((legCrewLegPosition = null or legCrewLegPosition = "") and tripAssignmentPosition = "FAA")) then { isABucketApplicable = true;}}if (isABucketApplicable = false and (thePayTrip.tripClass = "P" or   thePayLeg.legWorkCodeList.contains("PA"))) then {isABucketApplicable = true;}return isABucketApplicable;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetLegCrewPosition](fcnGetLegCrewPosition.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)

## Llamado por

- [fcnDistributeRedEyePremiumToPayBucket](fcnDistributeRedEyePremiumToPayBucket.md)

## Historial de cambios

```
APIC-1381 changes for Reserve - NonA and A bucket distribution.- block added for reserves
```

