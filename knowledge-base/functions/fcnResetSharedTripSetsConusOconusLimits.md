# fcnResetSharedTripSetsConusOconusLimits

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnResetSharedTripSetsConusOconusLimits`

## Propósito
Akshay M: DE6075  Created this function to reset tripsets current perdiem limits for every new schedule period. If a tripset is shared between 2 schedule periods, the second schedule period adds the conus/oconus pay for the second time and hence the limits were getting doubled. This function eliminates this defect.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
//             a SchedulePeriodPay might not contain a TripSet but still contain the trip which belongs to that TripSet, //and since setting of conus/oconus per diem limit  uses payTrip.tripSet, we need to reset the TripSet for each payTrip in a schedulePeriod.if (aSchedulePeriodPay<>null) then{for each TripPay in aSchedulePeriodPay.tripPayList as an array of TripPay do{if (it.payTrip <> null and it.payTrip.tripSet <> null) then{it.payTrip.tripSet.currentConusLimit = 0.it.payTrip.tripSet.currentOconusLimit = 0.}}}
```

## Historial de cambios

```
Akshay M: DE6075  Created this function to reset tripsets current perdiem limits for every new schedule period. If a tripset is shared between 2 schedule periods, the second schedule period adds the conus/oconus pay for the second time and hence the limits were getting doubled. This function eliminates this defect.
```

