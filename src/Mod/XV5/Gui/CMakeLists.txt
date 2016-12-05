
include_directories(
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${COIN3D_INCLUDE_DIRS}
    ${QT_INCLUDE_DIR}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
)

set(XV5Gui_LIBS
    XV5
    FreeCADGui
)

qt4_add_resources(XV5_QRC_SRCS Resources/XV5.qrc)

SET(XV5Gui_SRCS
    ${XV5_QRC_SRCS}
    AppXV5Gui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(XV5Gui SHARED ${XV5Gui_SRCS})
target_link_libraries(XV5Gui ${XV5Gui_LIBS})

fc_target_copy_resource(XV5Gui 
    ${CMAKE_SOURCE_DIR}/src/Mod/XV5
    ${CMAKE_BINARY_DIR}/Mod/XV5
    InitGui.py)

SET_BIN_DIR(XV5Gui XV5Gui /Mod/XV5)
SET_PYTHON_PREFIX_SUFFIX(XV5Gui)
    
install(TARGETS XV5Gui DESTINATION ${CMAKE_INSTALL_LIBDIR})
