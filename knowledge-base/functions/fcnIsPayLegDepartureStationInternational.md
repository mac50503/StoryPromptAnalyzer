# fcnIsPayLegDepartureStationInternational

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsPayLegDepartureStationInternational`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aGlobalDataCache <> null and aGlobalDataCache.stationMap <> null )then{  aDepartureStation is some Station initially aGlobalDataCache.stationMap.get(aPayLeg.departureLocation).if(aDepartureStation <> null and aDepartureStation is known and aDepartureStation.internationalIndicator is equal to "I") then{  return true.}}return false.
```

## Llamado por

- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)

