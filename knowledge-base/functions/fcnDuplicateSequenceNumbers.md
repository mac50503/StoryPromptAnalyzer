# fcnDuplicateSequenceNumbers

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDuplicateSequenceNumbers`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTripList | List<PayTrip> | |

## Lógica de negocio

```blaze
retVal is a string initially "none".aSeqNumList is some List<String> initially an ArrayList.if (aPayTripList <> null and aPayTripList.size() > 1) then{for each PayTrip in aPayTripList as an array of PayTrip do{aSeqNumList.add(it.sequenceNumber as an string).}for each PayTrip in aPayTripList as an array of PayTrip do{if (aSeqNumList.remove(it.sequenceNumber as an string)) then{if (aSeqNumList.contains(it.sequenceNumber as a string)) thenreturn "SEQUENCE NUMBER " it.sequenceNumber " IS DUPLICATED IN THE REQUEST".}}}return retVal.
```

