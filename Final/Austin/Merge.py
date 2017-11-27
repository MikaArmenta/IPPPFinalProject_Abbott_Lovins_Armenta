import pandas as pd

AAnn = pd.read_csv('Austin_Annual_Crime_Dataset_2015.csv')
AUF2015= pd.read_csv("Austin_UF_R2R_2015.csv")

#Combining datasets
stack = pd.concat([AAnn, AUF2015], axis=0)

#Removing hyphens from index names
stack.rename(columns={' X-Coordinate':'XCoord', ' Y-Coordinate':'YCoord'}, inplace = True)

#Merging key and council district info
stack[' Primary Key'].fillna(stack['GO Primary Key'], inplace=True)
stack.drop(['GO Primary Key'], axis = 1, inplace = True)

stack['CouncilDistrict'].fillna(stack['Council District'], inplace=True)
stack.drop(['Council District'], axis = 1, inplace = True)

stack['XCoord'].fillna(stack['GO X Coordinate'], inplace=True)
stack.drop(['GO X Coordinate'], axis = 1, inplace = True)

stack['YCoord'].fillna(stack['GO Y Coordinate'], inplace=True)
stack.drop(['GO Y Coordinate'], axis = 1, inplace = True)


#Removing spaces in column names
stack.columns = stack.columns.str.replace('\s+','')

stack.rename(columns={'PrimaryKey': 'Key', 'EffectonOfficer': 'OfficerEffects', 'NatureofContact':'NatureOfContact', 'HighestNIBRS/UCROffenseDescription':'NIBRS', 'OfficerYrsofService': 'OfficerYrsServ'}, inplace=True)


#Creating Boolean for UF incidents
stack['UF'] = stack['AreaCommand'].isnull()

#Reordering index for ease of navigating dataset
stack = stack.reindex_axis(['Key','CouncilDistrict','UF','XCoord','YCoord','RIN',
                            'DateOccurred','TimeOccurred','ClearanceDate', 'GOReportDate',
                            'R2RLevel','NIBRS','AreaCommand',  'Location', 'GOCensusTract',
                            'GODistrict','GOLocation','GOLocationZip','OfficerEffects','OfficerCommissionDate',
                            'OfficerYrsServ', 'OfficerOrganizationDesc', 'ReasonDesc','SubjectConductDesc', 'SubjectEffects',
                            'SubjectEthnicity', 'SubjectRace', 'SubjectResistance', 'SubjectSex', 'NatureOfContact',
                            'GOHighestOffenseDesc', 'NumberShots', 'WeaponUsed1', 'WeaponUsed2', 'WeaponUsed3', 'WeaponUsed4',
                            'WeaponUsed5', 'ClearanceStatus','MasterSubjectID'], axis=1)

#Sorting by council district
stack.sort_values(('CouncilDistrict'), inplace = True)

#Resetting index to Key
stack.set_index(['Key'], drop = False, inplace = True)

#Saving to csv
stack.to_csv('stack.csv')
