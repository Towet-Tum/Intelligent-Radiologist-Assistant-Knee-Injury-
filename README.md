# Intelligent-Radiologist-Assistant-Knee-Injury-

### Workflows
1. Update config.yaml
2. Update secrets.yaml [optional]
3. update params.yaml
4. Udate the entity
5. Update the configuration manager in src config 
6. Update the components 
7. Update the pipeline
8. Update the main .py
9. Update the dvc.yaml 




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project
```
### STEP 01- Create a virtual environment after opening the repository

```bash
python3 -m venv venv
```

```bash
source lung/bin/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python manage.py runserver
```

Now,
```bash
open up you local host and port (127.0.0.1:8000)
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag
