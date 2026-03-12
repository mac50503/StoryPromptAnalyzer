# fcnIsDPPayEndsInNextSPPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsDPPayEndsInNextSPPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| theLegPay | LegPay | |
| theSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
isDPPayEndsInNextSPPay is a boolean initially false.legSchedPeriodPay is some SchedulePeriodPay initially fcnGetSchedulePeriodPayForLegPay(theLegPay).firstDPInNextSP is some PayDutyPeriod initially fcnGetFirstDutyInNextSchedulePeriod(thePayTrip).if(legSchedPeriodPay <> nulland legSchedPeriodPay <> unknownand firstDPInNextSP <> null and firstDPInNextSP <> unknownand theDutyPeriod <> nulland theDutyPeriod <> unknownand theSchedulePeriodPay <> nulland theSchedulePeriodPay <> unknown) then {nextSchedPeriodPay is some SchedulePeriodPay initially fcnGetSchedulePeriodPayForDutyPeriodPay(firstDPInNextSP.dutyPeriodPay).if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(thePayTrip <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(thePayTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(legSchedPeriodPay.schedulePeriodName <> nextSchedPeriodPay.schedulePeriodNameand theSchedulePeriodPay.schedulePeriodName = legSchedPeriodPay.schedulePeriodName and if2025NewDomicileDayPayEffectiveDateActiveFlagand nextSchedPeriodPay.schedulePeriodStart <> nulland theDutyPeriod.releaseDateTime.toLocalDateTime().isAfter(nextSchedPeriodPay.schedulePeriodStart.toLocalDateTime())) then {isDPPayEndsInNextSPPay = true.}else if(legSchedPeriodPay.schedulePeriodName <> nextSchedPeriodPay.schedulePeriodNameand theSchedulePeriodPay.schedulePeriodName = legSchedPeriodPay.schedulePeriodNameand if2025NewDomicileDayPayEffectiveDateActiveFlag = false and theDutyPeriod.releaseDateTime.isAfter(nextSchedPeriodPay.schedulePeriodStart)) then {isDPPayEndsInNextSPPay = true.}}fcnShow(" ==>> EXITING function fcnIsDPPayEndsInNextSPPay ""   isDPPayEndsInNextSPPay ==>>"isDPPayEndsInNextSPPay).return isDPPayEndsInNextSPPay.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstDutyInNextSchedulePeriod](fcnGetFirstDutyInNextSchedulePeriod.md)
- [fcnGetSchedulePeriodPayForDutyPeriodPay](fcnGetSchedulePeriodPayForDutyPeriodPay.md)
- [fcnGetSchedulePeriodPayForLegPay](fcnGetSchedulePeriodPayForLegPay.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

