"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class RootMethods:
    """Funções chamadas diretamente em SapModel (sem sub-objeto)."""

    def __init__(self, raw):
        self._raw = raw

    def ApplicationExit(self, FileSave: bool):
        """If the model file is saved then it is saved with its current name. You should set the
        Sap2000 object variable to nothing after calling this function. This function
        returns zero if the function succeeds and nonzero if it fails.
    
        FileSave (input): If this item is True the existing model file is saved prior to
            closing Sap2000.
        """
        _r = self._raw.ApplicationExit(FileSave)
        return _r

    def ApplicationStart(self, Units: int = 3, Visible: bool = True, FileName: str = ''):
        """This function starts the Sap2000 application. When the model is not visible it does not
        appear on screen and it does not appear in the Windows task bar. If no filename is
        specified, you can later open a model or create a model through the API. The file
        name must have an .sdb, .$2k, .s2k, .xls, or .mdb extension. Files with .sdb
        extensions are opened as standard SAP2000 files. Files with .$2k and .s2k extensions
        are imported as text files. Files with .xls extensions are imported as Microsoft
        Excel files. Files with .mdb extensions are imported as Microsoft Access files. This
        function returns zero if the application successfully starts and nonzero if it
        fails.
    
        Units (input): The database units used when a new model is created. Data is
            internally stored in the program in the database units. The database units may
            be one of the following items in the eUnits enumeration: lb_in_F = 1 lb_ft_F = 2
            kip_in_F = 3 kip_ft_F = 4 kN_mm_C = 5 kN_m_C = 6 kgf_mm_C = 7 kgf_m_C = 8 N_mm_C
            = 9 N_m_C = 10 Ton_mm_C = 11 Ton_m_C = 12 kN_cm_C = 13 kgf_cm_C = 14 N_cm_C = 15
            Ton_cm_C = 16
        Visible (input): If this item is True then the application is visible when started.
            If it is False then the application is hidden when started.
        FileName (input): The full path of a model file to be opened when the Sap2000
            application is started. If no file name is specified, the application starts
            without loading an existing model.
        """
        _r = self._raw.ApplicationStart(Units, Visible, FileName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ApplicationStart falhou (ret={_r})".format(_r=_r))
        return None

    def GetKeyStringsExtendedEntityData(self, AppName: str, Key: str):
        """
    
        AppName (input): This is an application name of your choice under which your
            application previously stored some data. It is recommended you choose a unique
            name to guarantee no other third-party application resets the data that was set
            by your application. Application names are stored in their original
            capitalization and character set, but are compared in a case insensitive and
            culturally invariant manner for retrieval purposes.
        Key (input): This is an entry name under which the data provided in the remaining
            arguments was stored. Entry names are stored in their original capitalization
            and character set, but are compared in a case insensitive and culturally
            invariant manner for retrieval purposes.
        NumberValues (output): The number of strings stored for the given application name
            and entry name.
        Values (output): This is one-dimensional array of string values. The Values array is
            created as a dynamic, zero-based, array by the API user:
        """
        _r = self._raw.GetKeyStringsExtendedEntityData(AppName, Key, 0, "")
        *_outs, _ret = _r
        return (*_outs, _ret)

    def GetKeysWithStringsExtendedEntityData(self, AppName: str):
        """
    
        AppName (input): This is an application name of your choice under which your
            application previously stored some data. It is recommended you choose a unique
            name to guarantee no other third-party application resets the data that was set
            by your application. Application names are stored in their original
            capitalization and character set, but are compared in a case insensitive and
            culturally invariant manner for retrieval purposes.
        NumberKeys (output): The number of different entries for which data was previously
            stored under the application name AppName.
        """
        _r = self._raw.GetKeysWithStringsExtendedEntityData(AppName, 0, [])
        *_outs, _ret = _r
        return (*_outs, _ret)

    def SetStringsExtendedEntityData(self, AppName: str, Key: str, NumberValues: int, Values: str):
        """This function can be used to store metadata for a model, or any other data specific to your
        application.
    
        AppName (input): This is an application name of your choice under which your
            application previously stored some data. It is recommended you choose a unique
            name to guarantee no other third-party application resets the data that was set
            by your application. Application names are stored in their original
            capitalization and character set, but are compared in a case insensitive and
            culturally invariant manner for retrieval purposes.
        Key (input): This is an entry name under which the data provided in the remaining
            arguments was stored. This data can later be retrieved, reset, or deleted by
            providing a valid application name and entry name. Entry names are stored in
            their original capitalization and character set, but are compared in a case
            insensitive and culturally invariant manner for retrieval purposes.
        NumberValues (input): The number of strings to store for the given application name
            and entry name.
        Values (input): A one-dimensional array of strings containing NumberValues strings.
            These strings replace any strings previously stored for the given application
            name and entry name. Calling this function with NumberValues equal to zero is
            equivalent to erasing any previously stored data.
        """
        _r = self._raw.SetStringsExtendedEntityData(AppName, Key, NumberValues, Values)
        return _r

    def GetDatabaseUnits(self):
        """This function returns one of the following items from the eUnits enumeration indicating the
        database units for the model. All data is internally stored in the model in these
        units and converted to the present units as needed. lb_in_F = 1 lb_ft_F = 2 kip_in_F
        = 3 kip_ft_F = 4 kN_mm_C = 5 kN_m_C = 6 kgf_mm_C = 7 kgf_m_C = 8 N_mm_C = 9 N_m_C =
        10 Ton_mm_C = 11 Ton_m_C = 12 kN_cm_C = 13 kgf_cm_C = 14 N_cm_C = 15 Ton_cm_C = 16
        """
        _r = self._raw.GetDatabaseUnits()
        return _r

    def GetMergeTol(self):
        """This function retrieves the value of the program auto merge tolerance. The function returns
        zero if the tolerance is successfully retrieved; otherwise it returns a nonzero
        value.
    
        MergeTol (output): The program auto merge tolerance. [L]
        """
        _r = self._raw.GetMergeTol(0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GetMergeTol falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModelFilename(self, IncludePath: bool = True):
        """The function returns a string that represents the filename of the current model, with or
        without the full path.
    
        IncludePath (input): A boolean (True or False) value. When this item is True, the
            returned filename includes the full path where the file is located.
        """
        _r = self._raw.GetModelFilename(IncludePath)
        return _r

    def GetModelFilepath(self):
        """The function returns a string that represents the filepath of the current model.
        """
        _r = self._raw.GetModelFilepath()
        return _r

    def GetModelIsLocked(self):
        """The function returns True if the model is locked and False if it is unlocked. With some
        exceptions, definitions and assignments can not be changed in a model while the
        model is locked. If an attempt is made to change a definition or assignment while
        the model is locked and that change is not allowed in a locked model, an error will
        be returned.
        """
        _r = self._raw.GetModelIsLocked()
        return _r

    def GetPresentCoordSystem(self):
        """This function returns the name of the present coordinate system.
        """
        _r = self._raw.GetPresentCoordSystem()
        return _r

    def GetPresentUnits(self):
        """This function returns one of the following items from the eUnits enumeration indicating the
        units presently specified for the model: lb_in_F = 1 lb_ft_F = 2 kip_in_F = 3
        kip_ft_F = 4 kN_mm_C = 5 kN_m_C = 6 kgf_mm_C = 7 kgf_m_C = 8 N_mm_C = 9 N_m_C = 10
        Ton_mm_C = 11 Ton_m_C = 12 kN_cm_C = 13 kgf_cm_C = 14 N_cm_C = 15 Ton_cm_C = 16
        """
        _r = self._raw.GetPresentUnits()
        return _r

    def GetProjectInfo(self):
        """This function retrieves the project information data. The function returns zero if the data
        is successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of project info items returned.
        Item (output): This is an array that includes the name of the project information
            item.
        Data (output): This is an array that includes the data for the specified project
            information item.
        """
        _r = self._raw.GetProjectInfo(0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GetProjectInfo falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUserComment(self):
        """This function retrieves the data in the user comments and log. The function returns zero if
        the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Comment (output): The data in the user comments and log.
        """
        _r = self._raw.GetUserComment("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GetUserComment falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetVersion(self):
        """This function returns the SAP2000 program version. The function returns zero if the
        information is successfully retrieved; otherwise it returns a nonzero value.
    
        Version (output): The program version name that is externally displayed to the user.
        MyVersionNumber (output): The program version number that is used internally by the
            program and not displayed to the user.
        """
        _r = self._raw.GetVersion("", 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GetVersion falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def Hide(self):
        """This function hides the Sap2000 application. When the application is hidden it is not
        visible on the screen or on the Windows task bar. The function returns zero if the
        Sap2000 application is successfully hidden and nonzero if the function fails. If the
        application is already hidden calling this function returns an error.
        """
        _r = self._raw.Hide()
        if _r != 0:
            raise Sap2000ApiError("SapModel.Hide falhou (ret={_r})".format(_r=_r))
        return None

    def InitializeNewModel(self, Units: int = 3):
        """This function clears the previous model and initializes the program for a new model. If it
        is later needed, you should save your previous model prior to calling this function.
        After calling the InitializeNewModel function, it is not necessary to also call the
        ApplicationStart function because the functionality of the ApplicationStart function
        is included in the InitializeNewModel function. The function returns zero if a new
        model is successfully initialized, otherwise it returns a nonzero value.
    
        Units (input): This is the database units for the new model. All data is internally
            stored in the model in these units. The units are one of the following items in
            the eUnits enumeration: lb_in_F = 1 lb_ft_F = 2 kip_in_F = 3 kip_ft_F = 4
            kN_mm_C = 5 kN_m_C = 6 kgf_mm_C = 7 kgf_m_C = 8 N_mm_C = 9 N_m_C = 10 Ton_mm_C =
            11 Ton_m_C = 12 kN_cm_C = 13 kgf_cm_C = 14 N_cm_C = 15 Ton_cm_C = 16
        """
        _r = self._raw.InitializeNewModel(Units)
        if _r != 0:
            raise Sap2000ApiError("SapModel.InitializeNewModel falhou (ret={_r})".format(_r=_r))
        return None

    def SetAsActiveObject(self):
        """This function sets the active instance of a SapObject in the system Running Object Table
        (ROT), replacing the previous instance(s). When a new SapObject is created using the
        OAPI, it is automatically added to the system ROT if none is already present.
        Subsequent instances of the SapObject do not alter the ROT as long as at least one
        active instance of a SapObject is present in the ROT. The Windows API call
        GetObject() can be used to attach to the active SapObject instance registered in the
        ROT. This function returns zero if the current instance is successfully added to the
        system ROT and nonzero if it fails.
        """
        _r = self._raw.SetAsActiveObject()
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetAsActiveObject falhou (ret={_r})".format(_r=_r))
        return None

    def SetMergeTol(self, MergeTol: float):
        """This function sets the program auto merge tolerance. The function returns zero if the
        tolerance is successfully set; otherwise it returns a nonzero value.
    
        MergeTol (input): The program auto merge tolerance. [L]
        """
        _r = self._raw.SetMergeTol(MergeTol)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetMergeTol falhou (ret={_r})".format(_r=_r))
        return None

    def SetModelIsLocked(self, LockIt: bool):
        """The function returns zero if the locked status of the model is successfully set. Otherwise
        it returns a nonzero value. With some exceptions, definitions and assignments can
        not be changed in a model while the model is locked. If an attempt is made to change
        a definition or assignment while the model is locked and that change is not allowed
        in a locked model, an error will be returned.
    
        LockIt (input): The item is True if the model is to be locked and False if it is to
            be unlocked.
        """
        _r = self._raw.SetModelIsLocked(LockIt)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetModelIsLocked falhou (ret={_r})".format(_r=_r))
        return None

    def SetPresentCoordSystem(self, CSys: str):
        """This function sets the present coordinate system. The function returns zero if the present
        coordinate system is successfully set. Otherwise it returns a nonzero value.
    
        CSys (input): The name of a defined coordinate system.
        """
        _r = self._raw.SetPresentCoordSystem(CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetPresentCoordSystem falhou (ret={_r})".format(_r=_r))
        return None

    def SetPresentUnits(self, Units: int):
        """This function returns zero if the units are successfully set and nonzero if they are not
        set.
    
        Units (input): One of the following items in the eUnits enumeration: lb_in_F = 1
            lb_ft_F = 2 kip_in_F = 3 kip_ft_F = 4 kN_mm_C = 5 kN_m_C = 6 kgf_mm_C = 7
            kgf_m_C = 8 N_mm_C = 9 N_m_C = 10 Ton_mm_C = 11 Ton_m_C = 12 kN_cm_C = 13
            kgf_cm_C = 14 N_cm_C = 15 Ton_cm_C = 16
        """
        _r = self._raw.SetPresentUnits(Units)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetPresentUnits falhou (ret={_r})".format(_r=_r))
        return None

    def SetProjectInfo(self, Item: str, Data: str):
        """This function sets the data for an item in the project information. The function returns
        zero if the data is successfully set; otherwise it returns a nonzero value.
    
        Item (input): The name of the project information item to be set.
        Data (input): The data for the specified project information item.
        """
        _r = self._raw.SetProjectInfo(Item, Data)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetProjectInfo falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserComment(self, Comment: str, NumLines: int = 1, Replace: bool = False):
        """This function sets the user comments and log data. The function returns zero if the data is
        successfully set; otherwise it returns a nonzero value.
    
        Comment (input): The data to be added to the user comments and log.
        NumLines (input): The number of carriage return and line feeds to be included before
            the specified comment. This item is ignored if Replace = True. It is also
            ignored if there are no existing comments.
        Replace (input): If this item is True, all existing comments are replaced with the
            specified comment.
        """
        _r = self._raw.SetUserComment(Comment, NumLines, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SetUserComment falhou (ret={_r})".format(_r=_r))
        return None

    def Unhide(self):
        """This function unhides the Sap2000 application, that is, it makes it visible. When the
        application is hidden, it is not visible on the screen or on the Windows task bar.
        The function returns zero if the Sap2000 application is successfully unhidden (set
        visible) and nonzero if the function fails. If the application is already visible
        (not hidden) calling this function returns an error.
        """
        _r = self._raw.Unhide()
        if _r != 0:
            raise Sap2000ApiError("SapModel.Unhide falhou (ret={_r})".format(_r=_r))
        return None

    def UnsetAsActiveObject(self):
        """This function removes the current instance of a SapObject from the system Running Object
        Table (ROT). This function returns zero if the current instance is successfully
        removed from the system ROT and nonzero if it fails or if the current instance is
        not in the system ROT.
        """
        _r = self._raw.UnsetAsActiveObject()
        if _r != 0:
            raise Sap2000ApiError("SapModel.UnsetAsActiveObject falhou (ret={_r})".format(_r=_r))
        return None

    def Visible(self):
        """The function returns True if the Sap2000 application is visible on the screen, otherwise it
        returns False.
        """
        _r = self._raw.Visible()
        return _r

