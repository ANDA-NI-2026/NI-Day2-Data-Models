# NI Day 2: Data Models: From Arrays to Standardized Electrophysiology Data with Neo

## Staff

 - **Lead Trainer**:
   - Michael Denker, Forchungszentrum Jülich, Germany
 - **Lecturers**: 
   - Michael Denker, Forchungszentrum Jülich, Germany
 - **Teaching Assistants**: 
    - Ole Bialas, Uni Bonn, Germany
    - Cristiano Köhler, Forchungszentrum Jülich, Germany
    - Tobias Michels, Forchungszentrum Jülich, Germany
    - Julio Rodino, Forchungszentrum Jülich, Germany
    - Junji Ito, Forchungszentrum Jülich, Germany
    - Nicholas Del Grosso, Uni Bonn, Germany

## Session Overview

Neuroscience data comes from many instruments and file formats, but almost all of it ends up as numerical arrays that need names, units, and structure to be analysed and shared. This unit builds from the raw array up to standardized, metadata-rich data objects, giving you a way to represent and work with electrophysiology data regardless of where it came from.

In the homework, you will work with the two foundational array libraries. NumPy provides the n-dimensional array and the vectorised operations that work on it: you will create arrays in different ways, slice rows, columns, and elements, and perform mathematical operations along chosen axes. Xarray then builds on NumPy by attaching names, coordinates, and metadata to each axis, so that you can refer to dimensions and indices by meaning rather than by position.

The first in-person session introduces Neo, a Python library for representing neurophysiological data from heterogeneous sources in a common data representation. You will start with the `quantities` library to attach physical units to your data and handle unit conversions safely, then learn the core Neo data objects — `AnalogSignal`, `SpikeTrain`, `Event`, and `Epoch` — that capture the different kinds of signals and annotations in a recording.

The next session moves from individual data objects to complete datasets. You will organise `AnalogSignal`, `SpikeTrain`, `Event`, and `Epoch` objects into Neo's `Block` and `Segment` containers to build a trial-based dataset like one you would load from disk. You will then explore the contents of a dataset, select subsets using metadata, cut a recording into per-trial segments with Neo's utility functions, and transform and visualise a signal.