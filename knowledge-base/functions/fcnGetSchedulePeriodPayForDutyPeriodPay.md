# fcnGetSchedulePeriodPayForDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodPayForDutyPeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
retVal is some SchedulePeriodPay initially null.if (aDutyPeriodPay <> null and      aDutyPeriodPay.tripPay.startSchedulePeriodPay <> null and      aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodStart <> null and      aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodEnd <> null) then{if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aDutyPeriodPay.tripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aDutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if (aDutyPeriodPay.reportDateTime.toLocalDateTime().isBefore(aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and aDutyPeriodPay.reportDateTime.toLocalDateTime().isAfter(aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) then{retVal = aDutyPeriodPay.tripPay.startSchedulePeriodPay.}else if (aDutyPeriodPay.tripPay.endSchedulePeriodPay <> null and aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodStart <> null andaDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodEnd <> null andaDutyPeriodPay.reportDateTime.toLocalDateTime().isBefore(aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and  aDutyPeriodPay.reportDateTime.toLocalDateTime().isAfter(aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) then{retVal = aDutyPeriodPay.tripPay.endSchedulePeriodPay.}}else {if (aDutyPeriodPay.reportDateTime.isBefore(aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodStart) is equal to false and aDutyPeriodPay.reportDateTime.isAfter(aDutyPeriodPay.tripPay.startSchedulePeriodPay.schedulePeriodEnd) is equal to false) then{retVal = aDutyPeriodPay.tripPay.startSchedulePeriodPay.}else if (aDutyPeriodPay.tripPay.endSchedulePeriodPay <> null and aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodStart <> null andaDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodEnd <> null andaDutyPeriodPay.reportDateTime.isBefore(aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodStart) is equal to false and  aDutyPeriodPay.reportDateTime.isAfter(aDutyPeriodPay.tripPay.endSchedulePeriodPay.schedulePeriodEnd) is equal to false) then{retVal = aDutyPeriodPay.tripPay.endSchedulePeriodPay.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnGetFirstDutyInNextSchedulePeriod](fcnGetFirstDutyInNextSchedulePeriod.md)
- [fcnGetSchedulePeriodPayForLegPay](fcnGetSchedulePeriodPayForLegPay.md)
- [fcnIsDPPayEndsInNextSPPay](fcnIsDPPayEndsInNextSPPay.md)

