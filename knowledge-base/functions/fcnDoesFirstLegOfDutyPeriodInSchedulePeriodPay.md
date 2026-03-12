# fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriodPay <>null and aDutyPeriodPay <> null) then{if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aDutyPeriodPay <> null and aDutyPeriodPay.tripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aDutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null and     aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and     fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and      fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) then{return true.}else{return false.}}else {if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null and     aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and         fcnGetFirstLegOfDutyPeriod(aDutyPeriodPay.payDutyPeriod).scheduledDepartureDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and     fcnGetFirstLegOfDutyPeriod(aDutyPeriodPay.payDutyPeriod).scheduledDepartureDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) then{return true.}else{return false.}}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)
- [fcnGetFirstLegOfDutyPeriod](fcnGetFirstLegOfDutyPeriod.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnDistributeToLateReturnBuckets](fcnDistributeToLateReturnBuckets.md)

