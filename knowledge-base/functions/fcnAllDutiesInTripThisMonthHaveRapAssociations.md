# fcnAllDutiesInTripThisMonthHaveRapAssociations

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAllDutiesInTripThisMonthHaveRapAssociations`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.countOfUnassociatedDuties is an integer initially 0.if (aTripPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aSchedulePeriodPay) and     fcnGetRapAssociationListAsString(it.payDutyPeriod) = "none") thencountOfUnassociatedDuties += 1.}if (countOfUnassociatedDuties > 0) thenretVal = false.}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)

