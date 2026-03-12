# fcnGetPayDutyPeriodBySequenceNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayDutyPeriodBySequenceNumber`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSequenceNumber | integer | |
| thePayDutyPeriodList | List<PayDutyPeriod> | |

## Lógica de negocio

```blaze
if (thePayDutyPeriodList <> null and thePayDutyPeriodList <> unknown and thePayDutyPeriodList.size() > 0) then {for each PayDutyPeriod in thePayDutyPeriodList as an array of PayDutyPeriod do {if (it.sequenceNumber = theSequenceNumber) then {return it.}}}return null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

