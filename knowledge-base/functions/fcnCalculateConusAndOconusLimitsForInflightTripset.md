# fcnCalculateConusAndOconusLimitsForInflightTripset

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateConusAndOconusLimitsForInflightTripset`

## Propósito
8/18/2015 - Melissa S - DE7234 - Refactored this function to lop through the trip set list instead of firing for a single trip.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripSetList | List<TripSet> | |

## Lógica de negocio

```blaze
tripSetIndex is an integer initially 0.payTripIndex is an integer initially 0.if (theTripSetList <> null and theTripSetList.size() > 0) then{while (tripSetIndex < theTripSetList.size()) do {aTripSet is some TripSet initially theTripSetList.get(tripSetIndex).fcnShow("fcnCalculateConusAndOconusLimitsForInflightTripset for Schedule Period = " aTripSet.schedulePeriodName " ..tripSetName = " aTripSet.tripSetName " ...numConusDay = " aTripSet.numConusDay).if (aTripSet.payTripList.size() > 0) then {payTripIndex = 0.while (payTripIndex < aTripSet.payTripList.size()) do {aTripPay is some TripPay initially aTripSet.payTripList.get(payTripIndex).tripPay.fcnCalculateConusAndOconusLimitsForTripset(aTripSet, aTripPay).payTripIndex +=1.}}tripSetIndex += 1.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateConusAndOconusLimitsForTripset](fcnCalculateConusAndOconusLimitsForTripset.md)
- `fcnShow()`

## Historial de cambios

```
8/18/2015 - Melissa S - DE7234 - Refactored this function to lop through the trip set list instead of firing for a single trip.
```

