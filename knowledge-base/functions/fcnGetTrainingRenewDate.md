# fcnGetTrainingRenewDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetTrainingRenewDate`

## Propósito
03/12/2015 - US20192 - Melissa S - Switched logic for looking up the nonfly code to use new function/new decision table

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |

## Lógica de negocio

```blaze
tripCounter is an integer initially 0.aTrip is some LegalityTrip initially null.while (tripCounter < theTripList.size()) do {aTrip = theTripList.get(tripCounter).if (aTrip.ghostedFlag = false) then {if (aTrip.isTrainingQualNonFly) then {return fcnGetSWADayStart(aTrip.endDateTime).}}tripCounter+=1;}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSWADayStart](fcnGetSWADayStart.md)

## Historial de cambios

```
03/12/2015 - US20192 - Melissa S - Switched logic for looking up the nonfly code to use new function/new decision table
03/19-2015 - US20257 - Melissa S - Switched to use nonfly type saved on trip
04/08/2015 - US20485- Melissa S - Changed renew date to be based on the trainingQualNonFly list instead of trainingNonFly
04/08/2015 - US20485 - Melissa S - Changed renewDate to be based on the SWA Day the trip ends on
05/12/2015 US20484 Corey Gu - Added aTrip.ghostedFlag = false condition.
```

