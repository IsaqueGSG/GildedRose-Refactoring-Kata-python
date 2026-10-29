import io
import sys

from approvaltests import verify
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from texttest_fixture import main

def test_gilded_rose_approvals():
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py", 30]
        main()
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    # Usamos o PythonNativeReporter para comparar o texto internamente sem depender de programas externos no Windows
    verify(answer, reporter=PythonNativeReporter())

if __name__ == "__main__":
    test_gilded_rose_approvals()