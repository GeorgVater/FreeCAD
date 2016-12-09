#add_defintions(-D_FC_GUI_ENABLED_)
#add_defintions(-DXV5MAINPY)

if(BUILD_GUI)
    include_directories(
        ${Boost_INCLUDE_DIRS}
        ${COIN3D_INCLUDE_DIRS}
        ${ZLIB_INCLUDE_DIR}
        ${QT_INCLUDE_DIR}
        ${PYTHON_INCLUDE_DIRS}
        ${XercesC_INCLUDE_DIRS}
    )
else(BUILD_GUI)
    include_directories(
        ${Boost_INCLUDE_DIRS}
        ${ZLIB_INCLUDE_DIR}
        ${QT_INCLUDE_DIR}
        ${PYTHON_INCLUDE_DIRS}
        ${XercesC_INCLUDE_DIRS}
    )
endif(BUILD_GUI)

######################## XV5Main ########################
if(BUILD_GUI)

    SET(XV5_SRCS
        XV5.rc
        icon.ico
        MainGui.cpp
    )

    if(MSVC)
        SET(XV5_LIBS
            XV5Gui
            ${QT_QTMAIN_LIBRARY}
        )
    else(MSVC)
        SET(XV5_LIBS
            XV5Gui
        )
    endif(MSVC)

    add_executable(XV5Main WIN32 ${XV5_SRCS})
    target_link_libraries(XV5Main ${XV5_LIBS})

    SET_BIN_DIR(XV5Main XV5)

    if(WIN32)
        INSTALL(TARGETS XV5Main
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    else(WIN32)
        INSTALL(TARGETS XV5Main 
            RUNTIME DESTINATION bin
        )
    endif(WIN32)
endif(BUILD_GUI)
######################## XV5MainCmd ########################

SET(XV5MainCmd_SRCS
    MainCmd.cpp
)
add_executable(XV5MainCmd ${XV5MainCmd_SRCS})

target_link_libraries(XV5MainCmd 
    XV5App
    ${QT_QTCORE_LIBRARY}
    ${QT_QTXML_LIBRARY}
)

SET_BIN_DIR(XV5MainCmd XV5Cmd)

if(WIN32)
    INSTALL(TARGETS XV5MainCmd
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
else(WIN32)
    INSTALL(TARGETS XV5MainCmd 
        RUNTIME DESTINATION bin
    )
endif(WIN32)

######################## XV5MainPy ########################

SET(XV5MainPy_SRCS
    MainPy.cpp
)

add_library(XV5MainPy SHARED ${XV5MainPy_SRCS})

target_link_libraries(XV5MainPy XV5App)

SET_BIN_DIR(XV5MainPy XV5)
SET_PYTHON_PREFIX_SUFFIX(XV5MainPy)

if(WIN32)
    INSTALL(TARGETS XV5MainPy
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
else(WIN32)
    INSTALL(TARGETS XV5MainPy
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
endif(WIN32)

######################## XV5GuiPy ########################
if(BUILD_GUI)

    SET(XV5GuiPy_SRCS
        XV5GuiPy.cpp
    )

    add_library(XV5GuiPy SHARED ${XV5GuiPy_SRCS})

    target_link_libraries(XV5GuiPy XV5Gui)

    SET_BIN_DIR(XV5GuiPy XV5Gui)
    SET_PYTHON_PREFIX_SUFFIX(XV5GuiPy)
    if(WIN32)
        # Name clash with target "XV5Gui"
        # Must be called "XV5GuiPy_d" and "XV5GuiPy" to work so override default
        set_target_properties(XV5GuiPy PROPERTIES PDB_NAME_DEBUG "XV5GuiPy_d")
        set_target_properties(XV5GuiPy PROPERTIES PDB_NAME_RELEASE "XV5GuiPy")
    endif(WIN32)
    
    if(WIN32)
        INSTALL(TARGETS XV5GuiPy
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    else(WIN32)
        INSTALL(TARGETS XV5GuiPy
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    endif(WIN32)
endif(BUILD_GUI)
