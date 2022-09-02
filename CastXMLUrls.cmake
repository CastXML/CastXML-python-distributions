
#-----------------------------------------------------------------------------
# CastXML binaries

set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
set(linux32_binary_sha512 "NA")

set(linux64_binary_url    "https://data.kitware.com/api/v1/file/622961384acac99f42134a8a/download")
set(linux64_binary_sha512 "a2da44515bea720e57ee1d335e05aea279a9ca3c39caad4b501af330f8f54363f5cb5512dd53643966f68d28b9b69961ed9ecf286ded24615a5a946790090543")

set(macosx_binary_url    "https://data.kitware.com/api/v1/file/622961284acac99f42134a6a/download")
set(macosx_binary_sha512 "1964b50b51970e9f9249fe4cf896302df024781abe8e7d888e91d8b14dfa01b29face1d808c9bff10209b0d3e77963c03fe7b3e28d2ccaa4aba7d18d12c82b88")

set(win64_binary_url    "https://data.kitware.com/api/v1/file/622961504acac99f42134aaf/download")
set(win64_binary_sha512 "56cf92eb9ca543a6178689643d32a455da1f92da78ca58a8cb671798ac9f903dc6b687be1d3824ab0211ed49724b62185a21874810139de7dbb6cb39f63b860f")

# See https://github.com/CastXML/CastXML-python-distributions/issues/5
set(win32_binary_url    "${win64_binary_url}")
set(win32_binary_sha512 "${win64_binary_sha512}")
