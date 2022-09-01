
#-----------------------------------------------------------------------------
# CastXML binaries

set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
set(linux32_binary_sha512 "NA")

set(linux64_binary_url    "https://data.kitware.com/api/v1/file/617851882fa25629b9af3964/download")
set(linux64_binary_sha512 "1610df48287cc67cc9bf46c23c5fe0d26d1d98868041993f36670d9485b5f7126b702dfd6437760199d2f92dea0e527c32cae47dc399a17ce191e7cb9521a2cf")

set(macosx_binary_url    "https://data.kitware.com/api/v1/file/6178517f2fa25629b9af395a/download")
set(macosx_binary_sha512 "4a6ca04003d94a09a9dd3226d1f5a4a420db3fb2eb5fb63549fe9469afe39bf728cfc35b80e723764f2dd106faffe480afc0fb175cd5ec6b9971efa1422632d1")

set(win64_binary_url    "https://data.kitware.com/api/v1/file/617851942fa25629b9af396e/download")
set(win64_binary_sha512 "82ff5a23f385a0fddcd76c62fa109eb3cd087d6ba61ff0bdcd55a31341bdf2b383446260d53a4d2fac7d778f4d29c383de0429804d2050f0fb743e44c315fd94")

# See https://github.com/CastXML/CastXML-python-distributions/issues/5
set(win32_binary_url    "${win64_binary_url}")
set(win32_binary_sha512 "${win64_binary_sha512}")
