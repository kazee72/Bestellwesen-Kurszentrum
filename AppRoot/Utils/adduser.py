import sys
import logging
from sqlalchemy import exc

logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger(__name__)

def testAdduser(app,db,models):
    with app.app_context():
        email = "dooner@dooner.ch"
        name = "testAdduser"
        prename = "sdfa"
        pw = "anothersafepassword"
        user = models.User(email=email,name=name,prename=prename,password=pw)
        db.session.add(user)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            logger.info("User already exist in db:"+ str(e))
            db.session.rollback()
