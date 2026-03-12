# fcnFindReserveBlockDayIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnFindReserveBlockDayIndex`

## Propósito
Ben Lang DE6848/DE6870 06/18/2015 - Added functionality sort the K label reserve blocks before the B and T label reserve blocks while also supporting sorting all of them chronologically

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aReserveBlockDay | ReserveBlockDay | |
| preSort | boolean | |

## Lógica de negocio

```blaze
index is an integer initially 9999.elementIndex is an integer initially 0.isBefore is a boolean initially false.if (sortedArray <> null and sortedArray.count > 0) then{for each ReserveBlockDay in sortedArray do{elementIndex = sortedArray.getFirstElementIndex(it).isBefore = aReserveBlockDay.calendarDay.isBefore(it.calendarDay).if (index = 9999 and isBefore) then{index = elementIndex.// DE6872 - Sort K reserve blocks in chronological order follewed by B and T reserve blocks sorted in chronological orderif (aReserveBlockDay.reserveBlock.assignmentLabel = ("B" or "T") and it.reserveBlock.assignmentLabel = "K" and preSort) then{index = 9999.isBefore = false.}}}}if (index = 9999) thenindex = sortedArray.count.return index.
```

## Llamado por

- [fcnSortReserveBlockDayList](fcnSortReserveBlockDayList.md)

## Historial de cambios

```
Ben Lang DE6848/DE6870 06/18/2015 - Added functionality sort the K label reserve blocks before the B and T label reserve blocks while also supporting sorting all of them chronologically
```

