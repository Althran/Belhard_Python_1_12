from db.session import Session
from db.tables import tables

with Session as db_session:
    new_persons = tables.Persons(name='Viktor', surname='Komarets', birth_date='March')
    db_session.add(new_persons)
    db_session.commit()

    choice_person = db_session.query(tables.Persons).filter(tables.Persons.id == 1).first()

    changed_person = db_session.query(tables.Persons).filter(tables.Persons.id == 1).first()
    changed_person.name = 'New_name'
    db_session.commit()

    person = db_session.query(tables.Persons).filter(tables.Persons.id == 1).first()
    db_session.delete(person)
    db_session.commit()
