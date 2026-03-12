# fcnSetTripNonDeadheadBeginEndTimes

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetTripNonDeadheadBeginEndTimes`

## Propósito
RS - CREW-3446 - 9/18/2017 - Allow overriding of Per Diem dates

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aCrewPayResponse | CrewPayResponse | |

## Lógica de negocio

```blaze
aTripPay is some TripPay initially null.spIndex is an integer initially 0.tripIndex is an integer initially 0.//Setting the perdiemTimeAwayFromBase for each TripPay object in the SchedulePeriodPay, since these objects are not directly referenced with the CrewMemberLine.tripList  while (spIndex < aCrewPayResponse.schedulePeriodPayList.size()) do{tripIndex = 0.while (tripIndex < aCrewPayResponse.schedulePeriodPayList.get(spIndex).tripPayList.size()) do{aTripPay = aCrewPayResponse.schedulePeriodPayList.get(spIndex).tripPayList.get(tripIndex).fcnSetTripNonDeadheadBeginEndTime(aTripPay).tripIndex += 1.}spIndex += 1.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnSetTripNonDeadheadBeginEndTime](fcnSetTripNonDeadheadBeginEndTime.md)

## Historial de cambios

```
RS - CREW-3446 - 9/18/2017 - Allow overriding of Per Diem dates
```

