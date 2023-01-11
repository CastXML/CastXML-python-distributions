
#-----------------------------------------------------------------------------
# CastXML binaries

set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
set(linux32_binary_sha512 "NA")

set(linux64_binary_url    "https://data.kitware.com/api/v1/file/63bed74d6d3fc641a02d7e99/download")
set(linux64_binary_sha512 "986f8827d3ec8d58b5f91c9fc3cdaf66d29ff9cc1f1532dd6e72113cad64982546c6449dfe1cbf7ff2908272af81085b45e85791492995bc4a40e16034c819d9")

set(macosx_binary_url    "https://data.kitware.com/api/v1/file/63bed7726d3fc641a02d7e9f/download")
set(macosx_binary_sha512 "ef7a2ae83925583840faa763f513693a3c9e7d13889f1dfda4fbad03ef08264e01677450c2a3949ffc898a8e8b3714ea4910bd995125f32d3d95e8f977805574")

set(win64_binary_url    "https://data.kitware.com/api/v1/file/63bed83a6d3fc641a02d7ea3/download")
set(win64_binary_sha512 "df5a40605ac1c3487ed5e8bd202b681dd8f981b6a26b60c6fb5b7712a98bf4f3b55c6642c734f19c227c47a5937c8d78750a97d7498600fe2cd7a317b5096dcc")

# See https://github.com/CastXML/CastXML-python-distributions/issues/5
set(win32_binary_url    "${win64_binary_url}")
set(win32_binary_sha512 "${win64_binary_sha512}")
