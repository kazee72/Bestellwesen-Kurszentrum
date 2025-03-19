# Bestellwesen-Kurszentrum
System for material orders for our internal courses.
# Setup Flask secret token  
Start a python interactive shell:  
> python  
Run the following to generate a key:  
> import secrets  
> secrets.token_hex(64)  
copy the token into:  
> AppRoot/.env    
like this:
> FLASK_SECRET_KEY=insertKeyHere

# Initialize a db  

https://flask-migrate.readthedocs.io/en/latest/


> flask db init
# Migrate  

if we change the models.py we need to tell sqlalchemy to migrate and upgrade the database to be in sync with the model.


> flask db migrate  
> flask db upgrade
