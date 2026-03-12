# fcnDoesPayAdjustmentBeginInSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesPayAdjustmentBeginInSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayAdjustment | PayAdjustment | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aPayAdjustment <> null and aPayAdjustment <> unknown) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayAdjustment.effectiveDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}//fcnShow("===>>>ENTERING fcnDoesPayAdjustmentBeginInSchedulePeriod with Pay Adjustment " aPayAdjustment.adjustmentCode " ... effectiveDate = " aPayAdjustment.effectiveDateTime " ... SP = " aSchedulePeriodPay.schedulePeriodName).if (aPayAdjustment <> null and     aPayAdjustment <> unknown and     aSchedulePeriodPay <> null and     aSchedulePeriodPay <> unknown and    if2025NewDomicileDayPayEffectiveDateActiveFlag and aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and    (aPayAdjustment.effectiveDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) = false)  and    (aPayAdjustment.effectiveDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) = false) ) then {retVal = true.}else if (aPayAdjustment <> null and     aPayAdjustment <> unknown and     aSchedulePeriodPay <> null and     aSchedulePeriodPay <> unknown and    if2025NewDomicileDayPayEffectiveDateActiveFlag = false and    (aPayAdjustment.effectiveDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) = false)  and    (aPayAdjustment.effectiveDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) = false) ) then {retVal = true.}else {retVal = false.}//fcnShow("===>>>EXITING fcnDoesPayAdjustmentBeginInSchedulePeriod with Pay Adjustment " aPayAdjustment.adjustmentCode " ... SP = " aSchedulePeriodPay.schedulePeriodName " ...retunring " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)

