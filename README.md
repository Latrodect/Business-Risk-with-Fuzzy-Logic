# Risk Management Fuzzy-Logic Project

Hi! Welcome the Risk Management Fuzzy-Logic Project. This project will give you the what is the risk of starting a new business. This program calculate the risk with general problems of the real life. Now we have a twenty-four rules for calculating the risk level. This rule set created with a twenty parameters. You can find this rules  on the project folder.

## Explanation Algorithm with Graph

[![](https://mermaid.ink/img/eyJjb2RlIjoiXG5ncmFwaCBMUlxuQVvEsG1wb3J0IExpYnJhcnlzIF0gLS0gRm9yIG91dHB1dCAtLT4gQltDcmVhdGUgQ29uc2VxdWVudF1cbkEgLS0gRm9yIMSwbnB1dCAtLT4gQ1tDcmVhdGUgQW50ZWNlZGVudF1cbkIgLS0gd2l0aCB0cmltZiAgLS0-IER7TWVtYmVyc2hpcCBGdW5jdH1cbkMgLS0gd2l0aCBhdXRvbWYgLS0-IERcbkQgLS0gQ3JlYXRpbmcgLS0-IEgoUnVsZXMpXG5EIC0tPiBGXG5GIC0tIMSwbnB1dCBXZWlnaHQgLS0-IEYoQ29tcHV0ZSlcbkYtLSBTdXJmYWNlLCBHcmFwaCBhbmQgUmlzayBMZXZlbC0tPiBUW1N1cmZhY2VdXG5IIC0tIEdyYXBoLCBSZXN1bHQgLS0-VFxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiXG5ncmFwaCBMUlxuQVvEsG1wb3J0IExpYnJhcnlzIF0gLS0gRm9yIG91dHB1dCAtLT4gQltDcmVhdGUgQ29uc2VxdWVudF1cbkEgLS0gRm9yIMSwbnB1dCAtLT4gQ1tDcmVhdGUgQW50ZWNlZGVudF1cbkIgLS0gd2l0aCB0cmltZiAgLS0-IER7TWVtYmVyc2hpcCBGdW5jdH1cbkMgLS0gd2l0aCBhdXRvbWYgLS0-IERcbkQgLS0gQ3JlYXRpbmcgLS0-IEgoUnVsZXMpXG5EIC0tPiBGXG5GIC0tIMSwbnB1dCBXZWlnaHQgLS0-IEYoQ29tcHV0ZSlcbkYtLSBTdXJmYWNlLCBHcmFwaCBhbmQgUmlzayBMZXZlbC0tPiBUW1N1cmZhY2VdXG5IIC0tIEdyYXBoLCBSZXN1bHQgLS0-VFxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
- First  of all we need an Antecedent for input variables and Consequent for output variables.
- We need put this variables on 0-1 space with a membership. 
- - For Antecedent we will use .automf() funtion of scifuzzy library.
- - For Consequent we will use .trimf() function of scifuzzy library.
- After given them the membership degrees we can use them for creating our rule set.
- For computing this fuzzy variables we will give the real world input values.
- After the computing process we can plotting the System Surface, Graphs and Fuzzy Result. 

## Download and İnstall

İf you want  **download and install** correctly, make sure the all librarys dowload on your computer. And make sure the add your computer **path** the python. After doing this check fallow the steps down the below.
Open your **Command Prompt** or **Anaconda Prompt** and copy paste this line.
> pip install requirements.txt.

This little code will download all you needed  packages and librarys .

## Parameters and Rules
### Parameters
- Change in organizational management during the project
- Lack of cooperation from users
- Inadequate infrastructure
- Corporate politics with negative effect on project
- Failure to identify all stakeholders
- High level of technical complexity
- Unstable organizational environment
- Lack of adequate user involvement
- Project progress not monitored closely enough
- Lack of appropriate experience of the user representative
- Conflict among team members
- Staff turnover
- User resistance
- Lack of frozen system requirements
- New and/or unfamiliar subject matter for the system
- Unclear or misunderstanding system requirements
- Ambiguity and/or change of requirements

### Example Some Set of Rule
- If "Change in organizational management during the project" is low and "Lack of cooperation from users" is low and "Inadequate infrastructure" is low then risk is low.
- If "Corporate politics with negative effect on project" is low and "Failure to identify all stakeholders" is low and "High level of technical complexity" is low then risk is low.
- If "Unstable organizational environment" is low and "Lack of adequate user involvement" is low and "Project progress not monitored closely enough" is medium then risk is low.

 
## Description

You can fallow me on my [LinkedIn](https://www.linkedin.com/in/hasan-bahad%C4%B1r-nural-062b221a2/) Account and my personal [Blog](http://www.bahadirnural.org/).

