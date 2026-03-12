# fcnPayTripContainsPremiumLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnPayTripContainsPremiumLegs`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do {if (fcnPayDutyPeriodContainsPremiumLegs(it) is equal to true) then return true.}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnPayDutyPeriodContainsPremiumLegs](fcnPayDutyPeriodContainsPremiumLegs.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

