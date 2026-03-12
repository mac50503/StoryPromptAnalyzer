# fcnCalculateTimeZoneOffset

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateTimeZoneOffset`

## Propósito
Ben Lang 3/6/2015 DE5863 - Returns the offset between two dateTimes in milliseconds

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime1 | DateTime | |
| dateTime2 | DateTime | |

## Lógica de negocio

```blaze
offset1 is an integer initially dateTime1.zone.getOffset(dateTime2).offset2 is an integer initially dateTime2.zone.getOffset(dateTime1).return math().abs(offset2) - math().abs(offset1).
```

## Historial de cambios

```
Ben Lang 3/6/2015 DE5863 - Returns the offset between two dateTimes in milliseconds
fcnShow("dayLightSavingsOffset = " offset1).
fcnShow("dayLightSavingsOffset 2 = " offset2).
fcnShow("Offset = " (math().abs(offset2) - math().abs(offset1))).
```

