# fcnGetLegalityTripList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<LegalityTrip>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetLegalityTripList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theBlazeRequest | BlazeRequest | |

## Lógica de negocio

```blaze
theLegalityTripList is some List<LegalityTrip> initially null.if (theBlazeRequest.crewLegalityRequest<>unknown and  theBlazeRequest.crewLegalityRequest<> null) thentheLegalityTripList = theBlazeRequest.crewLegalityRequest.crewLine.tripList.else{theLegalityTripList = an ArrayList.theLegalityTripList.add(theBlazeRequest.tripLegalityRequest.trip).}return theLegalityTripList.
```

