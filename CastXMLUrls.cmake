
#-----------------------------------------------------------------------------
# CastXML binaries

set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
set(linux32_binary_sha512 "NA")

set(linux64_binary_url    "https://data.kitware.com/api/v1/file/6006edd02fa25629b9fca6a6/download")
set(linux64_binary_sha512 "bdbb67a10c5f8d1b738cd19cb074f409d4803e8077cb8c1072ef4eaf738fa871a73643f9c8282d58cae28d188df842c82ad6620b6d590b0396a0172a27438dce")

set(macosx_binary_url    "https://data.kitware.com/api/v1/file/6006eda52fa25629b9fca696/download")
set(macosx_binary_sha512 "5d937e938f7b882a3a3e7941e68f8312d0898aaf2082e00003dd362b1ba70b98b0a08706a1be28e71652a6a0f1e66f89768b5eaa20e5a100592d5b3deefec3f0")

set(win64_binary_url    "https://data.kitware.com/api/v1/file/6006ed812fa25629b9fca68a/download")
set(win64_binary_sha512 "bdd1e2c3b203019f758681067bb4dd68cb37abc930fee6b4b5d181bd805236352f888d061f32c7f93bde2eac2caa1265b93bbccff6656f98989dafd08f55847b")

# See https://github.com/CastXML/CastXML-python-distributions/issues/5
set(win32_binary_url    "${win64_binary_url}")
set(win32_binary_sha512 "${win64_binary_sha512}")