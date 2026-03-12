# main

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\main`

## Propósito
*(Sin descripción)*

## Lógica de negocio

```blaze
////////    THIS FUNCTION IS TO BE USED FOR TESTING ONLY... CAN BE USED TO TRACK PERFORMANCE...//////debugMode = true.//fcnShow("===>>> in function main...").//result is some RuleResult initially null.//xmlData  is a string initially "C:/brmsRepo/PayCalcs/CrewRules/CrewRulesDebug/src/test/resources/xmlData/sampleData.xml".//schema is a string initially "C:/brmsRepo/PayCalcs/CrewRules/CrewRulesDataModel/schemas/CrewRulesDataModel.xsd".//aCrewPayRequest is some CrewPayRequest initially CrewPayRequest.unmarshallXmlToRequest(xmlData, schema).//if (aCrewPayRequest <> null) then//result = determineCrewPay(aCrewPayRequest).//else//print("===>>> ERROR <<<=== call to CrewPayRequest.unmarshallXmlToRequest returned null...").//fcnShow("===>>> exiting function main...").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCalculateForcedPremiumTripsPayValue](fcnCalculateForcedPremiumTripsPayValue.md)
- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)
- [fcnCalculateReserveBlockCredit](fcnCalculateReserveBlockCredit.md)
- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)
- [fcnDistributeRemainingReserveGuarantee](fcnDistributeRemainingReserveGuarantee.md)
- [fcnEnforceLongevityPayMax](fcnEnforceLongevityPayMax.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnResetSchedulePeriodPay](fcnResetSchedulePeriodPay.md)
- [fcnRoundCrewPayValues](fcnRoundCrewPayValues.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- [fcnShowSchedulePeriodSummary](fcnShowSchedulePeriodSummary.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

