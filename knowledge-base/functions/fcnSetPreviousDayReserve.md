# fcnSetPreviousDayReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetPreviousDayReserve`

## Propósito
17 Feb - Tim A - USCH-2158 - added call to new utility function fcnGetStartOfPreviousSwaDay to return the previous SWA day at 3AM...

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aPayTripList | List<PayTrip> | |

## Lógica de negocio

```blaze
foundMatch is a boolean initially false.if (aPayLeg <> null and aPayTripList <> null and aPayTripList.size() > 0) then{//fcnShow("===>>> ENTERING function fcnSetPreviousDayReserve with leg " aPayLeg.sequenceNumber).//prevDay is some DateTime initially aPayLeg.scheduledDepartureDateTime.minusDays(1).prevDay is some DateTime initially fcnGetStartOfPreviousSwaDay(aPayLeg.scheduledDepartureDateTime).  for each PayTrip in aPayTripList as an array of PayTrip do{if (foundMatch = false and      fcnIsReserveBlock(it) = true and     fcnIsDateTimeWithinDateTimeRange(prevDay, it.beginDateTime, it.endDateTime)) then{foundMatch = true.aPayLeg.legPay.previousDayIsReserve = true.}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetStartOfPreviousSwaDay](fcnGetStartOfPreviousSwaDay.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)
- [fcnIsReserveBlock](fcnIsReserveBlock.md)
- `fcnShow()`

## Historial de cambios

```
17 Feb - Tim A - USCH-2158 - added call to new utility function fcnGetStartOfPreviousSwaDay to return the previous SWA day at 3AM...
```

