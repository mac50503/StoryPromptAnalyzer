# fcnGetCrewId

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetCrewId`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theCrewPayRequest | CrewPayRequest | |

## Lógica de negocio

```blaze
if (theCrewPayRequest <> null and theCrewPayRequest.crewLine.crewMemberList is not equal to null and      theCrewPayRequest.crewLine.crewMemberList.size() > 0) then{return theCrewPayRequest.crewLine.crewMemberList.get(0).crewId.}return "".
```

## Llamado por

- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

