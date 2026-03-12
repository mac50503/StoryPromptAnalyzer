# fcnCreateAndReturnSwaHolidayList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<SwaHoliday>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateAndReturnSwaHolidayList`

## Propósito
*(Sin descripción)*

## Lógica de negocio

```blaze
////  SETUP SWA HOLIDAYS...aSwaHolidayList is an ArrayList.swaHoliday1 is a SwaHoliday.    // NEW YEARS DAYswaHoliday1.startDateTime = DateTime.parse("2014-01-01T03:00:00").swaHoliday1.endDateTime = DateTime.parse("2014-01-02T02:59:00").aSwaHolidayList.add(swaHoliday1).swaHoliday2 is a SwaHoliday.     // THANKSGIVINGswaHoliday2.startDateTime = DateTime.parse("2014-11-27T03:00:00").swaHoliday2.endDateTime = DateTime.parse("2014-11-28T02:59:00").aSwaHolidayList.add(swaHoliday2).swaHoliday3 is a SwaHoliday.    // CHRISTMASswaHoliday3.startDateTime = DateTime.parse("2014-12-25T03:00:00").swaHoliday3.endDateTime = DateTime.parse("2014-12-26T02:59:00").aSwaHolidayList.add(swaHoliday3).return aSwaHolidayList.
```

