# fcnDetermineOconusPerDiemPayRate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineOconusPerDiemPayRate`

## Propósito
RS - CSCH-3895/CSCH-4055 - 10/27/2016 - Updated Per Diem Pay Rates

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime | DateTime | |

## Lógica de negocio

```blaze
oconusPayRate is a real initially fcnGetOConusPerDiemRateFromConfigCollection(dateTime);if(oconusPayRate <> 0.0) then{return oconusPayRate;}else if(fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(dateTime, "IF_2024_DOR_EFFECTIVE_DATE")) then{oconusPayRate is 3.45;}else if (dateTime.isAfter(DateTime.newInstance(2019, 1, 1, 2, 59))) then{oconusPayRate is 2.85;}else if(dateTime.isAfter(DateTime.newInstance(2016, 12, 1, 2, 59))) then{oconusPayRate is 2.80;}else{oconusPayRate is 2.65;}return oconusPayRate;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetOConusPerDiemRateFromConfigCollection](fcnGetOConusPerDiemRateFromConfigCollection.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)

## Historial de cambios

```
RS - CSCH-3895/CSCH-4055 - 10/27/2016 - Updated Per Diem Pay Rates
```

