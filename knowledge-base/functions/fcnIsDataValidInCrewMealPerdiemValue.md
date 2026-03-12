# fcnIsDataValidInCrewMealPerdiemValue

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsDataValidInCrewMealPerdiemValue`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aCrewPerdiemMeal | CrewPerDiemMeal | |

## Lógica de negocio

```blaze
if(aCrewPerdiemMeal.effectiveDateTime <> null and aCrewPerdiemMeal.effectiveDateTime <> unknown andaCrewPerdiemMeal.endDateTime <>null and aCrewPerdiemMeal.endDateTime <> unknown  andaCrewPerdiemMeal.payRateCode <> unknown and aCrewPerdiemMeal.perDiemRate <> unknown and aCrewPerdiemMeal.scheduledBlockTimeInHours <> unknown)then{return true.}return false
```

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)

