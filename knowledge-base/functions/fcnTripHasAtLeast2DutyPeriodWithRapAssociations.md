# fcnTripHasAtLeast2DutyPeriodWithRapAssociations

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnTripHasAtLeast2DutyPeriodWithRapAssociations`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.count is an integer initially 0.if (aPayTrip <> null and aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then{rapAssociationSeqNum is a string initially "none".for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{rapAssociationSeqNum = fcnGetRapAssociationListAsString(it).if (rapAssociationSeqNum <> "none") thencount += 1.}if (count >= 2) thenretVal = true.}fcnShow("===>>> EXITING fcnTripHasAtLeast2DutyPeriodWithRapAssociations for trip " aPayTrip.tripName " ... count of duties with RAP associations = " count " ...retuning " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetRapAssociationListAsString](fcnGetRapAssociationListAsString.md)
- `fcnShow()`

