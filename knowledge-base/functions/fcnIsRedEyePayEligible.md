# fcnIsRedEyePayEligible

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsRedEyePayEligible`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| anyPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if(not (theTrip.assignmentLabel =  (ignoring case) "I" or theTrip.tripClass = (ignoring case) ("C" or "L")) andnot (theTrip.creditType = "F") and  not (theDutyPeriod.creditType = "F") and((theDutyPeriod.dutyPeriodPay.highestDutyPeriodRig=0 and theDutyPeriod.dutyPeriodPay.dutyPeriodMinimum < theDutyPeriod.dutyPeriodPay.sumLegTotalCredits) or(theDutyPeriod.dutyPeriodPay.highestDutyPeriodRig < theDutyPeriod.dutyPeriodPay.sumLegTotalCredits)) and((theTrip.tripPay.tripPayInflight.highestTripRig=0 and theTrip.tripPay.tripPayInflight.adgValue < theTrip.tripPay.tripPayInflight.dutyPeriodSum) or(theTrip.tripPay.tripPayInflight.highestTripRig < theTrip.tripPay.tripPayInflight.dutyPeriodSum)) andnot (anyPayLeg.creditType = (ignoring case) "F") andanyPayLeg.redEye=RedEyeType.SCHEDULED andnot (anyPayLeg.creditType = (ignoring case) "F" or anyPayLeg.legWorkCodeList.contains("CT") or fcnIsLegReleasedDeadHead(anyPayLeg) or fcnIsNonPaidLimoLeg(anyPayLeg))) then {return true.}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsLegReleasedDeadHead](fcnIsLegReleasedDeadHead.md)
- [fcnIsNonPaidLimoLeg](fcnIsNonPaidLimoLeg.md)

