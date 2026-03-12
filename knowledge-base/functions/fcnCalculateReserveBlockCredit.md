# fcnCalculateReserveBlockCredit

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateReserveBlockCredit`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnCalculateReserveBlockCredit ... DP = " theDutyPeriodPay.sequenceNumber " ...CT = " theDutyPeriodPay.creditType " ... RAP association = " fcnGetRapAssociationListAsString(theDutyPeriodPay.payDutyPeriod) " ... dpm = " theDutyPeriodPay.dutyPeriodMinimum " ...dhr = " theDutyPeriodPay.dutyHourRatio " ... DP base pay = " theDutyPeriodPay.basePay " ... sum base leg pay = " theDutyPeriodPay.sumLegBaseCredits " ... sum leg pay = " theDutyPeriodPay.sumLegTotalCredits).retVal is a real.fallsOnReserveBlock is a boolean initially true.if (theDutyPeriodPay.payDutyPeriod.payDutyPeriodInflight <> null) thenif (theDutyPeriodPay.payDutyPeriod.payDutyPeriodInflight.rapAssociationList.size() = 0) thenfallsOnReserveBlock = false.if (theDutyPeriodPay.creditType = (ignoring case) "Q" or    // DE6965    theDutyPeriodPay.creditType = (ignoring case) "P") then // DE6494{retVal = fcnMaxOf3Numbers(theDutyPeriodPay.sumLegBaseCredits, theDutyPeriodPay.basePay, theDutyPeriodPay.dutyHourRatio).fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber " greatest of sum of leg base, base pay, or DHR of " retVal " to Reserve Block Day...").}else if (theDutyPeriodPay.creditType = (ignoring case) "F" or          theDutyPeriodPay.payDutyPeriod.dutyType = "RON") then // DE6848 and DE6870 - RON duty periods pay basePay on reserve days{retVal = theDutyPeriodPay.basePay.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s basePay of " theDutyPeriodPay.basePay " to Reserve Block Day...").}else if (theDutyPeriodPay.baseCreditType = (ignoring case) "M" or theDutyPeriodPay.creditType = (ignoring case) "M") then{retVal = theDutyPeriodPay.dutyPeriodMinimum.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s dutyPeriodMinimum of " theDutyPeriodPay.dutyPeriodMinimum " to Reserve Block Day...").}else if (theDutyPeriodPay.creditType = (ignoring case) "E") then{retVal = math().max(theDutyPeriodPay.basePay, theDutyPeriodPay.dutyHourRatio).fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s DHR of " theDutyPeriodPay.dutyHourRatio " to Reserve Block Day...").}else if (theDutyPeriodPay.creditType = (ignoring case) "D") then{retVal = theDutyPeriodPay.dutyHourRatio.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s DHR of " theDutyPeriodPay.dutyHourRatio " to Reserve Block Day...").}// DE6964else if (theDutyPeriodPay.sumLegTotalCredits >= theDutyPeriodPay.dutyHourRatio and theDutyPeriodPay.sumLegTotalCredits >= theDutyPeriodPay.basePay and fallsOnReserveBlock = false) then{retVal = theDutyPeriodPay.sumLegTotalCredits.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s sumLegTotalCredits of " theDutyPeriodPay.sumLegTotalCredits " to Reserve Block Day...").}// CSCH-2159else if (theDutyPeriodPay.sumLegTotalCredits >= theDutyPeriodPay.dutyHourRatio and theDutyPeriodPay.sumLegTotalCredits >= theDutyPeriodPay.basePay and fallsOnReserveBlock) then{retVal = theDutyPeriodPay.sumLegBaseCredits.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s sumLegBaseCredits of " theDutyPeriodPay.sumLegBaseCredits " to Reserve Block Day...").}//DE6649else if (theDutyPeriodPay.sumLegBaseCredits >= theDutyPeriodPay.dutyHourRatio and theDutyPeriodPay.sumLegBaseCredits < theDutyPeriodPay.basePay) then{retVal = theDutyPeriodPay.basePay.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s basePay of " theDutyPeriodPay.basePay " to Reserve Block Day...").}// remove if constructelse if (at least 1 PayLeg in theDutyPeriodPay.payDutyPeriod.legList as an array of PayLeg satisfies it.limoFlag = false) then{retVal = theDutyPeriodPay.dutyHourRatio.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s DHR of " theDutyPeriodPay.dutyHourRatio " to Reserve Block Day...").}else retVal = 0.if (theDutyPeriodPay.payDutyPeriod.dpFlags = (ignoring case) "S") then // SCHEDULER SPLIT...{theDutyPeriodPay.remainingSplitGuaranty = math().max(0.0, 4.0 - retVal).theDutyPeriodPay.remainingSplitGuaranty = fcnRoundUpAt2DecimalPlaces(theDutyPeriodPay.remainingSplitGuaranty).fcnShow("===>>> Setting DP split guaranty remaining to " theDutyPeriodPay.remainingSplitGuaranty).retVal = retVal + theDutyPeriodPay.remainingSplitGuaranty.fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s remaining split guaranty of " theDutyPeriodPay.remainingSplitGuaranty " to Reserve Block Day... value now = " retVal).}if (theDutyPeriodPay.tripPay <> null and  //// THIS WAS ADDED TO ALLOW BRUNIT TESTS TO DECLARE ONLY DUTIES    theDutyPeriodPay.tripPay.creditType = (ignoring case) "F") then{retVal += theDutyPeriodPay.tripExcess.    //// DE7232 - adding trip excess fcnShow("===>>> Adding DP " theDutyPeriodPay.sequenceNumber "'s trip excess of  " theDutyPeriodPay.tripExcess " to Reserve Block Day... value now = " retVal).}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)
- [fcnMaxOf3Numbers](fcnMaxOf3Numbers.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [main](main.md)

