# fcnIsLegWorkCodeInCrewMealExclusionary

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsLegWorkCodeInCrewMealExclusionary`

## Propósito
BLAZER-185 -11/11/2024 Namratha: Added Function for Crew Meal Perdiem Exclusionary Conditions

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
isLegWorkCodeInCrewMealExclusionary is a boolean initially false.if(aPayLeg.legWorkCodeList <> null and aPayLeg.legWorkCodeList.size() > 0 andaPayLeg.legWorkCodeList.contains("GR" ) ) then {isLegWorkCodeInCrewMealExclusionary = true.}return isLegWorkCodeInCrewMealExclusionary.
```

## Llamado por

- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnGetFirstFlyingLegOfDutyPeriod](fcnGetFirstFlyingLegOfDutyPeriod.md)

## Historial de cambios

```
BLAZER-185 -11/11/2024 Namratha: Added Function for Crew Meal Perdiem Exclusionary Conditions
```

