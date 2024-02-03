# Income Prediction Project

## Project Overview

The Income Prediction project is a comprehensive data science and machine learning endeavor, employing modular coding standards for effective project organization. The project encompasses data ingestion, data transformation, model training, and deployment stages, adhering to best practices in the field.

## Problem Statement

The primary objective is to accurately predict whether an individual's income exceeds $50,000 based on demographic and employment-related features. This problem holds significance in real-world scenarios, aiding decision-making processes and resource allocation.

## Dataset Overview

The dataset used for income prediction includes various features such as age, workclass, education, marital status, occupation, race, and more. The target variable is 'salary,' indicating whether an individual makes more or less than $50,000 annually.

### Project Structure Automation

The project kicks off with the creation of a `template.py` file, automating the folder structure of the entire project. This not only ensures a standardized layout but also streamlines collaboration and maintenance.

### Version Management

A `setup.py` file is introduced to facilitate versioning of the project. This allows for tracking changes, managing dependencies, and ensuring reproducibility across different environments.

### Data Ingestion

#### Data Loading and Artifacts
In the data ingestion phase, the dataset is loaded, and an 'artifacts' folder is created to store essential artifacts generated throughout the project.

#### Data Splitting
The dataset is split into training and testing sets, a critical step in model evaluation to ensure robust performance.

### Data Transformation

#### Label Encoding and Columns Transformation
Data transformation involves label encoding categorical variables and using a columns transformer for streamlined preprocessing. This prepares the data for the machine learning pipeline.

#### Model Training

##### Models Considered
The project explores three models – Random Forest Classifier, Decision Tree Classifier, and Logistic Regression. Grid Search CV is employed for hyperparameter tuning to enhance model performance.

##### Model Selection
After rigorous evaluation, the Random Forest Classifier emerges as the best-performing model, boasting an accuracy of 81%.

### Deployment with Flask

The project is deployed using the Flask framework, providing a web interface for users to interact with the income prediction model. This deployment ensures practical applicability and accessibility.

### Logger and Exception Handling

Custom exception handling and logging mechanisms are implemented to enhance code reliability and facilitate debugging. These additions contribute to the project's maintainability and robustness.


## Data Visualization

1. Distribution of numerical features    



2. income VS workclass     



3. income VS education


4. income VS marital.status



5. income VS occupation



6. income VS relationship



7. income VS sex






## Conclusion

The Income Prediction project showcases a systematic approach to data science and machine learning, incorporating modular coding practices for enhanced project structure and maintainability. The utilization of multiple models, thorough data transformation, and the deployment of the best-performing model via Flask demonstrate a comprehensive solution to the income prediction problem.