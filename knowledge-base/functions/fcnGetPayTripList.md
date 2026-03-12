# fcnGetPayTripList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<PayTrip>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayTripList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theBlazePayRequest | BlazePayRequest | |

## Lógica de negocio

```blaze
thePayTripList is some List<PayTrip> initially null.if (theBlazePayRequest.crewPayRequest <> null) thenthePayTripList = theBlazePayRequest.crewPayRequest.crewLine.tripList.else{thePayTripList = an ArrayList.thePayTripList.add(theBlazePayRequest.tripPayRequest.trip).}return thePayTripList.
```

