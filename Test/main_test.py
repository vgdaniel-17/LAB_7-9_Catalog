import unittest
import os


start_dir = os.path.dirname(os.path.abspath(__file__))
loader = unittest.TestLoader()

suite = loader.discover(start_dir, pattern='test_*.py', top_level_dir=start_dir)


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if result.wasSuccessful():
    print("\n✅ TOATE TESTELE AU TRECUT CU SUCCES!")
else:
    print("\n❌ AU EXISTAT ERORI IN TESTE.")