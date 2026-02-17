import json
import subprocess
import sys
from pathlib import Path


def test_cli_generate(tmp_path):
    spec = {"theme": "ruins"}
    spec_file = tmp_path / "spec.json"
    spec_file.write_text(json.dumps(spec))

    result = subprocess.run(
        [sys.executable, "-m", "wlm_world_generation_protocol.cli", "generate", str(spec_file)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert output["seed"]["theme"] == "ruins"
