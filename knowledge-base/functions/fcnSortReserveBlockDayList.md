# fcnSortReserveBlockDayList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSortReserveBlockDayList`

## Propósito
Ben Lang DE6848/DE6870 06/18/2015 - Added functionality sort the K label reserve blocks before the B and T label reserve blocks while also supporting sorting all of them chronologically

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReservePayrollReport | ReservePayrollReport | |
| preSort | boolean | |

## Lógica de negocio

```blaze
if (theReservePayrollReport.reserveBlockDayList <> null and theReservePayrollReport.reserveBlockDayList.count > 0) then{sortedArray is some array of ReserveBlockDay initially an array of ReserveBlockDay.fcnShow("===>>> UNSORTED reserveBlockDayList:").for each ReserveBlockDay in theReservePayrollReport.reserveBlockDayList do{fcnShow("===>>> calendar day = " DateTimeUtilities.getShortDateTimeString(it.calendarDay)).}index is an integer initially 0.for each ReserveBlockDay in theReservePayrollReport.reserveBlockDayList do{index = fcnFindReserveBlockDayIndex(it, sortedArray, preSort).//fcnShow("===>>> inserting " DateTimeUtilities.getShortDateTimeString(it.calendarDay) " at  index " index).sortedArray.insert(index, it).}theReservePayrollReport.reserveBlockDayList = sortedArray.fcnShow("===>>> SORTED reserveBlockDayList:").for each ReserveBlockDay in theReservePayrollReport.reserveBlockDayList do{fcnShow("===>>> calendar day = " DateTimeUtilities.getShortDateTimeString(it.calendarDay)).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindReserveBlockDayIndex](fcnFindReserveBlockDayIndex.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang DE6848/DE6870 06/18/2015 - Added functionality sort the K label reserve blocks before the B and T label reserve blocks while also supporting sorting all of them chronologically
```

