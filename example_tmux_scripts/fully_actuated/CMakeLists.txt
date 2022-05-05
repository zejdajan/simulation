cmake_minimum_required(VERSION 3.1.5)
project(hector_mapping)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  nav_msgs
  visualization_msgs
  tf
  message_filters
  laser_geometry
  tf_conversions
  message_generation
  nodelet
  )

find_package(Boost REQUIRED COMPONENTS thread)

find_package(Eigen3 REQUIRED)
set(Eigen_INCLUDE_DIRS ${EIGEN3_INCLUDE_DIRS})
set(Eigen_LIBRARIES ${Eigen_LIBRARIES})

add_message_files(FILES
  HectorDebugInfo.msg
  HectorIterData.msg
  )

## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES
  std_msgs
  nav_msgs
  )

set(LIBRARIES
  HectorMappingRos
  )

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${LIBRARIES}
  CATKIN_DEPENDS roscpp nav_msgs visualization_msgs tf message_filters laser_geometry tf_conversions message_runtime nodelet message_generation
  DEPENDS Eigen
  )

include_directories(HectorMappingRos
  include
  ${Boost_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  ${Eigen_INCLUDE_DIRS}
  )

add_library(HectorMappingRos
  src/HectorDebugInfoProvider.h
  src/HectorDrawings.h
  src/HectorMappingRos.h
  src/HectorMappingRos.cpp
  src/PoseInfoContainer.cpp
  src/PoseInfoContainer.h
  )

add_dependencies(HectorMappingRos
  hector_mapping_generate_messages_cpp
)

target_link_libraries(HectorMappingRos
  ${catkin_LIBRARIES}
  ${Boost_LIBRARIES}
  ${Eigen_LIBRARIES}
  )

## --------------------------------------------------------------
## |                           Install                          |
## --------------------------------------------------------------

install(TARGETS ${LIBRARIES}
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
  )

install(DIRECTORY launch msg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )

install(DIRECTORY ./
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  FILES_MATCHING PATTERN "*.xml"
  )
