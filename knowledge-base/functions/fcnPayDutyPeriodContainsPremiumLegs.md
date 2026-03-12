# fcnPayDutyPeriodContainsPremiumLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnPayDutyPeriodContainsPremiumLegs`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (aPayDutyPeriod <> null and aPayDutyPeriod.legList.size() > 0) then {for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do {if (it.legWorkCodeList <> null and     fcnIsPremiumPayLeg(it) is equal to true) thenreturn true.}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsPremiumPayLeg](fcnIsPremiumPayLeg.md)

## Llamado por

- [fcnPayTripContainsPremiumLegs](fcnPayTripContainsPremiumLegs.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

