## Dash Application Project
This project is a Dash application developed using the Dash framework, which allows you to build interactive web applications with Python. The intention of this project was a learning one. The other part of this project is a [bootcamp group project located](https://github.com/gamountainmama/data_dames "Neural Network Project") on this repository. This project is a neural network project that is building a model to predict various aspects of education from the potential success of a student in Computer Science to the effects of the the students demographics on their successs.

## Project Structure
The project structure is organized as follows:

* app.py: This is the main file that runs the Dash application server and defines the application layout and callbacks.
* components: This directory contains reusable components or modules that can be used in the application.
* apps: These files contain separate pages or sections of the web application.
* pages: This directory contains the different pages or sections of the application.
* data: This directory contains data files or datasets used by the application.
* 

## Datasets
The project utilizes three different datasets:

Kaggle Dataset: This dataset is sourced from Kaggle and provides data from four schools including demographics.

Rural Georgia Dataset: This dataset is from a school in a rural region in Georgia, it provides insight into students scores over a time period. The data has been cleaned and transformed by a a contributor in a bootcamp group.

Private School in Florida Dataset: This dataset is from a private school in Florida and includes information on all section grades for a snapshot for grades 9-12. The data is clean and was directly sourced from a SIS.

## Getting Started
This project was a learning project of the Dash Library. This was the first time using the library.  The intention was to develop a multipage website showcasing three different datasets. It is structured in the format required in the documentation. However, there is a currently a caching issues and the pages now load in different ports and are not accessible via the bootstrap dropdown menu. This project is a work in progress. Currently investigating The Explainer Dashboard to incorporate into this website.

To run the Dash application, follow these steps:

Install the required dependencies by running the requirements. (In the process of writing the correct requirements text: pip install -r requirements.txt.)
If the multipage system works: 
Execute the app.py file using Python: python app.py.
Open your web browser and navigate to the provided URL (usually http://127.0.0.1:8050 or http://localhost:8050).

To run currently:
Navigate to the pages folder and launch the files app1.py, app2.py, app3.py, app4.py respectively.

## Dependencies and Toolchain

A combination of the Dash framework for building the web application, Python programming language for coding the application logic, and various libraries such as Dash Bootstrap Components, Plotly Express, Pandas, and pathlib for specific functionalities were used.

* Dash: The core library for building Dash applications.
* Dash Bootstrap Components (dbc): A library of Bootstrap-themed Dash components.
* Plotly Express (px): A high-level library for interactive data visualization.
* Pandas: A powerful data manipulation and analysis library.
* pathlib: A module providing classes for working with file and directory paths.
* 
Website Views
Kaggle View - app1.py
Kaggle View Screenshot 1
Kaggle View Screenshot 2
FtL View - app2.py

## Website Views
### Kaggle View - app1.py

<img width="1135" alt="Screenshot 2023-05-17 at 7 51 11 PM" src="https://github.com/KellyPared/dash_dashboard/assets/40581033/6ee5fdf2-e8d3-4a90-85d2-c925f49249b2">

<img width="1155" alt="Screenshot 2023-05-17 at 7 51 29 PM" src="https://github.com/KellyPared/dash_dashboard/assets/40581033/265c9645-3a40-4474-880f-376dcdc9b934">

### Fl School - app2.py
<img width="1019" alt="Screenshot 2023-05-17 at 8 17 58 PM" src="https://github.com/KellyPared/dash_dashboard/assets/40581033/d63dba14-7f62-4ebb-b947-40e2fb8fabdb">

### Contributing
Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the project's GitHub repository.

### SME's
Developers capable of advance skills in data visualizations welcome also, experts in education interested in contributing data to analyze potential prediction models for students succeess based on students grades and a demographics. In addition, look into what makes a students successflul in Computer Science.

## License
This project is free to use, and modify.

## Resources
* Dash Documentation
* Dash Bootstrap Components Documentation
* Plotly Express Documentation
* Pandas Documentation
* pathlib Documentation
* ChatGPT
