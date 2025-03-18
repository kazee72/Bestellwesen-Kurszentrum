# Bestellwesen-Kurszentrum
System for material orders for our internal courses.

# Initialize a db  

https://flask-migrate.readthedocs.io/en/latest/


> flask db init
# Migrate  

if we change the models.py we need to tell sqlalchemy to migrate and upgrade the database to be in sync with the model.


> flask db migrate  
> flask db upgrade
