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

  from skolemizer import Skolemizer

  # Adding skolemization to a graph node

    if not getattr(self, "identifier", None):
        self.identifier = Skolemizer.add_skolemization()
