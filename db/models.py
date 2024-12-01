from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, BigInteger

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    aura = Column(Float, nullable=False)
    mitadas = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<User(user_id='{self.user_id}', aura='{self.aura}', mitadas='{self.mitadas}')>"

    # Método para incrementar aura
    def increment_aura(self, amount: float):
        self.aura += amount

    # Método para incrementar mitadas
    def increment_mitadas(self, amount: int):
        self.mitadas += amount