import platform

print(platform.platform(aliased=False, terse=False))
print(platform.platform(aliased=True, terse=True))
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.release())

print(platform.python_version())
print(platform.python_implementation())
print(platform.python_version_tuple())
