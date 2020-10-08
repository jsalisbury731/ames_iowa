### Project 2: SAT/ACT Investigation


### Problem Statement

Over the past couple of years, many colleges and universities have started discussing the possibility of dropping the SAT/ACT application requirement for incoming freshman. One notable university system in California that has already enacted this change is the University of California. 

As a result, it is clear that there may be a downwards trend in the coming years for SAT/ACT participation. The College Board, the organization responsible for sponsoring the SATs, is interested in seeing where their development funds would best be spent at the local school level and district level to increase their market share for standardized testing.

___
### Summary

Things to look into in this report:
- What is the statewide SAT to ACT participation rate?
- Which schools and districts have the highest ratio of SAT:ACT test takers?
- Which schools and districts have the lowest ratio of SAT:ACT test takers?
- Which schools and districts have the largest populations that fall into these groups?
- Which schools and districts might be best to target for increasing participation?

___
### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Id**|*float*|2019 SAT/ACT Results for California|Unique school identifier code combining the school, district, and county codes| 

___
### Data Observations

Important notes found in the Data that help lead to the conclusions.
- The ratio of 12th graders who took the SAT:ACT was 2.06 for the State of California.
- The ratios of SAT:ACT test takers skews to the right for both schools and districts, indicating a higher percentage of SAT takers than ACT takers.

<img src="./images/schools.png" width="50%" height="50%">
<img src="./images/districts.png" width="50%" height="50%">
 
- The first quartile bounds for schools and districts is 1.306 and 1.357, respectively.
- Two of the largest schools with a ratio in the first quartile are also in one of the largest five districts with the lowest SAT:ACT participation ratio.

___
### Conclusions and Recommendations

As a result of my preliminary analysis of the data and separation of the first quartile schools and districts based on SAT:ACT test taker ratio, I recommend that the College Board target certain schools and districts. These schools/districts are a combination of the lowest SAT:ACT test taker ration and the number of students enrolled.

The top five schools I'd recommend the College Board to target:

1. San Clemente High **
2. Dougherty Valley High
3. Arnold O. Beckman High
4. Los Alamitos High
5. Aliso Niguel High **
*** Represents schools in the top five recommended districts*

|School Name|District Name|12th Graders Enrolled|SAT to ACT Ratio|
|---|---|---|---|
|San Clemente High|Capistrano Unified|808|0.754839|
|Dougherty Valley High|San Ramon Valley Unified|766|0.918367|
|Arnold O. Beckman High|Tustin Unified|760|1.146667|
|Los Alamitos High|Los Alamitos Unified|758|1.217557|
|Aliso Niguel High|Capistrano Unified|749|0.821678|

The top five districts I'd recommend the College Board to target:

1. Capistrano Unified
2. Fontant Unified
3. Poway Unified
4. Fremont Union High
5. Salinas Union High

|District Name|12th Graders Enrolled|SAT to ACT Ratio|
|---|---|---|
|Capistrano Unified|4805|0.915464|
|Fontana Unified|2941|0.389149|
|Poway Unified|2918|1.171095|
|Fremont Union High|2761|1.006881|
|Salinas Union High|2683|1.405039|

If the College Board focuses on these schools and districts their budget will be best implemented as these schools/districts are taking the SAT proportionately less than the state average. These schools/districts also have the the largest populations based on the first quartile of states with a low SAT:ACT ratio, providing the greatest upside for the College Board.

___

### What Next

Things I would like to look into as the project continues:
- Which districts have the highest number of students applying to colleges?
- Do the findings about which districts have the lowest SAT:ACT ratio extend to their counties, or do the districts operate more independently?
- Do high schools that are geographically closer to major colleges or or universities which don't require the SAT or ACT have lower test participation rates?
___