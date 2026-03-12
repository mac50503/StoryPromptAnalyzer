# fcnIsDutyPeriodPayWithinSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsDutyPeriodPayWithinSchedulePeriodPay`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aDutyPeriodPay <> null and     aSchedulePeriodPay <> null and aDutyPeriodPay.tripPay <> null and    fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aDutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME") and    aDutyPeriodPay.reportDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) = false and    aDutyPeriodPay.releaseDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) = false) thenreturn true.else if (aDutyPeriodPay <> null and     aSchedulePeriodPay <> null and    aDutyPeriodPay.reportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) = false and    aDutyPeriodPay.releaseDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) = false) thenreturn true.elsereturn false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

