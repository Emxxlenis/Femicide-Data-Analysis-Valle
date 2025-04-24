# English

# Feminicide Analysis in Valle del Cauca (2020–2024) 

## 📊 Overview
This project performs a detailed analysis of feminicides in Valle del Cauca (Colombia) between 2018 and 2024. It utilizes official public data from Datos Abiertos Colombia, and focuses on visualizing trends, key municipalities, and affected subregions.


## 📈 Insights & Conclusions 

### 📅 By Year

The peak was in 2020 (almost 40% of all cases). There’s a notable decrease in 2023, followed by a rise again in 2024. This irregularity might reflect reporting issues or social/political changes.

### 🏙️ By Municipality

Cali alone accounts for over half of the total feminicides, which highlights an urgent need for focused policy and social interventions in urban zones.

### 🗺️ By Subregion

The southern part of Valle del Cauca is disproportionately affected. This could relate to demographic density or institutional weaknesses.



## 📁 Dataset

- **Source:** Datos Abiertos Colombia

- **Format:** Excel (.xlsx)

- **Columns:** Municipio, Año, Subregión, Número de víctimas.

- **Time range:** 2018–2024

## 🧪 Technical Stack

- **Language:** Python 3.12.9

- **Libraries:**

- `pandas` for data handling

- `seaborn` & `matplotlib` for visualization

- `openpyxl` for reading Excel files

Project structure:

```
├── data/
│   └──  raw/
│        └── feminicides_valle_cauca_2020_2024_raw.xlsx
│   
├── src/
│   ├── load_data.py
│   ├── analysis.py
│   ├── plotting.py
│   └── utils.py
├── main.py
├── requeriments.txt 
└── README.md
```


## ⚙️ How to Run

```
# 1. Clone the repo
$ git clone https://github.com/yourusername/valle-feminicide-analysis.git](https://github.com/Emxxlenis/Femicide-Data-Analysis-Valle/new/main?filename=README.md
$ cd valle-feminicide-analysis

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Run the main script
$ python main.py
```

The script will:

- Load and clean the dataset.
- Generate and save statistics (by year, municipality, subregion).
- Plot charts and save them in the `outputs/` directory.


## 📎 Citation

If you use this dataset, please cite:
> Government of Colombia (Datos Abiertos). Total de mujeres víctimas de feminicidio por municipio [Data set]. Retrieved from [https://www.datos.gov.co/Estad-sticas-Nacionales/Total-de-mujeres-victimas-de-feminicidio-por-munic/fs93-tx8v
](https://www.datos.gov.co/Estad-sticas-Nacionales/Total-de-mujeres-victimas-de-feminicidio-por-munic/fs93-tx8v/about_data)

## 🧠 Author & Motivation
Made by Emily Lenis, data & AI student from Cali. This project is part of a personal initiative to use technology for social impact.

## 📬 Feedback
Feel free to fork, suggest changes, or reach out via GitHub Issues.


# Español

# Análisis de Feminicidios en Valle del Cauca (2018–2024)

## 📊 Visión General  
Este proyecto realiza un análisis detallado de los feminicidios en el departamento del Valle del Cauca (Colombia) entre 2018 y 2024. Se utiliza un conjunto de datos oficial de Datos Abiertos Colombia, con el objetivo de visualizar tendencias, municipios clave y subregiones más afectadas.


## 📈 Hallazgos y Conclusiones

### 📅 Por Año  
El pico se presentó en 2020 (casi el 40% del total de casos). En 2023 se observa una disminución considerable, seguida de un aumento en 2024. Esta irregularidad puede deberse a fallos en el reporte o a cambios sociales/políticos.

### 🏙️ Por Municipio  
Solo Cali concentra más de la mitad de los feminicidios registrados, lo que evidencia una necesidad urgente de políticas públicas focalizadas y acciones sociales en zonas urbanas.

### 🗺️ Por Subregión  
La zona sur del Valle del Cauca es la más afectada. Esto podría estar relacionado con la densidad demográfica o con deficiencias institucionales en esas regiones.



## 📁 Conjunto de Datos

- **Fuente:** Datos Abiertos Colombia  
- **Formato:** Excel (.xlsx)  
- **Columnas:** Municipio, Año, Subregión, Número de víctimas  
- **Rango temporal:** 2018–2024

---

## 🧪 Tecnologías Utilizadas

- **Lenguaje:** Python 3.12.9  
- **Librerías:**  
  - `pandas` para manejo de datos  
  - `seaborn` y `matplotlib` para visualización  
  - `openpyxl` para lectura de archivos Excel  

**Estructura del proyecto:**

```
├── data/
│   └──  raw/
│        └── feminicides_valle_cauca_2020_2024_raw.xlsx
│   
├── src/
│   ├── load_data.py
│   ├── analysis.py
│   ├── plotting.py
│   └── utils.py
├── main.py
├── requeriments.txt 
└── README.md
```

## ⚙️ Cómo Ejecutarlo

```

# 1. Clona el repositorio
git clone https://github.com/yourusername/valle-feminicide-analysis.git
cd valle-feminicide-analysis

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Ejecuta el script principal
python main.py
```


El script realizará:

- Carga y limpieza del dataset

- Análisis por año, municipio y subregión

- Creación de visualizaciones almacenadas en el directorio `outputs/`


## 📎 Cita
Si utilizas este conjunto de datos, por favor cita:
> Gobierno de Colombia (Datos Abiertos). Total de mujeres víctimas de feminicidio por municipio [Conjunto de datos]. Recuperado de https://www.datos.gov.co/Estad-sticas-Nacionales/Total-de-mujeres-victimas-de-feminicidio-por-munic/fs93-tx8v

## 🧠 Autora y Motivación
Hecho por Emily Lenis, estudiante de Ingeniería de Datos e Inteligencia Artificial de Cali. Este proyecto hace parte de una iniciativa personal para usar la tecnología como motor de impacto social.

## 📬 Feedback
Siéntete libre de hacer fork, sugerir mejoras o dejar tus comentarios a través de GitHub Issues.
