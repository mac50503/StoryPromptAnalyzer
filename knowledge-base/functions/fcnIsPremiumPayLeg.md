# fcnIsPremiumPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsPremiumPayLeg`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and aPayLeg.legWorkCodeList <> null) then {if (aPayLeg.legWorkCodeList.contains("PP") or     aPayLeg.legWorkCodeList.contains("VR")  or     aPayLeg.legWorkCodeList.contains("CT")  or     aPayLeg.legWorkCodeList.contains("DT")) thenreturn true.}return false.
```

## Llamado por

- [fcnPayDutyPeriodContainsPremiumLegs](fcnPayDutyPeriodContainsPremiumLegs.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

