# Copyright (C) 2018 Leiden University Medical Center
# This file is part of pytest-workflow
#
# pytest-workflow is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# pytest-workflow is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pytest-workflow.  If not, see <https://www.gnu.org/licenses/

"""
Contains all functionality regarding the running of workflows and reporting
on stdout, stderr and exit code.
This file was created by A.H.B. Bollen
"""

from pathlib import Path
import shlex
import subprocess  # nosec: security implications have been considered
from typing import Optional, Union


class Workflow(object):

    def __init__(self, command: str,
                 cwd: Union[bytes, str] = None):
        """
        Initiates a workflow object
        :param command: The string that represents the command to be run
        :param cwd: The current working directory in which the command will
        be executed.
        """

        self.command = command
        self._proc_out = None
        self.cwd = cwd

    def run(self) -> subprocess.CompletedProcess:
        sub_procces_args = shlex.split(self.command)
        self._proc_out = subprocess.run(  # nosec: Shell is not enabled.
            sub_procces_args, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, cwd=self.cwd)

    def _log_to_file(self, log: bytes, output_file: Path):

    def stdout_to_file(self, output_file: Optional[Path] = None):
        if output_file is None:
            output_file = Path(self.cwd) / Path("log.out")
        with output_file.open("w") as file_handler:
            file_handler.write(self.stdout)
        return output_file

    @property
    def stdout(self) -> bytes:
        return self._proc_out.stdout  # for testing log

    @property
    def stderr(self) -> bytes:
        return self._proc_out.stderr  # for testing log

    @property
    def exit_code(self) -> int:
        return self._proc_out.returncode
