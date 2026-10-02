# Rewrite the CastXML revision pinned by the CastXML superbuild.
#
# Usage, from the superbuild source directory:
#   cmake -DCASTXML_GIT_TAG=<revision> -P PatchCastXMLSuperbuild.cmake
#
# The superbuild sets CastXML_GIT_TAG with CACHE ... FORCE, so the pin can only
# be changed by editing its CMakeLists.txt. Re-running this is harmless.

if(NOT CASTXML_GIT_TAG)
  message(FATAL_ERROR "CASTXML_GIT_TAG must be set")
endif()

file(READ CMakeLists.txt content)

set(pin_regex "set\\(CastXML_GIT_TAG \"[^\"]*\"")
if(NOT content MATCHES "${pin_regex}")
  message(FATAL_ERROR
    "Could not find the CastXML_GIT_TAG pin in the superbuild's CMakeLists.txt; "
    "PatchCastXMLSuperbuild.cmake needs updating for this superbuild revision.")
endif()

string(REGEX REPLACE "${pin_regex}" "set(CastXML_GIT_TAG \"${CASTXML_GIT_TAG}\""
  content "${content}")
file(WRITE CMakeLists.txt "${content}")
