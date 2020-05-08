## REQUIREMENTS GATHERING
### COMPANY OVERVIEW

| Company		| Detail        |
|-----------------------|---------------|
| Name			| XYZ           |
| Business Structure 	| Partnership	|
| Partners 		| Bikash Gupta(bikashgup@hotmail.com)<br/> Aditi Gajurel(aditigajurel1998@gmail.com)|
| Address		| Kathmandu, Nepal|
| Employee Number	| 40-50		|
| Company Type		| Private |
| Goal               	|  To provide best services to customer/client |

### ABOUT COMPANY

 - To measure the happiness and social wellbeing index of the citizens.
 - Encounters economic, environmental, health, and social factors for sentiment analysis.
 - Ubiquitous computing, into everyday objects to make them effectively communicate and perform useful tasks.
 - Also helps different businesses to understand the customer with their emotions and sentiments and improve the      perception of the customer with an ultimate goal to increase the brand reputation and sales. 
   
  
### Stakeholders

  |Actors   |           Roles                            |
  |-------------|----------------------------------------|
  |Customers    | the direct user of a product or service, often both internal and external to the company                           executing the project|
  |Project manager| the project's leader|
  |Resource managers| other managers who control resources needed for executing the project|
  |Executives| the top management in the company executing the project, those who direct the organization's                      strategy|
  |Steering committee| advisory group providing guidance on key decisions. Includes the sponsor, executives, and                  key stakeholders from the organization|
 
### CONTEXT ON PRODUCT

  - A platform to know the emotions and happiness level with the sources of information, mostly being the text.
  - Different services related to the sales and recommendations to the businesses for better brand reputation.
  - Now, product doesn’t prioritize the social and environmental factors.
  - Currently the system is
    - Data from third party
    - Hand labeling and annotation
    - Deep Learning Architecture with two labels, happy and unhappy. 

### ABOUT NEW SYSTEM/PRODUCT

  - Need to estimate the happiness Index and Social Wellbeing Index.
  - Two indicators have to be later differentiated among
    - Gender
    - Culture
    - Location
    - Religion
  - Indicators should to splitted on these factors.

### Expected Workflow

  1. Data  from different sources.
  2. Data Annotation and labeling using Mechanical Turk,
  3. A multi-layered neural network with 3 hidden layers of 125, 25 and 5 neurons respectively.

### Source of the Data

  - Emotionally rich texts from  product reviews, personal blogs/journals, social network websites, forums,           fiction   excerpts, analysis, critiques, and more.
  - Sources of text may come from news articles, stock market analyses, or political debates; anywhere that people     discuss and share their opinion freely could be a source.

### Deep Learning
 - Identify emotions from text using a bi-gram as the text feature representation. 
 - No. of Output Neurons: 5
 - Loss function: Cross Entropy
 - Expected Number of Training Iterations
 - Stochastic Gradient Descent

### Performance and Evaluation Metrics
  - Recall, Precision , Weighted and Unweighted Accuracy.
  - Weighted accuracy if any of the class is underrepresented.

### Functional and Non-Functional Requirements

  #### Functional Requirements
   - An end user might desire an automated at-a-glance presentation of the main points made in a single review or how  opinion changes from time to time.
  - An end user might desire the Happiness Index and Social Well being index based on different factors.

  #### Non-Functional Requirements
   - For private firms, the results are to be obtained within a month or less of the product distribution of the market.
   - For government firms, indexes are to be collaborated with the suggestions and strategies.

### SYSTEM USAGE

  - This system is expected to be used by common citizens for government services for free.
  - Also, the private firms can use this company as an outsourcing company to increase their sales and get high       customer satisfaction and integrate with their own recommendations.
