"""
Module and supports all the REST actions for the metrobús data
"""
from flask import abort
from config import db
from models import Metrobus, MetrobusSchema, Alcaldia, AlcaldiaSchema


def read_all_metrobuses():
    """
    Responds to a request for /api/metrobus
    with the complete lists of all metrobuses

    :return:        json string with list of metrobuses
    """
    # List of all metrobuses registered in database
    metrobuses = Metrobus.query.order_by(Metrobus._id).all()

    # Serialized data for the response
    metrobus_schema = MetrobusSchema(many=True)
    data = metrobus_schema.dump(metrobuses)
    return data


def read_metrobus(metrobus_id: int):
    """
    Responds to a request for /api/metrobus/{metrobus_id}
    with one matching metrobus from registered metrobuses in the database

    :param metrobus_id:   ID number of metrobus unit to find
    :return:              200 metrobus unit matching ID, 404 on metrobus unit not found
    """
    metrobus = Metrobus.query.filter(Metrobus._id == metrobus_id).one_or_none()

    if metrobus is not None:
        # Serialized data for the response
        metrobus_schema = MetrobusSchema()
        data = metrobus_schema.dump(metrobus)
        return data

    # Not found
    else:
        abort(
            404,
            f"Metrobus not found for ID: {metrobus_id}",
        )


def read_all_alcaldias():
    """
    Responds to a request for /api/alcaldia
    with the complete lists of all alcaldías in the CDMX

    :return:        json string with list of alcaldías
    """
    # List of all alcaldías registered in database
    alcaldias = Alcaldia.query.order_by(Alcaldia.nomgeo).all()

    # Serialized data for the response
    alcaldia_schema = AlcaldiaSchema(many=True)
    data = alcaldia_schema.dump(alcaldias)
    return data


def read_alcaldia(alcaldia_id: int):
    """
    Responds to a request for /api/alcaldia/{alcaldias_id}
    with one matching alcaldía from registered alcaldias in the database

    :param alcaldia_id:   ID number of alcaldía to find
    :return:              200 alcaldía matching ID, 404 on alcaldía not found
    """
    alcaldia = Alcaldia.query.filter(Alcaldia._id == alcaldia_id).one_or_none()

    if alcaldia is not None:
        # Serialized data for the response
        alcaldia_schema = AlcaldiaSchema()
        data = alcaldia_schema.dump(alcaldia)
        return data

    # Not found
    else:
        abort(
            404,
            f"Alcaldía not found for ID: {alcaldia_id}",
        )

