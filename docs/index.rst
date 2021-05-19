Skolemizer library
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

A library with utils for performing Skolemization on blank nodes (RDF)


Installation
------------

To install the skolemizer package,
run this command in your terminal:

.. code-block:: console

   $ pip install skolemizer


Usage
-----

This package can be used like this:

.. code-block::

  from datacatalogtordf import Catalog
  from skolemizer import Service

  # Create catalog object
  catalog = Catalog()
  catalog.identifier = "http://example.com/catalogs/1"
  catalog.title = {"en": "A service catalog"}
  catalog.publisher = "https://example.com/publishers/1"

  # Create a service:
  service = Service()
  service.identifier = "http://example.com/services/1"
  service.title = {"nb": "inntektsAPI", "en": "incomeAPI"}
  #
  # Add service to catalog:
  catalog.services.append(service)

  # Get rdf representation in turtle (default)
  rdf = catalog.to_rdf()
  print(rdf.decode())
