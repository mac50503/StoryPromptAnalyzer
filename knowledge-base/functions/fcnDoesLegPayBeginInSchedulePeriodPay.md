# fcnDoesLegPayBeginInSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesLegPayBeginInSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aLegPay <> null and aLegPay.dutyPeriodPay <> null and aLegPay.dutyPeriodPay.tripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aLegPay.dutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if (aLegPay <> null and aLegPay.payLeg <> null and aSchedulePeriodPay <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag and aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and      aLegPay.payLeg.scheduledDepartureDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and     aLegPay.payLeg.scheduledDepartureDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.else if (aLegPay <> null and aLegPay.payLeg <> null and aSchedulePeriodPay <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag = false and     aLegPay.payLeg.scheduledDepartureDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and     aLegPay.payLeg.scheduledDepartureDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

