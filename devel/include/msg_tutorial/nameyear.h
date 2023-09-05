// Generated by gencpp from file msg_tutorial/nameyear.msg
// DO NOT EDIT!


#ifndef MSG_TUTORIAL_MESSAGE_NAMEYEAR_H
#define MSG_TUTORIAL_MESSAGE_NAMEYEAR_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace msg_tutorial
{
template <class ContainerAllocator>
struct nameyear_
{
  typedef nameyear_<ContainerAllocator> Type;

  nameyear_()
    : name()
    , year(0)  {
    }
  nameyear_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , year(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef int16_t _year_type;
  _year_type year;





  typedef boost::shared_ptr< ::msg_tutorial::nameyear_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::msg_tutorial::nameyear_<ContainerAllocator> const> ConstPtr;

}; // struct nameyear_

typedef ::msg_tutorial::nameyear_<std::allocator<void> > nameyear;

typedef boost::shared_ptr< ::msg_tutorial::nameyear > nameyearPtr;
typedef boost::shared_ptr< ::msg_tutorial::nameyear const> nameyearConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::msg_tutorial::nameyear_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::msg_tutorial::nameyear_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::msg_tutorial::nameyear_<ContainerAllocator1> & lhs, const ::msg_tutorial::nameyear_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.year == rhs.year;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::msg_tutorial::nameyear_<ContainerAllocator1> & lhs, const ::msg_tutorial::nameyear_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace msg_tutorial

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::msg_tutorial::nameyear_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::msg_tutorial::nameyear_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_tutorial::nameyear_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_tutorial::nameyear_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_tutorial::nameyear_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_tutorial::nameyear_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::msg_tutorial::nameyear_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a9d7ce781d868659bc667665f71834f8";
  }

  static const char* value(const ::msg_tutorial::nameyear_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa9d7ce781d868659ULL;
  static const uint64_t static_value2 = 0xbc667665f71834f8ULL;
};

template<class ContainerAllocator>
struct DataType< ::msg_tutorial::nameyear_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msg_tutorial/nameyear";
  }

  static const char* value(const ::msg_tutorial::nameyear_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::msg_tutorial::nameyear_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n"
"int16 year\n"
;
  }

  static const char* value(const ::msg_tutorial::nameyear_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::msg_tutorial::nameyear_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.year);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct nameyear_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::msg_tutorial::nameyear_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::msg_tutorial::nameyear_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "year: ";
    Printer<int16_t>::stream(s, indent + "  ", v.year);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MSG_TUTORIAL_MESSAGE_NAMEYEAR_H
