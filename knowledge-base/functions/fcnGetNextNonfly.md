# fcnGetNextNonfly

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetNextNonfly`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTripList | List<PayTrip> | |
| fromDateTime | DateTime | |
| nonflyCodes | string | |

## Lógica de negocio

```blaze
retVal is some PayTrip initially null.if (fromDateTime <> null and aPayTripList <> null and aPayTripList.size() > 0) then{for each PayTrip in aPayTripList as an array of PayTrip do{if (retVal = null and                                  it.nonFlyCode <> null and     it.nonFlyCode <> "" and    nonflyCodes contains match (ignoring case)";"it.nonFlyCode";" = true and    it.beginDateTime.isAfter(fromDateTime)) thenretVal = it.}}if (retVal = null) thenfcnShow("===>>> EXITING fcnGetNextNonfly... returning " retVal).elsefcnShow("===>>> EXITING fcnGetNextNonfly... returning nonfly trip " retVal.tripName).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

