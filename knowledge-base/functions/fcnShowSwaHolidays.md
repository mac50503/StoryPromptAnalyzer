# fcnShowSwaHolidays

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\Logging\fcnShowSwaHolidays`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSwaHolidayList | List<SwaHoliday> | |

## Lógica de negocio

```blaze
if (aSwaHolidayList <> null) then{if (aSwaHolidayList.size() = 0) thenfcnShow("........The list of Swa Holidays is empty...").else{for each SwaHoliday in aSwaHolidayList as an array of SwaHoliday do{fcnShow("================================================================================================").fcnShow("........Swa Holiday start date: " DateTimeUtilities.getShortDateTimeString(it.startDateTime)).fcnShow("........Swa Holiday end date: " DateTimeUtilities.getShortDateTimeString(it.endDateTime)).}fcnShow("================================================================================================").}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

