from prefect import flow
from prefect_shell import shell_run_command


@flow
def main_flow():
    shell_run_command("python src/main.py")
