# Currency Conversion
The Currency Converter project allows you to convert from one currency to another with real-time exchange rates.
It is built using Python and [Exchange Rate Api](https://www.exchangerate-api.com/) that provides accurate and reliable currency conversion rates for 161 currencies. It provides integration for SaaS, Dashboards, and E-Commerce with exceptional uptime and support.

# Table Of Contents
1. [Code](https://github.com/karanzaveri/Currency-Conversion/#code)
2. [UML Diagrams](https://github.com/karanzaveri/Currency-Conversion/#uml-diagrams)
3. [Requirements Engineering](https://github.com/karanzaveri/Currency-Conversion/#requirements-engineering)
4. [DDD](https://github.com/karanzaveri/Currency-Conversion/#ddd)
5. [Metrics](https://github.com/karanzaveri/Currency-Conversion/#metrics)
6. [Clean Code Development](https://github.com/karanzaveri/Currency-Conversion/#clean-code-development)
7. [IDE](https://github.com/karanzaveri/Currency-Conversion/#ide)
8. [Functional Programming](https://github.com/karanzaveri/Currency-Conversion/#functional-programming)

# Code
To access the code: [Currency Conversion Code](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_coversion.py)

# UML Diagrams
### 1. Activity Diagram
* The activity diagram showcases a user-driven process, starting with entering source currency followed by target currency and then the amount. Once the valid data is entered, the conversion process is triggered and the converted amount with the applied exchange rate is displayed. 
* [Activity Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/ActivityDiagram.png)

### 2. Use Case Diagram
* The use case diagram outlines how the users interact with the system. Users initiate the currency conversion process by specifying source currency, target currency and amount, while the system performs conversions and provides the results.
* [Use Case Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/UseCaseDiagram.png)

### 3. Class Diagram
* The class diagram represents classes like Currency Converter, Currency Rates, GUI and Error Handling elements, illustrating their relationships and interactions in facilitating user input, data retrieval, and conversion processes within the application.
* [Class Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/ClassDiagram.png)

# Requirements Engineering
### 1. Functional Requirements
* Currency Conversion
* Real-Time Exchange Rates
* Graphical User Interface (GUI)
* User Input Handling
* Transaction History

### 2. Non-Functional Requirements
* Performance
* User Experience (UX)
* Reliability
* Maintainability
* Quality Assurance

### [Trello](https://trello.com/invite/b/g0aGcUnD/ATTI873728185d133e582c79efe96ca36a855FA179CA/currency-conversion)
* Tasklist [Screenshot](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/trello.png)

### [JIRA](https://karanzaveri92.atlassian.net/jira/software/projects/CC/boards/1?atlOrigin=eyJpIjoiZGZkYzc3ZDhjOTY0NGE0Mzg4NjU0MTQyNTNkNThkMzQiLCJwIjoiaiJ9)
* Kanban Board [Screenshot](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/jira.png)

# DDD
Domain-Driven Design (DDD) is an approach to software development that centers around a deep understanding of the business domain. 
[PDF](https://github.com/karanzaveri/Currency-Conversion/blob/main/docs/DDD.pdf)

# Metrics
* [Sonarqube](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/sonarqube.png)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=bugs)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

# Clean Code Development

Clean Code Development (CCD) focuses on writing code that is easy to read, understand, and maintain.
[PDF](https://github.com/karanzaveri/Currency-Conversion/blob/main/docs/Clean%20Code%20Development.pdf)

# IDE
I have used Visual Studio Code IDE, mentioned below are my few favorite shortcuts:
* F5 : Run and Debug
* Ctrl + ] / Ctrl + [ : Indentation
* Ctrl + / : Comment/Uncomment code lines
* Ctrl + B : Show or hide the sidebar
* Ctrl + Shift + P : Open the command palette

# Functional Programming
In my Currency Conversion code, certain functional programming principles are applied. Here's how the code adheres to these principles:

1. Final Data Structures:
The data attribute in the [RealTimeCurrencyConverter](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_coversion.py#L11) class is initialized with the result of the API call ('response.json()'), which is a final data structure containing exchange rates. The data is not modified afterward.

2. Side-Effect-Free Functions:
The [get_exchange_rates](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_coversion.py#L16) function in the RealTimeCurrencyConverter class has no side effects. It takes a URL as input, performs an HTTP GET request, and returns the JSON response. It does not modify any external state.
The 'convert' method also does not have side effects. It takes input values and returns a new calculated value without modifying any external state.

3. Higher-Order Functions:
The use of the 'requests.get' function in the 'get_exchange_rates' method can be considered a higher-order function. It takes a URL as an argument and returns a function (get) that performs an HTTP GET request.

4. Functions as Parameters and Return Values:
The [convert](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_coversion.py#L25) method in the 'RealTimeCurrencyConverter' class takes three parameters ('from_currency', 'to_currency', and 'amount') and returns a calculated value. It can be seen as a function that takes parameters and produces a result.
The 'command' parameter in the 'Button' widgets ('convert_button' and 'history_button') takes functions ('perform_conversion' and 'show_transaction_history') as parameters to be executed when the buttons are clicked.

5. Closures / Anonymous Functions:
The use of 'lambda' functions is not explicitly present in the code. However, the functions passed as parameters to the 'command' attribute of buttons can be considered as anonymous functions.
Overall, while the code incorporates some functional programming principles, it primarily follows an object-oriented paradigm due to its use of classes and methods.

# Built Using
![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

# Contact Me
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:karanzaveri92@gmail.com)
