# fcnNonflyIsNonflyType

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnNonflyIsNonflyType`

## Propósito
03/12/2015 - US20192 - Melissa S - New function to do the lookup in the decision table for a certain Nonfly Type

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| nonFlyCode | string | |
| nonFlyCodeType | NonflyCodeType | |

## Lógica de negocio

```blaze
baseNonFlyGenericCode is a string initially fcnGetBaseNonFlyGenericCode(nonFlyCode).if(baseNonFlyGenericCode <> null and baseNonFlyGenericCode <> unknown) then {return dtNonflyCodes_ForBase(baseNonFlyGenericCode, nonFlyCodeType).} else { return dtNonflyCodes_Inflight(nonFlyCode, nonFlyCodeType).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetBaseNonFlyGenericCode](fcnGetBaseNonFlyGenericCode.md)

## Llamado por

- [fcnDetermineTripTransientTerms](fcnDetermineTripTransientTerms.md)

## Historial de cambios

```
03/12/2015 - US20192 - Melissa S - New function to do the lookup in the decision table for a certain Nonfly Type
11/19/2025 - APIC-1686 - Use new NonFlyBase related decision table for the Base Related Nonfly codes, whoch ends with ST8, STW or starts with RT (NOT RTS)
```

