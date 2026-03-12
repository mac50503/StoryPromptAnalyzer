# fcnIsLegEligibleForLDPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsLegEligibleForLDPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isLegEligibleForLDPay is a boolean initially false.isOnOrAfterEDDEffectiveDate is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTrip.beginDateTime, "IF_2024CBA_EXTENDED PREMIUM PAY_EFFECTIVE_DATE").isOnOrAfterLDEffectiveDate  is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTrip.beginDateTime, "IF_2024_LD_BLAZE_EFFECTIVE_DATE").if(((isOnOrAfterEDDEffectiveDate and not thePayLeg.hasExtendedPremiumPay) or not isOnOrAfterEDDEffectiveDate)        and thePayLeg.legWorkCodeList.contains("LD")and isOnOrAfterLDEffectiveDate) then {isLegEligibleForLDPay = true.}fcnShow("Inside fcnIsLegEligibleForLDPay."" ...trip = " theTrip.tripNameAndDate" ... thePayLeg.legPay.sequenceNumber = "thePayLeg.legPay.sequenceNumber" .. isLegEligibleForLDPay = "isLegEligibleForLDPay).return isLegEligibleForLDPay.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

