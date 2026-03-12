# fcnDoesPayLegBeginInSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesPayLegBeginInSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayleg | PayLeg | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aPayleg <> null and aPayleg.payDutyPeriod <> null and aPayleg.payDutyPeriod.payTrip <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayleg.payDutyPeriod.payTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if (aPayleg <> null and aPayleg.scheduledDepartureDateTime <> null and aSchedulePeriodPay <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag and aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and     aPayleg.scheduledDepartureDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and     aPayleg.scheduledDepartureDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.else if (aPayleg <> null and aPayleg.scheduledDepartureDateTime <> null and aSchedulePeriodPay <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag = false and     aPayleg.scheduledDepartureDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and     aPayleg.scheduledDepartureDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)

