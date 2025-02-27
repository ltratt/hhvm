#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
import typing as _typing

import folly.iobuf as _fbthrift_iobuf
import thrift.py3.builder


import test.fixtures.basic.module.types as _test_fixtures_basic_module_types


_fbthrift_struct_type__MyStruct = _test_fixtures_basic_module_types.MyStruct
class MyStruct_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__MyStruct

    def __init__(self):
        self.MyIntField: _typing.Optional[int] = None
        self.MyStringField: _typing.Optional[str] = None
        self.MyDataField: _typing.Any = None
        self.myEnum: _typing.Optional[_test_fixtures_basic_module_types.MyEnum] = None
        self.oneway: _typing.Optional[bool] = None
        self.readonly: _typing.Optional[bool] = None
        self.idempotent: _typing.Optional[bool] = None
        self.floatSet: _typing.Optional[set] = None
        self.no_hack_codegen_field: _typing.Optional[str] = None

    def __iter__(self):
        yield "MyIntField", self.MyIntField
        yield "MyStringField", self.MyStringField
        yield "MyDataField", self.MyDataField
        yield "myEnum", self.myEnum
        yield "oneway", self.oneway
        yield "readonly", self.readonly
        yield "idempotent", self.idempotent
        yield "floatSet", self.floatSet
        yield "no_hack_codegen_field", self.no_hack_codegen_field

_fbthrift_struct_type__MyDataItem = _test_fixtures_basic_module_types.MyDataItem
class MyDataItem_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__MyDataItem

    def __init__(self):
        pass

    def __iter__(self):
        pass

_fbthrift_struct_type__MyUnion = _test_fixtures_basic_module_types.MyUnion
class MyUnion_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__MyUnion

    def __init__(self):
        self.myEnum: _typing.Optional[_test_fixtures_basic_module_types.MyEnum] = None
        self.myStruct: _typing.Any = None
        self.myDataItem: _typing.Any = None
        self.floatSet: _typing.Optional[set] = None

    def __iter__(self):
        yield "myEnum", self.myEnum
        yield "myStruct", self.myStruct
        yield "myDataItem", self.myDataItem
        yield "floatSet", self.floatSet

_fbthrift_struct_type__ReservedKeyword = _test_fixtures_basic_module_types.ReservedKeyword
class ReservedKeyword_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__ReservedKeyword

    def __init__(self):
        self.reserved_field: _typing.Optional[int] = None

    def __iter__(self):
        yield "reserved_field", self.reserved_field

_fbthrift_struct_type__UnionToBeRenamed = _test_fixtures_basic_module_types.UnionToBeRenamed
class UnionToBeRenamed_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__UnionToBeRenamed

    def __init__(self):
        self.reserved_field: _typing.Optional[int] = None

    def __iter__(self):
        yield "reserved_field", self.reserved_field

