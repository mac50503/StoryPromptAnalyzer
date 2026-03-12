# fcnIsLegEligibleForEDDPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsLegEligibleForEDDPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| thePayLeg | PayLeg | |
| calledFromRule | string | |
| calledFromRuleset | string | |

## Lógica de negocio

```blaze
isLegEligibleForEDDPay is a boolean initially false.if(theTrip <> nulland theTrip <> unknownand thePayLeg <> nulland thePayLeg <> unknown) then {isOnOrAfterEDDEffectiveDate is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTrip.beginDateTime, "IF_2024CBA_EXTENDED PREMIUM PAY_EFFECTIVE_DATE").if(isOnOrAfterEDDEffectiveDate and thePayLeg.hasExtendedPremiumPay) then {isLegEligibleForEDDPay = true.}fcnShow("Inside fcnIsLegEligibleForEDDPay."" ...calledFromRule = "calledFromRule" ...calledFromRuleset = "calledFromRuleset" ...trip = " theTrip.tripNameAndDate" ... thePayLeg.legPay.sequenceNumber = "thePayLeg.legPay.sequenceNumber" .. isLegEligibleForEDDPay = "isLegEligibleForEDDPay).}return isLegEligibleForEDDPay.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)

