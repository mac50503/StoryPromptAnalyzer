# fcnCalculateConusAndOconusLimitsForTripset

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateConusAndOconusLimitsForTripset`

## Propósito
Ben Lang - 4/22/2014 - US16536 - Sets the limits and taxes for conus and oconus pay.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripSet | TripSet | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripSet <> null and aTripPay <>null and fcnIsReserveBlock(aTripPay.payTrip) is equal to false) then{if(aTripSet.startDateTime.isBefore(DateTime.newInstance(2019, 1, 1, 0, 0))) then{aTripSet.conusLimit = aTripSet.numConusDay * 63.aTripSet.oconusLimit = aTripSet.numOconusDay * 68.aTripSet.perdiemLimit = aTripSet.numConusDay * 63 + aTripSet.numOconusDay * 68.}else if(aTripSet.startDateTime.isBefore(DateTime.newInstance(2022, 1, 1, 0, 0))) then{aTripSet.conusLimit = aTripSet.numConusDay * 66.aTripSet.oconusLimit = aTripSet.numOconusDay * 71.aTripSet.perdiemLimit = aTripSet.numConusDay * 66 + aTripSet.numOconusDay * 71.}else if(aTripSet.startDateTime.isBefore(DateTime.newInstance(2025, 1, 1, 0, 0))) then{aTripSet.conusLimit = aTripSet.numConusDay * 69.aTripSet.oconusLimit = aTripSet.numOconusDay * 74.aTripSet.perdiemLimit = aTripSet.numConusDay * 69 + aTripSet.numOconusDay * 74.}              else              {                             aTripSet.conusLimit = aTripSet.numConusDay * 80.aTripSet.oconusLimit = aTripSet.numOconusDay * 86.aTripSet.perdiemLimit = aTripSet.numConusDay * 80 + aTripSet.numOconusDay * 86.             }if (aTripSet.currentConusLimit + aTripPay.conusPay <= aTripSet.perdiemLimit) then{aTripSet.currentConusLimit += aTripPay.conusPay.aTripSet.currentOconusLimit = aTripSet.perdiemLimit  - aTripSet.currentConusLimit .}else{aTripSet.currentConusLimit  = aTripSet.perdiemLimit.aTripSet.currentOconusLimit = 0.}fcnShow("===>>> calculating Conus And Oconus Limits For Tripset " aTripSet.tripSetName " ... num couns days = " aTripSet.numConusDay " ... num oconus days = " aTripSet.numOconusDay " ... conus limit = " aTripSet.currentConusLimit  " ... oconus limit = " aTripSet.currentOconusLimit).              }
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsReserveBlock](fcnIsReserveBlock.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateConusAndOconusLimitsForInflightTripset](fcnCalculateConusAndOconusLimitsForInflightTripset.md)

## Historial de cambios

```
Ben Lang - 4/22/2014 - US16536 - Sets the limits and taxes for conus and oconus pay.
Namratha -10/16/24 -BLAEZR176- Sets the limits and taxes for conus and oconus pay for Post 2025.
```

