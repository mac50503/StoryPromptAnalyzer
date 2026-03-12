# fcnDetermineLegBlockTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnDetermineLegBlockTime`

## Propósito
hasBlock is a boolean initially false.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | LegalityLeg | |

## Lógica de negocio

```blaze
// If leg is a flying leg (not a deadhead, nonflycode in unknown)if (theLeg.isDeadhead = false and theLeg.nonFlyCode = ("" or (null as a string))) then {return Duration.newInstance(theLeg.determineDepartureDateTime(), theLeg.determineArrivalDateTime()).standardMinutes.} else {return 0;}
```

## Llamado por

- [fcnBuildTripCalculatedValuesList](fcnBuildTripCalculatedValuesList.md)
- [fcnDetermineDutyPeriodTransientTerms](fcnDetermineDutyPeriodTransientTerms.md)

## Historial de cambios

```
hasBlock is a boolean initially false.
nextLeg is some LegalityLeg.
nextNextLeg is some LegalityLeg.
legs is some List&lt;LegalityLeg&gt; initially theDutyPeriod.legList.
// If leg is a flying leg (not a deadhead, nonflycode in unknown)
if (theLeg.isDeadhead = false and theLeg.nonFlyCode = ("" or (null as a string))) then {
if (theLeg.legWorkCode = (null as a string) or (theLeg.legWorkCode &lt;&gt; ((null as a string) and "GR"))) then {
// If the flying leg is not a gate return - it has a block time
hasBlock = true.
} else if (theDutyPeriod.legList.indexOf(theLeg) + 1 &lt; theDutyPeriod.legList.size()) then {
// If the flying leg is a gate return
nextLeg = legs.get(theDutyPeriod.legList.indexOf(theLeg) + 1).
if (nextLeg.isDeadhead = false and nextLeg.nonFlyCode = ("" or (null as a string))) then {
if (nextLeg.legWorkCode = (null as a string) or (nextLeg.legWorkCode &lt;&gt; ((null as a string) and "GR"))) then {
// If the flying leg is immediately follwed by a non gate return flying leg - it has a block time
hasBlock = true.
// If the flying leg with a gate return is immediately follwed by another flying leg with a gate return
} else if (theDutyPeriod.legList.indexOf(theLeg) + 2 &lt; theDutyPeriod.legList.size()) then {
nextNextLeg = legs.get(theDutyPeriod.legList.indexOf(theLeg) + 2).
if (nextNextLeg.isDeadhead = false and nextNextLeg.nonFlyCode = ("" or (null as a string)) and nextNextLeg.legWorkCode = (null as a string) or (nextNextLeg.legWorkCode &lt;&gt; ((null as a string) and "GR"))) then {
// If the 2 flying legs with gate returns are immediately follwed by a non gate return flying leg
hasBlock = true.
}
}
}
}
}
if (hasBlock = true) then {
return Duration.newInstance(theLeg.determineDepartureDateTime(), theLeg.determineArrivalDateTime()).standardMinutes.
} else {
return 0;
}
```

