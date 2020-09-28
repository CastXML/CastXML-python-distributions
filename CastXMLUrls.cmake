
#-----------------------------------------------------------------------------
# CastXML binaries

set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
set(linux32_binary_sha512 "NA")

set(linux64_binary_url    "https://data.kitware.com/api/v1/file/5f6c9d2650a41e3d19a8e7ec/download")
set(linux64_binary_sha512 "85514042f024c705ea9647b4830ac5e58c83167792c2cfe9edab6ea4af52b0f8cb967ff53c5bfee6f8d6096f4de6a83c95d67c538f6fc0c537bc596948817585")

set(macosx_binary_url    "https://data.kitware.com/api/v1/file/5f6c9e3d50a41e3d19a8e85c/download")
set(macosx_binary_sha512 "cf7abb0eeb76ede7a36b6f1ac2545f2dcd00303c817810d118d12aaa1fe058d3348b6555e3ebe7bd47aba713ee02d489f1a33ba58d94d5b6e722fd1cae22647e")

set(win64_binary_url    "https://data.kitware.com/api/v1/file/5f6c9cd150a41e3d19a8e7b9/download")
set(win64_binary_sha512 "ed396ebd56301a4dd4c414a02f8c41293d1ed60df0802ccf4eb1f6db63bdf7d2ddea0eb66cc5ce1e1fd244e29d446072eae9fbe9f13159fb0213772a796a10eb")

# See https://github.com/CastXML/CastXML-python-distributions/issues/5
set(win32_binary_url    "${win64_binary_url}")
set(win32_binary_sha512 "${win64_binary_sha512}")
