# Usage

bring this up in a container using:
```shell
path/to/project/ $ docker compose up -d
```

access from `localhost:8501`


# Development:

using python 3.11

create a virtual environment

activate the virtual environment and install dependencies 

```shell
path/to/project/ $ poetry install --no-dev
```

OR 

```shell
path/to/project/ $ pip install -r requirements.txt
```

run the application:

```shell
path/to/project/ $ streamlit run src/streamlit_app.py
```