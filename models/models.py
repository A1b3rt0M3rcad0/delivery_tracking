from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    delivery_code = Column(String(11), unique=True)
    addresse_name = Column(String(100))
    full_address = Column(String(100))
    created_at = Column(Date)
    finished = Column(Boolean, default=False)

    # Relacionamento com as etapas de entrega
    delivery_steps = relationship("DeliveryStep", back_populates="post")


class DeliveryStep(Base):
    __tablename__ = 'delivery_steps'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    delivery_stage_name = Column(String(50))
    delivery_stage_description = Column(String(100))
    delivery_stage = Column(Integer)
    due_date_delivery_stage = Column(Integer)
    started_at = Column(Date)
    finished_at = Column(Date)
    finished = Column(Boolean, default=False)

    # Relacionamento com o post
    post = relationship("Post", back_populates="delivery_steps")

    # Restrição de unicidade composta
    __table_args__ = (UniqueConstraint('post_id', 'delivery_stage', name='unique_delivery_stage_per_post'),)