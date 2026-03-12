# fcnGetNextTripsWithinHours

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<PayTrip>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetNextTripsWithinHours`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriod | PayDutyPeriod | |
| tripList | List<PayTrip> | |
| hours | integer | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING function fcnGetNextTripsWithinHours with DP = " aDutyPeriod.sequenceNumber " searching for trips within the next " hours " hours from " aDutyPeriod.releaseDateTime).retVal is some List<PayTrip> initially an ArrayList.myTripIndex is an integer initially 0.nextIndex is an integer initially 1.aPayTrip is some PayTrip initially null.continue is a boolean initially true.diffInMinutes is a real initially 0.0.if (aDutyPeriod <> null and tripList <> null and tripList.size() > 0 and hours > 0) then{    myTripIndex = tripList.indexOf(aDutyPeriod.payTrip).nextIndex = myTripIndex + 1.while (tripList.size() > nextIndex and continue = true) do{aPayTrip = tripList.get(nextIndex).diffInMinutes = fcnGetTimeDiffInMinutes(aDutyPeriod.releaseDateTime, aPayTrip.beginDateTime).if (diffInMinutes >= 0 and  diffInMinutes <= hours * 60) then{fcnShow("===>>> diff in minutes between " aDutyPeriod.releaseDateTime " and " aPayTrip.beginDateTime " is " diffInMinutes).retVal.add(aPayTrip)}elsecontinue = false.nextIndex += 1.}}fcnShow("===>>> EXITING function fcnGetNextTripsWithinHours with DP = " aDutyPeriod.sequenceNumber " found " retVal.size() " trips within " hours " hours").return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

