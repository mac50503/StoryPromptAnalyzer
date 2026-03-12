# fcnIsPayLegArrrivalStationInternational

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsPayLegArrrivalStationInternational`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aGlobalDataCache <> null and aGlobalDataCache.stationMap <> null )then{  aArrivalStation is some Station initially aGlobalDataCache.stationMap.get(aPayLeg.arrivalLocation).  if(aArrivalStation <> null and  aArrivalStation is known and aArrivalStation.internationalIndicator is equal to "I") then{return true.}}return false.
```

## Llamado por

- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)

