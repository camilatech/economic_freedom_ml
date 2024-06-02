# Mercosur Economic Freedom Prediction Using Machine Learning

## Overview

This project, developed for my final degree thesis (TCC), aims to leverage machine learning to predict economic freedom in Mercosur countries. Utilizing MLOps practices and Kedro for reproducible workflows, the study evaluates three machine learning algorithms: Prophet, XGBoost, and Random Forest. Prophet demonstrated superior performance in predicting economic freedom trends based solely on economic freedom scores, providing valuable insights into the possible evolution of economic freedom in these countries.

For more details, you can read the full thesis [here](https://sistemabu.udesc.br/pergamumweb/vinculos/0000aa/0000aa48.pdf).

**Keywords:** Machine Learning, Economic Freedom, Mercosur, Forecasting, Trend Analysis

## Project Setup

### Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install Kedro:

```bash
pip install kedro
```

3. Navigate to the project folder and install the requirements:

```bash
pip install -r src/requirements.txt
```

### Running the Kedro Pipeline

To run the Kedro project, execute:

```bash
kedro run
```

### Testing the Project

Refer to `src/tests/test_run.py` for instructions on writing tests. Run your tests with:

```bash
kedro test
```

Configure the coverage threshold in the `.coveragerc` file.

### Project Dependencies

To generate or update the project dependencies:

```bash
kedro build-reqs
```

This command will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`.

### Working with Jupyter Notebooks

To use Jupyter notebooks in your Kedro project, first install Jupyter:

```bash
pip install jupyter
```

Start a local notebook server:

```bash
kedro jupyter notebook
```

For JupyterLab:

```bash
pip install jupyterlab
kedro jupyter lab
```

For an IPython session:

```bash
kedro ipython
```

### Converting Notebook Cells to Nodes

Add the `node` tag to a cell and convert it to a Python file within `src/<package_name>/nodes/`:

```bash
kedro jupyter convert <filepath_to_my_notebook>
```

To convert all notebooks at once:

```bash
kedro jupyter convert --all
```

### Ignoring Notebook Output Cells in `git`

Strip out all output cell contents before committing to `git`:

```bash
kedro activate-nbstripout
```

### Packaging Your Kedro Project

For more information on building project documentation and packaging, refer to the [Kedro documentation](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html).

### Data Sources

Data used in this project were extracted on:

- **09/02/2023** from [Heritage Foundation](https://www.heritage.org/index/explore?view=by-region-country-year&u=638115797667131343)
- **10/02/2023** from [World Population Review](https://worldpopulationreview.com/country-rankings/list-of-countries-by-continent)
