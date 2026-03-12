# fcnGetFirstFlyingLegScheduledDepartureDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstFlyingLegScheduledDepartureDateTime`

## Propósito
6/16/2015 - Ben Lang - Initial Development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(theDutyPeriod <> null and  theDutyPeriod.dutyPeriodPay <> null and theDutyPeriod.dutyPeriodPay.tripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theDutyPeriod.dutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(not if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if(theDutyPeriod.legList <> null and theDutyPeriod.legList.size() > 0) then{legCounter is an integer initially 0.while(legCounter < theDutyPeriod.legList.size()) do{if(theDutyPeriod.legList.get(legCounter).legWorkCodeList <> null and   theDutyPeriod.legList.get(legCounter).legWorkCodeList.contains("RS") = false) then return theDutyPeriod.legList.get(legCounter).scheduledDepartureDateTime.legCounter += 1;}}}return theDutyPeriod.reportDateTime.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnAssociateInflightPayDutyPeriodsToRaps](fcnAssociateInflightPayDutyPeriodsToRaps.md)
- [fcnDistributeRedEyePremiumToPayBucket](fcnDistributeRedEyePremiumToPayBucket.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay](fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay.md)
- [fcnGetEffectiveReportDateTime](fcnGetEffectiveReportDateTime.md)

## Historial de cambios

```
6/16/2015 - Ben Lang - Initial Development
```

