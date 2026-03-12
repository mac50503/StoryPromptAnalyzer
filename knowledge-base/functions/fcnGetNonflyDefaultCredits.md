# fcnGetNonflyDefaultCredits

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetNonflyDefaultCredits`

## Propósito
1/13/2017 Rachel Starfield - CREW-733 - Changed HS pay value from 2.0 to 3.0

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| nonFlyCode | string | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.select nonFlyCodecase "PT" : retVal = 2.0.case "RTS" : retVal = 4.0.case "BO": retVal = 2.0.case "VAPO" : retVal = 26.25.case "HS"     : retVal = 4.0.case "IN"      : retVal = 8.0.case "RNU" : retVal = 3.0.case "RNUH" : retVal = 3.0.otherwise : retVal = 0.0.if(retVal = 0) then {baseNonFlyGenericCode is a string initially fcnGetBaseNonFlyGenericCode(nonFlyCode).select baseNonFlyGenericCodecase "STW":retVal = 6.5.case"ST8":retVal = 6.5.case"RT":retVal = 5.5.}fcnShow("===>>> fcnGetNonflyDefaultCredits ... returning default credits for nonFlyCode " nonFlyCode " of " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetBaseNonFlyGenericCode](fcnGetBaseNonFlyGenericCode.md)
- `fcnShow()`

## Historial de cambios

```
1/13/2017 Rachel Starfield - CREW-733 - Changed HS pay value from 2.0 to 3.0
01/12/2025 APIC-1686 Use baseNonFlyGenericCode for all Nonfly Base
```

