# fcnGetNextLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetNextLeg`

## Propósito
2/10/2016 Mitesh P CSCH-1890 - This function will get the next leg following a given leg in a Duty Period.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegList | List<LegalityLeg> | |
| theLegCounter | integer | |

## Lógica de negocio

```blaze
if (theLegList <> null and theLegList.size() > 0 and theLegCounter < theLegList.size()-1) then {return theLegList.get(theLegCounter+1).} else {return null.}
```

## Historial de cambios

```
2/10/2016 Mitesh P CSCH-1890 - This function will get the next leg following a given leg in a Duty Period.
```

