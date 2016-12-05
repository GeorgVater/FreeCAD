
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(XV5_LIBS
    FreeCADApp
)

SET(XV5_SRCS
    AppXV5.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(XV5 SHARED ${XV5_SRCS})
target_link_libraries(XV5 ${XV5_LIBS})


fc_target_copy_resource(XV5 
    ${CMAKE_SOURCE_DIR}/src/Mod/XV5
    ${CMAKE_BINARY_DIR}/Mod/XV5
    Init.py)

SET_BIN_DIR(XV5 XV5 /Mod/XV5)
SET_PYTHON_PREFIX_SUFFIX(XV5)

install(TARGETS XV5 DESTINATION ${CMAKE_INSTALL_LIBDIR})
