# Guild Wars 2 Trading Post

## Goal
Goal of the project is to build a solution for:  
1. Gathering data from GW2 APIs.  
2. Storing data in database.  
3. Cleaning and preparing datasets for BI.

## Princaples
1. All ETL processes should be build on Python 3 or above. Other ETL tools could be applied as option.
2. All files data will be focused on JSON format. Other formats(csv,xml) is an option.
3. Main database will be SQL Server. Other databases will be an option.
4. Final BI tool will be Jupyter Notebooks. Other BI systems is an option.
5. Scheduler will be chosen later.
6. Tests will be done with .py scripts.

## Project - Tools
- **ETL** - Python3.x
- **Filesystem Storage** - JSON
- **Database** - SQL Server
- **BI** - JupyterNotebook Python
- **Test** - Python3.x
- **Scheduler** - Python scheduler/Windows Task Manager

## Subprojects
1. GW2API Extractor 
Python project for extracting data from api and storing data in JSON format.
2. GW2TP Staging
Database project for landing and staging layers. 
Python project for staging data in database landing and staging layers.
3. GW2TP DWH Core
Database project for core and datamarts layer.
Python project for core and datamarts layer processes.
4. GW2TP Control
Project for controlling life status of hole project. 
Should include scheduler and monitoring tools.
5. GW2TP BI
BI project with prepared analytics.