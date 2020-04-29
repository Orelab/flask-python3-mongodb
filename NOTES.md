## entrer dans le venv :
```
. venv/bin/activate
```

## Sortir du venv :
```
deactivate
```

## Lancer le serveur de dev :
```
export FLASK_APP=app.py
export FLASK_ENV=development

flask run
# ou
# flask run --host=0.0.0.0
# ou
# python -m flask run --host=0.0.0.0

```


## Fichier requirements.txt

Ce fichier permet de freezer es dépendances, un peu à la manière de package.json avec nodejs
```
pip freeze > requirements.txt
```
Ensuite, se contenter de faire un `pip install` pour recréer un environnement ;)