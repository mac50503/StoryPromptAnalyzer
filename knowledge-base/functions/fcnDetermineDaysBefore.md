# fcnDetermineDaysBefore

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineDaysBefore`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime1 | DateTime | |
| dateTime2 | DateTime | |

## Lógica de negocio

```blaze
daysBefore is an integer initially 0;if(dateTime1 <> null and dateTime2 <> null and dateTime1.isBefore(dateTime2)) then{earlierDate is some DateTime initially  DateTime.newInstance(dateTime1.year, dateTime1.monthOfYear, dateTime1.dayOfMonth, 0, 0, 0);laterDate is some DateTime initially   DateTime.newInstance(dateTime2.year, dateTime2.monthOfYear, dateTime2.dayOfMonth, 0, 0, 0);while(earlierDate.isBefore(laterDate)) do{earlierDate = earlierDate.plusDays(1);daysBefore += 1;}}return daysBefore;
```

