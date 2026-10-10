"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_File:
    """Wrapper para SapModel.File."""

    def __init__(self, raw):
        self._raw = raw

    def New2DFrame(self, TempType: int, NumberStorys: int, StoryHeight: float, NumberBays: int, BayWidth: float, Restraint: bool = True, Beam: str = 'Default', Column: str = 'Default', Brace: str = 'Default'):
        """Do not use this function to add to an existing model. This function should be used only for
        creating a new model and typically would be preceded by calls to ApplicationStart or
        InitializeNewModel. The function returns zero if the new 2D frame model is
        successfully created, otherwise it returns a nonzero value.
    
        TempType (input): One of the following 2D frame template types in the e2DFrameType
            enumeration. PortalFrame = 0 ConcentricBraced = 1 EccentricBraced = 2
        NumberStorys (input): The number of stories in the frame.
        StoryHeight (input): The height of each story. [L]
        NumberBays (input): The number of bays in the frame.
        BayWidth (input): The width of each bay. [L]
        Restraint (input): Joint restraints are provided at the base of the frame when this
            item is True.
        Beam (input): The frame section property used for all beams in the frame. This must
            either be Default or the name of a defined frame section property.
        Column (input): The frame section property used for all columns in the frame. This
            must either be Default or the name of a defined frame section property.
        Brace (input): The frame section property used for all braces in the frame. This
            must either be Default or the name of a defined frame section property. This
            item does not apply to the portal frame.
        """
        _r = self._raw.New2DFrame(TempType, NumberStorys, StoryHeight, NumberBays, BayWidth, Restraint, Beam, Column, Brace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.New2DFrame falhou (ret={_r})".format(_r=_r))
        return None

    def New3DFrame(self, TempType: int, NumberStorys: int, StoryHeight: float, NumberBaysX: int, BayWidthX: float, NumberBaysY: int, BayWidthY: float, Restraint: bool = True, Beam: str = 'Default', Column: str = 'Default', Area: str = 'Default', NumberXDivisions: int = 4, NumberYDivisions: int = 4):
        """Do not use this function to add to an existing model. This function should be used only for
        creating a new model and typically would be preceded by calls to ApplicationStart or
        InitializeNewModel. The function returns zero if the new 3D frame model is
        successfully created, otherwise it returns a nonzero value.
    
        TempType (input): One of the following 3D frame template types in the e3DFrameType
            enumeration. OpenFrame = 0 PerimeterFrame = 1 BeamSlab = 2 FlatPlate = 3
        NumberStorys (input): The number of stories in the frame.
        StoryHeight (input): The height of each story. [L]
        NumberBaysX (input): The number of bays in the global X direction of the frame.
        BayWidthX (input): The width of each bay in the global X direction of the frame. [L]
        NumberBaysY (input): The number of bays in the global Y direction of the frame.
        BayWidthY (input): The width of each bay in the global Y direction of the frame. [L]
        Restraint (input): Joint restraints are provided at the base of the frame when this
            item is True.
        Beam (input): The frame section property used for all beams in the frame. This must
            either be Default or the name of a defined frame section property.
        Column (input): The frame section property used for all columns in the frame. This
            must either be Default or the name of a defined frame section property.
        Area (input): The shell section property used for all floor slabs in the frame. This
            must either be Default or the name of a defined shell section property. This
            item does not apply to the open and perimeter frames.
        NumberXDivisions (input): The number of divisions for each floor area object in the
            global X direction. This item does not apply to the open and perimeter frames.
        NumberYDivisions (input): The number of divisions for each floor area object in the
            global Y direction. This item does not apply to the open and perimeter frames.
        """
        _r = self._raw.New3DFrame(TempType, NumberStorys, StoryHeight, NumberBaysX, BayWidthX, NumberBaysY, BayWidthY, Restraint, Beam, Column, Area, NumberXDivisions, NumberYDivisions)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.New3DFrame falhou (ret={_r})".format(_r=_r))
        return None

    def NewBeam(self, NumberSpans: int, SpanLength: float, Restraint: bool, Beam: str = 'Default'):
        """Do not use this function to add to an existing model. This function should be used only for
        creating a new model and typically would be preceded by calls to ApplicationStart or
        InitializeNewModel. The function returns zero if the new beam model is successfully
        created, otherwise it returns a nonzero value.
    
        NumberSpans (input): The number of spans for the beam.
        SpanLength (input): The length of each span. [L]
        Restraint (input): Joint restraints are provided at the ends of each span when this
            item is True.
        Beam (input): The frame section property used for the beam. This must either be
            Default or the name of a defined frame section property.
        """
        _r = self._raw.NewBeam(NumberSpans, SpanLength, Restraint, Beam)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.NewBeam falhou (ret={_r})".format(_r=_r))
        return None

    def NewBlank(self):
        """Do not use this function to add to an existing model. This function should be used only for
        creating a new model and typically would be preceded by calls to ApplicationStart or
        InitializeNewModel. The function returns zero if the new blank model is successfully
        created, otherwise it returns a nonzero value.
        """
        _r = self._raw.NewBlank()
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.NewBlank falhou (ret={_r})".format(_r=_r))
        return None

    def NewSolidBlock(self, XWidth: float, YWidth: float, Height: float, Restraint: bool = True, Solid: str = 'Default', NumberXDivisions: int = 5, NumberYDivisions: int = 8, NumberZDivisions: int = 10):
        """The function returns zero if the new solid block model is successfully created, otherwise it
        returns a nonzero value.
    
        XWidth (input): The total width of the solid block measured in the global X
            direction. [L]
        YWidth (input): The total width of the solid block measured in the global Y
            direction. [L]
        Height (input): The total height of the solid block measured in the global Z
            direction. [L]
        Restraint (input): Joint restraints are provided at the base of the solid block when
            this item is True.
        Solid (input): The solid property used for the solid block. This must either be
            Default or the name of a defined solid property.
        NumberXDivisions (input): The number of solid objects in the global X direction of
            the block.
        NumberYDivisions (input): The number of solid objects in the global Y direction of
            the block.
        NumberZDivisions (input): The number of solid objects in the global Z direction of
            the block.
        """
        _r = self._raw.NewSolidBlock(XWidth, YWidth, Height, Restraint, Solid, NumberXDivisions, NumberYDivisions, NumberZDivisions)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.NewSolidBlock falhou (ret={_r})".format(_r=_r))
        return None

    def NewWall(self, NumberXDivisions: int, DivisionWidthX: float, NumberZDivisions: int, DivisionWidthZ: float, Restraint: bool = True, Area: str = 'Default'):
        """Do not use this function to add to an existing model. This function should be used only for
        creating a new model and typically would be preceded by calls to ApplicationStart or
        InitializeNewModel. The function returns zero if the new wall model is successfully
        created, otherwise it returns a nonzero value.
    
        NumberXDivisions (input): The number of area objects in the global X direction of
            the wall.
        DivisionWidthX (input): The width of each area object measured in the global X
            direction. [L]
        NumberZDivisions (input): The number of area objects in the global Z direction of
            the wall.
        DivisionWidthZ (input): The height of each area object measured in the global Z
            direction. [L]
        Restraint (input): Joint restraints are provided at the base of the wall when this
            item is True.
        Area (input): The shell section property used for the wall. This must either be
            Default or the name of a defined shell section property.
        """
        _r = self._raw.NewWall(NumberXDivisions, DivisionWidthX, NumberZDivisions, DivisionWidthZ, Restraint, Area)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.NewWall falhou (ret={_r})".format(_r=_r))
        return None

    def OpenFile(self, FileName: str):
        """This function opens an existing Sap2000 file. The file name must have an sdb, $2k, s2k,
        xlsx, xls, or mdb extension. Files with sdb extensions are opened as standard
        Sap2000 files. Files with $2k and s2k extensions are imported as text files. Files
        with xlsx and xls extensions are imported as Microsoft Excel files. Files with mdb
        extensions are imported as Microsoft Access files. This function returns zero if the
        file is successfully opened and nonzero if it is not opened. The function is only
        applicable when you are accessing the Sap2000 API from an external application. It
        will return an error if you call it from VBA inside Sap2000.
    
        FileName (input): The full path of a model file to be opened in the Sap2000
            application.
        """
        _r = self._raw.OpenFile(FileName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.OpenFile falhou (ret={_r})".format(_r=_r))
        return None

    def Save(self, FileName: str = ''):
        """If a file name is specified, it should have an .sdb extension. If no file name is specified,
        the file is saved using its current name. If there is no current name for the file
        (the file has not been saved previously) and this function is called with no file
        name specified, an error will be returned. This function returns zero if the file is
        successfully saved and nonzero if it is not saved.
    
        FileName (input): The full path to which the model file is saved.
        """
        _r = self._raw.Save(FileName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.File.Save falhou (ret={_r})".format(_r=_r))
        return None


