# fcnGetNextLegInDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetNextLegInDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityLeg | LegalityLeg | |
| aLegalityDutyPeriod | LegalityDutyPeriod | |

## Lógica de negocio

```blaze
if (aLegalityLeg <> null and aLegalityDutyPeriod <> null) then{index is an integer initially aLegalityDutyPeriod.legList.indexOf(aLegalityLeg) + 1.if (aLegalityDutyPeriod.legList.size() > index) thenreturn aLegalityDutyPeriod.legList.get(index).}return null.
```

