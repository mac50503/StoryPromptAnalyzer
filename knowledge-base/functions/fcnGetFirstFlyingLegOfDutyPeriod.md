# fcnGetFirstFlyingLegOfDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstFlyingLegOfDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
legCounter is an integer initially 0;aPayLeg is some PayLeg initially null.isAdditionalUseCaseApplicableEffectiveDate is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayDutyPeriod.reportDateTime, "IF_2025_ADDITIONAL_CREW_MEALS_BLAZE_EFFECTIVE_DATETIME").if(aPayDutyPeriod.legList<>null and aPayDutyPeriod.legList.size()>0)then{while(legCounter < aPayDutyPeriod.legList.size()) do{if(isAdditionalUseCaseApplicableEffectiveDate) then {if((aPayDutyPeriod.legList.get(legCounter).nonFlyCode = null as a string oraPayDutyPeriod.legList.get(legCounter).nonFlyCode = "" or aPayDutyPeriod.legList.get(legCounter).nonFlyCode is unknown)  and (fcnIsLegWorkCodeInCrewMealExclusionary(aPayDutyPeriod.legList.get(legCounter)) = false))then  return aPayDutyPeriod.legList.get(legCounter).} else {if((aPayDutyPeriod.legList.get(legCounter).nonFlyCode = null as a string oraPayDutyPeriod.legList.get(legCounter).nonFlyCode = "" or aPayDutyPeriod.legList.get(legCounter).nonFlyCode is unknown))then  return aPayDutyPeriod.legList.get(legCounter).}legCounter+=1;}}return aPayLeg
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnIsLegWorkCodeInCrewMealExclusionary](fcnIsLegWorkCodeInCrewMealExclusionary.md)

## Llamado por

- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)

