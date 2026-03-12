# fcnGetLegGroundTimePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetLegGroundTimePay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| thePayTrip | PayTrip | |

## Lógica de negocio

```blaze
legGroundTimePay is a real initially 0.0.if(thePayTrip <> null and thePayTrip <> unknownand fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(thePayTrip.beginDateTime, "2024_CBA_GROUND_TIME_PAY_EFFECTIVE_DATE")and thePayLeg <> null and thePayLeg <> unknownand not fcnIsLegReleasedDeadHead(thePayLeg)and thePayLeg.payLegOverrideValues <> null and thePayLeg.payLegOverrideValues <> unknown and thePayLeg.payLegOverrideValues.groundTimeOverrideMinutes > 150)  then {//Ground Time Pay - 0.01 TFP for each minute over 150.legGroundTimePay = (thePayLeg.payLegOverrideValues.groundTimeOverrideMinutes - 150) * 0.01.}return fcnRoundUpAt2DecimalPlaces(legGroundTimePay).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnIsLegReleasedDeadHead](fcnIsLegReleasedDeadHead.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

