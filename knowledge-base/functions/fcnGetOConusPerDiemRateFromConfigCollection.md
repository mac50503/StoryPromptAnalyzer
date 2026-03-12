# fcnGetOConusPerDiemRateFromConfigCollection

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetOConusPerDiemRateFromConfigCollection`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDateTime | DateTime | |

## Lógica de negocio

```blaze
theConfigCollection is some ConfigCollection initially inFlightGlobalVar.configCollection.if(theConfigCollection <> null and theConfigCollection <> unknown and theDateTime <> null and theDateTime <> unknown and theConfigCollection.perDiemList <> null) then {for each PerDiem in theConfigCollection.perDiemList as an array of PerDiem do{if((theDateTime.isAfter(it.startDateTime) or theDateTime.isEqual(it.startDateTime)) and (theDateTime.isBefore(it.endDateTime) or theDateTime.isEqual(it.endDateTime))) then {return it.perDiemRateOconus;}}}return 0.0;
```

## Llamado por

- [fcnDetermineOconusPerDiemPayRate](fcnDetermineOconusPerDiemPayRate.md)

