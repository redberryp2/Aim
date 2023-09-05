# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plnctrl/fussInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import plnctrl.msg

class fussInfo(genpy.Message):
  _md5sum = "80f20e09e9bf88e655f5e38cccf2953f"
  _type = "plnctrl/fussInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint16       objNum
fusInfo[]   data

================================================================================
MSG: plnctrl/fusInfo
int32           classes
float32         posX
float32         posY
float32         posZ
float32         size
float32         distance
"""
  __slots__ = ['objNum','data']
  _slot_types = ['uint16','plnctrl/fusInfo[]']

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
      super(fussInfo, self).__init__(*args, **kwds)
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
      buff.write(_get_struct_H().pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_i5f().pack(_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance))
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
      end += 2
      (self.objNum,) = _get_struct_H().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = plnctrl.msg.fusInfo()
        _x = val1
        start = end
        end += 24
        (_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance,) = _get_struct_i5f().unpack(str[start:end])
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
      buff.write(_get_struct_H().pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_i5f().pack(_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance))
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
      end += 2
      (self.objNum,) = _get_struct_H().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = plnctrl.msg.fusInfo()
        _x = val1
        start = end
        end += 24
        (_x.classes, _x.posX, _x.posY, _x.posZ, _x.size, _x.distance,) = _get_struct_i5f().unpack(str[start:end])
        self.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_H = None
def _get_struct_H():
    global _struct_H
    if _struct_H is None:
        _struct_H = struct.Struct("<H")
    return _struct_H
_struct_i5f = None
def _get_struct_i5f():
    global _struct_i5f
    if _struct_i5f is None:
        _struct_i5f = struct.Struct("<i5f")
    return _struct_i5f