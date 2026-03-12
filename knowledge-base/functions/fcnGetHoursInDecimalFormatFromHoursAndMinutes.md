# fcnGetHoursInDecimalFormatFromHoursAndMinutes

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetHoursInDecimalFormatFromHoursAndMinutes`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| hoursAndMinutes | real | |

## Lógica de negocio

```blaze
//// hours and minutes will be passed in the following format://// 59 minutes will be passed in as 0.59//// 60 minutes will be passed in as 1.00//// 90 minutes will be passed in as 1.30//// negative 2 hours and 47 minutes will be passed in as-2.47retVal is a real initially 0.0.hoursComponent is an integer initially math().truncate(hoursAndMinutes).minsComponent is an real initially (hoursAndMinutes - hoursComponent) / 0.60.retVal = hoursComponent + minsComponent.retVal = fcnRoundUpAt2DecimalPlaces(retVal).//fcnShow("===>>> returning from fcnGetHoursInDecimalFormatFromHoursAndMinutes ... converted " hoursAndMinutes " to " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnApplyStaffBankAdjustments](fcnApplyStaffBankAdjustments.md)

