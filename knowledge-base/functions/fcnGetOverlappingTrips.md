# fcnGetOverlappingTrips

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<LegalityTrip>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetOverlappingTrips`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTrip | LegalityTrip | |
| aTripList | List<LegalityTrip> | |
| aDomicileSwaDay | DomicileSwaDay | |

## Lógica de negocio

```blaze
//fcnShow("===>>> ENTERING function fcnGetOverlappingTrips with trip = " aTrip.tripName).retVal is some List<LegalityTrip> initially an ArrayList.overlaps is a boolean initially false.aCandidateTrip is some LegalityTrip initially null.if (aTrip <> null and aTripList <> null and aTripList <> null and aTripList.size() > 0) then{for each LegalityTrip in aTripList as an array of LegalityTrip do {aCandidateTrip = it.if (aCandidateTrip <> aTrip) then{overlaps = false.//// TEST IF CANDIDATE TRIP BEGINS WITHIN SPAN OF BASE TRIPif (aCandidateTrip.beginDateTime.isBefore(aTrip.beginDateTime) = false and    aCandidateTrip.beginDateTime.isAfter(aTrip.endDateTime) = false) thenoverlaps = true.//// TEST IF CANDIDATE TRIP ENDS WITHIN SPAN OF BASE TRIPif (overlaps = false and                                      aCandidateTrip.endDateTime.isBefore(aTrip.beginDateTime) = false and   aCandidateTrip.endDateTime.isAfter(aTrip.endDateTime) = false) thenoverlaps = true.//// TEST IF CANDIDATE TRIP SPANS BASE TRIPif (overlaps = false and                                      aCandidateTrip.beginDateTime.isBefore(aTrip.beginDateTime) = true and   aCandidateTrip.endDateTime.isAfter(aTrip.endDateTime) = true) thenoverlaps = true.if (overlaps = true) thenretVal.add(aCandidateTrip).}}}//fcnShow("===>>> EXITING function fcnGetOverlappingTrips with trip = " aTrip.tripName " ...size of overlapping trips list = " retVal.size()).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`
- [ping](ping.md)

