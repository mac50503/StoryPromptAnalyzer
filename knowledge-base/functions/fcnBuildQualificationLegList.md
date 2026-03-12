# fcnBuildQualificationLegList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<LegalityLeg>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Qualifications\Functions\fcnBuildQualificationLegList`

## Propósito
11/4/2014 - MS - US18846

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |

## Lógica de negocio

```blaze
tripIndex is an integer initially 0.dutyIndex is an integer initially 0.legIndex is an integer initially 0.isReserveBlock is a boolean initially false.legArray is some List<LegalityLeg> initially an ArrayList.if (theTripList <> null) then {while (tripIndex < theTripList.size()) do {isReserveBlock = (theTripList.get(tripIndex).tripType =(ignoring case) "R").if (theTripList.get(tripIndex).firstDutyPeriod <> null) then {dutyIndex = 0.while (dutyIndex < theTripList.get(tripIndex).dutyPeriodList.size()) do {if (theTripList.get(tripIndex).dutyPeriodList.get(dutyIndex).firstLeg <> null) then {legIndex = 0.while (legIndex < theTripList.get(tripIndex).dutyPeriodList.get(dutyIndex).legList.size()) do {theTripList.get(tripIndex).dutyPeriodList.get(dutyIndex).legList.get(legIndex).onReserveBlock = isReserveBlock.legArray.add(theTripList.get(tripIndex).dutyPeriodList.get(dutyIndex).legList.get(legIndex)).legIndex +=1.}}dutyIndex += 1.}}tripIndex += 1.}}return legArray.
```

## Historial de cambios

```
11/4/2014 - MS - US18846
```

