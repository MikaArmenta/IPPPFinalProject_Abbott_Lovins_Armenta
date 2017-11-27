sqlite3 Austin.sqlite /* Database name = Austin.sqlite */

.headers on
.mode csv

/* AAnn2015 = Overall crime table */
CREATE TABLE AAnn2015 (GOPrimaryKey INTEGER, CouncilDistrict INTEGER, GOHighestOffenseDesc TEXT, HighestNIBRS TEXT,
                      GOReportDate DATE, GOLocation TEXT, ClearanceStatus TEXT, ClearanceDate DATE, GODistrict TEXT, GOLocationZip INTEGER,
                      GOCensusTract FLOAT, GOXCoordinate INTEGER, GOYCoordinate INTEGER);

.import Austin_Annual_Crime_Dataset_2015.csv AAnn2015


/* AUF2015 = use of force data */
CREATE TABLE AUF2015 (RIN INTEGER, PrimaryKey INTEGER, DateOccurred DATE, TimeOccurred TIME,
Location TEXT,  AreaCommand TEXT, NatureOfContact TEXT, ReasonDesc TEXT, R2RLevel INTEGER, MasterSubjectID TEXT,
SubjectSex TEXT, SubjectRace TEXT, SubjectEthnicity TEXT, SubjectConductDesc TEXT, SubjectResistance TEXT,
WeaponUsed1 TEXT, WeaponUsed2 TEXT, WeaponUsed3 TEXT, WeaponUsed4 TEXT, WeaponUsed5 TEXT, NumberShots INTEGER,
SubjectEffects TEXT, EffectonOfficer TEXT, OfficerOrganizationDesc TEXT, OfficerCommissionDate DATETIME,
OfficerYrsofService INTEGER, XCoordinate INTEGER, YCoordinate INTEGER, CouncilDistrict INTEGER);

.import Austin_UF_R2R_2015.csv AUF2015

/* Here goes SES data. Not sure what we're doing with it or where it's at though. */

/* Merging AAnn2015 and AUF2015 on CouncilDistrict and saved as AustinMerge_CD.csv */

.output testAustinMerge_CD.csv
.mode csv
SELECT *
FROM AAnn2015
JOIN AUF2015 ON AAnn2015.CouncilDistrict=AUF2015.CouncilDistrict
LIMIT 20;
.output stdout
/*To get full dataset, remove LIMIT 20 and rename: AustinMerge_CD. Be sure to
include the .mode csv in there! Otherwise it outputs each line to one cell in excel.
The file's too big to upload to github right now too. We'll have to figure out
how to downsize it or if we need to upload the whole thing.*/


/* Merging on Primary Key, grouping by district, and saved as
AustinMerge_PrimKey.csv */

.output testAustinMerge_PrimKey.csv
.mode csv
SELECT *
FROM AAnn2015
JOIN AUF2015 ON AAnn2015.GOPrimaryKey=AUF2015.PrimaryKey;
.output stdout

/*OK, so the above is keeping data where we have a match between the AAnn2015 GOPrimaryKey
and the AUF2015PrimaryKey (UoF incidents accounted for in overall crime dataset. As ye
can see, it's quite a bit more than the 192 I got from Pandas...) So, what we need to figure
out is how to get all of the incidents to show up - for this query to not exclude them */
