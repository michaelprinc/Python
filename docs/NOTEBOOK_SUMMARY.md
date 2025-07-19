# Notebook Overview

This repository contains a collection of Jupyter notebooks from a variety of
online courses and experiments. They are grouped by topic as follows:

## Data Visualization Series

- `Cognitive_class_Data_Visualization_with_Python.ipynb` – introductory
  exploration of plotting with pandas and matplotlib.
- `Cognitive_class_Data_Visualization_with_Python_2.ipynb`
- `Cognitive_class_Data_Visualization_with_Python_3.ipynb`
- `Cognitive_class_Data_Visualization_with_Python_4.ipynb`
- `Cognitive_class_Data_Visualization_with_Python_5.ipynb`

The notebooks above progressively cover loading data from Excel, generating
various chart types and styling plots. They can be run independently using
Jupyter or Google Colab.

## Machine Learning Exercises

- `Cognitive_class_ML.ipynb`
- `Cognitive_class_ML_2.ipynb`
- `Cognitive_class_ML_3.ipynb`
- `Cognitive_class_ML_4.ipynb`

These notebooks demonstrate small machine‑learning tasks ranging from
classification to clustering. They rely primarily on `scikit-learn` and
`pandas`.

## Other Notebooks

- `codecademy.ipynb` – miscellaneous practice from Codecademy courses.
- `kaggle_exercise.ipynb` – Kaggle starter exercises and examples.
- `RBI_task_v_03.ipynb` – a domain‑specific analysis for the RBI project.

## Recommendations and Future Work

1. **Convert common code into reusable modules.**  Repeated plotting and data
   loading logic could be moved into Python modules such as
   `utils/data_viz_utils.py` (added in this update).
2. **Add testing.**  Automated tests would ensure that utility functions and any
   future scripts behave as intended.
3. **Package the notebooks.**  Providing an environment file (e.g. `requirements.txt`)
   would make it easier for others to reproduce the analyses.
4. **Improve documentation.**  A short description at the top of each notebook
   outlining its goal will help new readers understand the context quickly.
