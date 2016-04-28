3D Viewer
=========

Controls
--------

Mouse and keyboard operation method depends on the control selected
in the export settings. There is list of mouse buttons and keys
in the about box. Press ``I`` key to show the box.

Identifying Features
--------------------

When you click on an object, layer name that the feature (object)
belongs to and the clicked coordinates (in order of x, y, z) are shown.
If ``Latitude and longitude (WGS84)`` option (in the
``Display of coordinates`` group of World page) is selected, longitude and
latitude are shown in DMS format (degrees, minutes and seconds). If
``Export attributes`` option of each vector layer is selected, attribute
list of the clicked feature follows them.

Controls Box
------------

This feature is available with **3DViewer(dat-gui) template**.

The controls box has:

* layer sub menus

   Each sub menu has:

   * a check box to toggle layer visibility
   * a slider to adjust layer transparency

* sub menu to control a vertically movable plane
* help button to show the about box

Rotate Animation
----------------

This feature is available with **OrbitControls**.

Pressing ``R`` key starts/stops rotate animation. Camera rotates around
the camera target clockwise.

Save Image
----------

Press ``Shift + S`` to show save image dialog, then enter image size and
click the OK button. In addition, with some web browsers, you need to
click a link to save image. The image file format is PNG. To change label
color and/or adjust label size, edit ``Qgis2threejs.css`` (``print-label`` class).

.. note:: A known issue: Wrong image output if the size is too large (`issue #42`__)

__ https://github.com/minorua/Qgis2threejs/issues/42


URL Parameters
--------------

You can get current view URL in the about box, and later restore the
view by entering the URL in the URL box of web browser.

Parameters used in view URL:

* cx, cy, cz: camera position
* tx, ty, tz: camera target
* ux, uy, uz: camera up direction (TrackballControls)

e.g.
file:///D:/example.html#cx=-64.8428840144039&cy=-40.75234765087484&cz=24.603200058346065

Other parameters:

* width: canvas width (pixels)
* height: canvas height (pixels)
* popup: pop up another window with specified width and height

.. raw:: html

   <!-- TODO: images -->


