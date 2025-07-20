# RBI_task_v_03 Notebook – SWOT Analysis

## Strengths
- End-to-end workflow covering preprocessing, model training and evaluation.
- Uses CatBoost and Hyperopt for robust modeling and tuning.
- Visualization of results (correlation matrix, histograms, SHAP plots).
- Saves trained model and predictions for downstream use.

## Weaknesses
- Heavy reliance on Google Colab specific setup (drive mounting and paths).
- Many `try/except` blocks silently ignore errors and hinder debugging.
- Code is largely procedural with duplicated logic and limited reuse.
- Hard-coded file names reduce portability and reproducibility.

## Opportunities
- Encapsulate preprocessing and modeling logic into reusable classes.
- Parameterize file paths and model settings for easier configuration.
- Add automated tests and requirements file for reproducibility.
- Provide a script or module to run the workflow outside notebooks.

## Threats
- Hidden errors due to broad exception handling can compromise data quality.
- Changes in data schema may break the notebook without clear messages.
- Lack of environment specification makes it hard to reproduce results.
- Manual steps (installing packages in cells) can lead to inconsistent runs.
