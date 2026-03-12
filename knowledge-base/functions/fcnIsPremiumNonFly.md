# fcnIsPremiumNonFly

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsPremiumNonFly`

## Propósito
1/16/2017 Rachel Starfield - CREW-147 - Created function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| nonFlyCode | string | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.select nonFlyCodecase "RTS" : retVal = true.case "MM": retVal = true.case "MMA": retVal = true.otherwise : retVal = false.if(retVal = false) then {baseNonFlyGenericCode is a string initially fcnGetBaseNonFlyGenericCode(nonFlyCode).select baseNonFlyGenericCodecase "STW":retVal = true.case"ST8":retVal = true.case"RT":retVal = true.}return retVal;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetBaseNonFlyGenericCode](fcnGetBaseNonFlyGenericCode.md)

## Historial de cambios

```
1/16/2017 Rachel Starfield - CREW-147 - Created function
1/19/2017 Rachel Starfield - CREW-62 - Added MM and MMA.
01/12/2025 APIC-1686 Use baseNonFlyGenericCode for all Nonfly Base
```

