from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Questions(Base):  # <- No extra spaces before this line
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)


class Choices(Base):  # <- Aligned with `class Questions`
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))