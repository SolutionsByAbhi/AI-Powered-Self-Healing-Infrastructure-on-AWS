import yaml
import subprocess


def execute(playbook):

    filename = f"runbooks/{playbook}.yaml"

    cmd = [
        "ansible-playbook",
        filename
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }
