# fcnDetermineConusPerDiemPayRate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineConusPerDiemPayRate`

## Propósito
RS - CSCH-3895/CSCH-4055 - 10/27/2016 - Updated Per Diem Pay Rates

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime | DateTime | |

## Lógica de negocio

```blaze
conusPayRate is a real initially fcnGetConusPerDiemRateFromConfigCollection(dateTime);if(conusPayRate <> 0.0) then{return conusPayRate;}else if(fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(dateTime, "IF_2024_DOR_EFFECTIVE_DATE")) then{conusPayRate is 2.90;}else if (dateTime.isAfter(DateTime.newInstance(2019, 1, 1, 2, 59))) then{conusPayRate is 2.35;}else if(dateTime.isAfter(DateTime.newInstance(2016, 12, 1, 2, 59))) then{conusPayRate is 2.30;}else{conusPayRate is 2.15;}return conusPayRate;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetConusPerDiemRateFromConfigCollection](fcnGetConusPerDiemRateFromConfigCollection.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnDistributeToFP5Bucket](fcnDistributeToFP5Bucket.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)

## Historial de cambios

```
RS - CSCH-3895/CSCH-4055 - 10/27/2016 - Updated Per Diem Pay Rates
```

