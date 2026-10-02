cmake_minimum_required(VERSION 3.20)

project(CastXMLPythonDistributions LANGUAGES C CXX)

#-----------------------------------------------------------------------------
# Build CastXML from source with the CastXML superbuild, which builds
# LLVM/Clang and then CastXML against them.
#-----------------------------------------------------------------------------
set(CASTXML_SUPERBUILD_GIT_TAG "0b677ec7bd49fa64bf7761aaed5a5129293c8094"
  CACHE STRING "CastXMLSuperbuild Git revision")

# The superbuild pins its own CastXML revision and FORCE-sets it in the cache,
# so it can't be overridden with -D. PatchCastXMLSuperbuild.cmake rewrites
# that pin to this revision instead.
set(CASTXML_GIT_TAG "v0.8.0" CACHE STRING "CastXML Git revision")

include(FetchContent)
FetchContent_Declare(castxmlsuperbuild
  GIT_REPOSITORY https://github.com/CastXML/CastXMLSuperbuild.git
  GIT_TAG ${CASTXML_SUPERBUILD_GIT_TAG}
  PATCH_COMMAND ${CMAKE_COMMAND}
    -DCASTXML_GIT_TAG=${CASTXML_GIT_TAG}
    -P ${CMAKE_CURRENT_SOURCE_DIR}/PatchCastXMLSuperbuild.cmake
  )
FetchContent_MakeAvailable(castxmlsuperbuild)

message(STATUS "CastXMLSuperbuild revision: ${CASTXML_SUPERBUILD_GIT_TAG}")
message(STATUS "CastXML revision: ${CASTXML_GIT_TAG}")

#-----------------------------------------------------------------------------
# Install
#-----------------------------------------------------------------------------
# The superbuild installs CastXML into <superbuild binary dir>/castxml while
# building. Ship that whole tree: bin/castxml finds its bundled Clang headers
# relative to itself in share/castxml.
install(DIRECTORY ${castxmlsuperbuild_BINARY_DIR}/castxml/
  DESTINATION .
  USE_SOURCE_PERMISSIONS
  )
