# fcnGetPreviousLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetPreviousLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegList | List<LegalityLeg> | |
| theLegCounter | integer | |

## Lógica de negocio

```blaze
if (theLegCounter > 0 and theLegList <> null and theLegList.size() > 0) then {return theLegList.get(theLegCounter-1).} else {return null.}
```

## Llamado por

- [fcnGetEndDateTimeForRONTHR](fcnGetEndDateTimeForRONTHR.md)
- [fcnGetPreviousLegBestArrivalForRONTAFB](fcnGetPreviousLegBestArrivalForRONTAFB.md)

