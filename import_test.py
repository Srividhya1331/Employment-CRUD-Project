import importlib, sys
importlib.invalidate_caches()
try:
    import employee.views as v
    print('Imported', v.__file__)
except Exception as e:
    import traceback
    traceback.print_exc()
    raise
