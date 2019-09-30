from sqlalchemy.schema import Column,ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float

from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token
from ...settings import app_config
from ...extensions import bcrypt

class Vysledky(CRUDModel):
    __tablename__ = 'vysledky'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True, doc="The user's username.")
    hodnoceni=Column(Float, nullable=False, index=False)

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.activate_token = generate_random_token()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

