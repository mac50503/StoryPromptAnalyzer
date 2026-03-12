# fcnIsNotABlankString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnIsNotABlankString`

## Propósito
9/15/25 - APIC-1580 -Sabyasachi Chanda - Created a Utility Function to check whether a String is Blank or not , it checks null too.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| inputString | string | |

## Lógica de negocio

```blaze
// inputString = null - retrun false// inputString = unknown - retrun false// inputString =  "" - retrun false// inputString =  " "- retrun false// inputString = "TEST" - retrun true// inputString = " TEST" - retrun true// inputString = "TEST " - retrun true// inputString = " TEST " - retrun trueisNotABlankString is a boolean initially false.if(inputString <> null and inputString <> unknown and inputString <> "" and inputString.trim().length() >0) then {isNotABlankString = true.}return isNotABlankString.
```

## Llamado por

- [fcnSetTripDomicileTimeZone](fcnSetTripDomicileTimeZone.md)

## Historial de cambios

```
9/15/25 - APIC-1580 -Sabyasachi Chanda - Created a Utility Function to check whether a String is Blank or not , it checks null too.
```

