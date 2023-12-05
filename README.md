# Currency Conversion
The Currency Converter project allows you to convert from one currency to another with real-time exchange rates.
It is built using Python various libraries like forex-python, tkinter.

# Table Of Contents
1. [Code](https://github.com/karanzaveri/Currency-Conversion/#code)
2. [Libraries Used](https://github.com/karanzaveri/Currency-Conversion/#libraries-used)
3. [UML Diagrams](https://github.com/karanzaveri/Currency-Conversion/#uml-diagrams)
4. [DDD](https://github.com/karanzaveri/Currency-Conversion/#ddd)
5. [Built Using](https://github.com/karanzaveri/Currency-Conversion/#built-using)

# Code
To access the code: [Currency Conversion Code](https://github.com/karanzaveri/Currency-Conversion/blob/main/Currency%20Converter.ipynb)

# Libraries Used
### forex-python
* Forex Python is a Free Foreign exchange rates and currency conversion library

#### Currency Source
https://theforexapi.com is a free API for current and historical foreign exchange rates published by European Central Bank. The rates are updated daily 3PM CET.

### tkinter
* Python's standard GUI toolkit for creating desktop applications with widgets, windows, and event handling.

# UML Diagrams
### 1. Activity Diagram
* The activity diagram showcases a user-driven process, starting with entering source currency followed by target currency and then the amount. Once the valid data is entered, the conversion process is triggered and the converted amount with the applied exchange rate is displayed. 
* [Activity Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/activity_diagram.png)

### 2. Use Case Diagram
* The use case diagram outlines how the users interact with the system. Users initiate the currency conversion process by specifying source currency, target currency and amount, while the system performs conversions and provides the results.
* [Use Case Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/use_case_diagram.png)

### 3. Class Diagram
* The class diagram represents classes like Currency Converter, Currency Rates, GUI and Error Handling elements, illustrating their relationships and interactions in facilitating user input, data retrieval, and conversion processes within the application.
* [Class Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/class_diagram.jpg)

# DDD
Domain-Driven Design (DDD) is an approach to software development that centers around a deep understanding of the business domain. Similar to planning a party by considering the needs and preferences of guests, DDD focuses on comprehending intricate business processes and requirements. It involves creating a well-thought-out plan for each software component, adapting it as user needs evolve. DDD aims to ensure that the software is not only functional but also aligns effectively with the dynamic and evolving demands of the real-world business domain.

## Core Domains

### 1. Financial Services
* Managing currency rates, conversions, and accurate financial calculations.

### 2. User Interface (UI)/User Experience (UX)
* Designing and managing the graphical interface for user interaction.

### 3. External APIs/Services Integration
* Interfacing with external API (like forex_python) for currency data retrieval and conversion.

### 4. User Input Handling
* Capturing and processing user input like the source currency, target currency, and conversion amount.

### 5. Data Representation
* Representing and displaying data in the graphical user interface using the Tkinter libary.

### 6. Dynamic GUI Elements
* Managing the dynamic update of GUI elements, such as available currencies, based on user input.

### 7. Error Handling and Validation
* Ensuring input data integrity and managing potential errors that can occur during user interactions or conversions.

### 8. State Management:
* Managing the state of GUI elements, determining when certain buttons should be enabled or disabled based on user actions.

### 9. Software Engineering/Architecture
* Designing the software structure, classes, and modules for efficiency and scalability.

## Domain Chart
* The Domain Chart represents the distinct domains within the application. The domains are interconnected to represent the structured and modular design of the application.
* [Domain Chart](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/domain_chart.png)

# Built Using
![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

# Contact Me
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:karanzaveri92@gmail.com)