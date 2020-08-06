cmake_minimum_required(VERSION 3.17)

project(CastXMLPythonDistributions)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR})

# Options
set(ARCHIVE_DOWNLOAD_DIR "${CMAKE_BINARY_DIR}" CACHE PATH "Directory where to download archives")

include(CastXMLUrls)

#-----------------------------------------------------------------------------
# Which archives ?
#-----------------------------------------------------------------------------
function(check_archive_var archive_var)
  if(NOT DEFINED "${archive_var}_url")
    message(FATAL_ERROR "Failed to determine which archive to download: '${archive_var}_url' variable is not defined")
  endif()
  if(NOT DEFINED "${archive_var}_sha512")
    message(FATAL_ERROR "Could you make sure variable '${archive_var}_sha512' is defined ?")
  endif()
endfunction()

set(binary_archive "linux32_binary")
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
  set(binary_archive "linux64_binary")
endif()
if(APPLE)
  set(binary_archive "macosx_binary")
endif()
if(WIN32)
  set(binary_archive "win32_binary")
  if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(binary_archive "win64_binary")
  endif()
endif()
check_archive_var("${binary_archive}")

#-----------------------------------------------------------------------------
# Summary
#-----------------------------------------------------------------------------
message(STATUS "*********************************************")
message(STATUS "CastXML Python Distribution")
message(STATUS "")
message(STATUS "  ARCHIVE_DOWNLOAD_DIR      : ${ARCHIVE_DOWNLOAD_DIR}")
message(STATUS "")
message(STATUS "    binary_archive             : ${binary_archive}")
message(STATUS "    <binary_archive>_url       : ${${binary_archive}_url}")
message(STATUS "    <binary_archive>_sha512    : ${${binary_archive}_sha512}")
message(STATUS "")
message(STATUS "*********************************************")

#-----------------------------------------------------------------------------
# Download pre-built archive
#-----------------------------------------------------------------------------
include(FetchContent)
FetchContent_Populate(castxmlrelease
  URL ${${binary_archive}_url}
  URL_HASH SHA512=${${binary_archive}_sha512}
  )
set(CASTXML_RELEASE_DIR ${castxmlrelease_SOURCE_DIR})

set(castxml_executable ${CASTXML_RELEASE_DIR}/bin/castxml${CMAKE_EXECUTABLE_SUFFIX})
install(PROGRAMS ${castxml_executable} DESTINATION bin)
install(DIRECTORY ${CASTXML_RELEASE_DIR}/share/ DESTINATION share)
