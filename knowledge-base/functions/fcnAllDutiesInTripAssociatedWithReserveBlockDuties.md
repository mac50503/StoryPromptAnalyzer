# fcnAllDutiesInTripAssociatedWithReserveBlockDuties

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAllDutiesInTripAssociatedWithReserveBlockDuties`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.countOfUnassociatedDuties is an integer initially 0.if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0) then{for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{if (fcnGetRapAssociationListAsString(it) = "none") thencountOfUnassociatedDuties += 1.}if (countOfUnassociatedDuties > 0) thenretVal = false.}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)

