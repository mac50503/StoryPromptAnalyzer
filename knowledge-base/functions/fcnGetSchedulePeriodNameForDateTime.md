# fcnGetSchedulePeriodNameForDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodNameForDateTime`

## Propósito
4/5/2016 - CSCH-2723 - Melissa S - Refactored for performance to use while loops and indexes instead of casting to Blaze arrays

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime | DateTime | |
| aSchedulePeriodPayList | List<SchedulePeriodPay> | |

## Lógica de negocio

```blaze
index is an integer initially 0.if (aDateTime <> null and aSchedulePeriodPayList<>null and aSchedulePeriodPayList.size() > 0) then {while (index < aSchedulePeriodPayList.size()) do {if(aSchedulePeriodPayList.get(index).schedulePeriodEnd <> null and aSchedulePeriodPayList.get(index).schedulePeriodStart <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if (if2025NewDomicileDayPayEffectiveDateActiveFlag and(aDateTime.toLocalDateTime().isAfter(aSchedulePeriodPayList.get(index).schedulePeriodStart.toLocalDateTime()) or aDateTime.toLocalDateTime().isEqual(aSchedulePeriodPayList.get(index).schedulePeriodStart.toLocalDateTime())) and       (aDateTime.toLocalDateTime().isBefore(aSchedulePeriodPayList.get(index).schedulePeriodEnd.toLocalDateTime()) or aDateTime.toLocalDateTime().isEqual(aSchedulePeriodPayList.get(index).schedulePeriodEnd.toLocalDateTime()))) then { return aSchedulePeriodPayList.get(index).schedulePeriodName.}else if ((aDateTime.isAfter(aSchedulePeriodPayList.get(index).schedulePeriodStart) or aDateTime.isEqual(aSchedulePeriodPayList.get(index).schedulePeriodStart)) and    (aDateTime.isBefore(aSchedulePeriodPayList.get(index).schedulePeriodEnd) or aDateTime.isEqual(aSchedulePeriodPayList.get(index).schedulePeriodEnd))) then {return aSchedulePeriodPayList.get(index).schedulePeriodName.}}index += 1.}}return "".
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)
- [fcnCreateTripSet](fcnCreateTripSet.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)

## Historial de cambios

```
4/5/2016 - CSCH-2723 - Melissa S - Refactored for performance to use while loops and indexes instead of casting to Blaze arrays
```

