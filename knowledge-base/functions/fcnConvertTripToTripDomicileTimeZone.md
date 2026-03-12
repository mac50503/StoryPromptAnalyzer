# fcnConvertTripToTripDomicileTimeZone

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnConvertTripToTripDomicileTimeZone`

## Propósito
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Trip level to domicile time zone.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnConvertTripToTripDomicileTimeZone with Trip = " aPayTrip.tripName "....sequence number" aPayTrip.sequenceNumber  "...tripDomicileTimeZone" aPayTrip.tripDomicileTimeZone);if(aPayTrip.tripDomicileTimeZone <> null and aPayTrip.tripDomicileTimeZone <> unknown) then {if (aPayTrip.beginDateTime <> null and aPayTrip.beginDateTime <> unknown) then {aPayTrip.beginDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayTrip.beginDateTime, aPayTrip.tripDomicileTimeZone);}if (aPayTrip.endDateTime <> null and aPayTrip.endDateTime <> unknown) then {aPayTrip.endDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayTrip.endDateTime,aPayTrip.tripDomicileTimeZone);}}fcnShow("===>>> EXITING fcnConvertTripToTripDomicileTimeZone...");
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnCreateTripPayResponse](fcnCreateTripPayResponse.md)

## Historial de cambios

```
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Trip level to domicile time zone.
```

