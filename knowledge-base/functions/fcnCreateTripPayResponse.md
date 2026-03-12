# fcnCreateTripPayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateTripPayResponse`

## Propósito
CREW-4750 - 4/23/2018 - Setting reports on holiday

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPayRequest | TripPayRequest | |
| includeInflight | boolean | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
theTripPayResponse is some TripPayResponse initially a TripPayResponse.theTripPay is some TripPay initially fcnCreateTripPay(theTripPayRequest.trip, includeInflight, aGlobalDataCache).theTripPayResponse.tripPay = theTripPay.//APIC-1586-Domicile Day Changesif2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTripPayRequest.trip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {//Function to set domicile time zonefcnSetTripDomicileTimeZone(theTripPayRequest.trip,aGlobalDataCache);// Function to convert non-transient fileds at Trip level to domicile time zone.fcnConvertTripToTripDomicileTimeZone(theTripPayRequest.trip);}// Set the reportsOnHoliday field for all PayDutyPeriodsfcnAssignDutyPeriodReportsOnHoliday(theTripPayRequest.trip, theTripPayRequest.swaHolidayList);return theTripPayResponse.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)
- [fcnConvertTripToTripDomicileTimeZone](fcnConvertTripToTripDomicileTimeZone.md)
- [fcnCreateTripPay](fcnCreateTripPay.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnSetTripDomicileTimeZone](fcnSetTripDomicileTimeZone.md)

## Historial de cambios

```
CREW-4750 - 4/23/2018 - Setting reports on holiday
APIC-1586-07/01/2025-Santosh Kudumu-Domicile Day Changes
```

