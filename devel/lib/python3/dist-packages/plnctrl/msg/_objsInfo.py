# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plnctrl/objsInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import plnctrl.msg

class objsInfo(genpy.Message):
  _md5sum = "519e5ac559f94c92999b0c7095c3df57"
  _type = "plnctrl/objsInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32       objNum
objInfo[]   data

================================================================================
MSG: plnctrl/objInfo
int16           classes
float32         posX
float32         posY
float32         posZ
float32         size
float32         distance
"""
  __slots__ = ['objNum','data']
  _slot_types = ['int32','plnctrl/objInfo[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       objNum,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(objsInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.objNum is None:
        self.objNum = 0
      if self.data is None:
        self.data = []
    else:
      self.objNum = 0
      self.data = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.objNum
      buff.write(_get_struct_i().pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_h5f().pack(_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.data is None:
        self.data = None
      end = 0
      start = end
      end += 4
      (self.objNum,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = plnctrl.msg.objInfo()
        _x = val1
        start = end
        end += 22
        (_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance,) = _get_struct_h5f().unpack(str[start:end])
        self.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.objNum
      buff.write(_get_struct_i().pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_h5f().pack(_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.data is None:
        self.data = None
      end = 0
      start = end
      end += 4
      (self.objNum,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = plnctrl.msg.objInfo()
        _x = val1
        start = end
        end += 22
        (_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance,) = _get_struct_h5f().unpack(str[start:end])
        self.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h5f = None
def _get_struct_h5f():
    global _struct_h5f
    if _struct_h5f is None:
        _struct_h5f = struct.Struct("<h5f")
    return _struct_h5f
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i