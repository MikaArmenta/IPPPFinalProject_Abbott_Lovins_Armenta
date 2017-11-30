#!/usr/bin/env python

import pandas as pd
import geopandas as gpd
import requests, json
%matplotlib inline

#When writing actual script, need to 'within line in open(...) and call directly from internet.

AAnn = pd.read_csv('Austin_Annual_Crime_Dataset_2015.csv')
AUF2015= pd.read_csv("Austin_UF_R2R_2015.csv")

#Renaming columns
AUF2015.rename(columns={' Primary Key': 'Key', ' Effect on Officer': ' OfficerEffects',
'Nature of Contact':'NatureOfContact', 'Officer Yrs of Service': 'OfficerYrsServ'}, inplace=True)
AAnn.rename(columns={'HighestNIBRS/UCROffenseDescription':'NIBRS', 'Council District': 'Council_District'}, inplace=True)

#Removing spaces in column names
AUF2015.columns = AUF2015.columns.str.replace('\s+','')
AAnn.columns = AAnn.columns.str.replace('\s+','')

#Dropping duplicates from AUF2015 set. Only AUF2015 has duplicates.
AUF2015 = AUF2015.drop_duplicates(subset='Key', keep='first', inplace = False)

#Merging datasets
stack = pd.merge(AAnn, AUF2015, left_on='GOPrimaryKey', right_on='Key', how='outer')

#Removing hyphens from index names
stack.rename(columns={'X-Coordinate':'XCoord', 'Y-Coordinate':'YCoord'}, inplace = True)

#Boolean for identifying UF incidents
stack['UF'] = stack['AreaCommand'].notnull() | (stack['Key'].notnull() & stack['GOPrimaryKey'].notnull())

#Putting info that was present in both datasets into same columns (keys,
#council districts, and geo coordinates)
stack['Key'].fillna(stack['GOPrimaryKey'], inplace=True)
stack.drop(['GOPrimaryKey'], axis = 1, inplace = True)

stack['CouncilDistrict'].fillna(stack['Council_District'], inplace=True)
stack.drop(['Council_District'], axis = 1, inplace = True)

stack['XCoord'].fillna(stack['GOXCoordinate'], inplace=True)
stack.drop(['GOXCoordinate'], axis = 1, inplace = True)

stack['YCoord'].fillna(stack['GOYCoordinate'], inplace=True)
stack.drop(['GOYCoordinate'], axis = 1, inplace = True)

#Reordering index for ease of navigating dataset
stack = stack.reindex_axis(['Key','CouncilDistrict','UF','XCoord','YCoord','RIN',
                           'DateOccurred','TimeOccurred','ClearanceDate', 'GOReportDate',
                           'R2RLevel','NIBRS','AreaCommand',  'Location', 'GOCensusTract',
                           'GODistrict','GOLocation','GOLocationZip','OfficerEffects',
                           'OfficerCommissionDate','OfficerYrsServ', 'OfficerOrganizationDesc',
                           'ReasonDesc','SubjectConductDesc', 'SubjectEffects',
                           'SubjectEthnicity', 'SubjectRace', 'SubjectResistance',
                           'SubjectSex', 'NatureOfContact', 'GOHighestOffenseDesc',
                           'NumberShots', 'WeaponUsed1', 'WeaponUsed2', 'WeaponUsed3',
                           'WeaponUsed4','WeaponUsed5', 'ClearanceStatus','MasterSubjectID'], axis=1)


#Sorting by council district
stack.sort_values(('CouncilDistrict'), inplace = True)

#Resetting index to Key
stack.set_index(['Key'], drop = False, inplace = True)

#Adding SES data for Council District to dataset
SES = pd.read_csv("Districts10_Socioeconomics.csv")
SES.set_index('Composite Socioeconomic Data for City Council Districts', inplace = True)
SES = SES.iloc[:, 2:12]
SES.dropna(thresh = 10, inplace = True)
ColNames = SES.iloc[0]
listnames = ColNames.str.extract('(\d+)').astype(int)
SES.columns = listnames
SES[listnames] = SES[listnames].replace({'\$': '', '%': '', ',':''}, regex=True)
SES

SES = SES.iloc[1:, :]
SES.swapaxes(1, 0)
stackfinal = pd.merge(SES.swapaxes(1, 0), stack, left_index = True, right_on = 'CouncilDistrict', how = 'outer')
stackfinal.columns=stackfinal.columns.str.replace('\s+','')
stackfinal.rename(columns={'IndivualsBelowPoverty':'NumBelowPoverty',
                          'AdultsAge25Plus': 'Age25Plus', 'NumberwithatleastaBachelorsDegree': 'NumWithBachelors',
                          'DriveAlone%': 'PercDriveAlone', 'TakeTransit%': 'PercTakeTrans',
                          'ActiveJourney(Walk,orBike,orOther)%':'ActiveJourney',
                          'LaborForceParticipationRate': 'LabForcePartRate',
                          'PercentwithoutHealthInsurance': 'PercSansHealthIns'}, inplace = True)

#Saving to .csv
stackfinal.to_csv('stackfinal.csv')
