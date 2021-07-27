"""
editing_vocabulary.py COPYRIGHT FUJITSU LIMITED 2021
"""
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EditingVocabulary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, term: str=None, preferred_label: str=None, uri: str=None, broader_term: str=None, synonym: List[str]=None, synonym_candidate: List[str]=None, broader_term_candidate: List[str]=None, part_of_speech: str=None, postion_x: str=None, postion_y: str=None, color1: str=None, color2: str=None):  # noqa: E501
        """EditingVocabulary - a model defined in Swagger

        :param id: The id of this EditingVocabulary.  # noqa: E501
        :type id: int
        :param term: The term of this EditingVocabulary.  # noqa: E501
        :type term: str
        :param preferred_label: The preferred_label of this EditingVocabulary.  # noqa: E501
        :type preferred_label: str
        :param uri: The uri of this EditingVocabulary.  # noqa: E501
        :type uri: str
        :param broader_term: The broader_term of this EditingVocabulary.  # noqa: E501
        :type broader_term: str
        :param synonym: The synonym of this EditingVocabulary.  # noqa: E501
        :type synonym: List[str]
        :param synonym_candidate: The synonym_candidate of this EditingVocabulary.  # noqa: E501
        :type synonym_candidate: List[str]
        :param broader_term_candidate: The broader_term_candidate of this EditingVocabulary.  # noqa: E501
        :type broader_term_candidate: List[str]
        :param part_of_speech: The part_of_speech of this EditingVocabulary.  # noqa: E501
        :type part_of_speech: str
        :param postion_x: The postion_x of this EditingVocabulary.  # noqa: E501
        :type postion_x: str
        :param postion_y: The postion_y of this EditingVocabulary.  # noqa: E501
        :type postion_y: str
        :param color1: The color1 of this EditingVocabulary.  # noqa: E501
        :type color1: str
        :param color2: The color2 of this EditingVocabulary.  # noqa: E501
        :type color2: str
        """
        self.swagger_types = {
            'id': int,
            'term': str,
            'preferred_label': str,
            'uri': str,
            'broader_term': str,
            'synonym': List[str],
            'synonym_candidate': List[str],
            'broader_term_candidate': List[str],
            'part_of_speech': str,
            'postion_x': str,
            'postion_y': str,
            'color1': str,
            'color2': str
        }

        self.attribute_map = {
            'id': 'id',
            'term': 'term',
            'preferred_label': 'preferred_label',
            'uri': 'uri',
            'broader_term': 'broader_term',
            'synonym': 'synonym',
            'synonym_candidate': 'synonym_candidate',
            'broader_term_candidate': 'broader_term_candidate',
            'part_of_speech': 'part_of_speech',
            'postion_x': 'postion_x',
            'postion_y': 'postion_y',
            'color1': 'color1',
            'color2': 'color2'
        }
        self._id = id
        self._term = term
        self._preferred_label = preferred_label
        self._uri = uri
        self._broader_term = broader_term
        self._synonym = synonym
        self._synonym_candidate = synonym_candidate
        self._broader_term_candidate = broader_term_candidate
        self._part_of_speech = part_of_speech
        self._postion_x = postion_x
        self._postion_y = postion_y
        self._color1 = color1
        self._color2 = color2

    @classmethod
    def from_dict(cls, dikt) -> 'EditingVocabulary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EditingVocabulary of this EditingVocabulary.  # noqa: E501
        :rtype: EditingVocabulary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this EditingVocabulary.


        :return: The id of this EditingVocabulary.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this EditingVocabulary.


        :param id: The id of this EditingVocabulary.
        :type id: int
        """

        self._id = id

    @property
    def term(self) -> str:
        """Gets the term of this EditingVocabulary.


        :return: The term of this EditingVocabulary.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term: str):
        """Sets the term of this EditingVocabulary.


        :param term: The term of this EditingVocabulary.
        :type term: str
        """

        self._term = term

    @property
    def preferred_label(self) -> str:
        """Gets the preferred_label of this EditingVocabulary.


        :return: The preferred_label of this EditingVocabulary.
        :rtype: str
        """
        return self._preferred_label

    @preferred_label.setter
    def preferred_label(self, preferred_label: str):
        """Sets the preferred_label of this EditingVocabulary.


        :param preferred_label: The preferred_label of this EditingVocabulary.
        :type preferred_label: str
        """

        self._preferred_label = preferred_label

    @property
    def uri(self) -> str:
        """Gets the uri of this EditingVocabulary.


        :return: The uri of this EditingVocabulary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this EditingVocabulary.


        :param uri: The uri of this EditingVocabulary.
        :type uri: str
        """

        self._uri = uri

    @property
    def broader_term(self) -> str:
        """Gets the broader_term of this EditingVocabulary.


        :return: The broader_term of this EditingVocabulary.
        :rtype: str
        """
        return self._broader_term

    @broader_term.setter
    def broader_term(self, broader_term: str):
        """Sets the broader_term of this EditingVocabulary.


        :param broader_term: The broader_term of this EditingVocabulary.
        :type broader_term: str
        """

        self._broader_term = broader_term

    @property
    def synonym(self) -> List[str]:
        """Gets the synonym of this EditingVocabulary.


        :return: The synonym of this EditingVocabulary.
        :rtype: List[str]
        """
        return self._synonym

    @synonym.setter
    def synonym(self, synonym: List[str]):
        """Sets the synonym of this EditingVocabulary.


        :param synonym: The synonym of this EditingVocabulary.
        :type synonym: List[str]
        """

        self._synonym = synonym

    @property
    def synonym_candidate(self) -> List[str]:
        """Gets the synonym_candidate of this EditingVocabulary.


        :return: The synonym_candidate of this EditingVocabulary.
        :rtype: List[str]
        """
        return self._synonym_candidate

    @synonym_candidate.setter
    def synonym_candidate(self, synonym_candidate: List[str]):
        """Sets the synonym_candidate of this EditingVocabulary.


        :param synonym_candidate: The synonym_candidate of this EditingVocabulary.
        :type synonym_candidate: List[str]
        """

        self._synonym_candidate = synonym_candidate

    @property
    def broader_term_candidate(self) -> List[str]:
        """Gets the broader_term_candidate of this EditingVocabulary.


        :return: The broader_term_candidate of this EditingVocabulary.
        :rtype: List[str]
        """
        return self._broader_term_candidate

    @broader_term_candidate.setter
    def broader_term_candidate(self, broader_term_candidate: List[str]):
        """Sets the broader_term_candidate of this EditingVocabulary.


        :param broader_term_candidate: The broader_term_candidate of this EditingVocabulary.
        :type broader_term_candidate: List[str]
        """

        self._broader_term_candidate = broader_term_candidate

    @property
    def part_of_speech(self) -> str:
        """Gets the part_of_speech of this EditingVocabulary.


        :return: The part_of_speech of this EditingVocabulary.
        :rtype: str
        """
        return self._part_of_speech

    @part_of_speech.setter
    def part_of_speech(self, part_of_speech: str):
        """Sets the part_of_speech of this EditingVocabulary.


        :param part_of_speech: The part_of_speech of this EditingVocabulary.
        :type part_of_speech: str
        """

        self._part_of_speech = part_of_speech

    @property
    def postion_x(self) -> str:
        """Gets the postion_x of this EditingVocabulary.


        :return: The postion_x of this EditingVocabulary.
        :rtype: str
        """
        return self._postion_x

    @postion_x.setter
    def postion_x(self, postion_x: str):
        """Sets the postion_x of this EditingVocabulary.


        :param postion_x: The postion_x of this EditingVocabulary.
        :type postion_x: str
        """

        self._postion_x = postion_x

    @property
    def postion_y(self) -> str:
        """Gets the postion_y of this EditingVocabulary.


        :return: The postion_y of this EditingVocabulary.
        :rtype: str
        """
        return self._postion_y

    @postion_y.setter
    def postion_y(self, postion_y: str):
        """Sets the postion_y of this EditingVocabulary.


        :param postion_y: The postion_y of this EditingVocabulary.
        :type postion_y: str
        """

        self._postion_y = postion_y

    @property
    def color1(self) -> str:
        """Gets the color1 of this EditingVocabulary.


        :return: The color1 of this EditingVocabulary.
        :rtype: str
        """
        return self._color1

    @color1.setter
    def color1(self, color1: str):
        """Sets the color1 of this EditingVocabulary.


        :param color1: The color1 of this EditingVocabulary.
        :type color1: str
        """

        self._color1 = color1

    @property
    def color2(self) -> str:
        """Gets the color2 of this EditingVocabulary.


        :return: The color2 of this EditingVocabulary.
        :rtype: str
        """
        return self._color2

    @color2.setter
    def color2(self, color2: str):
        """Sets the color2 of this EditingVocabulary.


        :param color2: The color2 of this EditingVocabulary.
        :type color2: str
        """

        self._color2 = color2