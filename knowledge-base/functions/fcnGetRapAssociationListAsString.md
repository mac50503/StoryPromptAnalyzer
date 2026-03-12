# fcnGetRapAssociationListAsString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetRapAssociationListAsString`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is a string initially "none".associatedObject is some PayDutyPeriod initially null.if (aPayDutyPeriod.payDutyPeriodInflight <> null and    aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList <> null and   aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size() > 0) then{count is an integer initially 0.associationCount is an integer initially aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size().while count < associationCount do{associatedObject = aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.get(count).if (count = 0) thenretVal  = associatedObject.sequenceNumber as a string.elseretVal = retVal ", " associatedObject.sequenceNumber as a string.count +=1.}}else if (aPayDutyPeriod.rapAssociation <> null) then retVal = aPayDutyPeriod.rapAssociation.sequenceNumber as a string.return retVal.
```

## Llamado por

- [fcnAllDutiesInTripAssociatedWithReserveBlockDuties](fcnAllDutiesInTripAssociatedWithReserveBlockDuties.md)
- [fcnAllDutiesInTripThisMonthHaveRapAssociations](fcnAllDutiesInTripThisMonthHaveRapAssociations.md)
- [fcnCalculateReserveBlockCredit](fcnCalculateReserveBlockCredit.md)
- [fcnGetGTPDistributionBucketName](fcnGetGTPDistributionBucketName.md)
- [fcnIsABucketApplicable](fcnIsABucketApplicable.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)
- [fcnTripHasAtLeast2DutyPeriodWithRapAssociations](fcnTripHasAtLeast2DutyPeriodWithRapAssociations.md)

