# Cara Menjalankan Dashboard

## Setup Environment Conda

Jika masih dalam environment (base)

```
conda deactivate
```

Jika tidak dalam environment conda

```
mkdir proyek_analisis_data
cd proyek_analisis_data
conda create --name main-ds python=3.11
conda activate main-ds
conda install requirements.txt
```

## Setup Environment - Shell/Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

# Menjalankan dashboard (streamlit app)

```
cd dashboard
streamlit run dashboard.py
```
