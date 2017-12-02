# IPPP_Abbott_Lovins_Armenta

### Intro to Programming for Public Policy, Final Project
#### Authors: Sam Abbott, Joey Lovins, Mika Armenta


#### Data Sources:

Our data sets can be found in the “Austin_Annual_Crime_Dataset_2015.csv” [1], “Austin_UF_R2R_2015.csv” [2], and “Districts10_Socioeconomics.csv” [3] files contained in our repository.

#### Summary:

We set out to evaluate whether or not police use of force could be predicted probabilistically by key demographic variables and other census data. For instance, what is the relationship between socioeconomic status—i.e. poverty rates, workforce participation rate, population density, and unemployment rates—by council district, with police use of force? Ultimately, we hoped to develop a model that could explain how variation in those key demographic variables could predict, probabilistically, a use of force incident.

As police use of force has become a highly publicized and politicized issue, gaining traction in the policy space, a new body of literature has begun to emerge. Researchers, particularly at Yale University and the University of Chicago, have developed some important projects looking into the relationship between use of force, racial and social demographics, and officers at-risk of adverse events [4]. Data scientists at the University of Chicago, for instance, recently published a paper suggesting that a data-driven Early Intervention Systems (EIS) could greatly reduce the probability of adverse events. Just one of a number of successful projects undertaken as part of the White House’s Police Data Initiative (launched under President Obama’s Task Force on 21st Century Policing), we hoped to provide a useful complement to this growing body of research to better understand and learn how to prevent unnecessary officer use of force.
We evaluated a few models to shed light on this area. The first was a standard regression model, evaluating how a number of socioeconomic variables relate to rates of criminal activity. We found statistically significant relationships between the socioeconomic covariates and our dependent variable of crime frequency. Our R^2 score, (.84), suggests that our model accounts for a significant amount of variation in rates of criminal activity by council district. While the coefficient estimates attached to our independent variables are quite small, they are each statistically significant. Our F-statistic, where P > F = 0.000, also corroborates our theory and provides grounds to reject the joint null hypothesis that the model has no explanatory power regarding variation in criminal activity.

In our second model, we ran a probit regression, regressing use of force (a binary) on a similar set of key demographic and socioeconomic variables as our first model. While the p-values on our coefficient estimates suggest that each variable in the model was statistically significant, their “economic” significance and magnitude should be interpreted with greater caution.

We then decomposed our crime frequency statistics by type of crime, in order to determine whether certain crime types were more or less related to each other and to use of force.  Correlation among types with use of force showed a ‘caught in the act’ effect, whereby more public/conspicuous crimes were more correlated to uses of force.

We then created a final model which can be customized by type of crime, and regresses use of force levels on that particular type of crime.  This code can be interacted with by entering a crime type string from the menu displayed in the notebook (e.g. “Theft,” “AggAssault”).

Following this, we provide spatial visualizations of use of force and crime levels across districts in the city of Austin.  Most obviously, these maps show a clear geographic division in crime levels between the west and east halves.

#### Data Reporting Issue:

Our analysis was hampered by some inconsistencies in the reporting and recording of use of force and annual crime data. For instance, of more than 40,000 criminal incidents and greater than 1,600 use of force incidents, only 192 cases were in common.  This severely restricted the sample size in our probit model, and thus the type and sort of variation in each independent variable. With more shared data between the two data sets, we would have more precise coefficient estimates and a better sense for the strength and magnitude of the relationship between use of force and key demographic data.

This difficulty is consistent with challenges in using police reported data elsewhere across the United States.  In a recent paper, “An Empirical Analysis of Racial Differences in Police Use of Force,” Dr. Roland G. Fryer (Faculty Director of EdLabs at Harvard) made similar claims about the startling absence of robust data on use of force incidents and other adverse police interactions. As he explains, “a primary obstacle to the study of police use of force has been the lack of readily available data. Data on lower level uses of force, which happen more frequently than officer-involved shootings, are virtually non-existent. This is due, in part, to the fact that most police precincts don’t explicitly collect data on use of force, and in part, to the fact that even when the data is hidden in plain view within police narrative accounts of interactions with civilians, it is exceedingly difficult to extract. Moreover, the task of compiling rich data on officer-involved shootings is burdensome. Until recently, data on officer-involved shootings were extremely rare and contained little information on the details surrounding an incident.” [5]  

#### References

1. https://data.austintexas.gov/Public-Safety/Annual-Crime-Dataset-2015/spbg-9v94

2. https://data.austintexas.gov/Public-Safety/R2R-2015/iydp-s2cf

3. https://austintexas.gov/page/district-demographics

    *Scroll to “Demographic and Socioeconomic City Council Districts Profiles” and click the link: “Composite Socioeconomic Council District Profiles.”*

4. https://dssg.uchicago.edu/wp-content/uploads/2016/04/identifying-police-officers-3.pdf

5. https://law.yale.edu/system/files/area/workshop/leo/leo16_fryer.pdf
